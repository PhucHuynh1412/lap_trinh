import numpy as np 

dataA = [float(num) for num in input('Nhập hệ số a,b,c: ').split(",")]
dataB = [float(num) for num in input('Nhập hệ số d,e,f: ').split(",")]

A = np.array([dataA[:2],dataB[:2]])
B = np.array([dataA[-1],dataB[-1]])

X = np.linalg.solve(A,B)

print(X)
