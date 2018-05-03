#!/usr/bin/python
import csv
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime
import dateutil.parser
import collections

#Filter data to plot
x_col=[]
y_col1=[]
y_col2=[]
y_col3=[]

counts=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
noIPs=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hoursN=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
column =0
length =0

dictionary={}
csvFile = sys.argv[1]
with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    a=readCSV.next() #Skip first line (Header line)
    for i in readCSV:


        #slit the iso time format in order to find hour
        #for average day
        j=i[0].split('T')

        x_col.append(dateutil.parser.parse(i[0]))
        y_col1.append(int(i[1]))
        y_col2.append(int(i[2]))
        y_col3.append(int(i[3]))

        #convert to datetime
        a = dateutil.parser.parse(j[0])

        #combine port 80 only, port 443 only and both ports
        if (a.strftime('%A') in dictionary):
            #dictionary[a.strftime('%A')].append(int(i[1])+int(i[2])+int(i[3]))
            dictionary[a.strftime('%A')].append(int(i[3]))
        elif a.strftime('%A') not in dictionary:
            #dictionary[a.strftime('%A')] = [int(i[1])+int(i[2])+int(i[3])]
            dictionary[a.strftime('%A')] = [int(i[3])]





#Find what the average day looks like
hours=[]
averageNoOfIps=[]
#orderedDictionary = collections.OrderedDict(sorted(dictionary.items()))
print(len(dictionary))
for k, v in dictionary.items():
    print(k,sum(v)/len(v))
    #hours.append(dateutil.parser.parse('2018-03-23T'+k))
    averageNoOfIps.append(sum(v)/len(v))
