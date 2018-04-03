#!/usr/bin/python
import csv
import sys
from datetime import datetime
import time
import os
import numpy as np
import matplotlib.pyplot as plt
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
csvFile = sys.argv[1]
with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    a=readCSV.next() #Skip first line (Header line)
    for i in readCSV:
        x_col=x_col+(i[0],)
        y_col.append(i[1])

y_pos = np.arange(len(x_col))
performance = y_col

color_list=[]
count=0
for name, hex in matplotlib.colors.cnames.iteritems():#and count < len(y_col):
    count=count+1
    color_list.append(name)
fig1, ax1 = plt.subplots()
for i,j,k,l in zip(y_pos,performance,color_list,x_col):
#ax1.bar(y_pos, performance, align='center', alpha=0.5,color=color_list,label=x_col)
    print(i, j,k,l)
    ax1.bar(i, int(j), align='center', alpha=0.5,color=k,label=l)
plt.xticks(y_pos, x_col,fontsize=5, rotation=90)#rotation=90
plt.ylabel('Amount')
plt.title('Programming language usage')

plt.legend(x_col, loc="best")


'''
tips2 = pd.read_csv(csvFile)
print(tips2)
sns.set_style("whitegrid")
#tips = sns.load_dataset(csvfile)
ax = sns.barplot(x=a[1], y=a[0], data=tips2)
plt.yticks(fontsize=6, rotation=0)
'''
plt.show()
