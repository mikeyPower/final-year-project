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


#Get timestamp of programme execution
now=str(int(time.time()))
str_now=str(datetime.now())

x_col=()
y_col=[]
csvFile = sys.argv[1]
with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    a=readCSV.next() #Skip first line (Header line)
    #x_col=x_col+(a,)
    for i in readCSV:
        x_col=x_col+(i[0],)
        y_col.append(i[1])


tips2 = pd.read_csv(csvFile)
print(tips2)
#sns.set_style("whitegrid")
#tips = sns.load_dataset(csvfile)
ax = sns.barplot(x=a[0], y=a[1], data=tips2,ci=None,hue='Cipher Suite')
#plt.xticks(fontsize=5, rotation=90)

#plt.legend()
plt.show()
