import numpy as np 
import math
import pyinputplus as pin
import scipy as sp 
import sklearn as skl 


#TODO: Cac hang so
pi = math.sqrt(10)
g = pi**2

def tinh_tan_so_goc():
    k,l = 0,0
    data = {1: 'Con lac don.',
            2: 'Con lac lo xo.'}
    for k,v in data.items():
        print(f'{k}. {v}')
    option = pin.inputInt('Truong hop nao: ')
    if option == 1:
        l = pin.inputFloat("Nhap chieu dai con lac don: ")
        w = math.sqrt(g/l)
    if option == 2:
        k = pin.inputFloat("Nhap do cung lo xo: ")
        m = pin.inputFloat("Khoi luong cua vat: ")
        w = math.sqrt(k/m)
    data = [w,k,l]
    return data

def tinh_chu_ki(w):
    T = (2*pi)/w
    return T

def tinh_co_nang(data):
    if data[1] != 0:
        A = pin.inputFloat('Nhap bien do cua dao dong: ')
        W_con_lac_lo_xo = 0.5*data[1]*A**2
        return W_con_lac_lo_xo
    if data[2] != 0:
        anpha = pin.inputFloat('Nhap bien do goc vao: ')
        m = pin.inputFloat('Nhap khoi luong cua vat: ')
        W_con_lac_don = m * g * data[2] * (1 - math.cos(anpha*math.pi/180))
        return W_con_lac_don 


def main():
    data = tinh_tan_so_goc()
    T = tinh_chu_ki(data[0])
    W = tinh_co_nang(data)
    
    print('='*15)
    print(f'tan so goc la: {data[0]} rad/s.')
    print(f"Chu ki cua con lac la: {T} s.")
    print(f"Nang luong cua dao dong la: {W} J")


if __name__ == "__main__":
    main()

