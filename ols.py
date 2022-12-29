import numpy as np
from matplotlib import pyplot as plt



np.random.seed(222)
X = np.random.normal(0,1, (200, 1))
w_target = np.random.normal(0,1, (1,1))

y = X@w_target + np.random.normal(0, 1, (200,1))


w_estimate = np.linalg.inv(X.T@X)@X.T@y
y_estimate = X@w_estimate


plt.figure(figsize=(15,10))
plt.scatter(X.flat, y_estimate.flat, label="Prediction")
plt.scatter(X.flat, y.flat, color='red', alpha=0.4, label="Data")
plt.tight_layout()
plt.title("Least Squares Regression")
plt.legend()
plt.savefig("least_squares.png")
plt.show()