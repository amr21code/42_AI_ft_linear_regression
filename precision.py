import sys
import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

try:
	import theta
	theta1 = theta.theta1
	theta0 = theta.theta0
	data = pd.read_csv('data.csv')
except:
	print("input files not found - check if data.csv is present and run train.py first")
	sys.exit(1)

def calc_mse(data, mean):
	mse = np.sum((data["price"] - mean) ** 2) / len(data)
	return mse

def calc_mse_lin_reg(data, theta0, theta1):
	predictions = theta1 * data["km"] + theta0
	squared_diff = (data["price"] - predictions) ** 2
	mse = np.sum(squared_diff) / len(data)
	return mse

mean = np.mean(data["price"])
plot_data = [mean] * len(data["km"])

mse = calc_mse(data, mean)
mse_lin_reg = calc_mse_lin_reg(data, theta0, theta1)
# print(mse_lin_reg)
# print(mse)
# print(mean)
r2 = (mse - mse_lin_reg) / mse
print("The km/price relationship accounts for r^2", round(r2*100,2), "% of the variation")
print("The Root Mean Squared Error is", round(math.sqrt(mse_lin_reg),0), "meaning that the prediction is in the range of +-", round(math.sqrt(mse_lin_reg),0), "of the price")




plt.scatter(x=data["km"], y=data["price"], color="black")
plt.xlabel("km")
plt.ylabel("price")
plt.plot(data["km"], plot_data)
plt.plot(list(range(20000, 250000)), [theta1 * x + theta0 for x in range(20000, 250000)], color="red")
plt.savefig('prescision.png')