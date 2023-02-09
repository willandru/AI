import numpy as np


x= np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]], np.float64)

print(x)
print(type(x))
print(x.shape)
print(x.dtype)
print(x.size)
print(len(x))


# MULTIPLICANDO ARRAYS

a=np.array([1 ,2 , 3])
b=np.array([9.0, 8.0, 7.0])


c=a*b
d=a-b
print("producto:", c)
print(c.dtype)
print("resta:", d)

e=2*a

