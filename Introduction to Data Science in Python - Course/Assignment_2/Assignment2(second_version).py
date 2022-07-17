def average_influenza_doses():
    import pandas as pd
    immCDC = pd.read_csv("NISPUF17.csv" , index_col=0)

# Version WITHOUT value_counts():

#extracting the two columns at the same time
    immCDC3 = immCDC[['CBF_01','P_NUMFLU']]
    #print(immCDC3.head())

# immCDC3:
    #boolean masks
    mask = immCDC3 < 10
    # based in mask, replace values per NAN
    new_immCDC3 = immCDC3.where(mask)

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
    print(t)

    return t

average_influenza_doses()
