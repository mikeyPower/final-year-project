#!/usr/bin/python
import sys
import csv

'''
This script simple finds all occurance of a given ip and prints them to the screen

Example: python find-ip-instances.py 134.226.63.120 tmp.csv

'''

csvFile = sys.argv[1]


csv.field_size_limit(sys.maxsize)
dictionary=[]
with open(csvFile) as csvfile:
    readCSV = csv.reader(x.replace('\0', '') for x in csvfile)
    #readCSV = csv.reader(csvfile, delimiter=',')
    #ipMatch = [x for i, x in enumerate(readCSV) if x[0] == ip]


    for j in readCSV:
        #print(i)

        #h=j[0].split(' ')
        k = j[0][0:13]
        #print(k)
        if (k not in dictionary):
            #print(h[0])
            dictionary.append(k)

print(len(set(dictionary)))
#for i in dictionary:
#    print(i)

print("first Scan", dictionary[0])
print("Last Scan", dictionary[-1])
