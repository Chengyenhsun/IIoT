import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("oddExperiment.txt", delimiter=" ", skiprows=1)

x = data[:, 1]
y = data[:, 0]

plt.scatter(x, y, label="Data Points")

p1 = np.poly1d(np.polyfit(x, y, 1))
plt.plot(x, p1(x), "r-", label=f"Fit of degree 1, LSE: {np.mean((p1(x)-y)**2):.5f}")

p2 = np.poly1d(np.polyfit(x, y, 2))
plt.plot(x, p2(x), "m-", label=f"Fit of degree 2, LSE: {np.mean((p2(x)-y)**2):.5f}")

plt.legend()
plt.title("oddExperiment Data")

plt.savefig("lab14_plus.png")
