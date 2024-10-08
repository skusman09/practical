'''
WAP to deal with the data using pandas library
Theory:
a. Pandas
b. Matplotlib
c. Numpy
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("/content/TSLA.csv")
print("Data")
print(df)
print("\n Bottom Data")
print(df.tail())
print("\n Top 3 rows of Data")
print(df.head(3))
print("\n Selecting a single column")
c = df["Close"]
print(c)
print(c.head)
c1 = df[["Close","Open"]].head()
print(c1)
print("\n Selecting Rows by Index")
print(df[100:110])
print("\n Selecting Rows by Index and Specific Columns")
d = df[100:110][['Close','Volume','High','Low']]
print(d)
print("\n by loc function")
print(df.loc[100:110])
print("\n by iloc function")
print(df.iloc[100:110])
print("\n Boolean Indexing")
print(df[df.Close>100])
print("\n Info Function")
print(df.info())
print("\n Describe Function")
print(df.describe())
print("\n Mean Function")
print(df['Close'].mean())
print("\n STD Function")
print(df['High'].std())
print("\n MAX Function")
print(df['Open'].max())
print("\n Shape")
print(df.shape)


import pandas as pd
data = {
    "day": ['1/1/2020', '1/2/2020', '1/3/2020', '1/4/2020', '1/5/2020', '1/6/2020', '1/7/2020'],
    "temperature": [32, 35, 28, 24, 32, 31, 32],
    "windspeed": [6, 7, 2, 7, 4, 2, 2],
    "event": ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain', 'Sunny', 'Snow']
    }
df = pd.DataFrame(data)
print(df)

df.columns
df.index
type(df['windspeed'])
df.dtypes
newdf = df.copy()
newdf
df.T
df.sort_index(axis=0, ascending = False)
df.sort_values("temperature" , axis = 0, ascending = False)
df
df.loc[0, 'temperature'] = 26
df.loc[4, 'event'] = 'Rain'
df
df.loc[(df['temperature'] <= 30) & (df['windspeed'] >= 6)]
df
df.loc[1, 'event']
df.iloc[[0,1], [1,3]]
df
df.drop([2,4], inplace = True)
df
df.drop(['windspeed'],axis =1)
df.reset_index(inplace = True)
df
df['Humidity']=[16,18,19,20,21]
df
df.notnull()
df.isnull().sum()
data1 = [
          ('shiv', 80),
          ('ram', 70)
]
df1 = pd.DataFrame(data1, columns = ['Name', 'Marks'])
df1
data2 = [
         {'name': 'sanket', 'marks':55},
         {'name': 'yug', 'marks':65}
]
df2 = pd.DataFrame(data2)
df2

df3 = pd.concat([df2, df1], ignore_index = True)
df3

df4 = pd.concat([df, df2], axis = 1)
df4

df5 = pd.concat([df3,df1], ignore_index = True)
df5
df5.info()

newdf.to_csv('weather_sample.csv', index = False)