"""case 4

1.  Create a new factor variable in the dataset with two levels
    "weekday" and "weekend" indicating whether a given date is a weekday or weekend.

2.  Make a plot containing a time series plot of the 5-minute interval
    (x-axis) and the average number of steps taken,
    average across all weekdays or weekends(y-axis)"""

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

df = pd.read_csv("activity.csv")
df["date"] = pd.to_datetime(df["date"])
dow = df["date"].dt.dayofweek
df["weekday"] = np.where(dow < 5, "weekday", "weekend")

reader = csv.reader(df)
headerRow = next(reader)

dictDate = {}
dictInterval = {}
dictweek = {}
for row in reader:
    steps = row[0]
    if (steps != 'NA'):
        week = int(row[3])
        dictInterval.setdefault(week, [])
        dictInterval[week].append(int(steps))

listWeekend = []
listWeekday = []

for i in dictInterval.keys():
        listweekend.append(sum(dictweek.get(i)))
        listweekdays.append(sum(dictweek.get(i)))

plt.plot(list(dictweek.keys("weekend")), listWeekend, c="red")
plt.plot(list(dictweek.keys("weekdays")), listWeekday, c="blue")
plt.title("Average Daily Activity")
plt.xlabel("Time Interval")
plt.ylabel("Average number of steps taken")
plt.show()



