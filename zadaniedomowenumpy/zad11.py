import numpy as np

x = np.arange(12).reshape(1,12)
print(x)
print(x.shape)

y = x.reshape((3,4))
b = y.ravel()
print(b)
print(b.shape)

z = x.reshape((4,3))
c = z.ravel()
print(c)
print(c.shape)

a = x.reshape((2,6))
d = a.ravel()
print(d)
print(d.shape)