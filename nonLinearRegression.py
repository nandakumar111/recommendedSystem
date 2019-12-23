import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# x = np.arange(-5.0, 5.0, 0.1)
# y = 2 * x + 3 # linear
# y = 1*(x**3) + 1*(x**2) + 1*x + 3 # cubic
# y = np.power(x,2) # quadratic
# y = np.exp(x) # Exponential
# y = np.log(x) # Logarithmic
# y_noise = 20 * np.random.normal(size=x.size)
# ydata = y + y_noise
# plt.plot(x, ydata, 'bo')
# plt.plot(x, y, 'r')
#
# plt.xlabel("Dependent Value")
# plt.ylabel("Independent Value")
# plt.show()
# downloading dataset

df = pd.read_csv("./dataset/china_gdp.csv")
df.head(10)
plt.figure(figsize=(8,5))
x_data, y_data = (df["Year"].values, df["Value"].values)
plt.plot(x_data, y_data, 'br')
plt.ylabel('GDP')
plt.xlabel('Year')
plt.show()
