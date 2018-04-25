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
        #y_col1.append(int(i[2]))

y_pos = np.arange(len(x_col))

color_list=[]

for name, hex in matplotlib.colors.cnames.iteritems():#and count < len(y_col):
    color_list.append(name)



#sns.set()
sns.set_style("ticks")

#After lightenning
cols1=['#ea4748',
'#5898cd',
'#6ec06c',
'#af6db9',
'#ff9832',
'#ffff5b',
'#cf713b',
'#f89acb']

cols2=['#e6194b','#3cb44b',	'#0082c8', '#f58231','#911eb4',
	'#46f0f0',	'#f032e6'	,'#d2f53c'	,'#fabebe',	'#008080'	,'#e6beff'	,'#aa6e28',
     '#fffac8',	'#800000',	'#aaffc3',	'#808000',	'#000080',	'#808080', '#FFFFFF','#000000','#ffe119']

cols3 =['#8dd3c7',
'#ffffb3',
'#bebada',
'#fb8072',#red
'#80b1d3',#blue
'#fdb462',
'#b3de69',
'#fccde5',
'#d9d9d9',
'#bc80bd',
'#ccebc5',
'#ffed6f']

#Plot graph
fig1, ax1 = plt.subplots()

for i,j,k,l in zip(y_pos,y_col,cols2,x_col):

    rects=ax1.bar(i, int(j), align='center',color=cols1[0],label=l)
    for rect in rects:
        height = rect.get_height()
    #    ax1.text(rect.get_x() + rect.get_width()/2., 1.005*height,
    #            '%d' % int(height),
    #            ha='center', va='bottom')


plt.xticks(y_pos, x_col,fontsize=None, rotation=0)

#label y-axis
plt.ylabel('Number of IP addresses')

#label x-axis
#plt.xlabel('Status Codes')
plt.xlabel('Ports')


#label title
plt.title('IP addresses to Ports')
#plt.title('Request of IP addresses on Both Ports to Port 80')



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
#plt.legend(x_col, loc="best")#bbox_to_anchor=(1, 0.5))

#Remove top and right spines
#sns.despine(ax=ax1)

#set ticks position to be only at left and bottom position
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')


#plt.show()
plt.savefig("IP addresses to Ports.svg")
#plt.savefig("Request of IP addresses on Both Ports to Port 80.svg")
