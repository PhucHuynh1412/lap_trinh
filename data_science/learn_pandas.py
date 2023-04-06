import pandas as pd 
import numpy as np

#TODO: lay du lieu data dang dung tab 
df = pd.read_csv('data.tsv', sep = '\t')

#TODO: xuat xem thanh cong chua 
print(df.head(5))

#TODO: xem kich thuoc hang cot, thong tin data 
print(df.shape)
print(df.info())


