def answer_three():
    import pandas as pd
    import numpy as np

    ScimEn_original = pd.read_excel(r'scimagojr country rank 1996-2021.xlsx')
    print(ScimEn_original)

# preparing the dataframe to concat:
    ScimEn = ScimEn_original.drop(columns=['Region'])
    print(ScimEn.head())

answer_three()
