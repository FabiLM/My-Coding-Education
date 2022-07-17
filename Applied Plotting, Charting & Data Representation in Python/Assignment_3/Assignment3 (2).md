
# Assignment 3 - Building a Custom Visualization

---

In this assignment you must choose one of the options presented below and submit a visual as well as your source code for peer grading. The details of how you solve the assignment are up to you, although your assignment must use matplotlib so that your peers can evaluate your work. The options differ in challenge level, but there are no grades associated with the challenge level you chose. However, your peers will be asked to ensure you at least met a minimum quality for a given technique in order to pass. Implement the technique fully (or exceed it!) and you should be able to earn full grades for the assignment.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ferreira, N., Fisher, D., & Konig, A. C. (2014, April). [Sample-oriented task-driven visualizations: allowing users to make better, more confident decisions.](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Ferreira_Fisher_Sample_Oriented_Tasks.pdf)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 571-580). ACM. ([video](https://www.youtube.com/watch?v=BI7GAs-va-Q))


In this [paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Ferreira_Fisher_Sample_Oriented_Tasks.pdf) the authors describe the challenges users face when trying to make judgements about probabilistic data generated through samples. As an example, they look at a bar chart of four years of data (replicated below in Figure 1). Each year has a y-axis value, which is derived from a sample of a larger dataset. For instance, the first value might be the number votes in a given district or riding for 1992, with the average being around 33,000. On top of this is plotted the 95% confidence interval for the mean (see the boxplot lectures for more information, and the yerr parameter of barcharts).


<br>

![20220717_163057_21](image/20220717_163057_21.png)

 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<h4 style="text-align: center;" markdown="1">Figure 1 from (Ferreira et al, 2014).</h4>

<br>

A challenge that users face is that, for a given y-axis value (e.g. 42,000), it is difficult to know which x-axis values are most likely to be representative, because the confidence levels overlap and their distributions are different (the lengths of the confidence interval bars are unequal). One of the solutions the authors propose for this problem (Figure 2c) is to allow users to indicate the y-axis value of interest (e.g. 42,000) and then draw a horizontal line and color bars based on this value. So bars might be colored red if they are definitely above this value (given the confidence interval), blue if they are definitely below this value, or white if they contain this value.


<br>

![20220717_163402_73](image/20220717_163402_73.png)

<h4 style="text-align: center;" markdown="1">  Figure 2c from (Ferreira et al. 2014). Note that the colorbar legend at the bottom as well as the arrows are not required in the assignment descriptions below.</h4>

<br>
<br>

**Easiest option:** Implement the bar coloring as described above - a color scale with only three colors, (e.g. blue, white, and red). Assume the user provides the y axis value of interest as a parameter or variable.


**Harder option:** Implement the bar coloring as described in the paper, where the color of the bar is actually based on the amount of data covered (e.g. a gradient ranging from dark blue for the distribution being certainly below this y-axis, to white if the value is certainly contained, to dark red if the value is certainly not contained as the distribution is above the axis).

**Even Harder option:** Add interactivity to the above, which allows the user to click on the y axis to set the value of interest. The bar colors should change with respect to what value the user has selected.

**Hardest option:** Allow the user to interactively set a range of y values they are interested in, and recolor based on this (e.g. a y-axis band, see the paper for more details).

---

*Note: The data given for this assignment is not the same as the data used in the article and as a result the visualizations may look a little different.*


```python
# Use the following data for this assignment:

import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650),
                       np.random.normal(43000,100000,3650),
                   np.random.normal(43500,140000,3650),
                   np.random.normal(48000,70000,3650)],
                  index=[1992,1993,1994,1995])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>...</th>
      <th>3640</th>
      <th>3641</th>
      <th>3642</th>
      <th>3643</th>
      <th>3644</th>
      <th>3645</th>
      <th>3646</th>
      <th>3647</th>
      <th>3648</th>
      <th>3649</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1992</th>
      <td>-8941.531897</td>
      <td>127788.667612</td>
      <td>-71887.743011</td>
      <td>-79146.060869</td>
      <td>425156.114501</td>
      <td>310681.166595</td>
      <td>50581.575349</td>
      <td>88349.230566</td>
      <td>185804.513522</td>
      <td>281286.947277</td>
      <td>...</td>
      <td>171938.760289</td>
      <td>150650.759924</td>
      <td>203663.976475</td>
      <td>-377877.158072</td>
      <td>-197214.093861</td>
      <td>24185.008589</td>
      <td>-56826.729535</td>
      <td>-67319.766489</td>
      <td>113377.299342</td>
      <td>-4494.878538</td>
    </tr>
    <tr>
      <th>1993</th>
      <td>-51896.094813</td>
      <td>198350.518755</td>
      <td>-123518.252821</td>
      <td>-129916.759685</td>
      <td>216119.147314</td>
      <td>49845.883728</td>
      <td>149135.648505</td>
      <td>62807.672113</td>
      <td>23365.577348</td>
      <td>-109686.264981</td>
      <td>...</td>
      <td>-44566.520071</td>
      <td>101032.122475</td>
      <td>117648.199945</td>
      <td>160475.622607</td>
      <td>-13759.888342</td>
      <td>-37333.493572</td>
      <td>103019.841174</td>
      <td>179746.127403</td>
      <td>13455.493990</td>
      <td>34442.898855</td>
    </tr>
    <tr>
      <th>1994</th>
      <td>152336.932066</td>
      <td>192947.128056</td>
      <td>389950.263156</td>
      <td>-93006.152024</td>
      <td>100818.575896</td>
      <td>5529.230706</td>
      <td>-32989.370488</td>
      <td>223942.967178</td>
      <td>-66721.580898</td>
      <td>47826.269111</td>
      <td>...</td>
      <td>165085.806360</td>
      <td>74735.174090</td>
      <td>107329.726875</td>
      <td>199250.734156</td>
      <td>-36792.202754</td>
      <td>-71861.846997</td>
      <td>26375.113219</td>
      <td>-29328.078384</td>
      <td>65858.761714</td>
      <td>-91542.001049</td>
    </tr>
    <tr>
      <th>1995</th>
      <td>-69708.439062</td>
      <td>-13289.977022</td>
      <td>-30178.390991</td>
      <td>55052.181256</td>
      <td>152883.621657</td>
      <td>12930.835194</td>
      <td>63700.461932</td>
      <td>64148.489835</td>
      <td>-29316.268556</td>
      <td>59645.677367</td>
      <td>...</td>
      <td>-13901.388118</td>
      <td>50173.686673</td>
      <td>53965.990717</td>
      <td>4128.990173</td>
      <td>72202.595138</td>
      <td>39937.199964</td>
      <td>139472.114293</td>
      <td>59386.186379</td>
      <td>73362.229590</td>
      <td>28705.082908</td>
    </tr>
  </tbody>
</table>
<p>4 rows × 3650 columns</p>
</div>




```python
# exctracting the lists based on the year to plot the histograms
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

%matplotlib notebook

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650),
                   np.random.normal(43000,100000,3650),
                   np.random.normal(43500,140000,3650),
                   np.random.normal(48000,70000,3650)],
                   index=[1992,1993,1994,1995])

