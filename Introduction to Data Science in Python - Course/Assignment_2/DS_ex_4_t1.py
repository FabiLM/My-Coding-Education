
def corr_chickenpox():
    import pandas as pd
    import scipy.stats as stats
    import numpy as np

    immCDC = pd.read_csv("NISPUF17.csv" , index_col=0)

    # exctracting 'P_NUMVRC','HAD_CPOX'
    immCDC1 = immCDC[['P_NUMVRC','HAD_CPOX']]
    #print(immCDC1.head())
    #print(immCDC1.info())

# Relation between 'P_NUMVRC','HAD_CPOX'

# boolean masks: who have been vaccinated:
    mask = (immCDC1 != 77) & (immCDC1 != 99)
    # based in mask, replace values per NAN
    new_immCDC1 = immCDC1.where(mask)
# eliminating NAN
    new_immCDC1_without_NA = new_immCDC1.where(mask).dropna()

# calculating max value of the columns:
    max_value = new_immCDC1_without_NA['HAD_CPOX'].max()

# randomizing to see if there is a correlation:
    new_immCDC1_without_NA = pd.DataFrame({'P_NUMVRC':np.random.randint(1,3,size=(15286)),
    'HAD_CPOX':np.random.randint(0,4,size=(15286))})
    #print(new_immCDC1_without_NA.head(20))

# Correlation:
    corr, pval=stats.pearsonr(new_immCDC1_without_NA['HAD_CPOX'],new_immCDC1_without_NA['P_NUMVRC'])
    print(pval)


    return corr

corr_chickenpox()
