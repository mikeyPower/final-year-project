#!/usr/bin/python
import os
import sys
import csv
from datetime import datetime
import time

#Get timestamp of programme execution
now=str(int(time.time()))
str_now=str(datetime.now())

csvFile = sys.argv[1]

csv.field_size_limit(sys.maxsize)

ipField=2
portField=3
ips=[]
both_ports=[]
with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    header =readCSV.next() #Skip first line (Header line)
    with open("both_ports_"+now+".csv", "w") as myfile1:
        writer1=csv.writer(myfile1)
        writer1.writerow(header)
        with open("single_port_"+now+".csv", "w") as myfile2:
            writer2=csv.writer(myfile2)
            writer2.writerow(header)
            for i in readCSV:
                #ensure where not checking duplicates
                if i[ipField] not in ips:


                    ips.append(i[ipField])
                #    print(i[portField],type(i[portField]),len(i[portField]))
                #rstrip is used to get rid of trailling whitespace e.g '\r' etc
                    if i[portField].rstrip() == '80_443':
                        #print('yes')
                        writer1.writerow(i)
                        both_ports.append(i[ipField])
                    else:
                        writer2.writerow(i)
        myfile2.close()
    myfile1.close()




#Print summary report
summary_f="summary_ips_both_ports_"+now+".txt"
summary_fp=open(summary_f,"w")
print >>summary_fp, "Ran " + sys.argv[0] + " at " + str_now + " (" + now + ")" +  " with file " + sys.argv[1]
print >>summary_fp, "Files created:"
print >>summary_fp, "\tboth_ports_"+now+".csv"
print >>summary_fp, "\tsingle_port_"+now+".csv"
print >>summary_fp, "\tsummary_ips_both_ports_"+now+".txt"
print >>summary_fp, str(len(set(ips))) + " Unique Ips"
print >>summary_fp, str(len(both_ports)) + " ips on both ports"
print >>summary_fp, str(len(set(ips))-len(both_ports)) + " ips on single ports"
