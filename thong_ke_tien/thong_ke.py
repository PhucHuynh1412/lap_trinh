#TODO: Thu vien
import pyinputplus as pin 

#TODO: Chuong trinh
def Nhan_thong_tin():
    muc_luong = pin.inputInt('Nhập mức lương: ')
    ca_sang = pin.inputInt('Tổng số ca sáng trong tuần: ')
    ca_toi = pin.inputInt('Tổng số ca tối trong tuần: ')
    ca_chu_nhat = pin.inputInt('Tổng số ca chủ nhật trong tuần: ')
    return muc_luong, ca_sang, ca_toi, ca_chu_nhat

def Tien_chi_hang_thang():
    tien_ngan_hang = 9100
    tien_phu_huynh = 2000
    tien_hoc_cho_con = 4500
    tien_hoc_them = 1400
    tien_tieu_xai = 2000
    tien_dien_thoai = 500
    tong_chi = tien_ngan_hang + tien_dien_thoai + tien_hoc_cho_con + tien_hoc_them + tien_phu_huynh + tien_tieu_xai
    return tong_chi

#TODO: Cac chuc nang cua chuong trinh
def Tinh_luong_du_dinh(muc_luong, ca_sang, ca_toi, ca_chu_nhat):
    luong_du_dinh = muc_luong * ca_sang * 4 + (muc_luong+40)*ca_toi*4 + (muc_luong+60) * ca_chu_nhat*4 
    return luong_du_dinh

def main():
    muc_luong, ca_sang, ca_toi, ca_chu_nhat = Nhan_thong_tin()
    luong_du_dinh = Tinh_luong_du_dinh(muc_luong, ca_sang, ca_toi, ca_chu_nhat)
    tien_song = Tien_chi_hang_thang()
    print(f"Múc lương dự định của tháng này là: {luong_du_dinh} ngàn đồng.")
    print(f"Tiền chi hàng tháng là: {tien_song} ngàn đồng.")


#TODO: In ra man hinh
if __name__ == '__main__':
    main()

