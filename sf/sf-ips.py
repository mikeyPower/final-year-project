#!/usr/bin/python

# modified by SF to count IPs and not IP/port combos

import sys
import os
import csv
import dateutil.parser
import pandas as pd
import datetime
import time
from datetime import timedelta, date

# map from date structure to just hour granularity
def justhour(val):
    return val[:13]

# our various output files, timestamped

# the timestamp, in time_t format
now=str(int(time.time()))

# has counts of IP's seen listening on which ports or both at that hour
hour_f="hours." + now + ".csv"
hour_f_header="hour,count(port80),count(port443),count(both)"
hour_fp=open(hour_f,"w");

# count per IP of how often/when seen
allip_f="ips." + now + ".csv"
allip_f_header="ip,firstseen,lastseen,count(80's),count(443's)"
allip_fp=open(allip_f,"w");

# count for "regularly-seen" IPs, same details as above
regip_f="regips." + now + ".csv"
regip_f_header="ip,obs_needed,firstseen,lastseen,count(80's),count(443's)"
regip_fp=open(regip_f,"w");

# how often do we need to see an IP for it to be "regularly-seen" 
# as a percentage of the number of hourly observations
reg_percent=90

# all other IPs are "irregular"
irregip_f="irregips." + now + ".csv"
irregip_f_header="ip,obs_needed,firstseen,lastseen,count(80's),count(443's)"
irregip_fp=open(irregip_f,"w");

# collect info per hour
hourlycounts={}
thishour=""
thishour_port80=[]
thishour_port443=[]
thishour_both=[]

# collect info on each ip
ipdets={}

# full mode - real data not in repo
home=os.path.expanduser('~')
file=home+'/data/tcd-surveys/TrinityIps.csv'
verbose=False

# test mode
if len(sys.argv)==2 and sys.argv[1] == 'test':
    # use a short test file with few records, with synthetic data generated using the m100.sh script
    file='fewrecs.csv'
    verbose=True

if verbose:
    print "Reading from " + file

with open(file) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for line in readCSV:
        hour=justhour(line[-3])
        # special case for first record
        if thishour=="":
            thishour=hour
        ip=line[0]
        port=line[6]
        #print ip + ":" + port
        if port != "80" and port != "443":
            print "Error - bad port: " + port
            continue
        if port=="80" and ip not in thishour_port80:
            thishour_port80.append(ip)
        elif port=="443" and ip not in thishour_port443:
            thishour_port443.append(ip)
        if hour!=thishour:
            # a new hour
            if verbose:
                print "80:", thishour_port80
                print
                print "443:", thishour_port443
                print
                print "both:", thishour_both
                print
            # check who's got both
            for ip80 in thishour_port80:
                if ip80 in thishour_port443:
                    if ip80 not in thishour_both:
                        thishour_both.append(ip80)
                    thishour_port80.remove(ip80)
                    thishour_port443.remove(ip80)
            if verbose:
                print "80:", thishour_port80
                print
                print "443:", thishour_port443
                print
                print "both:", thishour_both
                print
            # accumulate
            hourlycounts[hour]=[len(thishour_port80),len(thishour_port443),len(thishour_both)]
            # re-init
            thishour_port80=[]
            thishour_port443=[]
            thishour_both=[]
            thishour=hour
        # accumulate details on this IP
        if ip not in ipdets:
            ipdets[ip]={}
            ipdets[ip]['80']=0
            ipdets[ip]['443']=0
        thisone=ipdets[ip]
        if 'firstseen' not in thisone:
            thisone['firstseen']=hour
        thisone['lastseen']=hour
        thisone[port] += 1

print >>hour_fp, hour_f_header
for h in sorted(hourlycounts):
    print >>hour_fp, h + "," +  str(hourlycounts[h][0]) + "," + str(hourlycounts[h][1]) + "," + str(hourlycounts[h][2])

print >>allip_fp, allip_f_header
for det in sorted(ipdets):
    print >>allip_fp, det + "," + \
        ipdets[det]['firstseen'] + "," + \
        ipdets[det]['lastseen'] + "," + \
        str(ipdets[det]['80']) + "," + \
        str(ipdets[det]['443']) 

# split IPs into regular/irregular
obs_needed=int(len(hourlycounts)*reg_percent/100)

print >>regip_fp, regip_f_header
print >>irregip_fp, irregip_f_header
for det in sorted(ipdets):
    if ipdets[det]['80'] >= obs_needed or ipdets[det]['443'] >= obs_needed:
        print >>regip_fp, det + "," + \
            str(obs_needed) + "," + \
            ipdets[det]['firstseen'] + "," + \
            ipdets[det]['lastseen'] + "," + \
            str(ipdets[det]['80']) + "," + \
            str(ipdets[det]['443']) 
    else:
        print >>irregip_fp, det + "," + \
            str(obs_needed) + "," + \
            ipdets[det]['firstseen'] + "," + \
            ipdets[det]['lastseen'] + "," + \
            str(ipdets[det]['80']) + "," + \
            str(ipdets[det]['443']) 

