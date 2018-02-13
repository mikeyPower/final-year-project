import sys
import csv

'''
This script simple finds all occurance of a given ip and prints them to the screen

input.py 134.226.63.120 tmp.csv

'''

ip =  sys.argv[1]
csvFile = sys.argv[2]




with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    ipMatch = [x for i, x in enumerate(readCSV) if x[0] == ip]


    for i in ipMatch:
        print(i)
