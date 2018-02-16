#!/usr/bin/python

import dns.resolver
import socket
import sys
import os
import datetime
import time
import csv

# don't be noisy
verbose=False
super_verbose=False
file=""

now=str(int(time.time()))

# output files
# has IP's and reverse names
rev_f="reverse." + now + ".csv"
rev_f_header="ip,reverse-name"
rev_fp=open(rev_f,"w");
print >>rev_fp, rev_f_header

# just ips
norev_f="noreverse." + now + ".csv"
norev_f_header="ip"
norev_fp=open(norev_f,"w");
print >>norev_fp, norev_f_header

# sorta human readable summary
summary_f="rev-summary." + now + ".txt"
summary_fp=open(summary_f,"w")

# take a dot-sep IPv4 and see if there's interesting reverse-ip info
def do_reverse(ip):
    rdns=""
    try:
        req = '.'.join(reversed(ip.split("."))) + ".in-addr.arpa"
        answers = dns.resolver.query(req, "PTR")
        for rdata in answers:
            rdns=str(rdata)
            if verbose:
                print rdata
    except Exception as e: 
        if verbose:
            print >> sys.stderr, "dns exception " + str(e) + " for " + ip
    return rdns

# check inputs

if len(sys.argv) <2 or len(sys.argv) >3 :
    print >>sys.stderr, "usage: " + sys.argv[0] + " <file> [\"test\"] "
    sys.exit(1)

if len(sys.argv)==2:
    file = sys.argv[1]

# test mode
if len(sys.argv)==3 and sys.argv[2] == 'test':
    file = sys.argv[1]
    verbose=True

if verbose:
    print >>sys.stderr, "Being verbose. Reading from " + file

if not os.path.isfile(file) or not os.access(file,os.R_OK):
    print "Can't read input file: " + file + " - exiting"
    sys.exit(1)

start=datetime.datetime.utcnow()
with open(file) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    results=[]
    count=0
    for line in readCSV:
        if super_verbose:
            print line
        if count==0:
            # skip 1st line header
            count += 1
            continue
        count += 1
        ip = line[0]
        rdns = do_reverse(ip)
        results.append([ip,rdns])
        time.sleep(0.1)
end=datetime.datetime.utcnow()

revcount=0
for res in results:
    if res[1]=='':
        # no reverse
        print >>norev_fp, res[0]
    else:
        revcount += 1
        print >>rev_fp, res[0] + "," + res[1]


print >>summary_fp, "reverse looked up " + str(count) + " ips from file: " + file
print >>summary_fp, "started at " + str(start)
print >>summary_fp, "ended at " + str(end)
print >>summary_fp, str(revcount) + " had reverse names"
print >>summary_fp, str(count-revcount) + " did not"
