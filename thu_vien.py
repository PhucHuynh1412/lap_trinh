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

def tinh_quang_duong_bien_doi_deu():
    print("Đề bài có:")
    print("  1. Thời gian.")
    print("  2. Không có thời gian.")
    lua_chon = pin.inputInt("Bạn lựa chọn trường hợp: ")
    if lua_chon == 1:
        v0 = pin.inputFloat('Nhập vận tốc đầu: ')
        a = pin.inputFloat('Nhập gia tốc: ')
        t = pin.inputFloat('Nhập thời gian: ')
        s = v0*t + 0.5*a*t**2
        print(f"Quãng đường vật đi được là: {s}m")
    else:
        v0 = pin.inputFloat('Nhập vận tốc đầu: ')
        a = pin.inputFloat('Nhập gia tốc: ')
        v = pin.inputFloat('Nhập vận tốc sau: ')
        s = (v**2 - v0**2)/(2*a)
        print(f"Quãng đường vật đi được là: {s}m")

def kiem_tra_so_nguyen_to():
    n = pin.inputInt("Nhập số nguyên cần kiểm tra: ")
    count = 0
    for num in range(1,int(n/2)+1):
        if n % num == 0:
            count += 1
    if count > 1:
        print(f"{n} không phải là sô nguyên tố.")
    else:
        print(f"{n} là số nguyên tố.")

def nang_luong_phong_xa():
    f = pin.inputFloat('Nhập giá trị tần số của bức xạ: f = ')
    h = 6.625*10**(-34)
    E = h*f 
    print(f'Năng lượng của bức xạ là: {E} J')


def tinh_electron_du_thieu():
    q = pin.inputFloat('Nhập giá trị điện tích q = ')
    e = 1.6*10**(-19)
    n = q/e
    print(f'Số electron dư thiếu trong vật nhiễm điện: {n} hạt')

def tinh_luc_tinh_dien():
    q1 = pin.inputFloat('Nhập giá trị điện tích q1 = ')
    q2 = pin.inputFloat('Nhập giá trị điện tích q2 = ')
    e = pin.inputFloat('Nhập hằng số điện môi: ')
    r = pin.inputFloat('Nhập khoảng cách giữa 2 điện tích r = ')
    k = 9*10**9
    F = k*q1*q2/(e*r**2)
    print(f'Lực tĩnh điện giữa 2 điện tích là: {F} N')



