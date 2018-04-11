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
csvFile = sys.argv[1]
with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    a=readCSV.next() #Skip first line (Header line)
    for i in readCSV:
        x_col=x_col+(i[0],)
        y_col.append(int(i[1]))

y_col_tuple =tuple(y_col)
print(y_col_tuple)
y_pos = np.arange(len(x_col))




color_list=[]

for name, hex in matplotlib.colors.cnames.iteritems():#and count < len(y_col):
    color_list.append(name)


fig1, ax1 = plt.subplots()
for i,j,k,l in zip(y_pos,y_col,color_list,x_col):
#ax1.bar(y_pos, performance, align='center', alpha=0.5,color=color_list,label=x_col)
    #print(i, j,k,l)
    rects=ax1.bar(i, int(j), align='center', alpha=0.5,color='navy',label=l)
    for rect in rects:
        height = rect.get_height()
        ax1.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')


for i,j,k,l,m in zip(y_pos,y_col,color_list,x_col,y_col_tuple):
    rects=ax1.bar(i, int(j), align='center', alpha=0.5,color='lightpink',label=l,bottom=m)
    for rect in rects:
        height = rect.get_height()
        ax1.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')
    #ax1.text(i, int(j), str(j), color='blue', fontweight='bold')
plt.xticks(y_pos, [],fontsize=5, rotation=90)#rotation=90
plt.ylabel('Amount')
plt.title(a[0])


# Shrink current axis by 20%
#box = ax1.get_position()
#ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
plt.legend(x_col, loc="best")#bbox_to_anchor=(1, 0.5))


plt.show()
