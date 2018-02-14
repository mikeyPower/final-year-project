import csv
import sys

'''
This script takes a csv file and outputs the number of ips listenning on all ports
if file only has data with a single port then the total size of the file is outputed






NOTE:
Should be able to specify a range similar to range.py outputing port 80, port 443 and what ones are listenning on both for every
hour within the range
'''

csvFile = sys.argv[1]
with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    mostCount =0
    mostDate =''

    ports = []
    dates =[]
    for t in readCSV:
        dates.append(t[-3][:13])
        ports.append(t[6])
        #print(t[6])

    #get all the unique port numbers
    ports = list(set(ports))
    dates = list(set(dates))


    print('Number of Ports ',len(ports))
    print('Number of dates ',len(dates))

    #this creates a dictionary with the keys being the port number + the date and values being a list of ips at those specific port number and date
    dictionary = {}
    for v in dates:
        count = 0
        for t in ports:
            with open(csvFile) as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                #print(t)
             #could possible place the items as tuples if the nesting of arrays becomes a problem but unsure can i check for intersection and so what with tuples
                dictionary[t+'P'+v] =[x[0] for j, x in enumerate(readCSV) if x[6] == t and x[-3][:13]==v]
                count = count +1
                if count == len(ports):
                    dictionary['80+433P'+v] = list(set(dictionary['80'+'P'+v]) & set(dictionary['443'+'P'+v]))
                else:
                    continue

    for key, values in dictionary.items():
        print(key ,len(values))

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
