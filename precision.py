import sys
import math
try:
	import pandas as pd
	import matplotlib.pyplot as plt
	import numpy as np
except:
	print("you need to pip install matplotlib pandas numpy first")
	sys.exit(1)

try:
	import theta
	theta1 = theta.theta1
	theta0 = theta.theta0
	data = pd.read_csv('data.csv')
	data_norm = pd.read_csv('data.csv')
except:
	print("input files not found - check if data.csv is present and run train.py first")
	sys.exit(1)


mean = np.mean(data["price"])
plot_data = [mean] * len(data["km"])

def calc_mse(data, mean):
	mse = np.sum((data["price"] - mean) ** 2) / len(data)
	return mse

def calc_mse_lin_reg(data, theta0, theta1):
	predictions = theta1 * data["km"] + theta0
	squared_diff = (data["price"] - predictions) ** 2
	mse = np.sum(squared_diff) / len(data)
	return mse

mse = calc_mse(data, mean)
mse_lin_reg = calc_mse_lin_reg(data, theta0, theta1)
# print(math.sqrt(mse_lin_reg))
# print(mse)

def gradient_descent(theta1, theta0, points, L):
	theta1_gradient = 0
	theta0_gradient = 0

	n = len(points)

	for i in range(n):
		x = points.iloc[i].km
		y = points.iloc[i].price
		theta1_gradient = (((theta1 * x + theta0) - y) * x)
		theta0_gradient = ((theta1 * x + theta0) - y)
		theta1 -= L * (1/n) * theta1_gradient
		theta0 -= L * (1/n) * theta0_gradient

	return theta1, theta0


#get max for normalization
max_km = data_norm["km"].max()
max_price = data_norm["price"].max()

#normalization
data_norm["km"] /= max_km
data_norm["price"] /= max_price

rmse_precision = []
theta1_rmse = 0
theta0_rmse = 0

for i in range(1000):
	theta1_rmse, theta0_rmse = gradient_descent(theta1_rmse, theta0_rmse, data_norm, 0.1)
	# print(theta1_rmse, theta0_rmse)
	# print(math.sqrt(calc_mse_lin_reg(data, theta0_rmse, theta1_rmse)))
	rmse_precision.append(math.sqrt(calc_mse_lin_reg(data, theta0_rmse * max_price, theta1_rmse * max_price / max_km)))

plt.clf()
plt.plot(np.array(rmse_precision))
plt.savefig('prescision_rmse.png')

#de-normalization
theta1 *= max_price / max_km
theta0 *= max_price

r2 = (mse - mse_lin_reg) / mse
print("The km/price relationship accounts for r^2", round(r2*100,2), "% of the variation")
print("The Root Mean Squared Error is", round(math.sqrt(mse_lin_reg),0), "meaning that the prediction is in the range of +-", round(math.sqrt(mse_lin_reg),0), "of the price")



plt.scatter(x=data["km"], y=data["price"], color="black")
plt.xlabel("km")
plt.ylabel("price")
plt.plot(data["km"], plot_data)
plt.plot(list(range(20000, 250000)), [theta1 * x + theta0 for x in range(20000, 250000)], color="red")
plt.savefig('prescision.png')