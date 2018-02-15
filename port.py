import csv
import sys
from functions import dateRange

'''
This script takes a csv file and outputs the number of ips listenning on all ports
if file only has data with a single port then the total size of the file is outputed


Example: python port.py 5/2/2018 6/2/2018 0 23 tmp.csv
Output:
('Number of Ports ', 2)
('Number of ips listenning on Port 443 at 2018-02-05T00', 0)
('Number of ips listenning on Port 80 at 2018-02-05T00', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T00', 0)
('Number of ips listenning on Port 443 at 2018-02-05T01', 0)
('Number of ips listenning on Port 80 at 2018-02-05T01', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T01', 0)
('Number of ips listenning on Port 443 at 2018-02-05T02', 0)
('Number of ips listenning on Port 80 at 2018-02-05T02', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T02', 0)
('Number of ips listenning on Port 443 at 2018-02-05T03', 0)
('Number of ips listenning on Port 80 at 2018-02-05T03', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T03', 0)
('Number of ips listenning on Port 443 at 2018-02-05T04', 0)
('Number of ips listenning on Port 80 at 2018-02-05T04', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T04', 0)
('Number of ips listenning on Port 443 at 2018-02-05T05', 0)
('Number of ips listenning on Port 80 at 2018-02-05T05', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T05', 0)
('Number of ips listenning on Port 443 at 2018-02-05T06', 0)
('Number of ips listenning on Port 80 at 2018-02-05T06', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T06', 0)
('Number of ips listenning on Port 443 at 2018-02-05T07', 0)
('Number of ips listenning on Port 80 at 2018-02-05T07', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T07', 0)
('Number of ips listenning on Port 443 at 2018-02-05T08', 0)
('Number of ips listenning on Port 80 at 2018-02-05T08', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T08', 0)
('Number of ips listenning on Port 443 at 2018-02-05T09', 0)
('Number of ips listenning on Port 80 at 2018-02-05T09', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T09', 0)
('Number of ips listenning on Port 443 at 2018-02-05T10', 0)
('Number of ips listenning on Port 80 at 2018-02-05T10', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T10', 0)
('Number of ips listenning on Port 443 at 2018-02-05T11', 0)
('Number of ips listenning on Port 80 at 2018-02-05T11', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T11', 0)
('Number of ips listenning on Port 443 at 2018-02-05T12', 0)
('Number of ips listenning on Port 80 at 2018-02-05T12', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T12', 0)
('Number of ips listenning on Port 443 at 2018-02-05T13', 0)
('Number of ips listenning on Port 80 at 2018-02-05T13', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T13', 0)
('Number of ips listenning on Port 443 at 2018-02-05T14', 0)
('Number of ips listenning on Port 80 at 2018-02-05T14', 451)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T14', 0)
('Number of ips listenning on Port 443 at 2018-02-05T15', 1)
('Number of ips listenning on Port 80 at 2018-02-05T15', 1)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T15', 1)
('Number of ips listenning on Port 443 at 2018-02-05T16', 0)
('Number of ips listenning on Port 80 at 2018-02-05T16', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T16', 0)
('Number of ips listenning on Port 443 at 2018-02-05T17', 0)
('Number of ips listenning on Port 80 at 2018-02-05T17', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T17', 0)
('Number of ips listenning on Port 443 at 2018-02-05T18', 0)
('Number of ips listenning on Port 80 at 2018-02-05T18', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T18', 0)
('Number of ips listenning on Port 443 at 2018-02-05T19', 0)
('Number of ips listenning on Port 80 at 2018-02-05T19', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T19', 0)
('Number of ips listenning on Port 443 at 2018-02-05T20', 0)
('Number of ips listenning on Port 80 at 2018-02-05T20', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T20', 0)
('Number of ips listenning on Port 443 at 2018-02-05T21', 0)
('Number of ips listenning on Port 80 at 2018-02-05T21', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T21', 0)
('Number of ips listenning on Port 443 at 2018-02-05T22', 0)
('Number of ips listenning on Port 80 at 2018-02-05T22', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T22', 0)
('Number of ips listenning on Port 443 at 2018-02-05T23', 0)
('Number of ips listenning on Port 80 at 2018-02-05T23', 0)
('Number of ips listenning on Both Port 80 and 443 at 2018-02-05T23', 0)
NOTE:
Should be able to specify a range similar to range.py outputing port 80, port 443 and what ones are listenning on both for every
hour within the range
'''
start = sys.argv[1]
start = map(int,(start.split('/')))
startday = start[0]
startmonth = start[1]
startyear = start[2]

end = sys.argv[2]
end = map(int,end.split('/'))
endDay = end[0]
endMonth = end[1]
endYear = end[2]

startTime = sys.argv[3]
endTime = sys.argv[4]

csvFile = sys.argv[5]
dateIsoSub = dateRange(startday,startmonth,startyear,endDay,endMonth, endYear, startTime,endTime)

with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    mostCount =0
    mostDate =''

    ports = []
#    dates =[]
    for t in readCSV:
        #dates.append(t[-3][:13])
        ports.append(t[6])
        #print(t[6])

    #get all the unique port numbers
    ports = list(set(ports))
    #dates = list(set(dates))
    port80 =0;
    port443=0;

    print('Number of ports ',len(ports))

    #this creates a dictionary with the keys being the port number + the date and values being a list of ips at those specific port number and date#
    with open("ports1.csv", "w") as myfile:
        writer=csv.writer(myfile)
        writer.writerow(['Time','Port 80', 'Port 443', 'Both'])
        dictionary = {}
        for v in dateIsoSub:
            count = 0
            for t in ports:
                with open(csvFile) as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                #print(t)
             #could possible place the items as tuples if the nesting of arrays becomes a problem but unsure can i check for intersection and so what with tuples
             #list(set()) will remove any duplicate ips
                    dictionary[t+'P'+v] =list(set([x[0] for j, x in enumerate(readCSV) if x[6] == t and x[-3][:13]==v]))

                    if  t == '80':
                        port80 = len(dictionary[t+'P'+v])
                    elif t == '443':
                        port443 = len(dictionary[t+'P'+v])
                    else:
                        continue
                    #print('Number of ips listenning on Port ' +t+' at '+v ,len(dictionary[t+'P'+v]))
                    count = count +1
                    if count == len(ports):
                        dictionary['80+433P'+v] = list(set(dictionary['80'+'P'+v]) & set(dictionary['443'+'P'+v]))
                        writer.writerow([v,port80,port443,len(dictionary['80+433P'+v])])
                        #print('Number of ips listenning on Both Port 80 and 443 at '+v  ,len(dictionary['80+433P'+v]))
                    else:
                        continue
        myfile.close()

'''
    print(len(dictionary))
#find ips that are listenning on all ports
    intersectSet =dictionary.values()[0]
    print(dictionary.values()[0])
    for key, values in dictionary.items():
        if key == dictionary.keys()[0]:
             continue
        else:
            intersectSet = list(set(values) & set(intersectSet))#.difference(intersectSet))
    print('lenght',len(intersectSet))
'''
