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


    print('Number of Ports ',len(ports))

    #store each ip in a multi dimensial array so all ips listenning on port 80 are located at stableIps[0] etc
    dictionary = {}
    for t in ports:
        with open(csvFile) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
             #could possible place the items as tuples if the nesting of arrays becomes a problem but unsure can i check for intersection and so what with tuples
            dictionary[t] =[x[0] for j, x in enumerate(readCSV) if x[6] == t]


    print(len(dictionary))
#find ips that are listenning on all ports
    intersectSet =dictionary.values()[0]
    for key, values in dictionary.items():

        print(key)
        if key == dictionary.keys()[0]:
             continue
        else:
            print(goal)
            intersectSet = list(set(values).difference(intersectSet))
    print(len(intersectSet))
