import numpy as np 
import math 
import pyinputplus as pin 

#TODO: cac hang so

def tinh_toc_do_song():
    lamda = pin.inputFloat('Nhap buoc song (m): ')
    T = pin.inputFloat('Nhap chu ki song: ')
    f = 1/T
    v = lamda/T
    data = [v,T,f,lamda]
    return data 

def tinh_do_lech_pha(data):
    d = pin.inputFloat('Khoang cach 2 diem tren phuong truyen song (m): ')
    lamda = data[3]
    denta_phi = 2*math.pi*d/lamda
    return denta_phi

def main():
    data = tinh_toc_do_song()
    

if __name__ == "__main__":
    main()

    

