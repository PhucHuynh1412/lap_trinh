import sympy as sp 
import pyinputplus as pin 

A = pin.inputFloat('Nhập giá trị biên độ: ')
w = pin.inputFloat('Nhập giá trị của tần số góc: ')
phi = pin.inputFloat('Nhập giá trị pha ban đầu: ')

x = A*sp.cos(w*t + phi)
