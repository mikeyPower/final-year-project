#!/usr/bin/python
import csv
import sys
from functions import dateRange
from datetime import datetime
import time
import os
'''
This script takes a csv file and outputs the number of ips listenning on all ports
if file only has data with a single port then the total size of the file is outputed


Example: python port.py tmp.csv
Output: 3 csv files
        showing all ips on port 80, port 443 and those on both ports

NOTE SHOULD HAVE CODE TO CHECK FOR HEADER
'''

#Get timestamp of programme execution
now=str(int(time.time()))
str_now=str(datetime.now())
csvFile = sys.argv[1]

#create directory for outputted results
try:
    os.makedirs('port_'+now)
except OSError:
    if not os.path.isdir(path):
        raise

ips = []
port80 =[]
port443 =[]
dictionary={}
countPortIndex =6
with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    readCSV.next() #Skip first line (Header line)
    for i in readCSV:
        if i[0]+':'+i[6] not in ips:
            ips.append(i[0]+':'+i[6])
            #find ips on port 80 checking for duplicates
            if i[countPortIndex] == '80' and  i[0] not in port80:
                port80.append(i[0])

            #find ips on port 443 checking for duplicates
            elif i[countPortIndex] == '443' and i[0] not in port443:
                port443.append(i[0])


            #find the number of unique ips

            if (i[0] in dictionary) and (i[6] not in dictionary[i[0]]):
                dictionary[i[0]].append(i[6])
            elif i[0] not in dictionary:
                dictionary[i[0]] = [i[6]]
            else:
                continue
        else:
            continue
#Find number of Ips on both ports
bothPorts =[]
bothPorts = set(port80).intersection(port443)
multipe_ports=0
just80=0
just443=0
with open("port_"+now+"/both_ports_"+now+".csv", "w") as myfile2:
    writer2=csv.writer(myfile2)
    writer2.writerow(['Ip','Port'])
    with open("port_"+now+"/all_ip_ports_"+now+".csv", "w") as myfile3:
        writer3=csv.writer(myfile3)
        writer3.writerow(['Ip','Port'])
        with open("port_"+now+"/just_port_80_"+now+".csv", "w") as myfile4:
            writer4=csv.writer(myfile4)
            writer4.writerow(['Ip','Port'])
            with open("port_"+now+"/just_port_443_"+now+".csv", "w") as myfile5:
                writer5=csv.writer(myfile5)
                writer5.writerow(['Ip','Port'])
                with open("port_"+now+"/port_443_"+now+".csv", "w") as myfile1:
                    writer1=csv.writer(myfile1)
                    writer1.writerow(['Ip','Port'])
                    with open("port_"+now+"/port_80_"+now+".csv", "w") as myfile0:
                        writer0=csv.writer(myfile0)
                        writer0.writerow(['Ip','Port'])
                        for i in dictionary:
                            if len(dictionary[i]) > 1:
                                writer2.writerow([i,"80_43"])
                                writer0.writerow([i,"80_443"])
                                writer1.writerow([i,"80_443"])
                                multipe_ports=multipe_ports+1
                            elif len(dictionary[i]) == 1 and dictionary[i] == ['80']:
                                writer4.writerow([i,"80"])
                                writer0.writerow([i,"80"])
                                just80 = just80 +1
                            elif len(dictionary[i]) == 1 and dictionary[i] == ['443']:
                                writer5.writerow([i,"443"])
                                writer1.writerow([i,"443"])
                                just443 = just443+1
                            writer3.writerow([i,dictionary[i]])
                    myfile0.close()
                myfile1.close()
            myfile5.close()
        myfile4.close()
    myfile3.close()
myfile2.close()

#sanity check
if multipe_ports == len(bothPorts) and (len(dictionary)==just443+just80+multipe_ports):
    print('yes')
else:
    print('Error')


#summary of programme execution
summary_f="port_"+now+"/summary_ports_"+now+".txt"
summary_fp=open(summary_f,"w")
print >>summary_fp, "Ran " + sys.argv[0] + " at " + str_now + " (" + now + ")" +  " with file " + sys.argv[1]
print >>summary_fp, "Files created:"
print >>summary_fp, "\tjust_port_80_"+now+".csv"
print >>summary_fp, "\tjust_port_443_"+now+".csv"
print >>summary_fp, "\tport_80_"+now+".csv"
print >>summary_fp, "\tport_443_"+now+".csv"
print >>summary_fp, "\tboth_ports_"+now+".csv"
print >>summary_fp, str(len(dictionary)) + " Unique Ips"
print >>summary_fp, str(just80) + " Number of Ips only on port 80"
print >>summary_fp, str(just443) + " Number of Ips only on port 443"
print >>summary_fp, str(len(port80)) + " Number of Ips on port 80"
print >>summary_fp, str(len(port443)) + " Number of Ips on port 443"
print >>summary_fp, str(len(bothPorts)) + " Number of Ips on both ports"
