def answer_one():
    import pandas as pd
    import numpy as np

    enind = pd.read_excel(r'Energy Indicators.xlsx')
    #print(enind)
# Droping row undesirable:
    enindDR = enind.drop([0])
    #print(enindDR)

# Selecting the columns to work with:
    enindC = pd.DataFrame(enindDR,columns = ['Unnamed: 0','Energy Supply','Energy Supply per capita','Renewable Electricity Production'])
    #print(enindC)
# Rename columns names:
    enindCR = enindC.rename(columns = {'Unnamed: 0': 'Country','Renewable Electricity Production':'% Renewable','Energy Supply per capita':'Energy Supply per Capita'})
# print columns names:
    #print(enindCR.columns)
    #print(enindCR)
# Masking to replace '...' and 0 per NAN:
    mask = (enindCR != 0) & (enindCR != '...')
    new_enindCR = enindCR.where(mask)
    #print(new_enindCR)
# Multiplying *1.000.000 petajoule in magajoule in 'Energy Supply' column:
    new_enindCR['Energy Supply'] = new_enindCR['Energy Supply']*1000000
    #print(new_enindCR)
# Renaming list of country names:
    enind_country = new_enindCR.replace(['Republic of Korea','United States of America','United Kingdom of Great Britain and Northern Ireland',
    'China, Hong Kong Special Administrative Region'],['South Korea','United States','United Kingdom','Hong Kong'])
    #print(enind_country.head(30))
# extracting countries with "()" :
    pattern = '((?P<names>^[\w].*)(?:\ \()(?P<last>[\w].*\)$))'
    country1 = enind_country['Country'].str.extract(pattern).dropna().head(300)
    #print(country1)
    country2 = list(country1['names'])
    country3 = list(country1[0])
    #print(country2)
    #print(country3)
# replacing the extracted aboce in the enind_country DataFrame:
    enind_CR1 = enind_country.replace(country3,country2)
    #print(enind_CR1.head(40))

# extracting countries with number in the end:
    pattern1 = '((?P<names>^[A-Za-z]+)(\d+))'
    country4 = enind_country['Country'].str.extract(pattern1).dropna().head(300)
    #print(country4)
# creating lists to use in the replace:
    country5 = list(country4['names'])
    country6 = list(country4[0])
# replacing the extracted aboce in the enind_country DataFrame:
    enind_CR2 = enind_country.replace(country6,country5)
    #print(enind_CR2.head(40))

# converting the name of the dataframe to specified in the exercise:
    Energy = enind_CR2
    print(Energy)




answer_one()
