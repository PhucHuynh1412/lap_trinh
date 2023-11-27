import numpy as np
import pyinputplus as pin 

data = np.arange(2000,3201)
for num in data:
    if num % 7 == 0 and num % 5 != 0:
        print(num, end=', ')

print('-'*30)
print(data)