print(df.T.describe())

## CHANGING THE INDEX INTO COLUMNS

df1= df.unstack().unstack()
df1.head()

```

                    1992           1993           1994           1995
    count    3650.000000    3650.000000    3650.000000    3650.000000
    mean    33312.107476   41861.859541   39493.304941   47743.550969
    std    200630.901553   98398.356203  140369.925240   69781.185469
    min   -717071.175466 -321586.023683 -450827.613097 -189865.963265
    25%   -102740.398364  -26628.302213  -57436.397393    1774.555612
    50%     29674.931050   43001.976658   41396.781369   49404.322978
    75%    167441.838695  108296.577923  137261.713785   94164.333867
    max    817505.608159  395586.505068  490091.665037  320826.888044





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1992</th>
      <th>1993</th>
      <th>1994</th>
      <th>1995</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-8941.531897</td>
      <td>-51896.094813</td>
      <td>152336.932066</td>
      <td>-69708.439062</td>
    </tr>
    <tr>
      <th>1</th>
      <td>127788.667612</td>
      <td>198350.518755</td>
      <td>192947.128056</td>
      <td>-13289.977022</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-71887.743011</td>
      <td>-123518.252821</td>
      <td>389950.263156</td>
      <td>-30178.390991</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-79146.060869</td>
      <td>-129916.759685</td>
      <td>-93006.152024</td>
      <td>55052.181256</td>
    </tr>
    <tr>
      <th>4</th>
      <td>425156.114501</td>
      <td>216119.147314</td>
      <td>100818.575896</td>
      <td>152883.621657</td>
    </tr>
  </tbody>
</table>
</div>




```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import seaborn as sns
from matplotlib.cm import ScalarMappable
import matplotlib.cm

%matplotlib notebook

             ## Calculating Confidence Interval
## Preparing to color bars in the animation event:
intervals=[]
for idx in df.index:
    df_int = st.norm.interval(alpha=0.95, loc=np.mean(df.loc[idx]), scale=st.sem(df.loc[idx]))
    intervals.append(df_int)
#print(intervals)
#print(df_int)

## Preparing to plot vline as confidence interval (that´s a constant doesn´t need to change every event plot):
df_int1 = st.norm.interval(alpha=0.95, loc=np.mean(df1), scale=st.sem(df1))
#print(df_int1)
            ## Preparing data to plot in vlines:
df_int_min = df_int1[0].tolist()
df_int_max = df_int1[1].tolist()
x = df.index.tolist()
#print(x)
#print(df_int_min)

            ## Preparing bar plot based on mean:
df_mean = df1.mean()
#print(df_mean)

            ## CALCULATE PROBABILITY
y = 39820.885842987082  # just any value

def calc_probs(y, df_int):
    if y < df_int[0]:
        result = 1.0
    elif y > df_int[1]:
        result = 0.0
    else:
        result = 2*((df_int[1]+df_int[0])/2-y)/(df_int[1]-df_int[0])
    return result

          ## COLOR PLOT
probs = [calc_probs(y, df_int) for df_int in intervals]
my_cmap = plt.cm.get_cmap('coolwarm')
colors = my_cmap(probs)
sm = plt.cm.ScalarMappable(cmap=my_cmap,norm = plt.Normalize(0,1))
sm.set_array([])

         ## PLOTTING
fig, ax  = plt.subplots()

#(a) Bar Chart:
bar = df_mean.plot(kind='bar', width = 0.95, color = colors)
plt.ylabel('Values')
plt.xlabel('Year')

cbar=plt.colorbar(sm,orientation = 'horizontal')

#(b) Confidence Interval:
plt.vlines(range(len(x)), df_int_min, df_int_max, color='k')
#plt.xticks(range(len(x)),x)

#(c) Hline:
h_line = plt.axhline(y,color='gray',linestyle='--',linewidth=1)

        ## FUNCTION 'ONCLICK' - ANIMATION

def onclick(event):
    h_line.set_ydata(event.ydata)
    probs=[calc_probs(event.ydata,df_int) for df_int in intervals]
    my_cmap = plt.cm.get_cmap('coolwarm')
    colors = my_cmap(probs)
    bar = df_mean.plot(kind='bar', width = 0.95, color = colors)


plt.gcf().canvas.mpl_connect('button_press_event', onclick)
```

![20220717_162902_92](image/20220717_162902_92.png)
