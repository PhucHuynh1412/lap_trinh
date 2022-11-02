import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb 
import pandas as pd 
import math
import pyinputplus as pin 


def giai_phuong_trinh_bac_2():
    a = pin.inputFloat("Nhập hệ số a: ")
    b = pin.inputFloat("Nhập hệ số b: ")
    c = pin.inputFloat("Nhập hệ số c: ")
    
    if a == 0:
        if b == 0:
            print("Phương trình vô nghiệm.")
        else:
            print("Phương trình có nghiệm: x = {-c/b}")
    elif a != 0:
        delta = b**2 - 4*a*c
        if delta < 0:
            print("Phương trình vô nghiệm.")
        elif delta == 0:
            print(f"Phương trình có nghiệm kép: x = {-b/(2*a)}")
        elif delta > 0:
            x1 = (-b - math.sqrt(delta))/(2*a)
            x2 = (-b + math.sqrt(delta))/(2*a)
            print("Phương trình có 2 nghiệm:")
            print(f"  x1 = {x1}")
            print(f"  x2 = {x2}")

def tim_so_lon_nhat():
    nhap = input("Nhập n số cần tìm số lớn nhất: ")
    data = nhap.split(' ')
    data_num = []
    for num in data:
        data_num.append(float(num))
    print(f"Số lớn nhất trong dãy số là: {max(data_num)}")
    
