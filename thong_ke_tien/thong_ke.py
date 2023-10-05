#TODO: Thu vien
import pyinputplus as pin 


#TODO: Chuong trinh

def Nhan_thong_tin():
    muc_luong = pin.inputInt('Nhập mức lương: ')
    ca_sang = pin.inputInt('Tổng số ca sáng trong tuần: ')
    ca_toi = pin.inputInt('Tổng số ca tối trong tuần: ')
    ca_chu_nhat = pin.inputInt('Tổng số ca chủ nhật trong tuần: ')
    return muc_luong, ca_sang, ca_toi, ca_chu_nhat

#TODO: Cac chuc nang cua chuong trinh
def Tinh_luong_du_dinh(muc_luong, ca_sang, ca_toi, ca_chu_nhat):
    luong_du_dinh = muc_luong * ca_sang * 4 + (muc_luong+40)*ca_toi*4 + (muc_luong+60) * ca_chu_nhat*4 
    return luong_du_dinh

def main():
    muc_luong, ca_sang, ca_toi, ca_chu_nhat = Nhan_thong_tin()
    luong_du_dinh = Tinh_luong_du_dinh(muc_luong, ca_sang, ca_toi, ca_chu_nhat)
    print(f"Múc lương dự định của tháng này là: {luong_du_dinh} ngàn đồng.")


#TODO: In ra man hinh
if __name__ == '__main__':
    main()

