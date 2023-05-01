import pandas as pd 
import numpy as np 

data = pd.Series([1,2,3,4,5,6])
print(data)

data = pd.Series(100)
print(data)

data = pd.Series(100, index=range(3))
print(data)


