import socket
import sys
from datetime import datetime
import time
import csv
import os

now=str(int(time.time()))
str_now=str(datetime.now())

if len(sys.argv)==2:
    file = sys.argv[1]

if not os.path.isfile(file) or not os.access(file,os.R_OK):
    print "Can't read input file: " + file + " - exiting"
    sys.exit(1)


csvFile = sys.argv[1]

portCount = 0
portError=0
dictionary = {}
ips = []
with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    readCSV.next() #Skip first line (Header line)
    with open("error_open_ports_"+now+".csv", "w") as myfile1:
        writer1=csv.writer(myfile1)
        writer1.writerow(['Queried Ip','Port','Error'])
        for i in readCSV:
            if i[0] not in ips:
                ips.append(i[0])
                dictionary[i[0]] =[]
                print(i[0])
                try:
                    for port in range(80,100):
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(0.5) #for hanging Connections
                        result = sock.connect_ex((i[0], port))
                        if result == 0:
                            dictionary[i[0]].append(port)
                        else:
                            continue
                        sock.close()
                        time.sleep(0.05)
                except Exception as e:
                    #print >> sys.stderr, "Connection Error:  " + str(e) + " for " + i[0]
                    writer1.writerow([i[0],str(port), str(e)])
            else:
                continue

with open("open_ports_"+now+".csv", "w") as myfile:
    writer=csv.writer(myfile)
    writer.writerow(['Queried Ip','Ports'])
    for j, k in dictionary.items():
            writer.writerow([j,k])






#Print summary report
summary_f="summary_open_ports_"+now+".txt"
summary_fp=open(summary_f,"w")
print >>summary_fp, "Ran " + sys.argv[0] + " at " + str_now + " (" + now + ")" +  " with file " + sys.argv[1]
print >>summary_fp, "Files created:"
print >>summary_fp, "\topen_ports_"+now+".csv"
print >>summary_fp, "\terror_open_ports_"+now+".csv"
print >>summary_fp, str(len(ips)) + " Unique ips found"
