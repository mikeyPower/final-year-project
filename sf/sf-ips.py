#!/usr/bin/python

# modified by SF to count IPs and not IP/port combos

import sys
import csv
import dateutil.parser
import pandas as pd
import datetime
from datetime import timedelta, date

# map from date structure to just hour granularity
def justhour(val):
    return val[:13]

start = datetime.date(2018, 2, 6)#started on the 06/02/2018T00
end = datetime.date(2018, 2, 7)#Will finish on the 12/02/2018T23
dateIso = []
dateIsoSub = []
datelist = pd.date_range(start, end, freq='1H').tolist()
index = pd.Index(datelist)
for x in index[:-1]:#loop through everything bar the last element in the list
	dateIso.append(x.isoformat())
	dateIsoSub.append(x.isoformat()[:13])

hourlycounts={}
thishour=""
thishour_port80=[]
thishour_port443=[]
thishour_both=[]

# full mode
file='TrinityIps.csv'
verbose=False


# test mode
if len(sys.argv)==2 and sys.argv[1] == 'test':
    # use a short test file, generated via:
    #       head -1000 | tail -99 TrinityIps.csv >100recs.csv
    #       tail -1 TrinityIps.csv >>100recs.csv
    # the tail is so that we have at least one record from a different hours
    # the bash script m100.sh does the above
    file='100recs.csv'
    verbose=True

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

print "hour,port80,port443,both"
for h in sorted(hourlycounts):
    print h + "," +  str(hourlycounts[h][0]) + "," + str(hourlycounts[h][1]) + "," + str(hourlycounts[h][2])

