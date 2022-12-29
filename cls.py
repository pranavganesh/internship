from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(222)
X = np.random.normal(0, 2, (200, 2))

w_target = np.random.normal(0,1, (2,1))

d = np.random.normal(0,1, (1,1))
C = np.random.normal(0,1, (1,2))


y = X@w_target + np.random.normal(0, 0.2, (200,1))

Y_tilde = [y, d]
X_tilde = [X, C]

lambd = np.asarray([1.0, 10000.0])


A_tilde = np.bmat([[np.sqrt(l)*x] for l,x in zip(lambd, X_tilde)])
y_tilde = np.bmat([[np.sqrt(l)*y] for l,y in zip(lambd, Y_tilde)])

w_estimate = np.linalg.inv(A_tilde.T@A_tilde)@A_tilde.T@y_tilde


y_estimate = X@w_estimate



x1 = y_estimate.flatten()
x2 = X[:, 0].flatten()
y_estimate = y_estimate.flatten()
y_true = y.flatten()

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x1,x2,y_estimate, label="Estimate")
ax.scatter(x1,x2,y_true, label="Ground Truth")
ax.view_init(elev=10., azim=20)

ax.set_xlabel('X0')
ax.set_ylabel('X1')
ax.set_zlabel('Y')

plt.legend()
plt.tight_layout()
plt.savefig("3d.jpeg")
plt.show()



