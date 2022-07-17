def answer_one():
    import pandas as pd
    import numpy as np

    enind = pd.read_excel(r'Energy Indicators.xlsx')
    #print(enind)
    GDP_original = pd.read_excel('API_NY.GDP.MKTP.CD_DS2_en_excel_v2_4150762.xls',skiprows=3)
    ScimEn_original = pd.read_excel(r'scimagojr country rank 1996-2021.xlsx')
    #print(enind)

# (A) ENERGY df:
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
# replacing the extracted above in the enind_country DataFrame:
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
    enind_CR2 = enind_CR1.replace(country6,country5)
    #print(enind_CR2.head(40))
# converting the name of the dataframe to specified in the exercise:
    Energy = enind_CR2
    #print(Energy)

# (B) GDP df:

# renaming the countries:
    GDP1= GDP_original.replace(['Korea, Rep.','Iran, Islamic Rep','Hong Kong SAR, China'],
    ['South Korea','Iran','Hong Kong'])
    #print(GDP1.head(130))
# rename the column "Country Name" to 'Country':
    GDP1 = GDP1.rename(columns = {'Country Name': 'Country'})
    #print(GDP1.head(130))
# creating df with the specific columns
    GDP = GDP1[['Country','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']]
    #print(GDP.head())

# (C) ScimEn df:
# preparing the dataframe to concat:
    ScimEn = ScimEn_original.drop(columns=['Region'])
    ScimEn_m = ScimEn[:15]
    #print(ScimEn_m.head())

# Meging:
    df = pd.merge(ScimEn,Energy,how='inner',left_on='Country',right_on='Country')
    final_df = pd.merge(df,GDP,how='inner',left_on='Country',right_on='Country')
    final_df = final_df.set_index('Country')
    print(final_df)
    print(len(final_df))

# CONCATENING:
    #df = pd.concat([ScimEn_m,Energy,GDP], axis=1)
    #print(df.head())
# droping column 'Country' and 'Index replace with Rank'
    #df1 = df.set_index('Country')
    #print(df1.head())
    #print(df1.columns)
    #print(len(df1))

    return final_df

answer_one()
