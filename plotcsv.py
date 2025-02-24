import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

#Import the file metadata
##Define the filename

str_filename = 'test_002_000.csv'

##Open the file and instantiate the csv reader

fh = open(str_filename)
csv_reader = csv.reader(fh)

##Read in the header labels

csv_header = next(csv_reader)
#Out[1] ['X', 'CH1', 'CH2']

##Read in the dates, first as a string, then convert to a datetime

lst_dt_csv = next(csv_reader)
#Out[2] ['Date and Time',
#Out[3]  '2021-12-09 05:36:10.782-08:00',
#Out[4]  '2021-12-09 05:36:10.782-08:00']

dt_csv = np.array(list(map(datetime.fromisoformat, lst_dt_csv[1:3])))
#Out[5] array([datetime.datetime(2021, 12, 9, 5, 36, 10, 782000, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=57600))),
#Out[6]        datetime.datetime(2021, 12, 9, 5, 36, 10, 782000, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=57600)))],
#Out[7]        dtype=object)

##Read in the sampling frequency

lst_fs = next(csv_reader)
np_d_fs = np.array(list(map(float, lst_fs[1:3])))
#OUT[8] array([1305.625068, 1305.625068])

##Close the file

fh.close()

#Construct the dataframe
df_sig = pd.read_csv(str_filename, header=None, skiprows=5, names=csv_header)

#Plot the dataframe data

df_sig.CH1.plot()
plt.xlabel('Sample number')
plt.xlim([0, 1200])
plt.ylabel('Signal value, volts')
plt.ylim([-0.5, 0.5])
plt.title('CSV data')
plt.grid()


figure = plt.gcf()
figure.set_size_inches(4*1.6, 4)
plt.savefig('CSV Visualization.pdf')