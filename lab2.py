import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('a3/data_wrangling_rl1_2022_u5885254.csv')
## select rows that have at least one missing value. axis of 1 means missing column value, axis of 0 means missing row value
print(df[df.isnull().any(axis=1)])

## impute missing value by its mean
# mean_temp = df['MinTemp'].mean()
# df['MinTemp'].fillna(mean_temp)

# ## z-score normalisation
# mean_temp = df['MinTemp'].mean()
# std_val = df['MinTemp'].std()
# MinTempZsc=[]

# for val in df['MinTemp']:
#   MinTempZsc.append((val-mean_temp)/std_val)

# df['MinTempZsc'] = MinTempZsc

# ## plot
# df[['MinTemp','MinTempZsc']].plot(kind='hist', bins=50)

# df[['MinTemp','MinTempZsc']].plot(kind='box')

# plt.show()