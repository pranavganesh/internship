import numpy as np
from matplotlib import pyplot as plt



np.random.seed(222)
X = np.random.normal(0,1, (100, 1))

w_target_1 = np.random.normal(0,1, (1,1))
w_target_2 = np.random.normal(0,1, (1,1))
w_target_3 = np.random.normal(0,1, (1,1))

y_1 = X@w_target_1 + np.random.normal(0, 0.2, (100,1))
y_2 = X@w_target_1 + np.random.normal(0, 0.2, (100,1))
y_3 = X@w_target_1 + np.random.normal(0, 0.2, (100,1))

Y = [y_1,y_2,y_3]

lambd = np.asarray([0.3, 0.1, 0.1])

A_tilde = np.bmat([[l*X] for l in lambd])
y_tilde = np.bmat([[l*y] for l,y in zip(lambd, Y)])

w_estimate = np.linalg.inv(A_tilde.T@A_tilde)@A_tilde.T@y_tilde
print(w_estimate)
y_estimate = X@w_estimate

plt.figure(figsize=(15,10))
plt.scatter(X.flat, y_estimate.flat, label="Prediction")
plt.scatter(X.flat, y_1.flat, color='red', alpha=0.3, label="Data1")
plt.scatter(X.flat, y_2.flat, color='green', alpha=0.3, label="Data2")
plt.scatter(X.flat, y_3.flat, color='orange', alpha=0.3, label="Data3")

plt.tight_layout()
plt.title("Multi-Objetive Least Squares Regression")
plt.legend()
plt.savefig("estimate.png")
plt.show()