#!/usr/bin/python
import csv
import sys
from functions import dateRange
from datetime import datetime
import time
'''
This script takes a csv file and outputs the number of ips listenning on all ports
if file only has data with a single port then the total size of the file is outputed


Example: python port.py tmp.csv
Output: 3 csv files
        showing all ips on port 80, port 443 and those on both ports

NOTE SHOULD HAVE CODE TO CHECK FOR HEADER
'''

now=str(int(time.time()))
str_now=str(datetime.now())
csvFile = sys.argv[1]

ips = []
port80 =[]
port443 =[]
countPortIndex =6
with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    readCSV.next() #Skip first line (Header line)
    '''row1 = next(readCSV)
    for j in row1:
        if j == 'Port':
            #print('PORT 80 GUYS')
            break
        else:
            countPortIndex = countPortIndex+1
'''


    with open("port_80_"+now+".csv", "w") as myfile:
        writer=csv.writer(myfile)
        writer.writerow(['Ip','Port'])
        with open("port_443_"+now+".csv", "w") as myfile1:
            writer1=csv.writer(myfile1)
            writer1.writerow(['Ip','Port'])
            for i in readCSV:

                #find ips on port 80 checking for duplicates
                if i[countPortIndex] == '80' and  i[0] not in port80:
                    port80.append(i[0])
                    #writer.writerow([i[0],i[countPortIndex]])
                    writer.writerow([i[0],i[6]])
                #find ips on port 443 checking for duplicates
                elif i[countPortIndex] == '443' and i[0] not in port443:
                    port443.append(i[0])
                    writer1.writerow(i)
                else:
                    continue

                #find the number of unique ips
                if i[0] not in ips:
                    ips.append(i[0])
                else:
                    continue
        myfile1.close()
    myfile.close()

#Find number of Ips on both ports
bothPorts =[]
bothPorts = set(port80).intersection(port443)
with open("both_ports_"+now+".csv", "w") as myfile2:
    writer2=csv.writer(myfile2)
    writer2.writerow(['Ip'])
    for i in bothPorts:
        writer2.writerow([i])

myfile2.close()




summary_f="summary_ports_"+now+".txt"
summary_fp=open(summary_f,"w")
print >>summary_fp, "Ran " + sys.argv[0] + " at " + str_now + " (" + now + ")" +  " with file " + sys.argv[1]
print >>summary_fp, "Files created:"
print >>summary_fp, "\tport_80_"+now+".csv"
print >>summary_fp, "\tport_443_"+now+".csv"
print >>summary_fp, "\tboth_ports_"+now+".csv"
print >>summary_fp, str(len(ips)) + " Unique Ips"
print >>summary_fp, str(len(port80)) + " Number of Ips on port 80"
print >>summary_fp, str(len(port443)) + " Number of Ips on port 443"
print >>summary_fp, str(len(bothPorts)) + " Number of Ips on both ports"
