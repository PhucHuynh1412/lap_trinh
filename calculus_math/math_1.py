import sympy as sp 

x , y = sp.symbols('x y')

print(sp.sin(x))

print(sp.exp(x))

print(sp.log(x, 10))

print(x**(3/2))

print(x**(sp.Rational(3,2)))

result = sp.limit(sp.sin(x/2 + sp.sin(x)), x , sp.pi)
print(result)

result = sp.limit(2*sp.exp(1/x) / (sp.exp(1/x) + 1), x , 0, dir='+')
print(result)

result = sp.limit(2*sp.exp(1/x) / (sp.exp(1/x) + 1), x , 0, dir='-')
print(result)

result = sp.limit((sp.cos(x) - 1) / x , x , sp.oo)
print(result)

result = sp.diff(((y + sp.sin(x)) / (1 - sp.cos(x)))**2,x)
print(result)

