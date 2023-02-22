import sys
import pandas as pd
import matplotlib.pyplot as plt

try:
	data = pd.read_csv('data.csv')
except FileNotFoundError:
	print("file not found")
	sys.exit(1)

#get max for normalization
max_km = data["km"].max()
max_price = data["price"].max()

#normalization
data["km"] /= max_km
data["price"] /= max_price

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

theta1 = 0
theta0 = 0
L = 0.1
epochs = 1000

for i in range(epochs):
	theta1, theta0 = gradient_descent(theta1, theta0, data, L)


#de-normalization
data["km"] *= max_km
data["price"] *= max_price
theta1 *= max_price / max_km
theta0 *= max_price

#export thetas
file = open('theta.py', 'w')
filcontent = "theta0 = " + str(theta0) + "\r\n" + "theta1 = " + str(theta1) + "\r\n"
file.write(filcontent)
file.close()


plt.scatter(x=data["km"], y=data["price"], color="black")
plt.plot(list(range(20000, 250000)), [theta1 * x + theta0 for x in range(20000, 250000)], color="red")
plt.savefig('plot.png')