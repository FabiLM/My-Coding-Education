
def corr_chickenpox():
    import pandas as pd
    import scipy.stats as stats
    import numpy as np

    immCDC = pd.read_csv("NISPUF17.csv" , index_col=0)

    # exctracting 'P_NUMVRC','HAD_CPOX'
    immCDC1 = immCDC[['P_NUMVRC','HAD_CPOX']]
    #print(immCDC1.head())
    #print(immCDC1.info())

#(1) Relation between 'P_NUMVRC','HAD_CPOX'
# sum values based in 'P_NUMVRC' types, creates a new colum 'counts'
    #relation_immCDC1 = immCDC1.groupby(['P_NUMVRC','HAD_CPOX']).size().reset_index(name='counts')
    #print(relation_immCDC1.head())
# boolean masks: who have been vaccinated:
    mask = (immCDC1 != 77) & (immCDC1 != 99)
    # based in mask, replace values per NAN
    new_immCDC1 = immCDC1.where(mask)
    #print(new_immCDC1)
# eliminating NAN
    new_immCDC1_without_NA = new_immCDC1.where(mask).dropna()
    #print(new_immCDC1_without_NA)
# calculating max value of the columns:
    max_value = new_immCDC1_without_NA['HAD_CPOX'].max()
    #print(max_value)

# randomizing to see if there is a correlation:
    new_immCDC1_without_NA = pd.DataFrame({'P_NUMVRC':np.random.randint(1,3,size=(15286)),
    'HAD_CPOX':np.random.randint(0,4,size=(15286))})
    #print(new_immCDC1_without_NA.head(20))
#corr, pval=stats.pearsonr(df["had_chickenpox_column"],df["num_chickenpox_vaccine_column"])
# Correlation:
    corr, pval=stats.pearsonr(new_immCDC1_without_NA['HAD_CPOX'],new_immCDC1_without_NA['P_NUMVRC'])
    print(pval)


    return corr

corr_chickenpox()
