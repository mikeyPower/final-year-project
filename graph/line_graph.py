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

#Filter data to plot
x_col=[]
y_col1=[]
y_col2=[]
y_col3=[]
csvFile = sys.argv[1]
with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    a=readCSV.next() #Skip first line (Header line)
    for i in readCSV:
        x_col.append(dateutil.parser.parse(i[0]))
        y_col1.append(int(i[1]))
        y_col2.append(int(i[2]))
        y_col3.append(int(i[3]))

x  =np.array(x_col)
y =np.array(y_col1)



sns.set()
current_palette =sns.set_palette("husl")










fig, ax = plt.subplots()
plt.xlabel('Time')
plt.ylabel('No. of Ips')
plt.title('Variation in Ips on Both Ports over Time')

# plot
ax.plot(x_col,y_col1,c='purple',linestyle='dashed', marker='o') #Port80 Only
#ax.plot(x_col,y_col2,c='green',linestyle='dashed', marker='o') #Port 443 Only
#ax.plot(x_col,y_col3,c='red',linestyle='dashed', marker='o') #Both Ports

xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
ax.xaxis.set_major_formatter(xfmt)
plt.xticks(fontsize=None, rotation= 90 )

ax.xaxis.set_major_locator(HourLocator(interval=72))

plt.gcf().autofmt_xdate()
#plt.show()
plt.savefig("Variation in Ips on Port 80 over Time.svg")
