#!/usr/bin/python
import csv
import sys
from datetime import datetime
import time
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from matplotlib import cm

#Get timestamp of programme execution
now=str(int(time.time()))
str_now=str(datetime.now())

#Filter data to plot
x_col=()
y_col=[]
y_col1=[]
csvFile = sys.argv[1]
with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    a=readCSV.next() #Skip first line (Header line)
    print(a)
    for i in readCSV:
        #print(i)
        x_col=x_col+(i[0],)
        y_col.append(int(i[1]))
        y_col1.append(int(i[2]))

y_col_tuple =tuple(y_col)
print(y_col_tuple)
y_pos = np.arange(len(x_col))




color_list=[]

for name, hex in matplotlib.colors.cnames.iteritems():#and count < len(y_col):
    color_list.append(name)

#After lightenning
cols1=['#ea4748',
'#5898cd',
'#6ec06c',
'#af6db9',
'#ff9832',
'#ffff5b',
'#cf713b',
'#f89acb']

sns.set_style("ticks")

fig1, ax1 = plt.subplots()
rects=ax1.bar(y_pos,y_col, align='center', color=cols1[0],label=a[1])
for i,j,k,l in zip(y_pos,y_col,color_list,x_col):
#ax1.bar(y_pos, performance, align='center', alpha=0.5,color=color_list,label=x_col)
    print(i, j,k,l)
    #rects=ax1.bar(i, int(j), align='center', color=cols1[0],label=a[1])
    for rect in rects:
        height = rect.get_height()
        #Place value above graph
        #ax1.text(rect.get_x() + rect.get_width()/2., 1.05*height,
        #        '%d' % int(height),
        #        ha='center', va='bottom')

rects=ax1.bar(y_pos,y_col1, align='center', color=cols1[1],label=a[2])#,bottom=y_col_tuple)
for i,j,k,l,m in zip(y_pos,y_col,color_list,x_col,y_col_tuple):
    #rects=ax1.bar(i, int(j), align='center',color=cols1[1],label=a[2],bottom=m)
    for rect in rects:
        height = rect.get_height()
        #Place value above graph
        #ax1.text(rect.get_x() + rect.get_width()/2., 1.05*height,
        #        '%d' % int(height),
        #        ha='center', va='bottom')
    #ax1.text(i, int(j), str(j), color='blue', fontweight='bold')
plt.xticks(y_pos, x_col, rotation=0)#rotation=90
plt.ylabel('Number of IP addresses')
plt.xlabel('Ports')
plt.title('ZMap vs ZGrab')

ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')

#Set yxis limits
#ymin = 0
#ymax = max(y_col)+max(y_col1)+500
#axes = plt.gca()
#axes.set_ylim([ymin,ymax])

# Shrink current axis by 20%
#box = ax1.get_position()
#ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
plt.legend(['ZMap','ZGrab'], loc="best")#bbox_to_anchor=(1, 0.5))

plt.savefig("ZMap vs ZGrab.png")
#plt.show()
