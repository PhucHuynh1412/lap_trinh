import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb 
import pandas as pd 
import math
import pyinputplus as pin 
import gtts 
import pyttsx3 
import os
import sys 
import wikipedia


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

def ve_do_thi_chuyen_dong_thang_deu():
    x0 = pin.inputFloat("Nhập tọa độ đầu của vật: ")
    t0 = pin.inputFloat("Nhập thời điểm đầu của vật: ")
    v = pin.inputFloat("Nhập tốc độ của vật: ")
    chieu = pin.inputStr("Nhập dấu của vận tốc: ")
    if chieu.strip() == "+":
        print("Vật chuyển động ngược chiều dương.")
        t = pin.inputFloat("Nhập thời điểm sau của vật: ")
        dt = np.arange(t0,t+1)        
        x = x0 + v*(dt-t0)
        plt.plot(dt,x)
        plt.grid()
        plt.show()

def tinh_van_toc_bien_doi_deu():
    print("Đề bài có:")
    print("  1. Thời gian.")
    print("  2. Không có thời gian.")
    lua_chon = pin.inputInt("Bạn lựa chọn trường hợp: ")
    if lua_chon == 1:
        v0 = pin.inputFloat("Nhập vận tốc ban đầu: ")
        a = pin.inputFloat("Nhập gia tốc của vật: ")
        t = pin.inputFloat("Thời điểm t là: ")
        v = v0 + a*t 
        print(f"Vận tốc của vật ở thời điểm {t}s là: {v} m/s")
    if lua_chon == 2:
        s = pin.inputFloat("Nhập quãng đường vật đi: ")
        a = pin.inputFloat("Nhập gia tốc của vật: ")
        v0 = pin.inputFloat("Nhập vận tốc ban đầu: ")
        v = sqrt(2*a*s - v0**2)
        print(f"Vận tốc của vật ở thời điểm {t}s là: {v} m/s")

