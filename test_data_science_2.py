import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./dataset/automobile.csv')
# print(df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr())

# sns.regplot(x='engine-size', y='price', data=df)
# plt.ylim(0,)
# plt.show()

# df['stroke'].replace('?',np.nan, inplace=True)
# df['stroke'] = df['stroke'].astype('float')
# sns.regplot(x='stroke', y='price', data=df)
# plt.ylim(0,)
# plt.show()
# print(df[['stroke', 'price']].corr())

# sns.boxplot(x='drive-wheels', y='price', data=df)
# plt.ylim(0,)
# plt.show()

# drive_wheels_counts = df['drive-wheels'].value_counts().to_frame().rename(columns={'drive-wheels': 'value_counts'})
# drive_wheels_counts.index.name = 'drive-wheels'
# print(drive_wheels_counts)

# print(df['drive-wheels'].unique())

df_group_one = df[['drive-wheels', 'body-style', 'price']]
group_test1 = df_group_one.groupby(['drive-wheels', 'body-style'], as_index=False).mean()

grouped_pivot = group_test1.pivot(index='drive-wheels', columns='body-style')
grouped_pivot = grouped_pivot.fillna(0)  # fill missing values with 0

# print(df[['body-style', 'price']].groupby(['body-style'],as_index=False).mean())
# plt.pcolor(grouped_pivot, cmap='RdBu')
# plt.colorbar()
# plt.show()

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
X = df[['highway-mpg', 'engine-size']].head(100)
Y = df['price'].head(100)
lm.fit(X,Y)
Yhat=lm.predict(X)
df = df.head(100)
print(df.corr())
