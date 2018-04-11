#!/usr/bin/python
import csv
import sys
#from functions import dateRange
from datetime import datetime
import time
import os

#Get timestamp of programme execution
now=str(int(time.time()))
str_now=str(datetime.now())

csvFile = sys.argv[1]

port = sys.argv[2]
statusLine=6
ipField=2
portField=3
#if status line is 'Not Present' we know it is off/dead
#So ip:statusLine we will filter by
notAliveIp=[]
aliveIp=[]
ips=[]
numberOfFields=0
csv.field_size_limit(sys.maxsize)

with open(csvFile) as csvfile:
    #readCSV = csv.reader(csvfile, delimiter=',')
    readCSV = csv.reader(x.replace('\0', '') for x in csvfile)
    with open("alive_ips_"+now+".csv", "w") as myfile1:
        writer1=csv.writer(myfile1)
        if port == '80':
            numberOfFields=12
            writer1.writerow(['Time','Domain','Ip','Port','Connected','Server','Status Line','Cache Control','Header Expires','Pragma','Location','Body'])
        else:
            numberOfFields=31
            writer1.writerow(['Time','Domain','Ip','Port','Connected','Server','Status Line','Cache Control','Header Expires','Pragma','Location',
            'Secure Regotitation','TlS Version','Self Signed','Subject Common Name','Certificate Alt Names','Browser Trusted',
            'Cipher','Issuer','Matches Domain','Cert Start','Cert End','Cert Validity Length','Cert Expired','Public Key','Public Key Length',
            'Signature Algorithm','Key Algorithm','Curve Id','Compression Method','Body'])
        for i in readCSV:
            ips.append(i[ipField]+':'+i[portField])
            if (i[ipField]+':'+i[portField] not in notAliveIp) and (i[statusLine] == 'Not Present'):
            	notAliveIp.append(i[ipField]+':'+i[portField])

            elif (i[ipField]+':'+i[portField] not in aliveIp) and (i[statusLine] != 'Not Present'):
                if len(i) ==numberOfFields :
                    if i[len(i)-1] != 'Not Present':
                        writer1.writerow(i)
                        aliveIp.append(i[ipField]+':'+i[portField])

    myfile1.close()


defNotAliveIp = list(set(ips) - set(aliveIp))
with open("not_alive_ips_"+now+".csv", "w") as myfile2:
    writer2=csv.writer(myfile2,quoting=csv.QUOTE_NONE,escapechar='\r')
    writer2.writerow(['Ip','Port'])
    for i in defNotAliveIp:
        j= i.split(':')
        #print(i.split(':'))
        #print(j[1])
        writer2.writerow([j[0],j[1]])
myfile2.close()

#print(otherSet)

#Print summary report
summary_f="summary_ips_alive_"+now+".txt"
summary_fp=open(summary_f,"w")
print >>summary_fp, "Ran " + sys.argv[0] + " at " + str_now + " (" + now + ")" +  " with file " + sys.argv[1]
print >>summary_fp, "Files created:"
print >>summary_fp, "\talive_ips_"+now+".csv"
print >>summary_fp, "\tsummary_ips_alive_"+now+".txt"
print >>summary_fp, str(len(set(ips))) + " Unique Ips"
print >>summary_fp, str(len(aliveIp)) + " ips on"
print >>summary_fp, str(len(defNotAliveIp)) + " ips not on"
