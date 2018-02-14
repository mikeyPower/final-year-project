import csv
import dateutil.parser
import pandas as pd
import datetime
from datetime import timedelta, date
import sys
'''
This script outputs the number of ips on both port 80 and 443 at a given time, writing the peak time all it's ips to a csv csv
while also writing the lowest number of ips at a given time to a csv file

example run:
python peak-nonpeak.py 5/2/2018 5/6/2018 14 21 tmp.csv



NOTE:
Should give the option to specifiy what ports you want to see or all ports
'''

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

start = datetime.date(startyear, startmonth, startday)#Actualy started on the 06/02/2018T00
end = datetime.date(endYear, endMonth, endDay)

dateIsoSub = []
datelist = pd.date_range(start, end, freq='1H').tolist()
index = pd.Index(datelist)
for x in index[:-1]:#loop through everything except the last element

    dateIsoSub.append(x.isoformat()[:13])


    lenght = dateIsoSub[:]
    for q in lenght:
    #print(q)
        if q[11:] < startTime:
        #print(y[11:])
            dateIsoSub.remove(q)
        elif q[11:] > endTime:
            dateIsoSub.remove(q)
        else:
            continue

    #break
with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    mostCount =0
    mostDate =''

    dates = []
#create a list of times substring till the hour of the csv file
    for t in readCSV:
        dates.append(t[-3][:13])

#count how many times each date occurence occurs within the dates array from 06/02/2018T00 - 12/02/2018T23
    results = []
    for q in dateIsoSub:
        r = dates.count(q)
        results.append(r)
        print(r,q)


#Print the min and max hour as well as the index to which they occur in the results array
    print('\n')
    minIndex = results.index(min(results))
    print(results[minIndex], dateIsoSub[minIndex])
    maxIndex = results.index(max(results))
    print(results[maxIndex], dateIsoSub[maxIndex])

#write all the ip address that have the timestamp that coralates with the most ip address in the college
    with open(csvFile) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        open('peakIps.csv', 'w').close()
        open('notPeakIps.csv','w').close()
        for u in readCSV:
            if u[-3][:13] == dateIsoSub[maxIndex]:
               with open("peakIps.csv", "a") as myfile:
			   writer=csv.writer(myfile)
			   writer.writerow(u)
               myfile.close()
               #print(u)
               #break
            elif u[-3][:13] == dateIsoSub[minIndex]:
                with open("notPeakIps.csv","a") as  myfile2:
                             writer=csv.writer(myfile2)
                             writer.writerow(u)
                myfile2.close()
            else:
               #break
               continue
