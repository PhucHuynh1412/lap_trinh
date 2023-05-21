import numpy as np 
import pyinputplus as pin 

print('Phương trình 2 ẩn có dạng: ')
print('    a1x + b1y = c1')
print('    a2x + b2y = c2')

print("="*10)
a1 = pin.inputFloat('Nhập giá trị a1: ')
b1 = pin.inputFloat('Nhập giá trị b1: ')
c1 = pin.inputFloat('Nhập giá trị c1: ')

print("="*10)
a2 = pin.inputFloat('Nhập giá trị a2: ')
b2 = pin.inputFloat('Nhập giá trị b2: ')
c2 = pin.inputFloat('Nhập giá trị c2: ')

print("="*10)
A = np.array([[a1,b1],[a2,b2]])
B = np.array([c1,c2])

X = np.linalg.solve(A,B)


print(f'x = {X[0]}')


