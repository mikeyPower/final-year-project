import os
import socket
import sys
from datetime import datetime
import csv
import time


'''


Note host name is truncating when adding to csv file converting to string prior to adding seems to have fixed it

'''
if len(sys.argv)==2:
    file = sys.argv[1]

if not os.path.isfile(file) or not os.access(file,os.R_OK):
    print "Can't read input file: " + file + " - exiting"
    sys.exit(1)
#the timestamp, in time_t format
now=str(int(time.time()))
str_now=str(datetime.now())

#csv file input
csvFile=sys.argv[1]
ip=''
rdns=""


dnsError=[]

ips = []
dns =[]
dnsCount =0
dictionary = {}
dnsResolvedCount = 0
noDnsCount =0;
multiple_ip_to_dns_count =0
with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    readCSV.next() #Skip first line (Header line)
    #ipAddress = list(set([x[0]for i, x in enumerate(readCSV)]))
    #for i in readCSV:
    #    print(i)
    #print(len(ipAddress))
    with open("resolved_ip_to_dns"+now+".csv", "w") as myfile:
        writer=csv.writer(myfile)
        writer.writerow(['Queried Ip','Port','Hostname', 'alias-list', 'Ip'])
        with open("unresolved_ip_to_dns"+now+".csv", "w") as myfile1:
            writer1=csv.writer(myfile1)
            writer1.writerow(['Queried Ip','Port','Error'])
            for i in readCSV:
                if i[0] not in ips: #if the ip has already been checked no need to get Hostname
                    ips.append(i[0])
                    try:
                        rdns=socket.gethostbyaddr(i[0]+".")

                        time.sleep(0.05)

                        if (str(rdns[0]) in dictionary) and (i[0] not in dictionary[str(rdns[0])]):
                            dictionary[str(rdns[0])].append(i[0])
                            dnsResolvedCount =dnsResolvedCount+1
                            writer.writerow([i[0],i[1],str(rdns[0]), rdns[1], rdns[2]])
                        elif str(rdns[0]) not in dictionary:
                            dictionary[str(rdns[0])] = [i[0]]
                            dnsResolvedCount =dnsResolvedCount+1
                            writer.writerow([i[0],i[1],str(rdns[0]), rdns[1], rdns[2]])
                        else:
                            continue


                    #    dnsResolvedCount =dnsResolvedCount+1
                    #    writer.writerow([i[0],i[1],strdns[0], strdns[1], strdns[2]])
                    except Exception as e:
                        if i[0] not in dnsError:
                                #print >> sys.stderr, "dns exception " + str(e) + " for " + i[0]
                            writer1.writerow([i[0],i[1], str(e)])
                            noDnsCount = noDnsCount +1
                            dnsError.append(i[0])
                        else:
                            continue
                else:
                    continue
        myfile1.close()
    myfile.close()




#Find all dns that have multipe ips
multiple_ip_to_dns_count =0
with open("multiple_ip_to_dns"+now+".csv", "w") as myfile2:
    writer2=csv.writer(myfile2)
    writer2.writerow(['Queried Ip','Port'])
    for i in dictionary:

        if len(dictionary[i]) > 1:
            writer2.writerow([i,dictionary[i]])
            multiple_ip_to_dns_count = multiple_ip_to_dns_count+1
        else:
           continue


#Print summary report
summary_f="summary_dns_"+now+".txt"
summary_fp=open(summary_f,"w")
print >>summary_fp, "Ran " + sys.argv[0] + " at " + str_now + " (" + now + ")" +  " with file " + sys.argv[1]
print >>summary_fp, "Files created:"
print >>summary_fp, "\tmultiple_ip_to_dns"+now+".csv"
print >>summary_fp, "\tresolved_ip_to_dns"+now+".csv"
print >>summary_fp, "\tunresolved_ip_to_dns"+now+".csv"
print >>summary_fp, str(len(ips)) + " Unique ips found"
print >>summary_fp, str(dnsResolvedCount) + " had reverse names"
print >>summary_fp, str(noDnsCount) + " did not"
print >>summary_fp, str(multiple_ip_to_dns_count) + " DNS had multipe ips"
print >>summary_fp, str(len(dictionary)) + " Unique DNS found"
