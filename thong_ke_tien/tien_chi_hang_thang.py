import pyinputplus as pin 
import datetime as dtt   

tien_ngan_hang = 9100 
tien_ba_me = 2000
tien_hoc_cho_con = 4500
tien_dien_thoai = 500 
tien_hoc_them = 1400
thang_hien_tai = dtt.datetime.now().month


def tinh_tong_tien_chi():
    tong_chi = tien_ngan_hang + tien_ba_me + tien_ba_me + tien_dien_thoai + tien_hoc_cho_con + tien_hoc_them
    print (f"- Tổng chi của tháng {thang_hien_tai} là: {tong_chi}")
    return tong_chi

if __name__ == "__main__":
    tinh_tong_tien_chi()

