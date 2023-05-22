import pyinputplus as pin 
import datetime
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

# TODO: Tính tiền gửi quỹ trái phiếu của techcombank  
def CCQ_techcombank():
    hang_tuan = 100 
    return hang_tuan*4 

# TODO: Tính tiền xài trong tháng
def tinh_tien_xai(luong, tien_con):
    tien_ba_me = 2000
    tien_no = 9100
    tien_tiet_kiem = 2000 
    tien_dau_tu = CCQ_techcombank()
    tien_xai = luong - tien_no - tien_ba_me - tien_tiet_kiem - tien_con - tien_dau_tu
    return tien_no, tien_ba_me, tien_tiet_kiem, tien_xai, tien_dau_tu

# TODO: Lưu dữ liệu vào file text
def take_date():
    now = datetime.datetime.now()
    month = now.month
    year = now.year
    return f'{month}-{year}'

def ghi(tien_tk, tien_dt):
    date = take_date()
    with open('data.txt', 'r') as f:
        lines = f.readlines()
        data = lines[len(lines)-1].split(' - ')
    print(data)
    if data[0] in date:
        return 'Đã cập nhật tháng này rồi.'
    tong_tk = int(data[3]) + tien_tk
    tong_dt = int(data[4]) + tien_dt
    text = date + ' - ' + str(tien_tk) + ' - ' + str(tien_dt) + ' - ' + str(tong_tk) + ' - ' + str(tong_dt) + '\n'
    with open('data.txt','a') as f:
        f.write(text)
    return "Cập nhật xong."

#TODO: xuất dữ liệu ra màn hình
def thong_ke():
    data = []
    with open('data.txt', 'r') as f:
        print(f.read())


# TODO: Xuất ra màn hình tiền lương, tiền tiết kiệm và tiền xài
def xuat(tien_luong, tien_xai, tien_tiet_kiem,tien_dau_tu):
    text_1 = f'- Tiền lương tháng này là: {tien_luong}'
    text_2 = f'- Tiền xài tháng này là: {tien_xai}'
    text_3 = f'- Tiền tiết kiệm tháng này là: {tien_tiet_kiem}'
    text_4 = f'- Tiền đầu tư chứng chỉ quỹ trái phiếu của techcombank: {tien_dau_tu}'
    print('*'*80)
    print(f'*  {text_1}' + ' '*(76 - len(text_1)) + '*')
    print(f'*  {text_2}' + ' '*(76 - len(text_2)) + '*')
    print(f'*  {text_3}' + ' '*(76 - len(text_3)) + '*')
    print(f'*  {text_4}' + ' '*(76 - len(text_4)) + '*')
    print('*'*80)

def main():
    muc_luong, so_ca_ngay, so_ca_toi, so_ca_chu_nhat, tien_con = nhap()
    muc_sang, muc_toi, muc_chu_nhat = muc_luong_quy_dinh(muc_luong)
    luong = so_ca_ngay * 4 * muc_sang + so_ca_toi * 4 * muc_toi + so_ca_chu_nhat * 4 * muc_chu_nhat
    tien_no, tien_ba_me, tien_tiet_kiem, tien_xai, tien_dau_tu = tinh_tien_xai(luong,tien_con)
    xuat(luong, tien_xai, tien_tiet_kiem,tien_dau_tu)
    print(ghi(tien_tiet_kiem, tien_dau_tu))
    thong_ke()


if __name__ == "__main__":
    main()
   
