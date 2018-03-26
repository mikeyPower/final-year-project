import csv
import sys
from functions import dateRange
'''
This script outputs the number of ips that are considered stable( i.e continuosly up for a given period) and those not considered
stable. As well as taking account for what port the ip is found on

A smaple command that can be proformed is as follows:
python range.py 5/2/2018 5/6/2018 14 21 tmp.csv

The date is structured as (day/month/year)
With time as 24 hour

This command will output the number of stable and non stable Ips between 5/2/2018T14 to 5/6/2018T21 i.e the only information we
want is between those time times between those days

NOTE:
Duplicated Entries are removed with the use of sets()
'''

#If need all info could seperate by using a delimiter and then splitting to convert back them if too heavy with nesting of arrays


#Need to define 4 parameter
#Parameters: x = starting time hour
#                     y = ending time hour
#                     z = starting date
#                     v = end date
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

#print(startday,startmonth,startyear,endDay,endMonth, endYear,startTime, endTime)
dateIsoSub =dateRange(startday,startmonth,startyear,endDay,endMonth, endYear, startTime,endTime)

with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    mostCount =0
    mostDate =''

#create a list of times substring till the hour of the csv file
    dates = [x[-3][:13] for i, x in enumerate(readCSV)]


#this creates a dictionary with the keys being the date and values being a list of ips with port number at those date
    dateIsoSub = dateRange(startday,startmonth,startyear,endDay,endMonth, endYear, startTime,endTime)
    dictionary = {}
    for t in dateIsoSub:
        with open(csvFile) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            dictionary[t] =[x[0]+'P'+x[6] for j, x in enumerate(readCSV) if x[-3][:13] == t]


    #get the intersection of all the ips at certain times to find the most stableIps
    intersectSet =dictionary.values()[0]
    for key, values in dictionary.items():

        #print(key)
        if key == dictionary.keys()[0]: ##skip the first value in dictionary
             continue
        else:
            intersectSet = list(set(values)& set(intersectSet))
    print('Number of ips that are constent',len(intersectSet))


	#get the unstable ip address
    difSet = []
    for key, values in dictionary.items():
        differenceSet = list(set(values) - set(intersectSet))
        difSet.extend(differenceSet)
    print('Number of ips that are inconsistent',len(difSet))

    #for i in difSet:
    #    print(i)
    #This creates an array of all the fields outputed by zmap for every ip that is found to be unstable i.e not
    #consistently up for the given range
    nonStableIps = []
    for t in difSet:
        with open(csvFile) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            nonStableIps = [x for i, x in enumerate(readCSV) if x[0]+'P'+x[6] == t]
