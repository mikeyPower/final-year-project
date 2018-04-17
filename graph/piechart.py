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

#Filter data to plot
x_col=()
y_col=[]
csvFile = sys.argv[1]
with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    a=readCSV.next() #Skip first line (Header line)
    for i in readCSV:
        #print(i)
        x_col=x_col+(i[0],)
        y_col.append(int(i[1]))

sns.set()
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

#http://www.color-hex.com/color-palette/5361
cols =['#ffb3ba',
    '#bae1ff',
	'#ffdfba',
	'#ffffba',
	'#baffc9']


#http://www.color-hex.com/color-palette/45191
cols1=['#4aac59',
	'#4348e6',
	'#4e1b7b',
	'#fffa99',
	'#727272']


cols2=['#e6194b','#3cb44b',	'#0082c8', '#f58231','#911eb4',
	'#46f0f0',	'#f032e6'	,'#d2f53c'	,'#fabebe',	'#008080'	,'#e6beff'	,'#aa6e28',
     '#fffac8',	'#800000',	'#aaffc3',	'#808000',	'#000080',	'#808080', '#FFFFFF','#000000','#ffe119']

fig1, ax1 = plt.subplots()
patches, texts, autotexts = ax1.pie(y_col, explode=None, autopct='%1.1f%%',
shadow=False, startangle=90, colors=cols2)#,labels=x_col)
ax1.axis('equal')
#fig1.set_facecolor('w') #change canvas color
plt.title(a[0])

#Change font size
proptease = fm.FontProperties()
#proptease.set_size('small')
plt.setp(autotexts, fontproperties=proptease)
plt.setp(texts, fontproperties=proptease)


#Shrink current axis by 20%
#box = ax1.get_position()
#ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])


#plt.legend(patches, zip(x_col,percent), loc="best",bbox_to_anchor=(0.8, 0.5)) display name and percentage
plt.legend(patches, x_col, loc="best")#bbox_to_anchor=(0.8, 0.85),prop={'size':None})

#plt.show() # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig("Ips to Hostname.png")
