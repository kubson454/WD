import numpy as np

x = np.arange(81).reshape(9,9)
print(x)
print(x.shape)

y = x.reshape((3,27))
print(y)