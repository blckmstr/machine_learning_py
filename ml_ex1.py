import matplotlib.pyplot as plt
import os
import numpy as np

print(os.getcwd())

data = []

with open(os.getcwd()+'/ex1data1.txt','r') as f:
    data = f.read().replace('\n',',').split(',')
    data = data[:-1]

X = np.array(data[::2])
y=[]
for i in data:
    if i not in X:
        y.append(i)

y = np.array(y)
y = y.astype('float')
print(len(X),len(y))

#plt.scatter(X,y)
#plt.show()

X_train = np.c_[np.ones(X.shape[0]), X]
X_train = X_train.astype('float')
print(y.dtype)
theta = np.zeros(2)
#computing the cost

def compute_cost(X,y,theta):
    # number of training examples
    m = len(X)
    print(theta.dtype)
    H = np.dot(X_train, theta)
    print(H)
    error = H - y
    print(error)
    return np.sum(error ** 2) / (2 * m)

print(compute_cost(X_train,y,theta))
    
