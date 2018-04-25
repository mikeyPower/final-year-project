#!/usr/bin/python
import csv
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime
import dateutil.parser
import matplotlib.dates as mdates
from matplotlib.dates import HourLocator
import seaborn as sns
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

        '''
        #slit the iso time format in order to find hour
        #for average day
        j=i[0].split('T')

        x_col.append(dateutil.parser.parse(i[0]))
        y_col1.append(int(i[1]))
        y_col2.append(int(i[2]))
        y_col3.append(int(i[3]))

        #combine port 80 only, port 443 only and both ports
        if (j[1] in dictionary):
            dictionary[j[1]].append(int(i[1])+int(i[2])+int(i[3]))
        elif j[1] not in dictionary:
            dictionary[j[1]] = [int(i[1])+int(i[2])+int(i[3])]
            '''
#Used for Maximum Irregular ip addresses with copy irreg_ips============
        column = 0
        length = length +1
        for k in i:
            counts[column]=counts[column]+int(k)
            if int(k) >=1:
                noIPs[column]=noIPs[column]+1
            column = column +1

#======================================================================

print(length)
column=0
for i in counts:
    #counts[column]=counts[column]/length
    column=column+1

print(counts)
print(noIPs)
hoursNew =[]
for i in hoursN:
    hoursNew.append(dateutil.parser.parse('2018-03-23T'+i))


#Find what the average day looks like
hours=[]
averageNoOfIps=[]
orderedDictionary = collections.OrderedDict(sorted(dictionary.items()))
print(len(dictionary))
for k, v in orderedDictionary.items():
    hours.append(dateutil.parser.parse('2018-03-23T'+k))
    averageNoOfIps.append(sum(v)/len(v))


print(averageNoOfIps)
#sns.set()
#current_palette =sns.set_palette("husl")
sns.set_style("ticks")

#http://colorbrewer2.org/#type=qualitative&scheme=Set1&n=8
#see pie chrt for original
#After lightenning
cols1=['#ea4748','#5898cd','#6ec06c','#af6db9','#ff9832','#ffff5b','#cf713b','#f89acb']




cols2=['#e6194b','#3cb44b',	'#0082c8', '#f58231','#911eb4',
	'#46f0f0',	'#f032e6'	,'#d2f53c'	,'#fabebe',	'#008080'	,'#e6beff'	,'#aa6e28',
     '#fffac8',	'#800000',	'#aaffc3',	'#808000',	'#000080',	'#808080', '#FFFFFF','#000000','#ffe119']





fig, ax = plt.subplots()
#plt.xlabel('Time (Date:Hour:Minute)')
plt.xlabel('Time (Hour:Minute)')




#Pick a y-labe
plt.ylabel('Number of IP addresses')
#plt.ylabel('Number of Times Seen')





#Pick a title
#plt.title('Variation in IP addresses on Port 80 (only) over Time')
#plt.title('Variation in IP addresses on Port 443 (only) over Time')
#plt.title('Variation in IP addresses on Both Ports over Time')
#plt.title('Average Day in Trinity College Dublin')
plt.title('Maximum Number of Irregular IP addresses')
#plt.title('Total number occurences of Irregular IP addresses')

# plot graph
#ax.plot(x_col,y_col1,c=cols1[0],linestyle='dashed', marker='o')#,alpha=0.8) #Port80 Only
#ax.plot(x_col,y_col2,c=cols1[1],linestyle='dashed', marker='o')#,alpha=0.8) #Port 443 Only
#ax.plot(x_col,y_col3,c=cols1[2],linestyle='dashed', marker='o')#,alpha=0.8) #Both Ports
#ax.plot(hours,averageNoOfIps,c=cols1[3],linestyle='dashed', marker='o') #average day  of Trinity
ax.plot(hoursNew,noIPs,c=cols1[4],linestyle='dashed', marker='o')#,alpha=.8) #Maximum Number of Irregular IP addresses In an Average Day
#ax.plot(hoursNew,counts,c=cols1[6],linestyle='dashed', marker='o')#,alpha=0.8) #Total number of occurences of Irregular Ip addresses on Average

#format date on x axis
#xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')#show day month year hours minutes
xfmt = mdates.DateFormatter('%H:%M') #Show hours and minutes



ax.xaxis.set_major_formatter(xfmt)
plt.xticks(fontsize=None, rotation= 90 )

#ax.xaxis.set_major_locator(HourLocator(interval=120))#everything else
ax.xaxis.set_major_locator(HourLocator(interval=1))#For average day of Trinity

ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

plt.gcf().autofmt_xdate()
#plt.show()
#plt.savefig("Variation in Ip addresses on Port 80 over Time.svg")
#plt.savefig("Variation in IP addresses on Port 443 over Time.svg")
#plt.savefig("Variation in Ip addresses on Both Ports over Time.svg")
#plt.savefig("Average Day in Trinity College Dublin.svg")
plt.savefig("Maximum Number of Irregular IP addresses In an Average Day.svg")
#plt.savefig("Total number occurences of Irregular IP addresses on Average.svg")
