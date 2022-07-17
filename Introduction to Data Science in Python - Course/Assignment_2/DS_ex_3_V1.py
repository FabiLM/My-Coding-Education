def chickenpox_by_sex():
    import pandas as pd
    from functools import reduce
    immCDC = pd.read_csv("NISPUF17.csv" , index_col=0)


# Version using value_counts():

    #extracting 'SEX', 'P_NUMVRC'
    immCDC1 = immCDC[['SEX','P_NUMVRC']]

    # exctracting 'SEX','IAGECPXR'
    immCDC2 = immCDC[['SEX','AGECPOXR']]

    # exctracting 'SEX','IAGECPXR'
    immCDC3 = immCDC[['P_NUMVRC','AGECPOXR']]

    # exctracting 'SEX','AGECPOXR', 'P_NUMVRC'
    immCDC4 = immCDC[['SEX','P_NUMVRC','AGECPOXR']]


#(1) Relation 'SEX', 'P_NUMVRC'

# sum values based in SEX types, creates a new colum 'counts'
    relation_immCDC1 = immCDC1.value_counts().to_frame('counts1').reset_index()

# boolean masks: who have been vaccinated:
    mask = relation_immCDC1 != 0
    # based in mask, replace values per NAN
    new_immCDC1 = relation_immCDC1.where(mask)

# eliminating NAN
    new_immCDC1_without_NA = new_immCDC1.where(mask).dropna()

# counting kids who have been vaccinated by 'SEX':
    sum_kids_vaccinated = new_immCDC1_without_NA.groupby('SEX')['counts1'].sum()

# sum the values obtained above in sum_kids_vaccinated:
    total_KV = new_immCDC1_without_NA['counts1'].sum()
    #print('Total kids vaccinated:',total_KV)

#(2) Relation 'SEX', 'AGECPOXR'

# sum values based in SEX types, creates a new colum 'counts'
    relation_immCDC2 = immCDC2.value_counts().to_frame('counts2').reset_index()

# counting values relation_immCDC dataframe, total number of boys and girls who had chickenpox:
    sum_kids_had_chickenpox = relation_immCDC2.groupby('SEX')['counts2'].sum()

    # returned the numbers of male and female
# there is no need for mask here

#(3) Relation between 'P_NUMVRC','AGECPOXR'
# sum values based in 'P_NUMVRC' types, creates a new colum 'counts'
    relation_immCDC3 = immCDC3.value_counts().to_frame('counts3').reset_index()

# boolean masks: who have been vaccinated:
    mask = relation_immCDC3 != 0
    # based in mask, replace values per NAN
    new_immCDC3 = relation_immCDC3.where(mask)

# eliminating NAN
    new_immCDC3_without_NA = new_immCDC3.where(mask).dropna()

# counting kids who have been vaccinated and had chickenpox
    sum_kids_vaccinated_chickenpox = new_immCDC3_without_NA.groupby('P_NUMVRC')['counts3'].sum()

# sum the values obtained above in sum_kids_vaccinated_chickenpox:
    total_KVC = new_immCDC3_without_NA['counts3'].sum()
    #print('Total kids vaccinated who had chickenpox:',total_KVC)

# (4) Vaccine efficiency:
# new column sum values based in the 'SEX','P_NUMVRC','AGECPOXR'
    relation_immCDC4 = immCDC4.value_counts().to_frame('counts4').reset_index()

# boolen masking
    mask = relation_immCDC4 != 0
# based in mask, replace values per NAN
    new_immCDC4 = relation_immCDC4.where(mask)
# eliminating NAN
    new_immCDC4_without_NA = new_immCDC4.where(mask).dropna()

# total values kids who had chickenpox and were vaccinated:
    total_KVC1 = new_immCDC4_without_NA['counts4'].sum()
    #print('Total kids who were vaccinated and had chickenpox:',total_KVC1)

# counting kids who have been vaccinated and had chickenpox divided by sex:
    kids_vacinne= new_immCDC4_without_NA.groupby('SEX')['counts4'].sum()

# replace index

# (5) Dividing numbers obtained from:sum_kids_vaccinated & kids_vaccine
    division = kids_vacinne/sum_kids_vaccinated

# renaming keys for the future dictionary
    new_keys = division.rename({1:'male',2:'female'})

# (6) Creating dictionary:
    d = dict(new_keys)
    print(d)

    return d

chickenpox_by_sex()
