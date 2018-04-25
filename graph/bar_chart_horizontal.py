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

#Filter data to plot
x_col=()
y_col=[]
csvFile = sys.argv[1]
with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    a=readCSV.next() #Skip first line (Header line)
    for i in readCSV:
        x_col=x_col+(i[0],)
        y_col.append(int(i[1]))

y_pos = np.arange(len(x_col))

color_list=[]

for name, hex in matplotlib.colors.cnames.iteritems():#and count < len(y_col):
    color_list.append(name)

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

fig1, ax1 = plt.subplots()
for i,j,k,l in zip(y_pos,y_col,cols1,x_col):

    #print(i, j,k,l)
    rects=ax1.barh(i, int(j),align='center',color=k,label=l)
    #for rect in rects:
    #    height = rect.get_height()
    #    ax1.text(i, j,
        #        '%d' % int(height),
        #        ha='center', va='bottom')
ax1.set_yticks(y_pos)
#ax1.set_yticklabels(x_col)
#plt.yticks(fontsize=4.5)

#pick an x-axis label
plt.xlabel('Number of IP addresses')


#pick an x-axis label
plt.ylabel('Cipher Suites')

#pick a y-axis label
#plt.ylabel(a[0])

#Pick a title
#plt.title('Request of IP addresses on Both Ports to Port 80')
plt.title('Cipher Suites In TCD')


#ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')


#Shrink current axis by 20%
#box = ax1.get_position()
#ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])

#plot legend
plt.legend(x_col, loc="best",prop={'size':10})#bbox_to_anchor=(1, 0.5))


#plt.show()
#plt.savefig("Request of IP addresses on Both Ports to Port 80.png")
plt.savefig("Cipher Suites In TCD.svg")
