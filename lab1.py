import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('a3/data_wrangling_rl1_2022_u5885254.csv')
df2 = pd.read_csv('a3/data_wrangling_rl2_2022_u5885254.csv')

# print first 5 rows
# print(df.head())

# print last 5 rows
# print(df.tail())

# print column names
# print(df.columns)

# view column values
# print(df['Date'])
# print(df[['Date','Location']])

# number of records
# print(df.size)
# print(df2.size)

# list row labels and column names
# print(df.axes)

# list the types of the columns
# print(df.dtypes)

# select the rows that have at least one missing value
# print(df[df.isnull().any(axis=1)])
# print(df2[df2.isnull().any(axis=1)])

# select the rows that have missing values in all columns
# print(df[df.isnull().all(axis=1)])

# describe Date column
# print(df[['Date','Location']].describe())

# compute the correlation
# print(df['MinTemp'].corr(df['MaxTemp']))

# view all the unique values of a column
# print(df['Date'].unique())

# plot histogram
## df[['MinTemp','MaxTemp']].plot(kind='hist', bins=50)

# plot box
# df[['MinTemp','MaxTemp']].plot(kind='box')

# plot density distribution
# df[['MinTemp','MaxTemp']].plot(kind='kde')

# show plot
# plt.show()

# save plot to images
# plt.savefig()

date_match = df[df['birth_date'].str.match(
    '^((0[1-9])|(1[0-2]))\/((0[1-9])|(1[0-9])|(2[0-9])|(3[0-1]))\/(\d{4})$') == True]
date_match2 = df2[df2['birth_date'].str.match(
    '^((0[1-9])|(1[0-2]))\/((0[1-9])|(1[0-9])|(2[0-9])|(3[0-1]))\/(\d{4})$') == True]

print(len(date_match))
print(len(date_match2))
