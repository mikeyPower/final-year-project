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
from matplotlib import font_manager as fm
from matplotlib import cm


#Get timestamp of programme execution
now=str(int(time.time()))
str_now=str(datetime.now())

x_col=()
y_col=[]
csvFile = sys.argv[1]
with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    readCSV.next() #Skip first line (Header line)
    for i in readCSV:
        x_col=x_col+(i[0],)
        y_col.append(int(i[1]))


percent=[]
for i in y_col:
    percent.append("{0:.1f}".format((float(i)/sum(y_col))*100))

y_pos = np.arange(len(x_col))
performance = y_col

color_list =[]
for name, hex in matplotlib.colors.cnames.iteritems():
    color_list.append(name)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

#a=np.random.random(40)
#cs=cm.Set1(np.arange(40)/40.)

fig1, ax1 = plt.subplots()
patches, texts, autotexts = ax1.pie(y_col, explode=None, labels=x_col, autopct='%1.1f%%',
shadow=True, startangle=90, colors=color_list)
ax1.axis('equal')
fig1.set_facecolor('w') #change canvas color

#Change font size
proptease = fm.FontProperties()
proptease.set_size('xx-small')
plt.setp(autotexts, fontproperties=proptease)
plt.setp(texts, fontproperties=proptease)

'''
index =0
for i in y_col:
    print(y_pos,int(i),str(x_col[index]))
    #plt.plot(y_pos[index], label=str(x_col[index]))
    index=index+1
'''
#plot legend
plt.legend(patches, zip(x_col,percent), loc="best")

plt.show() # Equal aspect ratio ensures that pie is drawn as a circle.
