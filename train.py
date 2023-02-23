import sys
try:
	import pandas as pd
	import matplotlib.pyplot as plt
except:
	print("you need to pip install matplotlib pandas first")
	sys.exit(1)
import signal, sys
def sigint_handler(signal, frame):
    print ('Ctrl+C not allowed')

signal.signal(signal.SIGINT, sigint_handler)

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
theta0_prev = None
L = 0.1
epochs = 10000
try:
	approx = int(sys.argv[1])
	print("custom approximation set to:", approx)
except:
	print("no custom approximation, setting to standard 8")
	approx = 8

for i in range(epochs):
	theta1, theta0 = gradient_descent(theta1, theta0, data, L)
	if (i % 1000) == 0:
		print(i, "/", epochs, "- thetas", theta1, theta0)
	if theta0_prev != round(theta0, approx):
		theta0_prev = round(theta0, approx)
	else:
		print("stopped at iteration", i, "- reached approximation to", approx,"th decimal place")
		break


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
plt.xlabel("km")
plt.ylabel("price")
plt.plot(list(range(20000, 250000)), [theta1 * x + theta0 for x in range(20000, 250000)], color="red")
plt.savefig('plot.png')