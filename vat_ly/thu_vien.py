#import seaborn as sb 
import pandas as pd 
import math
import pyinputplus as pin 
import gtts 
import pyttsx3 
import os
import sys 
import wikipedia
from time import sleep
import numpy as np 
import scipy
import sklearn as skl 


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

def nang_luong_buc_xa():
    h = 6.625*10**(-34)
    e = 1.6*10**(-19)
    c = 3e8
    print('Đề cho trường hợp nào: ')
    print('1. Đề cho tần số.')
    print('2. Đề cho bước sóng.')
    lua_chon = pin.inputInt('Lựa chọn trường hợp nào: ')

    if lua_chon == 1:
        f = pin.inputFloat('Nhập tần số của bức xạ: ')
        w = h*f/e
        lamda = h*c/f
        print(f'Năng lượng của bức xạ là: {round(w,3)} eV .')
        print(f'Bước sóng của bức xạ là: {round(lamda,3)} um.')
    if lua_chon == 2:
        lamda = pin.inputFloat('Nhập bước sóng của bức xạ: ')
        f = c/lamda
        w = h*c/lamda
        print(f'Năng lượng của bức xạ là: {round(w,3)} eV .')
        print(f'Bước sóng của bức xạ là: {round(lamda,3)} um.')

def cong_thoat_electron():
    h = 6.625e-34
    c = 3e8
    data = {1: 'Tính công thoát của electron', 2: 'Tính giới hạn quang điện'}
    for k,v in data.items():
        print(f'{k}. {v}.')
    lua_chon = pin.inputInt('Bạn chọn trường hợp nào: ')
    if lua_chon == 1:
        lamda_0 = pin.inputFloat('Nhập giá trị của giới hạn quang điện: ')
        A = h*c/lamda_0
        print(f'Công thoát của electron là: {A} J.')
    elif lua_chon == 2:
        A = pin.inputFloat('Nhập giá trị của công thoát: ')
        lamda_0 = h*c/A
        print('Giới hạn quang điện là: {lamda_0} m.')

def dong_nang_ban_dau_cuc_dai_electron():
    h = 6.625e-34
    c = 3e8
    m = 9.1e-31
    lamda = pin.inputFloat('Nhập bước sóng của bức xạ: ')
    lamda_0 = pin.inputFloat('Nhập giới hạn quang điện: ')
    if lamda > lamda_0:
        print('Không xảy ra hiện tượng quang điện')
    else:
        W = h*c*(1/lamda - 1/lamda_0)
        v = math.sqrt(2*W/m)
        print(f'Động năng ban đầu cực đại của electron là: {W} J.')
        print(f'Vận tốc của electron là: {v} m/s.')

def khoang_van():
    lamda = pin.inputFloat('Nhập bước sóng: ')
    D = pin.inputFloat('Nhập khoảng cách 2 khe đến màn: ')
    a = pin.inputFloat('Nhập khoảng cách 2 khe: ')
    i = lamda*D/a
    print(f'Khoảng vân là: {i} mm')

def tinh_goc_khuc_xa():
    n1 = pin.inputFloat('Nhập chiết suất môi trường tới: ')
    i = pin.inputFloat('Nhập góc tới i (theo độ): ')
    n2 = pin.inputFloat('Nhập chiết suất môi trường khúc xạ: ')
    r = math.acos(n1*math.sin(i*math.pi/180)/n2)*180/math.pi
    print(r)

def so_hat_nhan_con_lai():
    t = pin.inputFloat('Nhập thời gian: ')
    T = pin.inputFloat('Nhập chu kỳ bán rã: ')
    N0 = pin.inputFloat('Nhập số hạt nhân ban đầu: ')
    N = N0*2**(-t/T)
    print(f'Số hạt nhân còn lại sau thời gian {t} là: {N}.')

def luc_dan_hoi():
    k = pin.inputFloat('Nhập độ cứng k: ')
    delta_l = pin.inputFloat('Nhập độ biến dạng: ')
    F = k * delta_l
    print(f'Lực đàn hồi có độ lớn là: {F} N' )

