import sympy as sp 
from sympy import *

init_printing(use_unicode=True)   # in ra kieu unicode hay latex
x, y , a , w , phi, t = symbols('x y a w phi t')           # dat ki hieu cho x va y 

f = exp(x) * sin(x) + exp(x) * cos(x)
print(f)

f1 = integrate(f,x)
print(f1)

f = x + 2 * y
print(f)

f1 = x * f
print(f1)

f2 = expand(x * f)          # nhan phan phoi vao
print(f2)
f3 = factor(f2)         # rut nhan tu chung
print(f3) 

f = exp(x) * sin(x) + exp(x) * cos(x)
f1 = integrate(f,x)
print(f1)

f = sin(x**2)
f1 = integrate (f, (x,-oo,oo))
print(f1)

f = sin(x)/x
f1 = limit(f,x,0)   # lim x --> 0 
print(f1)

f = x**2 - 2
rs = solve(f,x)
print(rs)
