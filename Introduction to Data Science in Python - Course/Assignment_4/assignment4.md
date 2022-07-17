
# Assignment 4

## Description
In this assignment you must read in a file of metropolitan regions and associated sports teams from [assets/wikipedia_data.html](assets/wikipedia_data.html) and answer some questions about each metropolitan region. Each of these regions may have one or more teams from the "Big 4": NFL (football, in [assets/nfl.csv](assets/nfl.csv)), MLB (baseball, in [assets/mlb.csv](assets/mlb.csv)), NBA (basketball, in [assets/nba.csv](assets/nba.csv) or NHL (hockey, in [assets/nhl.csv](assets/nhl.csv)). Please keep in mind that all questions are from the perspective of the metropolitan region, and that this file is the "source of authority" for the location of a given sports team. Thus teams which are commonly known by a different area (e.g. "Oakland Raiders") need to be mapped into the metropolitan region given (e.g. San Francisco Bay Area). This will require some human data understanding outside of the data you've been given (e.g. you will have to hand-code some names, and might need to google to find out where teams are)!

For each sport I would like you to answer the question: **what is the win/loss ratio's correlation with the population of the city it is in?** Win/Loss ratio refers to the number of wins over the number of wins plus the number of losses. Remember that to calculate the correlation with [`pearsonr`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html), so you are going to send in two ordered lists of values, the populations from the wikipedia_data.html file and the win/loss ratio for a given sport in the same order. Average the win/loss ratios for those cities which have multiple teams of a single sport. Each sport is worth an equal amount in this assignment (20%\*4=80%) of the grade for this assignment. You should only use data **from year 2018** for your analysis -- this is important!

## Notes

1. Do not include data about the MLS or CFL in any of the work you are doing, we're only interested in the Big 4 in this assignment.
2. I highly suggest that you first tackle the four correlation questions in order, as they are all similar and worth the majority of grades for this assignment. This is by design!
3. It's fair game to talk with peers about high level strategy as well as the relationship between metropolitan areas and sports teams. However, do not post code solving aspects of the assignment (including such as dictionaries mapping areas to teams, or regexes which will clean up names).
4. There may be more teams than the assert statements test, remember to collapse multiple teams in one city into a single value!

## Question 1
For this question, calculate the win/loss ratio's correlation with the population of the city it is in for the **NHL** using **2018** data.


```python
import pandas as pd
import numpy as np
import scipy.stats as stats
import re

nhl_df=pd.read_csv("assets/nhl.csv")
cities=pd.read_html("assets/wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]
#print(nhl_df.head(50))
#print(cities)

def nhl_correlation():

    # First visualizing and studying df: NO HEADER

    #(1)
    #print(cities.columns)
    #print(nhl_df.columns)
    #(2)
    #print(cities.info())
    #print(nhl_df.info())


    #Second: Selecting columns to work with:

        # NHL columns:
    nhl_df1 = nhl_df[['team','W','L','League']]
    #print(nhl_df1.head(50))
    #print(cities.columns)
        # Cities columns:
    cities1 = cities[['Metropolitan area','Population (2016 est.)[8]','NHL']]
    #print(cities1.head(40))

    # Third: cleaning & preparing  data

    # NHL for year 2018 only: excluding rows out of the year 2018, and in the middle dividing divisions:
    nhl_df1.drop([0,9,18,26],0,inplace=True)
    nhl_df1.drop(nhl_df1.index[31:170], inplace=True)
    #print(nhl_df1)

    # Eliminating rows of the cities where there is not any NHL team:
    cities1.drop([14,15,18,19,20,21,23,24,25,27,28,32,33,38,40,41,42,44,45,46,48,49,50],0,inplace=True)
    #print(cities)

    # Standardization of the columns: split, creat a list and create new column into df. It´s easier create a new column, and
    # then discard the old one!
      #(a) Cities:
    l= []
    for i in cities1['NHL']:
        i=i.split('[')
        l.append(i[0])
    cities1['NHL'] = l
    #print(cities1)

      #(b) NHL:
    li = []
    for i in nhl_df1['team']:
        i = re.findall("[^*]+", i)
        li.append(i[0])
    nhl_df1['team'] = li
    #print(nhl_df1.head(30))


    nhl_df1['Metropolitan area'] = nhl_df1['team']
    #print(nhl_df)
    nhl_df1['Metropolitan area'] = nhl_df1['Metropolitan area'].map({'Tampa Bay Lightning':'Tampa Bay Area',
     'Boston Bruins':'Boston',
     'Toronto Maple Leafs':'Toronto',
     'Florida Panthers':'Miami–Fort Lauderdale',
     'Detroit Red Wings':'Detroit',
     'Montreal Canadiens':'Montreal',
     'Ottawa Senators':'Ottawa',
     'Buffalo Sabres':'Buffalo',
     'Washington Capitals':'Washington, D.C.',
     'Pittsburgh Penguins':'Pittsburgh',
     'Philadelphia Flyers':'Philadelphia',
     'Columbus Blue Jackets':'Columbus',
     'New Jersey Devils':'New York City',
     'Carolina Hurricanes':'Raleigh',
     'New York Islanders':'New York City',
     'New York Rangers':'New York City',
     'Nashville Predators':'Nashville',
     'Winnipeg Jets':'Winnipeg',
     'Minnesota Wild':'Minneapolis–Saint Paul',
     'Colorado Avalanche':'Denver',
     'St. Louis Blues':'St. Louis',
     'Dallas Stars':'Dallas–Fort Worth',
     'Chicago Blackhawks':'Chicago',
     'Vegas Golden Knights':'Las Vegas',
     'Anaheim Ducks':'Los Angeles',
     'San Jose Sharks':'San Francisco Bay Area',
     'Los Angeles Kings':'Los Angeles',
     'Calgary Flames':'Calgary',
     'Edmonton Oilers':'Edmonton',
     'Vancouver Canucks':'Vancouver',
     'Arizona Coyotes':'Phoenix'})
    #print(nhl_df1)

    # Seting the same index as a key to merge:
    #(a) NHL:
    nhl_df1 = nhl_df1.set_index('Metropolitan area')
    #(b) Cities:
    cities1 = cities1.set_index('Metropolitan area')

    # MERGE os 2 dataframes, joining without duplicates:
    df = nhl_df1.join(cities1)
    df1 = df.reset_index()
    #print(df1)

    # Create a column with the ration win/loss:
    # First pass to numeric:
    df1['W']=pd.to_numeric(df1['W'])
    df1['L']=pd.to_numeric(df1['L'])
    df1['Population (2016 est.)[8]']=pd.to_numeric(df1['Population (2016 est.)[8]'])
    df1.rename(columns = {'Population (2016 est.)[8]':'Population'}, inplace = True)
    # Then calculate:
    df1['ratio_WL'] = df1['W'] / (df1['W'] + df1['L'])
    #print(df1)

    # Droping columns that are not necessary:
    df2 = df1.drop(['League','NHL'], axis=1)
    #print(df2)

    # grouping by cities:
    df3 = df2.groupby('Metropolitan area').agg({'ratio_WL': np.nanmean, 'Population': np.nanmean})
    #print(df3)

    # Population and win_loss_by_region in the same order as cities['Metropolitan area']
    population_by_region = df3['Population']
    #print(len(population_by_region))
    win_loss_by_region = df3['ratio_WL']
    #print(len(win_loss_by_region ))

    t = stats.pearsonr(population_by_region, win_loss_by_region)
    answer_NHL = t[0]

    return answer_NHL


nhl_correlation()
```
```
    0.012486162921209907
```


## Question 2
For this question, calculate the win/loss ratio's correlation with the population of the city it is in for the **NBA** using **2018** data.


```python
import pandas as pd
import numpy as np
import scipy.stats as stats
import re

nba_df=pd.read_csv("assets/nba.csv")
cities=pd.read_html("assets/wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]
#print(nba_df)

def nba_correlation():
    # First visualizing and studying df: NO HEADER

    #(1)
    #print(cities.columns)
    #print(nba_df.columns)
    #(2)
    #print(cities.info())
    #print(n_badf.info())


    #Second: Selecting columns to work with:

        # NHL columns:
    nba_df1 = nba_df[['team','W','L','year']]
    #print(nba_df1.head(50))
    #print(cities.columns)
        # Cities columns:
    cities1 = cities[['Metropolitan area','Population (2016 est.)[8]','NBA']]
    #print(cities1.head(50))

    # Third: cleaning & preparing  data

    # NBA for year 2018 only: excluding rows out of the year 2018, and in the middle dividing divisions:
    nba_df1.drop(nba_df1.index[30:170], inplace=True)
    #print(nba_df1)

    # Eliminating rows of the cities where there is not any NHL team:
    cities1.drop([16,17,19,20,21,22,23,26,29,30,31,34,35,36,37,39,40,43,44,47,48,49,50],0,inplace=True)
    #print(cities1)

    # Standardization of the columns: split, creat a list and create new column into df. It´s easier create a new column, and
    # then discard the old one!
      #(a) Cities:
    l= []
    for i in cities1['NBA']:
        i=i.split('[')
        l.append(i[0])
    cities1['NBA'] = l
    #print(cities1)

      #(b) NBA:
    l1 = []
    for i in nba_df1['team']:
        i = re.findall("[\w].+[a-z]", i)
        l1.append(i[0])
    nba_df1['team'] = l1
    #print(nba_df1.head(30))

    nba_df1['Metropolitan area'] = nba_df1['team']
    #print(nba_df1)
    nba_df1['Metropolitan area'] = nba_df1['Metropolitan area'].map({'Toronto Raptors':'Toronto',
     'Boston Celtics':'Boston',
     'Philadelphia 76ers':'Philadelphia',
     'Cleveland Cavaliers':'Cleveland',
     'Indiana Pacers':'Indianapolis',
     'Miami Heat':'Miami–Fort Lauderdale',
     'Milwaukee Bucks':'Milwaukee',
     'Washington Wizards':'Washington, D.C.',
     'Detroit Pistons':'Detroit',
     'Charlotte Hornets':'Charlotte',
     'New York Knicks':'New York City',
     'Brooklyn Nets':'New York City',
     'Chicago Bulls':'Chicago',
     'Orlando Magic':'Orlando',
     'Atlanta Hawks':'Atlanta',
     'Houston Rockets':'Houston',
     'Golden State Warriors':'San Francisco Bay Area',
     'Portland Trail Blazers':'Portland',
     'Oklahoma City Thunder':'Oklahoma City',
     'Utah Jazz':'Salt Lake City',
     'New Orleans Pelicans':'New Orleans',
     'San Antonio Spurs':'San Antonio',
     'Minnesota Timberwolves':'Minneapolis–Saint Paul',
     'Denver Nuggets':'Denver',
     'Los Angeles Clippers':'Los Angeles',
     'Los Angeles Lakers':'Los Angeles',
     'Sacramento Kings':'Sacramento',
     'Dallas Mavericks':'Dallas–Fort Worth',
     'Memphis Grizzlies':'Memphis',
     'Phoenix Suns':'Phoenix'})
    #print(nba_df1)

    # Seting the same index as a key to merge:
    #(a) NBA:
    nba_df1 = nba_df1.set_index('Metropolitan area')
    #(b) Cities:
    cities1 = cities1.set_index('Metropolitan area')

    # MERGE os 2 dataframes, joining without duplicates:
    df = nba_df1.join(cities1)
    df1 = df.reset_index()
    #print(df1)

    # Create a column with the ration win/loss:
    # First pass to numeric:
    df1['W']=pd.to_numeric(df1['W'])
    df1['L']=pd.to_numeric(df1['L'])
    df1['Population (2016 est.)[8]']=pd.to_numeric(df1['Population (2016 est.)[8]'])
    df1.rename(columns = {'Population (2016 est.)[8]':'Population'}, inplace = True)
    # Then calculate:
    df1['ratio_WL'] = df1['W'] / (df1['W'] + df1['L'])
    #print(df1)

    # Droping columns that are not necessary:
    df2 = df1.drop(['year','NBA'], axis=1)
    #print(df2)

    # grouping by cities:
    df3 = df2.groupby('Metropolitan area').agg({'ratio_WL': np.nanmean, 'Population': np.nanmean})
    #print(df3)

    # Population and win_loss_by_region in the same order as cities['Metropolitan area']
    population_by_region = df3['Population']
    #print(len(population_by_region))
    win_loss_by_region = df3['ratio_WL']
    #print(len(win_loss_by_region ))

    t= stats.pearsonr(population_by_region, win_loss_by_region)
    answer_NBA = t[0]

    return answer_NBA

nba_correlation()

```
```
    -0.17657160252844617
```


## Question 3
For this question, calculate the win/loss ratio's correlation with the population of the city it is in for the **MLB** using **2018** data.


```python
import pandas as pd
import numpy as np
import scipy.stats as stats
import re

mlb_df=pd.read_csv("assets/mlb.csv")
cities=pd.read_html("assets/wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]

def mlb_correlation():
        # First visualizing and studying df: NO HEADER

    #(1)
    #print(cities.columns)
    #print(mlb_df.columns)
    #(2)
    #print(cities.info())
    #print(mlb_df.info())


    #Second: Selecting columns to work with:

        # MLB columns:
    mlb_df1 = mlb_df[['team','W','L','year']]
    #print(mlb_df1.head(50))
    #print(cities.columns)
        # Cities columns:
    cities1 = cities[['Metropolitan area','Population (2016 est.)[8]','MLB']]
    #print(cities1)

    # Third: cleaning & preparing  data

    # MLB for year 2018 only: excluding rows out of the year 2018, and in the middle dividing divisions:
    mlb_df1.drop(mlb_df1.index[30:150], inplace=True)
    #print(mlb_df1)

    # Eliminating rows of the cities where there is not any NHL team:
    cities1.drop([24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,50],0,inplace=True)
    #print(cities1)

    # Standardization of the columns: split, creat a list and create new column into df. It´s easier create a new column, and
    # then discard the old one!
      #(a) Cities:
    l= []
    for i in cities1['MLB']:
        i=i.split('[')
        l.append(i[0])
    cities1['MLB'] = l
    #print(cities1)

      #(b) MLB:

    mlb_df1['team'].values.tolist()
    #print(mlb_df1.head(30))

    mlb_df1['Metropolitan area'] = mlb_df1['team']
    #print(mlb_df1)
    mlb_df1['Metropolitan area'] = mlb_df1['Metropolitan area'].map({'Boston Red Sox':'Boston',
     'New York Yankees':'New York City',
     'Tampa Bay Rays':'Tampa Bay Area',
     'Toronto Blue Jays':'Toronto',
     'Baltimore Orioles':'Baltimore',
     'Cleveland Indians':'Cleveland',
     'Minnesota Twins':'Minneapolis–Saint Paul',
     'Detroit Tigers':'Detroit',
     'Chicago White Sox':'Chicago',
     'Kansas City Royals':'Kansas City',
     'Houston Astros':'Houston',
     'Oakland Athletics':'San Francisco Bay Area',
     'Seattle Mariners':'Seattle',
     'Los Angeles Angels':'Los Angeles',
     'Texas Rangers':'Dallas–Fort Worth',
     'Atlanta Braves':'Atlanta',
     'Washington Nationals':'Washington, D.C.',
     'Philadelphia Phillies':'Philadelphia',
     'New York Mets':'New York City',
     'Miami Marlins':'Miami–Fort Lauderdale',
     'Milwaukee Brewers':'Milwaukee',
     'Chicago Cubs':'Chicago',
     'St. Louis Cardinals':'St. Louis',
     'Pittsburgh Pirates':'Pittsburgh',
     'Cincinnati Reds':'Cincinnati',
     'Los Angeles Dodgers':'Los Angeles',
     'Colorado Rockies':'Denver',
     'Arizona Diamondbacks':'Phoenix',
     'San Francisco Giants':'San Francisco Bay Area',
     'San Diego Padres':'San Diego'})
    #print(nba_df1)

    # Seting the same index as a key to merge:
    #(a) MLB:
    mlb_df1 = mlb_df1.set_index('Metropolitan area')
    #(b) Cities:
    cities1 = cities1.set_index('Metropolitan area')

    # MERGE os 2 dataframes, joining without duplicates:
    df = mlb_df1.join(cities1)
    df1 = df.reset_index()
    #print(df1)

    # Create a column with the ration win/loss:
    # First pass to numeric:
    df1['W']=pd.to_numeric(df1['W'])
    df1['L']=pd.to_numeric(df1['L'])
    df1['Population (2016 est.)[8]']=pd.to_numeric(df1['Population (2016 est.)[8]'])
    df1.rename(columns = {'Population (2016 est.)[8]':'Population'}, inplace = True)
    # Then calculate:
    df1['ratio_WL'] = df1['W'] / (df1['W'] + df1['L'])
    #print(df1)

    # Droping columns that are not necessary:
    df2 = df1.drop(['year','MLB'], axis=1)
    #print(df2)

    # grouping by cities:
    df3 = df2.groupby('Metropolitan area').agg({'ratio_WL': np.nanmean, 'Population': np.nanmean}).fillna(0)
    #print(df3)

    # Population and win_loss_by_region in the same order as cities['Metropolitan area']
    population_by_region = df3['Population']
    #print(len(population_by_region))
    win_loss_by_region = df3['ratio_WL']
    #print(len(win_loss_by_region ))

    t = stats.pearsonr(population_by_region, win_loss_by_region)
    answer_MLB = t[0]

    return answer_MLB

mlb_correlation()
```
```
    0.15027698302669307
```

## Question 4
For this question, calculate the win/loss ratio's correlation with the population of the city it is in for the **NFL** using **2018** data.


```python
import pandas as pd
import numpy as np
import scipy.stats as stats
import re

nfl_df=pd.read_csv("assets/nfl.csv")
cities=pd.read_html("assets/wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]

def nfl_correlation():
    # First visualizing and studying df: NO HEADER

    #(1)
    #print(cities.columns)
    #print(nfl_df.columns)
    #(2)
    #print(cities.info())
    #print(nfl_df.info())


    #Second: Selecting columns to work with:

        # NFL columns:
    nfl_df1 = nfl_df[['team','W','L','year']]
    #print(nfl_df1.head(50))
    #print(cities.columns)
        # Cities columns:
    cities1 = cities[['Metropolitan area','Population (2016 est.)[8]','NFL']]
    #print(cities1.head(50))

    # Third: cleaning & preparing  data

    # NFL for year 2018 only: excluding rows out of the year 2018, and in the middle dividing divisions:
    nfl_df1.drop([0,5,10,15,20,25,30,35],0,inplace=True)
    nfl_df1.drop(nfl_df1.index[32:199], inplace=True)
    #print(nfl_df1)

    # Eliminating rows of the cities where there is not any NHL team:
    cities1.drop([13,22,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,49,50],0,inplace=True)
    #print(cities1)

    # Standardization of the columns: split, creat a list and create new column into df. It´s easier create a new column, and
    # then discard the old one!
      #(a) Cities:
    l= []
    for i in cities1['NFL']:
        i=i.split('[')
        l.append(i[0])
    cities1['NFL'] = l
    #print(cities1)

      #(b) NFL:
    l1 = []
    for i in nfl_df1['team']:
        i = re.findall("[\w].+[a-z]", i)
        l1.append(i[0])
    nfl_df1['team'] = l1
    #print(nfl_df1.head(30))

    nfl_df1['Metropolitan area'] = nfl_df1['team']
    #print(nfl_df1)
    nfl_df1['Metropolitan area'] = nfl_df1['Metropolitan area'].map({'New England Patriots':'Boston',
     'Miami Dolphins':'Miami–Fort Lauderdale',
     'Buffalo Bills':'Buffalo',
     'New York Jets':'New York City',
     'Baltimore Ravens':'Baltimore',
     'Pittsburgh Steelers':'Pittsburgh',
     'Cleveland Browns':'Cleveland',
     'Cincinnati Bengals':'Cincinnati',
     'Houston Texans':'Houston',
     'Indianapolis Colts':'Indianapolis',
     'Tennessee Titans':'Nashville',
     'Jacksonville Jaguars':'Jacksonville',
     'Kansas City Chiefs':'Kansas City',
     'Los Angeles Chargers':'Los Angeles',
     'Denver Broncos':'Denver',
     'Oakland Raiders':'San Francisco Bay Area',
     'Dallas Cowboys':'Dallas–Fort Worth',
     'Philadelphia Eagles':'Philadelphia',
     'Washington Redskins':'Washington, D.C.',
     'New York Giants':'New York City',
     'Chicago Bears':'Chicago',
     'Minnesota Vikings':'Minneapolis–Saint Paul',
     'Green Bay Packers':'Green Bay',
     'Detroit Lions':'Detroit',
     'New Orleans Saints':'New Orleans',
     'Carolina Panthers':'Charlotte',
     'Atlanta Falcons':'Atlanta',
     'Tampa Bay Buccaneers':'Tampa Bay Area',
     'Los Angeles Rams':'Los Angeles',
     'Seattle Seahawks':'Seattle',
     'San Francisco 49ers':'San Francisco Bay Area',
     'Arizona Cardinals':'Phoenix'})
    #print(nfl_df1)

    # Seting the same index as a key to merge:
    #(a) NFL:
    nfl_df1 = nfl_df1.set_index('Metropolitan area')
    #(b) Cities:
    cities1 = cities1.set_index('Metropolitan area')

    # MERGE os 2 dataframes, joining without duplicates:
    df = nfl_df1.join(cities1)
    df1 = df.reset_index()
    #print(df1)

    # Create a column with the ration win/loss:
    # First pass to numeric:
    df1['W']=pd.to_numeric(df1['W'])
    df1['L']=pd.to_numeric(df1['L'])
    df1['Population (2016 est.)[8]']=pd.to_numeric(df1['Population (2016 est.)[8]'])
    df1.rename(columns = {'Population (2016 est.)[8]':'Population'}, inplace = True)
    # Then calculate:
    df1['ratio_WL'] = df1['W'] / (df1['W'] + df1['L'])
    #print(df1)

    # Droping columns that are not necessary:
    df2 = df1.drop(['year','NFL'], axis=1)
    #print(df2)

    # grouping by cities:
    df3 = df2.groupby('Metropolitan area').agg({'ratio_WL': np.nanmean, 'Population': np.nanmean})
    #print(df3)

    # Population and win_loss_by_region in the same order as cities['Metropolitan area']
    population_by_region = df3['Population']
    #print(len(population_by_region))
    win_loss_by_region = df3['ratio_WL']
    #print(len(win_loss_by_region ))

    t = stats.pearsonr(population_by_region, win_loss_by_region)
    answer_NFL = t[0]

    return answer_NFL

nfl_correlation()
```
```
    0.004922112149349393
```

## Question 5
In this question I would like you to explore the hypothesis that **given that an area has two sports teams in different sports, those teams will perform the same within their respective sports**. How I would like to see this explored is with a series of paired t-tests (so use [`ttest_rel`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html)) between all pairs of sports. Are there any sports where we can reject the null hypothesis? Again, average values where a sport has multiple teams in one region. Remember, you will only be including, for each sport, cities which have teams engaged in that sport, drop others as appropriate. This question is worth 20% of the grade for this assignment.


```python
import pandas as pd
import numpy as np
import scipy.stats as stats
import re

mlb_df=pd.read_csv("assets/mlb.csv")
nhl_df=pd.read_csv("assets/nhl.csv")
nba_df=pd.read_csv("assets/nba.csv")
nfl_df=pd.read_csv("assets/nfl.csv")
cities=pd.read_html("assets/wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]

#def sports_team_performance():

#(A) NFLfunction:

def nfl_func():

          # NHL columns:
    nfl_df1 = nfl_df[['team','W','L','year']]
    #print(nfl_df1.head(50))
    #print(cities.columns)
        # Cities columns:
    cities1 = cities[['Metropolitan area','Population (2016 est.)[8]','NFL']]
    #print(cities1.head(50))

    # Third: cleaning & preparing  data

    # NFL for year 2018 only: excluding rows out of the year 2018, and in the middle dividing divisions:
    nfl_df1.drop([0,5,10,15,20,25,30,35],0,inplace=True)
    nfl_df1.drop(nfl_df1.index[32:199], inplace=True)
    #print(nfl_df1)

    # Eliminating rows of the cities where there is not any NHL team:
    cities1.drop([13,22,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,49,50],0,inplace=True)
    #print(cities1)

    # Standardization of the columns: split, creat a list and create new column into df. It´s easier create a new column, and
    # then discard the old one!
      #(a) Cities:
    l= []
    for i in cities1['NFL']:
        i=i.split('[')
        l.append(i[0])
    cities1['NFL'] = l
    #print(cities1)

      #(b) NFL:
    l1 = []
    for i in nfl_df1['team']:
        i = re.findall("[\w].+[a-z]", i)
        l1.append(i[0])
    nfl_df1['team'] = l1
    #print(nfl_df1.head(30))

    nfl_df1['Metropolitan area'] = nfl_df1['team']
    #print(nfl_df1)
    nfl_df1['Metropolitan area'] = nfl_df1['Metropolitan area'].map({'New England Patriots':'Boston',
     'Miami Dolphins':'Miami–Fort Lauderdale',
     'Buffalo Bills':'Buffalo',
     'New York Jets':'New York City',
     'Baltimore Ravens':'Baltimore',
     'Pittsburgh Steelers':'Pittsburgh',
     'Cleveland Browns':'Cleveland',
     'Cincinnati Bengals':'Cincinnati',
     'Houston Texans':'Houston',
     'Indianapolis Colts':'Indianapolis',
     'Tennessee Titans':'Nashville',
     'Jacksonville Jaguars':'Jacksonville',
     'Kansas City Chiefs':'Kansas City',
     'Los Angeles Chargers':'Los Angeles',
     'Denver Broncos':'Denver',
     'Oakland Raiders':'San Francisco Bay Area',
     'Dallas Cowboys':'Dallas–Fort Worth',
     'Philadelphia Eagles':'Philadelphia',
     'Washington Redskins':'Washington, D.C.',
     'New York Giants':'New York City',
     'Chicago Bears':'Chicago',
     'Minnesota Vikings':'Minneapolis–Saint Paul',
     'Green Bay Packers':'Green Bay',
     'Detroit Lions':'Detroit',
     'New Orleans Saints':'New Orleans',
     'Carolina Panthers':'Charlotte',
     'Atlanta Falcons':'Atlanta',
     'Tampa Bay Buccaneers':'Tampa Bay Area',
     'Los Angeles Rams':'Los Angeles',
     'Seattle Seahawks':'Seattle',
     'San Francisco 49ers':'San Francisco Bay Area',
     'Arizona Cardinals':'Phoenix'})
    #print(nfl_df1)

    # Seting the same index as a key to merge:
    #(a) NFL:
    nfl_df1 = nfl_df1.set_index('Metropolitan area')
    #(b) Cities:
    cities1 = cities1.set_index('Metropolitan area')

    # MERGE os 2 dataframes, joining without duplicates:
    df = nfl_df1.join(cities1)
    df1 = df.reset_index()
    #print(df1)

    # Create a column with the ration win/loss:
    # First pass to numeric:
    df1['W']=pd.to_numeric(df1['W'])
    df1['L']=pd.to_numeric(df1['L'])
    df1['Population (2016 est.)[8]']=pd.to_numeric(df1['Population (2016 est.)[8]'])
    df1.rename(columns = {'Population (2016 est.)[8]':'PopulationC_NFL'}, inplace = True)
    df1.rename(columns = {'team':'NFLteam'}, inplace = True)
    # Then calculate:
    df1['NFLratio_WL'] = df1['W'] / (df1['W'] + df1['L'])
    #print(df1)

    # Droping columns that are not necessary:
    df2 = df1.drop(['year','NFL'], axis=1)
    #print(df2)

    # grouping by cities:
    df3 = df2.groupby('Metropolitan area').agg({'NFLratio_WL': np.nanmean, 'PopulationC_NFL': np.nanmean})
    #print(df3)

    return df3


# (B) MLB function:

def mlb_func():
        # First visualizing and studying df: NO HEADER

    #(1)
    #print(cities.columns)
    #print(mlb_df.columns)
    #(2)
    #print(cities.info())
    #print(mlb_df.info())

    #Second: Selecting columns to work with:

        # MLB columns:
    mlb_df1 = mlb_df[['team','W','L','year']]
    #print(mlb_df1.head(50))
    #print(cities.columns)
        # Cities columns:
    cities1 = cities[['Metropolitan area','Population (2016 est.)[8]','MLB']]
    #print(cities1)

    # Third: cleaning & preparing  data

    # MLB for year 2018 only: excluding rows out of the year 2018, and in the middle dividing divisions:
    mlb_df1.drop(mlb_df1.index[30:150], inplace=True)
    #print(mlb_df1)

    # Eliminating rows of the cities where there is not any NHL team:
    cities1.drop([24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,50],0,inplace=True)
    #print(cities1)

    # Standardization of the columns: split, creat a list and create new column into df.
      #(a) Cities:
    l= []
    for i in cities1['MLB']:
        i=i.split('[')
        l.append(i[0])
    cities1['MLB'] = l
    #print(cities1)

      #(b) MLB:

    mlb_df1['team'].values.tolist()
    #print(mlb_df1.head(30))

    mlb_df1['Metropolitan area'] = mlb_df1['team']
    #print(mlb_df1)
    mlb_df1['Metropolitan area'] = mlb_df1['Metropolitan area'].map({'Boston Red Sox':'Boston',
     'New York Yankees':'New York City',
     'Tampa Bay Rays':'Tampa Bay Area',
     'Toronto Blue Jays':'Toronto',
     'Baltimore Orioles':'Baltimore',
     'Cleveland Indians':'Cleveland',
     'Minnesota Twins':'Minneapolis–Saint Paul',
     'Detroit Tigers':'Detroit',
     'Chicago White Sox':'Chicago',
     'Kansas City Royals':'Kansas City',
     'Houston Astros':'Houston',
     'Oakland Athletics':'San Francisco Bay Area',
     'Seattle Mariners':'Seattle',
     'Los Angeles Angels':'Los Angeles',
     'Texas Rangers':'Dallas–Fort Worth',
     'Atlanta Braves':'Atlanta',
     'Washington Nationals':'Washington, D.C.',
     'Philadelphia Phillies':'Philadelphia',
     'New York Mets':'New York City',
     'Miami Marlins':'Miami–Fort Lauderdale',
     'Milwaukee Brewers':'Milwaukee',
     'Chicago Cubs':'Chicago',
     'St. Louis Cardinals':'St. Louis',
     'Pittsburgh Pirates':'Pittsburgh',
     'Cincinnati Reds':'Cincinnati',
     'Los Angeles Dodgers':'Los Angeles',
     'Colorado Rockies':'Denver',
     'Arizona Diamondbacks':'Phoenix',
     'San Francisco Giants':'San Francisco Bay Area',
     'San Diego Padres':'San Diego'})
    #print(nba_df1)

    # Seting the same index as a key to merge:
    #(a) MLB:
    mlb_df1 = mlb_df1.set_index('Metropolitan area')
    #(b) Cities:
    cities1 = cities1.set_index('Metropolitan area')

    # MERGE os 2 dataframes, joining without duplicates:
    df = mlb_df1.join(cities1)
    df1 = df.reset_index()
    #print(df1)

    # Create a column with the ration win/loss:
    # First pass to numeric:
    df1['W']=pd.to_numeric(df1['W'])
    df1['L']=pd.to_numeric(df1['L'])
    df1['Population (2016 est.)[8]']=pd.to_numeric(df1['Population (2016 est.)[8]'])
    df1.rename(columns = {'Population (2016 est.)[8]':'PopulationC_MLB'}, inplace = True)
    df1.rename(columns = {'team':'MLBteam'}, inplace = True)
    # Then calculate:
    df1['MLBratio_WL'] = df1['W'] / (df1['W'] + df1['L'])
    #print(df1)

    # Droping columns that are not necessary:
    df2 = df1.drop(['year','MLB'], axis=1)
    #print(df2)

    # grouping by cities:
    df3 = df2.groupby('Metropolitan area').agg({'MLBratio_WL': np.nanmean, 'PopulationC_MLB': np.nanmean}).fillna(0)
    #print(df3)

    return df3

# (C) NBA function:

def nba_func():

    # First visualizing and studying df: NO HEADER

    #(1)
    #print(cities.columns)
    #print(nba_df.columns)
    #(2)
    #print(cities.info())
    #print(n_badf.info())


    #Second: Selecting columns to work with:

        # NHL columns:
    nba_df1 = nba_df[['team','W','L','year']]
    #print(nba_df1.head(50))
    #print(cities.columns)
        # Cities columns:
    cities1 = cities[['Metropolitan area','Population (2016 est.)[8]','NBA']]
    #print(cities1.head(50))

    # Third: cleaning & preparing  data

    # NBA for year 2018 only: excluding rows out of the year 2018, and in the middle dividing divisions:
    nba_df1.drop(nba_df1.index[30:170], inplace=True)
    #print(nba_df1)

    # Eliminating rows of the cities where there is not any NHL team:
    cities1.drop([16,17,19,20,21,22,23,26,29,30,31,34,35,36,37,39,40,43,44,47,48,49,50],0,inplace=True)
    #print(cities1)

    # Standardization of the columns: split, creat a list and create new column into df.
      #(a) Cities:
    l= []
    for i in cities1['NBA']:
        i=i.split('[')
        l.append(i[0])
    cities1['NBA'] = l
    #print(cities1)

      #(b) NBA:
    l1 = []
    for i in nba_df1['team']:
        i = re.findall("[\w].+[a-z]", i)
        l1.append(i[0])
    nba_df1['team'] = l1
    #print(nba_df1.head(30))

    nba_df1['Metropolitan area'] = nba_df1['team']
    #print(nba_df1)
    nba_df1['Metropolitan area'] = nba_df1['Metropolitan area'].map({'Toronto Raptors':'Toronto',
     'Boston Celtics':'Boston',
     'Philadelphia 76ers':'Philadelphia',
     'Cleveland Cavaliers':'Cleveland',
     'Indiana Pacers':'Indianapolis',
     'Miami Heat':'Miami–Fort Lauderdale',
     'Milwaukee Bucks':'Milwaukee',
     'Washington Wizards':'Washington, D.C.',
     'Detroit Pistons':'Detroit',
     'Charlotte Hornets':'Charlotte',
     'New York Knicks':'New York City',
     'Brooklyn Nets':'New York City',
     'Chicago Bulls':'Chicago',
     'Orlando Magic':'Orlando',
     'Atlanta Hawks':'Atlanta',
     'Houston Rockets':'Houston',
     'Golden State Warriors':'San Francisco Bay Area',
     'Portland Trail Blazers':'Portland',
     'Oklahoma City Thunder':'Oklahoma City',
     'Utah Jazz':'Salt Lake City',
     'New Orleans Pelicans':'New Orleans',
     'San Antonio Spurs':'San Antonio',
     'Minnesota Timberwolves':'Minneapolis–Saint Paul',
     'Denver Nuggets':'Denver',
     'Los Angeles Clippers':'Los Angeles',
     'Los Angeles Lakers':'Los Angeles',
     'Sacramento Kings':'Sacramento',
     'Dallas Mavericks':'Dallas–Fort Worth',
     'Memphis Grizzlies':'Memphis',
     'Phoenix Suns':'Phoenix'})
    #print(nba_df1)

    # Seting the same index as a key to merge:
    #(a) NBA:
    nba_df1 = nba_df1.set_index('Metropolitan area')
    #(b) Cities:
    cities1 = cities1.set_index('Metropolitan area')

    # MERGE os 2 dataframes, joining without duplicates:
    df = nba_df1.join(cities1)
    df1 = df.reset_index()
    #print(df1)

    # Create a column with the ration win/loss:
    # First pass to numeric:
    df1['W']=pd.to_numeric(df1['W'])
    df1['L']=pd.to_numeric(df1['L'])
    df1['Population (2016 est.)[8]']=pd.to_numeric(df1['Population (2016 est.)[8]'])
    df1.rename(columns = {'Population (2016 est.)[8]':'PopulationC_NBA'}, inplace = True)
    df1.rename(columns = {'team':'NBAteam'}, inplace = True)
    # Then calculate:
    df1['NBAratio_WL'] = df1['W'] / (df1['W'] + df1['L'])
    #print(df1)

    # Droping columns that are not necessary:
    df2 = df1.drop(['year','NBA'], axis=1)
    #print(df2)

    # grouping by cities:
    df3 = df2.groupby('Metropolitan area').agg({'NBAratio_WL': np.nanmean, 'PopulationC_NBA': np.nanmean})
    #print(df3)

    return df3


# (D) NHL function:

def nhl_func():

    # First visualizing and studying df: NO HEADER

    #(1)
    #print(cities.columns)
    #print(nhl_df.columns)
    #(2)
    #print(cities.info())
    #print(nhl_df.info())


    #Second: Selecting columns to work with:

        # NHL columns:
    nhl_df1 = nhl_df[['team','W','L','League']]
    #print(nhl_df1.head(50))
    #print(cities.columns)
        # Cities columns:
    cities1 = cities[['Metropolitan area','Population (2016 est.)[8]','NHL']]
    #print(cities1.head(40))

    # Third: cleaning & preparing  data

    # NHL for year 2018 only: excluding rows out of the year 2018, and in the middle dividing divisions:
    nhl_df1.drop([0,9,18,26],0,inplace=True)
    nhl_df1.drop(nhl_df1.index[31:170], inplace=True)
    #print(nhl_df1)

    # Eliminating rows of the cities where there is not any NHL team:
    cities1.drop([14,15,18,19,20,21,23,24,25,27,28,32,33,38,40,41,42,44,45,46,48,49,50],0,inplace=True)
    #print(cities)

    # Standardization of the columns: split, creat a list and create new column into df.
      #(a) Cities:
    l= []
    for i in cities1['NHL']:
        i=i.split('[')
        l.append(i[0])
    cities1['NHL'] = l
    #print(cities1)

      #(b) NHL:
    li = []
    for i in nhl_df1['team']:
        i = re.findall("[^*]+", i)
        li.append(i[0])
    nhl_df1['team'] = li
    #print(nhl_df1.head(30))


    nhl_df1['Metropolitan area'] = nhl_df1['team']
    #print(nhl_df)
    nhl_df1['Metropolitan area'] = nhl_df1['Metropolitan area'].map({'Tampa Bay Lightning':'Tampa Bay Area',
     'Boston Bruins':'Boston',
     'Toronto Maple Leafs':'Toronto',
     'Florida Panthers':'Miami–Fort Lauderdale',
     'Detroit Red Wings':'Detroit',
     'Montreal Canadiens':'Montreal',
     'Ottawa Senators':'Ottawa',
     'Buffalo Sabres':'Buffalo',
     'Washington Capitals':'Washington, D.C.',
     'Pittsburgh Penguins':'Pittsburgh',
     'Philadelphia Flyers':'Philadelphia',
     'Columbus Blue Jackets':'Columbus',
     'New Jersey Devils':'New York City',
     'Carolina Hurricanes':'Raleigh',
     'New York Islanders':'New York City',
     'New York Rangers':'New York City',
     'Nashville Predators':'Nashville',
     'Winnipeg Jets':'Winnipeg',
     'Minnesota Wild':'Minneapolis–Saint Paul',
     'Colorado Avalanche':'Denver',
     'St. Louis Blues':'St. Louis',
     'Dallas Stars':'Dallas–Fort Worth',
     'Chicago Blackhawks':'Chicago',
     'Vegas Golden Knights':'Las Vegas',
     'Anaheim Ducks':'Los Angeles',
     'San Jose Sharks':'San Francisco Bay Area',
     'Los Angeles Kings':'Los Angeles',
     'Calgary Flames':'Calgary',
     'Edmonton Oilers':'Edmonton',
     'Vancouver Canucks':'Vancouver',
     'Arizona Coyotes':'Phoenix'})
    #print(nhl_df1)

    # Seting the same index as a key to merge:
    #(a) NHL:
    nhl_df1 = nhl_df1.set_index('Metropolitan area')
    #(b) Cities:
    cities1 = cities1.set_index('Metropolitan area')

    # MERGE os 2 dataframes, joining without duplicates:
    df = nhl_df1.join(cities1)
    df1 = df.reset_index()
    #print(df1)

    # Create a column with the ration win/loss:
    # First pass to numeric:
    df1['W']=pd.to_numeric(df1['W'])
    df1['L']=pd.to_numeric(df1['L'])
    df1['Population (2016 est.)[8]']=pd.to_numeric(df1['Population (2016 est.)[8]'])
    df1.rename(columns = {'Population (2016 est.)[8]':'PopulationC_NHL'}, inplace = True)
    df1.rename(columns = {'team':'NHLteam'}, inplace = True)
    # Then calculate:
    df1['NHLratio_WL'] = df1['W'] / (df1['W'] + df1['L'])
    #print(df1)

    # Droping columns that are not necessary:
    df2 = df1.drop(['League','NHL'], axis=1)
    #print(df2)

    # grouping by cities:
    df3 = df2.groupby('Metropolitan area').agg({'NHLratio_WL': np.nanmean, 'PopulationC_NHL': np.nanmean})
    #print(df3)

    return df3


# Grouping df from functions:

def sports_team_performance():

    #(1) Calling df:

    NFL = nfl_func()
    NBA = nba_func()
    MLB = mlb_func()
    NHL = nhl_func()
    #(1) Grouping NFL - NBA:

    nba_nfl =pd.merge(NBA,NFL, on='Metropolitan area')
    pval_nba_nfl = stats.ttest_rel(nba_nfl['NBAratio_WL'],nba_nfl['NFLratio_WL'])[1]
    #print(nba_nfl)
    nba_nhl =pd.merge(NBA,NHL, on='Metropolitan area')
    pval_nba_nhl = stats.ttest_rel(nba_nhl['NBAratio_WL'],nba_nhl['NHLratio_WL'])[1]
    #print(nba_nhl)
    nba_mlb =pd.merge(NBA,MLB, on='Metropolitan area')
    pval_nba_mlb = stats.ttest_rel(nba_mlb['NBAratio_WL'],nba_mlb['MLBratio_WL'])[1]
    #print(nba_mlb)
    nhl_nfl =pd.merge(NHL,NFL, on='Metropolitan area')
    pval_nhl_nfl = stats.ttest_rel(nhl_nfl['NHLratio_WL'],nhl_nfl['NFLratio_WL'])[1]
    #print(nhl_nfl)
    nhl_mlb =pd.merge(NHL,MLB, on='Metropolitan area')
    pval_nhl_mlb = stats.ttest_rel(nhl_mlb['NHLratio_WL'],nhl_mlb['MLBratio_WL'])[1]
    #print(nhl_mlb)
    nfl_mlb =pd.merge(NFL,MLB, on='Metropolitan area')
    pval_nfl_mlb = stats.ttest_rel(nfl_mlb['NFLratio_WL'],nfl_mlb['MLBratio_WL'])[1]

    p_value = {'NFL': {"NFL": np.nan, 'NBA': pval_nba_nfl, 'NHL': pval_nhl_nfl, 'MLB': pval_nfl_mlb},
       'NBA': {"NFL": pval_nba_nfl, 'NBA': np.nan, 'NHL': pval_nba_nhl, 'MLB': pval_nba_mlb},
       'NHL': {"NFL": pval_nhl_nfl, 'NBA': pval_nba_nhl, 'NHL': np.nan, 'MLB': pval_nhl_mlb},
       'MLB': {"NFL": pval_nfl_mlb, 'NBA': pval_nba_mlb, 'NHL': pval_nhl_mlb, 'MLB': np.nan}
      }

    return pd.DataFrame(p_value)

sports_team_performance()

```
