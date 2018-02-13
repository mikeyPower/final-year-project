import csv
import dateutil.parser
import pandas as pd
import datetime
from datetime import timedelta, date

start = datetime.date(2018, 2, 5)#Actualy started on the 06/02/2018
end = datetime.date(2018, 2, 13)
dateIso = []
dateIsoSub = []
datelist = pd.date_range(start, end, freq='1H').tolist()
index = pd.Index(datelist)
for x in index:
	dateIso.append(x.isoformat())
	dateIsoSub.append(x.isoformat()[:13])

with open('tmp.csv') as csvfile:
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
    #print(minIndex, dateIsoSub[minIndex])
    maxIndex = results.index(max(results))
    #print(maxIndex, dateIsoSub[maxIndex])

#write all the ip address that have the timestamp that coralates with the most ip address in the college
    with open('tmp.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for u in readCSV:
            if u[-3][:13] == dateIsoSub[maxIndex]:
               with open("test2.csv", "a") as myfile:
			   writer=csv.writer(myfile)
			   writer.writerow(u)
               myfile.close()
               #print(u)
               #break
            else:
               #break
               continue
