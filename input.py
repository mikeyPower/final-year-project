import sys
import csv

ip =  sys.argv[1]




with open('tmp.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    ipMatch = []
#create a list of times substring till the hour of the csv file
    for i in readCSV:
        if i[0] == ip:
            ipMatch.append(i)
        else:
            continue


    for i in ipMatch:
        print(i)
