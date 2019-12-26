import pandas as pd
import numpy as np
# import matplotlib.pylab as plt

# other_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
# df = pd.read_csv(other_path, header=None)
#
# headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
#          "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
#          "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
#          "peak-rpm","city-mpg","highway-mpg","price"]
#
# df.columns = headers
# df['price'] = df['price'].replace('?',np.nan)
# df.dropna(subset=['price'], axis=0, inplace=True)
# df['price'] = df['price'].astype('int')
# df.to_csv('./dataset/automobile.csv', index=False)

# TODO() If you don't have data set you can enable above lines

df = pd.read_csv('./dataset/automobile.csv')
bins = np.linspace(min(df['price']), max(df['price']), 4)
group_name = ['Low', 'Medium', 'High']
df['price_binned'] = pd.cut(df['price'], bins, labels=group_name, include_lowest=True)

import matplotlib as plt
from matplotlib import pyplot
plt.pyplot.hist(df["horsepower"])

# set x/y labels and plot title
# plt.pyplot.xlabel("horsepower")
# plt.pyplot.ylabel("count")
# plt.pyplot.title("horsepower bins")
# plt.pyplot.show()

df['horsepower'] = df['horsepower'].replace('?',np.nan)
df.dropna(subset=["horsepower"], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('int')
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_name, include_lowest=True )

# print(df['horsepower'].head(5))
# print(pd.get_dummies(df['fuel-type']))
# print(df['horsepower-binned'].value_counts())

# draw historgram of attribute "horsepower" with bins = 3
# plt.pyplot.hist(df["horsepower"], bins = 3)

# set x/y labels and plot title
# plt.pyplot.xlabel("horsepower")
# plt.pyplot.ylabel("count")
# plt.pyplot.title("horsepower bins")
# plt.pyplot.show()

# dummy_variable_2 = pd.get_dummies(df['aspiration'])

# change column names for clarity
# dummy_variable_2.rename(columns={'std':'aspiration-std', 'turbo': 'aspiration-turbo'}, inplace=True)

# df = pd.concat([df, dummy_variable_2], axis=1)
# df.drop("aspiration", axis = 1, inplace=True)
# print(df['aspiration-std'].head(4))
df['price'] = df['price'] + 1
print(df['price'].std())
