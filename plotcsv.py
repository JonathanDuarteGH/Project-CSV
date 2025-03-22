import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime, timedelta
import numpy as np

# Import the file metadata
##Define the filename

str_filename = "test_002_000.csv"

##Open the file and instantiate the csv reader

fh = open(str_filename)
csv_reader = csv.reader(fh)

##Read in the header labels

csv_header = next(csv_reader)
# Out[1] ['X', 'CH1', 'CH2']

##Read in the dates, first as a string, then convert to a datetime

lst_dt_csv = next(csv_reader)
# Out[2] ['Date and Time',
# Out[3]  '2021-12-09 05:36:10.782-08:00',
# Out[4]  '2021-12-09 05:36:10.782-08:00']

dt_csv = np.array(list(map(datetime.fromisoformat, lst_dt_csv[1:3])))
# Out[5] array([datetime.datetime(2021, 12, 9, 5, 36, 10, 782000, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=57600))),
# Out[6]        datetime.datetime(2021, 12, 9, 5, 36, 10, 782000, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=57600)))],
# Out[7]        dtype=object)

##Read in the sampling frequency

lst_fs = next(csv_reader)
np_d_fs = np.array(list(map(float, lst_fs[1:3])))
# OUT[8] array([1305.625068, 1305.625068])

##Close the file

fh.close()

# Construct the dataframe
df_sig = pd.read_csv(str_filename, header=None, skiprows=5, names=csv_header)

# Plot the dataframe data

df_sig.CH1.plot()
plt.xlabel("Sample number")
plt.xlim([0, 1200])
plt.ylabel("Signal value, volts")
plt.ylim([-0.5, 0.5])
plt.title("CSV data")
plt.grid()


figure = plt.gcf()
figure.set_size_inches(4 * 1.6, 4)
plt.savefig("CSV Visualization.pdf")

ns = len(df_sig.index)

assert abs(np_d_fs[0] - np_d_fs[1]) < 1e-15, (
    "The sampling frequency (fs) must be the same for both data series"
)

df_sig["elap_time"] = np.linspace(0, (ns - 1), ns) / np_d_fs[0]

df_sig.plot("elap_time", "CH1")
plt.xlabel("Elapsed time, seconds")
plt.xlim([min(df_sig.elap_time), max(df_sig.elap_time)])
plt.ylabel("Signal value, volts")
plt.ylim([-0.5, 0.5])
plt.title("CSV data (Elapsed Time)")
plt.grid()


figure = plt.gcf()
figure.set_size_inches(4 * 1.6, 4)
plt.savefig("CSV Visualization_ElapsedTime2.pdf")

assert dt_csv[0] == dt_csv[1], "Both datetime stamps must be the same"

add_secs = lambda np_sec: [dt_csv[0] + timedelta(seconds=d_sec) for d_sec in np_sec]

df_sig["dt"] = add_secs(df_sig["elap_time"].to_numpy(dtype=float))

df_sig = df_sig.set_index("dt")

df_sig.head()

##Out[9]
#                                     X	CH1	    CH2	    elap_time
#                               dt
# 2021-12-09 05:36:10.782000-08:00	0	0.05	-0.024	0.000000
# 2021-12-09 05:36:10.782766-08:00	1	0.02	0.048	0.000766
# 2021-12-09 05:36:10.783532-08:00	2	0.02	-0.008	0.001532
# 2021-12-09 05:36:10.784298-08:00	3	0.06	0.064	0.002298
# 2021-12-09 05:36:10.785064-08:00	4	0.02	0.136	0.003064

dt_local = df_sig.index.to_pydatetime()

plt.plot(dt_local, df_sig["CH1"])

# This changes the formatter.
plt.gca().xaxis.set_major_formatter(
    matplotlib.dates.DateFormatter("%Y-%m-%d %H:%M:%S.%f")
)

plt.xlabel("Date and time")
plt.xlim([min(dt_local), max(dt_local)])
plt.xticks(dt_local, rotation=45)
plt.locator_params(axis="x", nbins=4)

plt.ylabel("Signal value, volts")
plt.ylim([-0.5, 0.5])
plt.title("CSV data (Timeseries)")
plt.grid()


figure = plt.gcf()
figure.set_size_inches(4 * 1.6, 4)
plt.savefig("CSV Visualization_TimeSeries3.pdf")
