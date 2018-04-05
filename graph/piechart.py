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
    a=readCSV.next() #Skip first line (Header line)
    for i in readCSV:
        x_col=x_col+(i[0],)
        y_col.append(int(i[1]))


#sns.set_style("whitegrid")

#Calculate percentage of each segement to one decimal place
percent=[]
for i in y_col:
    percent.append("{0:.1f}".format((float(i)/sum(y_col))*100))

y_pos = np.arange(len(x_col))
performance = y_col

#generate a list of colors
color_list =[]
for name, hex in matplotlib.colors.cnames.iteritems():
    color_list.append(name)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

#a=np.random.random(40)
#cs=cm.Set1(np.arange(40)/40.)

fig1, ax1 = plt.subplots()
patches, texts, autotexts = ax1.pie(y_col, explode=None, autopct='%1.1f%%',
shadow=True, startangle=90, colors=color_list)
ax1.axis('equal')
#fig1.set_facecolor('w') #change canvas color
plt.title(a[0])

#Change font size
proptease = fm.FontProperties()
#proptease.set_size('small')
plt.setp(autotexts, fontproperties=proptease)
plt.setp(texts, fontproperties=proptease)


#plot legend
# Shrink current axis by 20%
#box = ax1.get_position()
#ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])


#plt.legend(patches, zip(x_col,percent), loc="best",bbox_to_anchor=(0.8, 0.5)) display name and percentage
plt.legend(patches, x_col, loc="best",bbox_to_anchor=(0.8, 0.85),prop={'size':10})

plt.show() # Equal aspect ratio ensures that pie is drawn as a circle.
