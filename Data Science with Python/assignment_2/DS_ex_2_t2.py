def average_influenza_doses():
    import pandas as pd
    immCDC = pd.read_csv("NISPUF17.csv" , index_col=0)

    #extracting the two columns at the same time
    immCDC3 = immCDC[['CBF_01','P_NUMFLU']]
    #print(immCDC3.head())

# immCDC1:
    #boolean masks
    mask = immCDC3 < 10
    # based in mask, replace values per NAN
    new_immCDC3 = immCDC3.where(mask)
    #print(new_immCDC3.head())
    # eliminating NAN: can be done, because in this case the numbers NAN cases are not represenntative.
    # but it´s not necessatry because in sum will be not used.

# sum values based in CBF_01 types, creates a new colum 'counts'
    relation_immCDC = new_immCDC3.value_counts().to_frame('counts').reset_index()
    #print(relation_immCDC)
# counting values relation_immCDC dataframe :
    sum_values1 = relation_immCDC.groupby('CBF_01')['counts'].sum()
    #print(sum_values1)
# multiply 2 columns, create a new column 'Multipl'
    relation_immCDC['Multipl'] = relation_immCDC.P_NUMFLU * relation_immCDC.counts
    #print(relation_immCDC)
# counting values mutiplied in relation_immCDC dataframe:
    sum_mult = relation_immCDC.groupby('CBF_01')['Multipl'].sum()
    #print(sum_mult)
# calculating the medium:
    result = sum_mult/sum_values1
    #print(result)
# creating a tuple:
    t = tuple(result)
    print(t)

    return t

average_influenza_doses()
