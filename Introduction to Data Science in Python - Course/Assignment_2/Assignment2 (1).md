
# Assignment 2
For this assignment you'll be looking at 2017 data on immunizations from the CDC. Your datafile for this assignment is in [assets/NISPUF17.csv](assets/NISPUF17.csv). A data users guide for this, which you'll need to map the variables in the data to the questions being asked, is available at [assets/NIS-PUF17-DUG.pdf](assets/NIS-PUF17-DUG.pdf). **Note: you may have to go to your Jupyter tree (click on the Coursera image) and navigate to the assignment 2 assets folder to see this PDF file).**

## Question 1
Write a function called `proportion_of_education` which returns the proportion of children in the dataset who had a mother with the education levels equal to less than high school (<12), high school (12), more than high school but not a college graduate (>12) and college degree.

*This function should return a dictionary in the form of (use the correct numbers, do not round numbers):*
```
    {"less than high school":0.2,
    "high school":0.4,
    "more than high school but not college":0.2,
    "college":0.2}
```


```python
def proportion_of_education():
    import pandas as pd
    import numpy as np
    immCDC = pd.read_csv("assets/NISPUF17.csv")

    immCDC = immCDC['EDUC1']

    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    relation=dict()

    for EDUC1 in immCDC:
        count = count + 1
        if EDUC1 == 4:
            count4 = count4 + 1
        if EDUC1 == 3:
            count3 = count3 + 1
        if EDUC1 == 2:
            count2 = count2 + 1
        if EDUC1 == 1:
            count1 = count1 + 1
    relation = {"less than high school": count1/count, "high school": count2/count,
    "more than high school but not college": count3/count, "college": count4/count}

    return relation

proportion_of_education()
```

    {'less than high school': 0.10202002459160373,
     'high school': 0.172352011241876,
     'more than high school but not college': 0.24588090637625154,
     'college': 0.47974705779026877}


## Question 2

Let's explore the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine from a healthcare provider. Return a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not.

