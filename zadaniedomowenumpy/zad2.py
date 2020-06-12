import numpy as np

x = np.array([[5,4,2], [4,1,2], [5,2,1]])
y = np.array([[2,4,5,3], [1,2,5,3], [4,1,3,5], [3,4,2,1]])

print(x.min(axis=1))
print(x.min(axis=0))

print(y.min(axis=1))
print(y.min(axis=0))