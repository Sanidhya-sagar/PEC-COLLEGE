import matplotlib.pyplot as plt
X = []
Y = []
for i in range(10):
    X.append(i)
    Y.append(i * i)

plt.plot(X, Y, marker = 'o')
plt.grid(True)
plt.show()
