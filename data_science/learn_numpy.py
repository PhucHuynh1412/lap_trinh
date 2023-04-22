import numpy as np 

mt = np.arange(10)
print(mt)

a1 = mt.reshape(2,5)
print(a1)

a2 = np.array(range(20)).reshape(4,5)
print(a2)

a3 = a2.T
print(a3)

a = a2 * a3
print(a)

