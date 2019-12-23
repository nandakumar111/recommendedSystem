import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

df = pd.read_csv("./dataset/FuelConsumption.csv")
# df.head()
#
# df.describe()

cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
# cdf.head(9)

# viz = cdf[['CYLINDERS', 'ENGINESIZE', 'CO2EMISSIONS', 'FUELCONSUMPTION_COMB']]
# viz.hist()

# plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS, edgecolors='blue', color='blue')
# plt.xlabel("CYLINDERS")
# plt.ylabel("CO2EMISSIONS")
# plt.show()

msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

# plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, edgecolors='blue', color='blue')
# plt.xlabel("ENGINESIZE")
# plt.ylabel("CO2EMISSIONS")
# plt.show()

from sklearn import linear_model

regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])

regr.fit(train_x, train_y)
# print('Coefficient : ', regr.coef_)
# print('Intercept : ', regr.intercept_)

# plt.scatter(cdf[['ENGINESIZE']], cdf[['CO2EMISSIONS']], color="blue")
# plt.plot(train_x, regr.coef_[0][0] * train_x + regr.intercept_[0], '-r')
# plt.xlabel('Engine Size')
# plt.ylabel('CO2 Emission')
# plt.show()

from sklearn.metrics import r2_score
train_y_ = regr.predict(train_x)
print("Mean absolute error: %.2f" % np.mean(np.absolute(train_y_ - train_y)))
print("MSE: %.2f" % np.mean((train_y_ - train_y) ** 2))
print("R2 Score: %.2f" % r2_score(train_y_, train_y))
