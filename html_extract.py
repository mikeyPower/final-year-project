#!/usr/bin/python
import csv
import sys
from functions import dateRange
from datetime import datetime
import time
import os

#Get timestamp of programme execution
now=str(int(time.time()))
str_now=str(datetime.now())

csvFile = sys.argv[1]
#if status line is 'Not Present' we know it is off/dead
#So ip:statusLine we will filter by
csv.field_size_limit(sys.maxsize)

#create directory for outputted results
try:
    os.makedirs('html_'+now)
except OSError:
    if not os.path.isdir(path):
        raise

with open(csvFile) as csvfile:
    #readCSV = csv.reader(csvfile, delimiter=',')
    readCSV = csv.reader(x.replace('\0', '') for x in csvfile)
    readCSV.next() #ignore header file

    for i in readCSV:
        #print(len(i))
        file1 = open(str("html_"+now+"/"+i[2]+'.txt'),'w')
        file1.write(i[-1])
        #print(i[-1])
        file1.close()


print('Finished')
