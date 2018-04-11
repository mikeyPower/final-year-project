#!/usr/bin/python
import os
import sys
import csv
import time


#Get timestamp of programme execution
now=str(int(time.time()))
str_now=str(datetime.now())

csvFile = sys.argv[1]

ipField=2
portField=3
ips=[]
both_ports=[]
with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    header =readCSV.next() #Skip first line (Header line)
    with open("ips_both_ports_"+now+".csv", "w") as myfile1:
        writer1=csv.writer(myfile1)
        writer1.writerow(header)
        for i in readCSV:
            #ensure where not checking duplicates
            if i[ipField] not in ips:


                ips.append(i[ipField])
                if i[portField] == '80_443':
                    writer1.writerow(i)
                    both_ports.append(i[ipField])




#Print summary report
summary_f="summary_ips_both_ports_"+now+".txt"
summary_fp=open(summary_f,"w")
print >>summary_fp, "Ran " + sys.argv[0] + " at " + str_now + " (" + now + ")" +  " with file " + sys.argv[1]
print >>summary_fp, "Files created:"
print >>summary_fp, "\tips_both_ports_"+now+".csv"
print >>summary_fp, "\tsummary_ips_both_ports_"+now+".txt"
print >>summary_fp, str(len(set(ips))) + " Unique Ips"
print >>summary_fp, str(len(both_ports)) + " ips on both ports"
