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

print(df.info())
df.isnull()
df.isnull().sum()

df.dropna(subset=["ca"], axis=0, inplace=True)
df.dropna(subset=["thal"], axis=0, inplace=True)
# reset index, because we droped two rows
#df.reset_index(drop=True, inplace=True)
#df.head()

df.isnull().sum()



"""Replace original value by (original value)/(maximum value)."""

df['chol']= df['chol']/df['chol'].max()
print(df['chol'].head(3))

"""Binning is a process of transforming continuous numerical variables into discrete categorial “bins” for grouped analysis."""

df['age'].dtype
#df['age'].astype("int")
print(df['age'].head())

df.columns

df.boxplot()
plt.show()

#boxplot
plt.boxplot(df['ca'])
plt.title('Boxplot for ca')
plt.show()

Q1 = np.percentile(df['ca'], 25)
Q3 = np.percentile(df['ca'], 75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = [x for x in df['ca'] if x < lower_bound or x > upper_bound]

print("IQR Outliers:", outliers,"\n")

df.corr().head()

df.corr().tail()

df[['age','sex','num']].corr()

df["age"].unique()

df

gender_mapping = {1: 'male', 0: 'female'}
mapped_data = [gender_mapping[x] for x in df['sex']]

print("\n")
print(mapped_data)
