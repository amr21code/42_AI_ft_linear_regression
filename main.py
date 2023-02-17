import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

# plt.scatter(data.km, data.price)
# plt.savefig('plot.png')


def gradient_descent(m_now, b_now, points, L):
	m_gradient = 0
	b_gradient = 0

	n = len(points)

	for i in range(n):
		x = points.iloc[i].km
		y = points.iloc[i].price
		
		m_gradient += (1/n)  * (((m_now * x + b_now) - y) * x)
		b_gradient += (1/n) * ((m_now * x + b_now) - y)

		m_now = m_now - m_gradient * L 
		b_now = b_now - b_gradient * L

	return m_now, b_now

m = 0
b = 0
L = 0.000000000008
epochs = 1000

for i in range(epochs):
	m, b = gradient_descent(m, b, data, L)

print(m, b)

plt.scatter(data.km, data.price, color="black")
plt.plot(list(range(20000, 250000)), [m * x + b for x in range(20000, 250000)], color="red")
plt.savefig('plot.png')
