import csv
import sys

'''
This script takes a csv file and outputs the number of ips listenning on all ports
if file only has data with a single port then the total size of the file is outputed
'''

csvFile = sys.argv[1]
with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    mostCount =0
    mostDate =''

    ports = []
    for t in readCSV:
        ports.append(t[6])
        #print(t[6])

    #get all the unique port numbers
    ports = list(set(ports))


    print(len(ports))

    #store each ip in a multi dimensial array so all ips listenning on port 80 are located at stableIps[0] etc
    ips = []
    count =0
    for t in ports:
        ips.append([])
        with open('tmp.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for u in readCSV:
                if u[6]==t:
                    ips[count].append(u[0]) #could possible place the items as tuples if the nesting of arrays becomes a problem but unsure can i check for intersection and so what with tuples
                else:
	               #break
                    continue
            count = count +1


#find ips that are listenning on all ports
    intersectSet =ips[0]
    print(len(intersectSet))
    for i in ips[1:]:
         intersectSet = list(set(i).difference(intersectSet))
    print(len(intersectSet))
