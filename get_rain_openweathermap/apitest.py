# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:58:17 2015

@author: stvhoey
"""

import requests
import datetime, calendar
import pandas as pd

startdate = datetime.datetime(2015, 9, 1, 0, 0)
enddate = datetime.datetime(2015, 9, 8, 0, 0)

# http://openweathermap.org -  API REQUEST
response = requests.get("http://api.openweathermap.org/data/2.5/history/city?q=Ghent,\
                        BE&type=hour&start=%d&end=%d"%(calendar.timegm(startdate.timetuple()), calendar.timegm(enddate.timetuple())))
data = response.json()

rain_info = {}
for record in data['list']:
    try:
        rain_info[datetime.datetime.fromtimestamp(record['dt'])] = record['rain'].values()[0]
    except:
        rain_info[datetime.datetime.fromtimestamp(record['dt'])] = 0.0

raindata = pd.Series(rain_info)

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.vlines(raindata.index, np.zeros(len(raindata)), raindata.values)
ax.xaxis.set_major_locator(
                mpl.dates.DayLocator())
ax.xaxis.set_major_formatter(
                mpl.dates.DateFormatter('%d %b \n %Y'))
