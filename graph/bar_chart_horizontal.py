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


fig1, ax1 = plt.subplots()
for i,j,k,l in zip(y_pos,y_col,color_list,x_col):

    print(i, j,k,l)
    rects=ax1.barh(i, int(j),align='center', alpha=0.5,color=k,label=l)
    #for rect in rects:
    #    height = rect.get_height()
    #    ax1.text(i, j,
        #        '%d' % int(height),
        #        ha='center', va='bottom')
ax1.set_yticks(y_pos)
ax1.set_yticklabels(x_col)
plt.xlabel('Amount')
plt.title(a[0])



# Shrink current axis by 20%
#box = ax1.get_position()
#ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
plt.legend(x_col, loc="best")#bbox_to_anchor=(1, 0.5))


plt.show()
