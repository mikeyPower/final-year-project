#!/usr/bin/python
import csv
import sys
from datetime import datetime
import time
import os
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import seaborn as sns
import pandas as pd
import matplotlib.pyplot
from matplotlib import cm
import matplotlib

#Get timestamp of programme execution
now=str(int(time.time()))
str_now=str(datetime.now())

x_col=()
y_col=[]
y_col1=[]
csvFile = sys.argv[1]


with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    a=readCSV.next() #Skip first line (Header line)
    for i in readCSV:
        x_col=x_col+(i[0],)
        y_col.append(int(i[1]))
        y_col1.append(int(i[2]))

y_pos = np.arange(len(x_col))

color_list=[]

for name, hex in matplotlib.colors.cnames.iteritems():#and count < len(y_col):
    color_list.append(name)



#sns.set()
sns.set_style("ticks")


cols2=['#e6194b','#3cb44b',	'#0082c8', '#f58231','#911eb4',
	'#46f0f0',	'#f032e6'	,'#d2f53c'	,'#fabebe',	'#008080'	,'#e6beff'	,'#aa6e28',
     '#fffac8',	'#800000',	'#aaffc3',	'#808000',	'#000080',	'#808080', '#FFFFFF','#000000','#ffe119']

#Plot graph
fig1, ax1 = plt.subplots()

#width of bar
width = 0.35

label=['Regualar','Irregular']
rects1=ax1.bar(y_pos-width/2, y_col, align='center', width=width,alpha=0.8,color=cols2[0],label=label[0])

rects2=ax1.bar(y_pos+width/2, y_col1, align='center', width=width,alpha=0.8,color=cols2[1],label=label[1])


plt.xticks(y_pos, x_col,fontsize=None, rotation=0)

#label y-axis
plt.ylabel('Number of IP addresses')

#label x-axis
plt.xlabel('Ports')


#label title
plt.title('Regular vs Irregular IP addresses')



#Set axis limits
#ymin = 0
#ymax = max(y_col)+50
#axes = plt.gca()
#axes.set_xlim([xmin,xmax])
#axes.set_ylim([ymin,ymax])

#Shrink current axis by 20%
#box = ax1.get_position()
#ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])

#Plot legend
plt.legend(label, loc="best")#bbox_to_anchor=(1, 0.5))

#Remove top and right spines
#sns.despine(ax=ax1)

#set ticks position to be only at left and bottom position
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')


#plt.show()
plt.savefig("Regular vs Irregular IP addresses.svg")
