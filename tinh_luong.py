import pyinputplus as pin 
import numpy as np 

# TODO: Nhập cơ sở dữ liệu ban đầu 
def nhap():
    print('Nhập các thông tin cơ bản để tính lương:')
    muc_luong = pin.inputInt('  * Nhập mức lương 1 ca: ')
    so_ca_ngay = pin.inputInt('  * Số ca ngày trong tuần: ')
    so_ca_toi = pin.inputInt('  * Số ca tối trong tuần: ')
    so_ca_chu_nhat = pin.inputInt('  * Số ca chủ nhật: ')
    tien_con = pin.inputFloat("Nhập tiền đóng học phí cho con: ")
    return muc_luong, so_ca_ngay, so_ca_toi, so_ca_chu_nhat, tien_con


# TODO: Mức lương quy định 
def muc_luong_quy_dinh(muc_luong):
    muc_sang = muc_luong
    muc_toi = muc_luong + 40
    muc_chu_nhat = muc_luong + 60
    return muc_sang, muc_toi, muc_chu_nhat

# TODO: Tính tiền gửi finhay hoặc tikop
def tikop():
    pass

# TODO: Tính tiền xài trong tháng
def tinh_tien_xai(luong, tien_con):
    tien_ba_me = 2000
    tien_no = 9100
    tien_tiet_kiem = (luong - tien_no)*0.15
    tien_xai = luong - tien_no - tien_ba_me - tien_tiet_kiem - tien_con 
    return tien_no, tien_ba_me, tien_tiet_kiem, tien_xai

# TODO: Lưu dữ liệu vào file text
def ghi(data):
    pass

# TODO: Xuất ra màn hình tiền lương, tiền tiết kiệm và tiền xài
def xuat(tien_luong, tien_xai, tien_tiet_kiem):
    text_1 = f'- Tiền lương tháng này là: {tien_luong}'
    text_2 = f'- Tiền xài tháng này là: {tien_xai}'
    text_3 = f'- Tiền tiết kiệm tháng này là: {tien_tiet_kiem}'
    print('*'*50)
    print(f'*  {text_1}' + ' '*(46 - len(text_1)) + '*')
    print(f'*  {text_2}' + ' '*(46 - len(text_2)) + '*')
    print(f'*  {text_3}' + ' '*(46 - len(text_3)) + '*')
    print('*'*50)

def main():
    muc_luong, so_ca_ngay, so_ca_toi, so_ca_chu_nhat, tien_con = nhap()
    muc_sang, muc_toi, muc_chu_nhat = muc_luong_quy_dinh(muc_luong)
    luong = so_ca_ngay * 4 * muc_sang + so_ca_toi * 4 * muc_toi + so_ca_chu_nhat * 4 * muc_chu_nhat
    tien_no, tien_ba_me, tien_tiet_kiem, tien_xai = tinh_tien_xai(luong,tien_con)
    xuat(luong, tien_xai, tien_tiet_kiem)

if __name__ == "__main__":
    main()
   
