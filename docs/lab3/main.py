import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/mezgoodle/ad_labs/master/data/Crime.csv')
# print(df)

ser = pd.Series(df['CrimeRate'], index=[i for i in range(0 + 3, len(df['CrimeRate']) + 3)])
print(ser.loc[3:5])
print(ser.iloc[3:5])

df['WageRatio'] = df['Wage'] / df['StateSize']
print(df['WageRatio'])

a = pd.Series(np.arange(0, 7))
b = pd.Series(['I', 'II', 'III'])
multi_in = pd.MultiIndex.from_product([['A', 'B'], b, a])
df = df[:-5]
df.set_index([multi_in], inplace=True)
print(df)
print(df.mean(level=1))
print(df.max(level=2))
# s = pd.Series(df['CrimeRate'])
# print(s[s > 100])
# print(s[:, 'II', :])
# print(s['A', 'II'])
