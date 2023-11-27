import numpy as np
import pyinputplus as pin 
import math as m 

n = pin.inputInt('Nhập vào số tự nhiên cần tính giai thừa: ')
giai_thua_n = m.factorial(n)
print(f"Giai thừa của số tự nhiên {n} là: {giai_thua_n}")