*This function should return a tuple in the form (use the correct numbers:*

```python
def average_influenza_doses():
    import pandas as pd
    import numpy as np
    immCDC = pd.read_csv("assets/NISPUF17.csv", index_col=0)

#extracting the two columns at the same time
    immCDC3 = immCDC[['CBF_01','P_NUMFLU']]
    #print(immCDC3.head())

# immCDC3:
    #boolean masks
    mask = immCDC3 < 10
    # based in mask, replace values per NAN
    new_immCDC3 = immCDC3.where(mask)
    #print(new_immCDC3.head())

# new column sum values based in the 'CBF_01','P_NUMFLU' without 'value_counts':
    relation_immCDC = new_immCDC3.groupby(['CBF_01','P_NUMFLU']).size().reset_index(name='counts')

# counting values relation_immCDC dataframe :
    sum_values1 = relation_immCDC.groupby('CBF_01')['counts'].sum()

# multiply 2 columns, create a new column 'Multipl'
    relation_immCDC['Multipl'] = relation_immCDC.P_NUMFLU * relation_immCDC.counts

# counting values mutiplied in relation_immCDC dataframe:
    sum_mult = relation_immCDC.groupby('CBF_01')['Multipl'].sum()

# calculating the medium:
    result = sum_mult/sum_values1

# creating a tuple:
    t = tuple(result)

    return t

average_influenza_doses()
```
```
    (1.8799187420058687, 1.5963945918878317)
```


## Question 3
It would be interesting to see if there is any evidence of a link between vaccine effectiveness and sex of the child. Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it (at least one varicella dose) versus those who were vaccinated but did not contract chicken pox. Return results by sex.

*This function should return a dictionary in the form of (use the correct numbers):*
```
    {"male":0.2,
    "female":0.4}
```

Note: To aid in verification, the `chickenpox_by_sex()['female']` value the autograder is looking for starts with the digits `0.0077`.


```python
def chickenpox_by_sex():
    import pandas as pd

    immCDC = pd.read_csv("assets/NISPUF17.csv" , index_col=0)

    immCDC4 = immCDC[['SEX','P_NUMVRC','HAD_CPOX']]
    #print(immCDC4.head())

# Vaccine efficiency:
# new column sum values based in the 'SEX','P_NUMVRC','HAD_CPOX'
    relation_immCDC4 = immCDC4.groupby(['SEX','P_NUMVRC','HAD_CPOX']).size().reset_index(name='counts4')
# boolen masking
    mask = (relation_immCDC4 != 0) & (relation_immCDC4 != 77)
# based in mask, replace values per NAN
    new_immCDC4 = relation_immCDC4.where(mask)
# eliminating NAN
    new_immCDC4_without_NA = new_immCDC4.where(mask).dropna()

# KIDS who even vaccinated had chickenpox:

# filtering and sum kids who had chickenpox:
    KVC1 = new_immCDC4_without_NA.groupby(['SEX','P_NUMVRC','HAD_CPOX'])
    total_KVC1= KVC1.filter(lambda x: x['HAD_CPOX'] < 2)
# total values kids who had chickenpox and were vaccinated by SEX:
    soma_KVC1 = total_KVC1.groupby('SEX')['counts4'].sum()
    #print('Total kids who were vaccinated and had chickenpox:',soma_KVC1)

# KIDS who were vaccinated and did not had chickenpox:

# filtering and sum kids who had chickenpox:
    KVC2 = new_immCDC4_without_NA.groupby(['SEX','P_NUMVRC','HAD_CPOX'])
    total_KVC2= KVC2.filter(lambda x: x['HAD_CPOX'] > 1)
# total values kids who had chickenpox and were vaccinated by SEX:
    soma_KVC2 = total_KVC2.groupby('SEX')['counts4'].sum()
    #print('Total kids who were vaccinated and had chickenpox:',soma_KVC2)

# Dividing numbers obtained from:sum_kids_vaccinated & kids_vaccine
    division = soma_KVC1/soma_KVC2
# renaming keys for the future dictionary
    new_keys = division.rename({1:'male',2:'female'})

# (6) Creating dictionary:
    d = dict(new_keys)

    return d

chickenpox_by_sex()

```
```
    {'male': 0.009675583380762664, 'female': 0.0077918259335489565}
```


## Question 4
A correlation is a statistical relationship between two variables. If we wanted to know if vaccines work, we might look at the correlation between the use of the vaccine and whether it results in prevention of the infection or disease [1]. In this question, you are to see if there is a correlation between having had the chicken pox and the number of chickenpox vaccine doses given (varicella).

Some notes on interpreting the answer. The `had_chickenpox_column` is either `1` (for yes) or `2` (for no), and the `num_chickenpox_vaccine_column` is the number of doses a child has been given of the varicella vaccine. A positive correlation (e.g., `corr > 0`) means that an increase in `had_chickenpox_column` (which means more no’s) would also increase the values of `num_chickenpox_vaccine_column` (which means more doses of vaccine). If there is a negative correlation (e.g., `corr < 0`), it indicates that having had chickenpox is related to an increase in the number of vaccine doses.

Also, `pval` is the probability that we observe a correlation between `had_chickenpox_column` and `num_chickenpox_vaccine_column` which is greater than or equal to a particular value occurred by chance. A small `pval` means that the observed correlation is highly unlikely to occur by chance. In this case, `pval` should be very small (will end in `e-18` indicating a very small number).

[1] This isn’t really the full picture, since we are not looking at when the dose was given. It’s possible that children had chickenpox and then their parents went to get them the vaccine. Does this dataset have the data we would need to investigate the timing of the dose?


```python
def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd


    immCDC = pd.read_csv("assets/NISPUF17.csv")

    # exctracting 'P_NUMVRC','HAD_CPOX'
    immCDC1 = immCDC[['HAD_CPOX','P_NUMVRC']]
    #print(immCDC1.head())
    #print(immCDC1.info())

#(1) Relation between 'P_NUMVRC','HAD_CPOX'

# boolean masks: who have been vaccinated:
    mask = immCDC1 != 77
    # based in mask, replace values per NAN
    new_immCDC1 = immCDC1.where(mask)
    #print(len(new_immCDC1))
# eliminating NAN
    new_immCDC1_without_NA = new_immCDC1.where(mask).dropna()

# Correlation:
    corr, pval=stats.pearsonr(new_immCDC1_without_NA['HAD_CPOX'],new_immCDC1_without_NA['P_NUMVRC'])

    return corr

corr_chickenpox()
```
```
    0.07044873460147986
```
