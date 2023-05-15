import numpy as np  

x1 = np.random.randint(10, size=(3,4,5))
print(x1)

x2 = np.arange(5)
x3 = np.arange(1,10,2)

x = np.concatenate([x2,x3])
print(x)

xx1 = np.arange(6).reshape(2,3)
xx2 = np.array([[1,2,3],[4,5,6]])

print(xx1)
print(xx2)

xx = np.concatenate([xx1,xx2])
print(xx)

xxx = np.concatenate([xx1,xx2], axis=1)
print(xxx)

