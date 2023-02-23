import sys
try:
	import theta
# theta1 = -0.02084648959347221
# theta0 = 8447.90304693619
	theta1 = theta.theta1
	theta0 = theta.theta0
except:
	theta1 = 0
	theta0 = 0

mileage = input("please enter your mileage:")

# print(theta0)
# print(theta1)

try:
	if int(mileage) < 0:
		raise Exception()
	prediction = theta1 * int(mileage) + theta0
	if prediction < 0:
		prediction = 0
	print("the predicted price to sell a car with", mileage, "km mileage is:", round(prediction,0))
except:
	print("wrong input")
	sys.exit(1)