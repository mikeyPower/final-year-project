import datetime
import dateutil.parser
import pandas as pd
from datetime import timedelta, date
'''
This function generates a list of timestamp in isoformat up to and including end date
e,g an input with the same start and end day will generate a empty array

Example: 5/2/2018 6/2/2018 14 21
0utput:
'2018-02-05T14'
'2018-02-05T15'
'2018-02-05T16'
'2018-02-05T17'
'2018-02-05T18'
'2018-02-05T19'
'2018-02-05T20'
'2018-02-05T21'
'2018-02-06T14'
'2018-02-06T15'
'2018-02-06T16'
'2018-02-06T17'
'2018-02-06T18'
'2018-02-06T19'
'2018-02-06T20'
'2018-02-06T21'


'''


def dateRange(startday,startmonth,startyear,endDay,endMonth, endYear, startTime,endTime):
    start = datetime.date(startyear, startmonth, startday)#Actualy started on the 06/02/2018T00
    end = datetime.date(endYear, endMonth, endDay+1)

    dateIsoSub = []
    datelist = pd.date_range(start, end, freq='1H').tolist()
    index = pd.Index(datelist)
    for x in index[:-1]:#loop through everything except the last element
        if x.isoformat()[11:13] < startTime:
            continue
        elif x.isoformat()[11:13] > endTime:
            continue
        else:
            dateIsoSub.append(x.isoformat()[:13])

    return dateIsoSub
