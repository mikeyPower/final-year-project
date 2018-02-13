import sys
import csv

'''
This script simple finds all occurance of a given ip and prints them to the screen


'''





ip =  sys.argv[1]
csvFile = sys.argv[2]




with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    ipMatch = []
    for i in readCSV:
        if i[0] == ip:
            ipMatch.append(i)
        else:
            continue


    for i in ipMatch:
        print(i)
