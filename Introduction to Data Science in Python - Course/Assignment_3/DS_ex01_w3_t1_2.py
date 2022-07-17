def answer_two():
    import pandas as pd
    import numpy as np

    GDP_original = pd.read_excel('API_NY.GDP.MKTP.CD_DS2_en_excel_v2_4150762.xls',skiprows=3)
    #print(GDP_original)

# renaming the countries:
    GDP1= GDP_original.replace(['Korea, Rep.','Iran, Islamic Rep','Hong Kong SAR, China'],
    ['South Korea','Iran','Hong Kong'])
    #print(GDP1.head(130))
# rename the column "Country Name" to 'Country':
    GDP1 = GDP1.rename(columns = {'Country Name': 'Country'})
    #print(GDP1.head(130))
# creating df with the specific columns

    GDP = GDP1[['Country','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']]
    print(GDP.head())

answer_two()
