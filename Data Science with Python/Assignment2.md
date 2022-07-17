# Assignment 2

Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to Preview the Grading for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.

An NOAA dataset has been stored in the file data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv. This is the dataset to use for this assignment. Note: The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) Daily Global Historical Climatology Network (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.

Each row in the assignment datafile corresponds to a single observation.

The following variables are provided to you:

id : station identification code
date : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
element : indicator of element type
TMAX : Maximum temperature (tenths of degrees C)
TMIN : Minimum temperature (tenths of degrees C)
value : data value for element (tenths of degrees C)

For this assignment, you must:

Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.

Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.

Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.

Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.

The data you have been given is near Ann Arbor, Michigan, United States, and the stations the data comes from are shown on the map below.

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
​
´´´{
def leaflet_plot_stations(binsize, hashid):

  &nbsp;&nbsp;  df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))
​
  &nbsp;&nbsp;  station_locations_by_hash = df[df['hash'] == hashid]
​
&nbsp;&nbsp; lons = station_locations_by_hash['LONGITUDE'].tolist()
    &nbsp;&nbsp; lats = station_locations_by_hash['LATITUDE'].tolist()
​
    &nbsp;&nbsp;  plt.figure(figsize=(8,8))
​
    &nbsp;&nbsp; plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

​
    &nbsp;&nbsp; return mplleaflet.display()
