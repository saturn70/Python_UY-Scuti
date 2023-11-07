#https://archive.ics.uci.edu/static/public/45/data.csv
import numpy as np
import pandas as pd
df=pd.read_csv('https://archive.ics.uci.edu/static/public/45/data.csv')
#first five rows
print(df.head())
print(df.tail())
print(df.columns)
print(df.shape)
print(df.describe())
print(df['age'])
print(df['age'].head())
print(df['age'].tail())
print(df['age'].max())
print(df['age'].min())
