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
print(csvFile)

csvFile1 = sys.argv[2]
print(csvFile1)

csv.field_size_limit(sys.maxsize)

ipField=2
outer=[]
inner=[]
ips_present=[]
count =0
count_not_present =0
found =1
m=[]
with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    header =readCSV.next() #Skip first line (Header line)
    #print(len(readCSV))
    #print(len(header))
    with open("irreg_ips_zgrab_"+now+".csv", "w") as myfile1:
        writer1=csv.writer(myfile1)
        #writer1.writerow(header)
        for i in readCSV:
            outer.append(i[ipField])
            count = count +1
            if found == 0:
                #write to m to csv
                writer1.writerow(m)
                count_not_present=count_not_present+1
            found = 0
            with open(csvFile1) as csvfile1:
                readCSV1 = csv.reader(csvfile1, delimiter=',')
                header1 =readCSV1.next() #Skip first line (Header line)
                for j in readCSV1:
                    m =i
                    if count == 1:
                        inner.append(j[ipField])
                #ensure where not checking duplicates
                    #print(str(i[ipField]),str(j[0]))
                    if str(i[ipField]) == str(j[ipField]):
                        ips_present.append(i[ipField])
                        #writer1.writerow(i)
                        found =1


        myfile1.close()

#figure out which csv is larger
if len(set(outer))>=len(set(inner)):
    ips = outer
else:
    ips =inner

hi = set(inner)-set(ips_present)
print(hi)
#Print summary report
summary_f="summary_get_same_ips_"+now+".txt"
summary_fp=open(summary_f,"w")
print >>summary_fp, "Ran " + sys.argv[0] + " at " + str_now + " (" + now + ")" +  " with file " + sys.argv[1]+"  "+sys.argv[2]
print >>summary_fp, "Files created:"
print >>summary_fp, "\tirreg_ips_zgrab_"+now+".csv"
print >>summary_fp, "\tsummary_get_same_ips_"+now+".txt"
print >>summary_fp, str(len(set(ips))) + " Unique Ips"
print >>summary_fp, str(len(ips_present)) + " ips Present"
print >>summary_fp, str(len(set(ips))-len(ips_present)) + " ips not Present"
print >>summary_fp, str(count_not_present) + " ips not Present"