​}'''



## CODE STARTS HERE

% matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

### LOAD AND EXPLORE DATA
```
df = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
print(df.head())
df.shape
print(df.columns)
print(df.info())

```

Index  | ID  | Date  | Element  | Data_Value
--|---|---|---|--
0  | USW00094889  | 2014-11-12  | TMAX  | 22
1  | USC00208972  | 2009-04-29  | TMIN  | 56
2  | USC00200032  | 2008-05-26  | TMAX  | 278
3  | USC00205563  | 2005-11-11  | TMAX  | 139
4  | USC00200230  | 2014-02-27  | TMAX  | -106


Index(['ID', 'Date', 'Element', 'Data_Value'], dtype='object')

<class 'pandas.core.frame.DataFrame'>

RangeIndex: 165085 entries, 0 to 165084
Data columns (total 4 columns):
```
| ID |            | 165085 | non-null object |
| Date |          | 165085 | non-null object |
| Element |       | 165085 | non-null object |
| Data_Value |    | 165085 | non-null int64  |
```
```
dtypes: int64(1), object(3)
memory usage: 5.0+ MB
None
```

### NUMBER OF STATIONS
```
df['ID'].unique()
len(df['ID'].unique())
```

```
Out[]:
array(['USW00094889', 'USC00208972', 'USC00200032', 'USC00205563',
       'USC00200230', 'USW00014833', 'USC00207308', 'USC00203712',
       'USW00004848', 'USC00200220', 'USC00205822', 'USC00200842',
       'USC00205450', 'USC00201250', 'USC00207320', 'USC00200228',
       'USC00202308', 'USW00014853', 'USC00205050', 'USC00208202',
       'USC00208080', 'USC00207312', 'USC00205451', 'USC00201502'], dtype=object)
```
24

### SORTING DATE
```
df = df.sort_values(by='Date')
df.head()

df['T']=df['Data_Value']/10
df.head()
```

### REMOVE Year 2015:

#### First: create a df for 2015
```
mask2015 = df['Date'] >= '2015-01-01'
df2015 = df.where(mask2015).dropna()
print(df2015.head(10))
```
#### Second: create df without 2015:
```
mask2015 = df['Date'] < '2015-01-01'
df_less2015 = df.where(mask2015).dropna()
df_less2015.head(10)
```

  ```
         ID        Date Element  Data_Value     T   T/10
43095  USW00014833  2015-01-01    TMIN       -88.0  -8.8
51805  USC00208972  2015-01-01    TMAX       -67.0  -6.7
43140  USC00202308  2015-01-01    TMIN      -106.0 -10.6
43653  USC00200228  2015-01-01    TMAX       -50.0  -5.0
43652  USC00200228  2015-01-01    TMIN       -89.0  -8.9
51804  USC00208972  2015-01-01    TMIN      -106.0 -10.6
43141  USC00202308  2015-01-01    TMAX       -50.0  -5.0
43383  USW00014853  2015-01-01    TMAX        11.0   1.1
43337  USW00014853  2015-01-01    TMIN       -71.0  -7.1
43096  USW00014833  2015-01-01    TMAX       -21.0  -2.1
```

### REMOVE LEAP DAYS

#### Looking for Leap Days:
```
leap_days1 = df_less2015.loc[df['Date'].str.contains('2008-02-29', case = False)]
leap_days2 = df_less2015.loc[df['Date'].str.contains('2012-02-29', case = False)]
print(leap_days1.head())
print(leap_days2.head())
```
```
         ID        Date Element  Data_Value     T    T/10
135281  USC00205451  2008-02-29    TMAX       -33.0  -3.3
133079  USC00200032  2008-02-29    TMAX        17.0   1.7
123556  USC00205822  2008-02-29    TMAX       -22.0  -2.2
133727  USC00207308  2008-02-29    TMAX       -22.0  -2.2
154086  USC00208972  2008-02-29    TMIN      -128.0 -12.8
```
```
         ID       Date Element  Data_Value      T  T/10
19907  USC00208202  2012-02-29    TMIN       -56.0 -5.6
19608  USC00207308  2012-02-29    TMIN       -67.0 -6.7
23551  USW00014833  2012-02-29    TMIN         6.0  0.6
19680  USC00207312  2012-02-29    TMAX        67.0  6.7
20809  USC00208972  2012-02-29    TMAX        56.0  5.6
```
#### Masking Leap Days
```
mask = (df_less2015['Date'] != '2008-02-29') & (df_less2015['Date'] != '2012-02-29')
df_without_LD = df_less2015.where(mask).dropna()
df_without_LD.head()
```
#### Verifying leap days where dropped
```
leap_days3 = df_without_LD.loc[df['Date'].str.contains('2008-02-29', case = False)]
leap_days4 = df_without_LD.loc[df['Date'].str.contains('2012-02-29', case = False)]
print(leap_days3.head())
print(leap_days4.head())
```

### Convert Date in datetime
```
df_without_LD['Date'] = pd.to_datetime(df_without_LD['Date'], format='%Y-%m-%d')
print(df_without_LD.info())
print(df_without_LD.head())
```

### Maximum Value 'Date':
```
max_value = df_without_LD.loc[df_without_LD['Date'].idxmax()]
print(max_value)
```

#### Splitting datetime in different rows:
```
df_without_LD['day']=df_without_LD['Date'].dt.day
df_without_LD['month']=df_without_LD['Date'].dt.month
df_without_LD['year']=df_without_LD['Date'].dt.year
print(df_without_LD.head())
print(df_without_LD.info())
```
```
        ID       Date Element  Data_Value     T    T/10   day  month  year
60995  USW00004848 2005-01-01    TMIN         0.0   0.0    1      1  2005
17153  USC00207320 2005-01-01    TMAX       150.0  15.0    1      1  2005
17155  USC00207320 2005-01-01    TMIN       -11.0  -1.1    1      1  2005
10079  USW00014833 2005-01-01    TMIN       -44.0  -4.4    1      1  2005
10073  USW00014833 2005-01-01    TMAX        33.0   3.3    1      1  2005
```
<class 'pandas.core.frame.DataFrame'>
```
Int64Index: 151245 entries, 60995 to 62784
Data columns (total 8 columns):
ID            151245 non-null object
Date          151245 non-null datetime64[ns]
Element       151245 non-null object
Data_Value    151245 non-null float64
T             151245 non-null float64
day           151245 non-null int64
month         151245 non-null int64
year          151245 non-null int64
dtypes: datetime64[ns](1), float64(2), int64(3), object(2)
memory usage: 10.4+ MB
None
```
### Dividing df into dfs

#### Divide df_without_LP in 2 news df, one with values TMAX e another with values TMIN:

***Same system Boolean mask:***

##### TMIN:
```
mask_MIN = df_without_LD['Element'] != 'TMAX'
df_TMIN = df_without_LD.where(mask_MIN).dropna()
df_TMIN.head()
```

##### TMAX:
```
mask_MAX = df_without_LD['Element'] != 'TMIN'
df_TMAX = df_without_LD.where(mask_MAX).dropna()
df_TMAX.head()
```

### Working with the news dfs:

#### **_TMAX_**
##### Finding the TMAX for each Day:
```
MAX_day = df_TMAX.groupby(['Date'])['T'].transform(max) == df_TMAX['T']
df_MAX_day = df_TMAX[MAX_day]
df_MAX_day.head(30)
```

##### Dropping duplicates based in 'Date':
```
df_MAX_day.Date.duplicated()
df_MAX_day = df_MAX_day.drop_duplicates(subset=['Date'],keep='last')
df_MAX_day.head(10)
```

##### Grouping per month and day:
```
max_temp = df_MAX_day.groupby([(df_MAX_day['month']),(df_MAX_day['day'])])['T'].max()
max_temp = pd.DataFrame(max_temp).reset_index()
print(max_temp.head())
print(len(max_temp))
```
```
        Month    Day      T
| 0 |  | 1.0 | | 1.0 | | 15.6 |
| 1 |  | 1.0 | | 2.0 | | 13.9 |
| 2 |  | 1.0 | | 3.0 | | 13.3 |
| 3 |  | 1.0 | | 4.0 | | 10.6 |
| 4 |  | 1.0 | | 5.0 | | 12.8 |
```
365

#### **_TMIN_**

##### Finding the TMIN for each day:
```
MIN_day = df_TMIN.groupby(['Date'])['T'].transform(min) == df_TMIN['T']
df_MIN_day = df_TMIN[MIN_day]
df_MIN_day.head(30)
```

##### Dropping duplicates based in 'Date':
```
df_MIN_day.Date.duplicated()
df_MIN_day = df_MIN_day.drop_duplicates(subset=['Date'],keep='last')
df_MIN_day.head()
```

##### Grouping per month and day:
```
min_temp = df_MIN_day.groupby([(df_MIN_day['month']),(df_MIN_day['day'])])['T'].min()
min_temp = pd.DataFrame(min_temp).reset_index()
print(min_temp.head())
```
```
        Month    Day       T
| 0 |  | 1.0 | | 1.0 | | -16.0 |
| 1 |  | 1.0 | | 2.0 | | -26.7 |
| 2 |  | 1.0 | | 3.0 | | -26.7 |
| 3 |  | 1.0 | | 4.0 | | -26.1 |
| 4 |  | 1.0 | | 5.0 | | -15.0 |
```
### Extracting TMAX and TMIN 2015

###### Convert Date in datetime
```
df2015['Date'] = pd.to_datetime(df2015['Date'], format='%Y-%m-%d')
print(df2015.info())
```

##### Splitting datetime in different rows:
```
df2015['day']=df2015['Date'].dt.day
df2015['month']=df2015['Date'].dt.month
df2015['year']=df2015['Date'].dt.year
print(df2015.head())
```

```
         ID       Date Element  Data_Value     T   T/10  day  month  year
43095  USW00014833 2015-01-01    TMIN       -88.0  -8.8    1      1  2015
51805  USC00208972 2015-01-01    TMAX       -67.0  -6.7    1      1  2015
43140  USC00202308 2015-01-01    TMIN      -106.0 -10.6    1      1  2015
43653  USC00200228 2015-01-01    TMAX       -50.0  -5.0    1      1  2015
43652  USC00200228 2015-01-01    TMIN       -89.0  -8.9    1      1  2015
```
#### **_TMIN 2015_**

##### TMIN_2015:
```
mask_MIN2015 = df2015['Element'] != 'TMAX'
df_TMIN2015 = df2015.where(mask_MIN2015).dropna()
df_TMIN2015.head()
```

##### Finding the TMIN for each day:
```
MIN_day2015 = df_TMIN2015.groupby(['Date'])['T'].transform(min) == df_TMIN2015['T']
df_MIN_day2015 = df_TMIN2015[MIN_day2015]
df_MIN_day2015.head(30)
```
##### Dropping duplicates based in 'Date':
```
df_MIN_day2015.Date.duplicated()  **#verification    existence duplicates**
df_MIN_day2015 = df_MIN_day2015.drop_duplicates(subset=['Date'],keep='last')
df_MIN_day2015.head()
```

##### Grouping per month and day:
```
min_temp2015 = df_MIN_day2015.groupby([(df_MIN_day2015['month']),(df_MIN_day2015['day'])])['T'].min()
min_temp2015 = pd.DataFrame(min_temp2015).reset_index()
print(min_temp2015.head())
```
```
         Month   Day       T
| 0 |  | 1.0 | | 1.0 | | -13.3 |
| 1 |  | 1.0 | | 2.0 | | -12.2 |
| 2 |  | 1.0 | | 3.0 | | -6.7 |
| 3 |  | 1.0 | | 4.0 | | -8.8 |
| 4 |  | 1.0 | | 5.0 | | -15.5 |
```
#### **_TMAX 2015_**

##### TMAX_2015:
```
mask_MAX2015 = df2015['Element'] != 'TMIN'
df_TMAX2015 = df2015.where(mask_MAX2015).dropna()
df_TMAX2015.head()
```

##### Finding the TMAX for each Day:
```
MAX_day2015 = df_TMAX2015.groupby(['Date'])['T'].transform(max) == df_TMAX2015['T']
df_MAX_day2015 = df_TMAX2015[MAX_day2015]
df_MAX_day2015.head(30)
```

##### Dropping duplicates based in 'Date':
```
df_MAX_day2015.Date.duplicated()
df_MAX_day2015 = df_MAX_day2015.drop_duplicates(subset=['Date'],keep='last')
df_MAX_day2015.head(10)
```

##### Grouping per month and day:
```
max_temp2015 = df_MAX_day2015.groupby([(df_MAX_day2015['month']),(df_MAX_day2015['day'])])['T'].max()
max_temp2015 = pd.DataFrame(max_temp2015).reset_index()
print(type(max_temp2015))
print(max_temp2015.head())
print(max_temp2015.shape)
```

<class 'pandas.core.frame.DataFrame'>
```
        Month    Day      T
| 0 |  | 1.0 | | 1.0 | | 1.1 |
| 1 |  | 1.0 | | 2.0 | | 3.9 |
| 2 |  | 1.0 | | 3.0 | | 3.9 |
| 3 |  | 1.0 | | 4.0 | | 4.4 |
| 4 |  | 1.0 | | 5.0 | | 2.8 |
```
(365, 3)

### Comparing data 2015 and the other years, to the scatterplot:
```
record_high = max_temp2015[max_temp2015['T'] > max_temp['T'] ]
record_low = min_temp2015[min_temp2015['T'] < min_temp['T'] ]
print(len(record_high))
print(record_low.head())
```

37
```
         Month    Day       T
| 4 |   | 1.0 | | 5.0 | | -15.5 |
| 10 |  | 1.0 | | 11.0 | | -20.0 |
| 33 |  | 2.0 | | 3.0 | | -23.8 |
| 44 |  | 2.0 | | 14.0 | | -23.9 |
| 45 |  | 2.0 | | 15.0 | | -26.0 |
```
## Plotting part

### Setting de ticks:
#### x ticks 2015:
```
xticks = (pd.date_range('1/1/2015','31/12/2015', freq = 'M') -1 + pd.Timedelta('1D')).strftime('%-j').astype(int)
xticks
```
```
Out[ ]:
array([  1,  32,  60,  91, 121, 152, 182, 213, 244, 274, 305, 335])
```
#### x ticks 2015 labels:
```
xticks_labels = pd.to_datetime(xticks, format = '%j').strftime('%b')
xticks_labels
```
```
Out[ ]:
array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
       'Oct', 'Nov', 'Dec'],
      dtype='<U3')
```

### Create a list from temperature MAX values and temperature MIN values and days to plot LINE:

#### TMAX list:
```
list_TMAX = max_temp['T'].tolist()
```
#### TMIN list:
```
list_MIN = min_temp['T'].tolist()
```


## **_PLOTTING_**
```
fig = plt.figure()
ax = plt.axes()
```

### Working with the axes limits, x/y labels, graph title and setting xticks
```
ax.set(ylim=(-35,45), xlim=(0,365),xlabel='Month', ylabel='Temperature( °C)', title= 'Record High&Low - Temperature x Day (2005-2014)')
plt.xticks(xticks,xticks_labels)
plt.tick_params(left=False,bottom=False)
```

### PLOTTING LINE GRAPH:

**(a) Preparing points to plot:**
```
y1points = np.array(list_TMAX)
y2points = np.array(list_MIN)
```

**(b) Plotting, working line thickness, color and line intensity:**
```
#plt.plot(df_MAX_day['T'], c='b')  --> option
#plt.plot(df_MIN_day['T'], c='r')  --> option
```
```
top = plt.plot(y1points,c='r',alpha = 0.3, linewidth=1)
down = plt.plot(y2points,c='b',alpha = 0.5, linewidth=1)
plt
```

### PLOTTING SCATTER:

```
plt.scatter(record_high.index, record_high['T'], s=20, c='r',linewidths=0.1)
plt.scatter(record_low.index, record_low['T'], s=20, c='b',linewidths=0.1)
```

### LEGEND
```
plt.legend(loc=0,labels = ['Tmax(2005-2014)','Tmin (2005-2014)', 'Record T-High','Record T-Low'],frameon=False, fontsize = 'x-small')
```

### FILL BETWEEN LINES:
```
ax.fill_between(range(0,365) , y1points, y2points, facecolor='gray', alpha=0.2 )
```
```
plt.show()
```
![Record High&Low](images/2022/07/record-high-low.png)
