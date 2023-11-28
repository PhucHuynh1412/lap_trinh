#TODO: Khai bao thu vien su dung
import matplotlib.pyplot as plt 
import numpy as np 
import pyinputplus as pin 

#TODO: Thong tin phuong trinh chuyen dong
def thong_tin():
    x0 = pin.inputFloat("Nhập tọa độ ban đầu: ")
    v = pin.inputFloat("Nhập vận tốc của vật: ")
    return x0, v 

def ve_do_thi(x0, v):
    t = np.arange(100)
    x = x0 + v * t 
    plt.plot(t,x)
    plt.show()

def main():
    x0, v = thong_tin()
    ve_do_thi(x0,v)

if __name__ == "__main__":
    main()

