
import dns.resolver
import socket
import sys
from datetime import datetime
import csv
import time


'''
Will have to take into consideration header lines

'''

#the timestamp, in time_t format
now=str(int(time.time()))
str_now=str(datetime.now())

#csv file input
csvFile=sys.argv[1]
ip=''
rdns=''


#find out how many ips resolve to dns as well as those that don't
dnsError=[]
dnsMul=[]
dictionary = {}
dnsResolvedCount = 0
noDnsCount =0;

with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #ipAddress = list(set([x[0]for i, x in enumerate(readCSV)]))
    with open("resolved_ip_to_dns"+now+".csv", "w") as myfile:
        writer=csv.writer(myfile)
        writer.writerow(['Queried Ip','Port','Hostname', 'alias-list', 'Ip'])
        with open("unresolved_ip_to_dns"+now+".csv", "w") as myfile1:
            writer1=csv.writer(myfile1)
            writer1.writerow(['Queried Ip, Error'])
            for i in readCSV:
                try:
                    rdns=socket.gethostbyaddr(i[0])
                            #dnsResolvedCount =dnsResolvedCount+1
                            #writer.writerow([i[0],rdns[0], rdns[1], rdns[2]])
                    if rdns[0] in dictionary and i[0] not in dictionary[rdns[0]]:
                        dictionary[rdns[0]].append(i[0])
                        dnsResolvedCount =dnsResolvedCount+1
                        writer.writerow([i[0],i[6],rdns[0], rdns[1], rdns[2]])
                    elif rdns[0] not in dictionary:
                        dictionary[rdns[0]] = [i[0]]
                        dnsResolvedCount =dnsResolvedCount+1
                        writer.writerow([i[0],i[6],rdns[0], rdns[1], rdns[2]])
                    else:
                        break

                except Exception as e:
                    if i[0] not in dnsError:
                        print >> sys.stderr, "dns exception " + str(e) + " for " + i[0]
                        writer1.writerow([i[0],i[6], e])
                        noDnsCount = noDnsCount +1
                        dnsError.append(i[0])
                    else:
                        break
        myfile1.close()
    myfile.close()




#Find all dns that have multipe ips
multiple_ip_to_dns_count =0
with open("multiple_ip_to_dns"+now+".csv", "w") as myfile2:
    writer2=csv.writer(myfile2)
    writer2.writerow(['DNS','Ips reachable'])

    for i in dictionary:
        if len(dictionary[i]) > 1:
            writer2.writerow([i,dictionary[i]])
            multiple_ip_to_dns_count = multiple_ip_to_dns_count+1
        else:
           continue



#Print summary report
summary_f="summary"+now+".txt"
summary_fp=open(summary_f,"w")
print >>summary_fp, "Ran " + sys.argv[0] + " at " + str_now + " (" + now + ")"
print >>summary_fp, str(noDnsCount+dnsResolvedCount) + " Unique ips found"
print >>summary_fp, str(dnsResolvedCount) + " had reverse names"
print >>summary_fp, str(noDnsCount) + " did not"
print >>summary_fp, str(multiple_ip_to_dns_count) + " DNS had multipe ips"
print >>summary_fp, str(len(dictionary)) + " Unique DNS found"