import pyinputplus as pin 

def nhap_du_lieu():
    muc_luong = pin.inputInt('Nhập mức lương: ')
    so_ca_sang = pin.inputInt('Nhập số ca sáng: ')
    so_ca_toi = pin.inputInt('Nhập số ca tối: ')
    so_ca_cn = pin.inputInt('Số ca chủ nhật: ')
    return muc_luong,so_ca_sang,so_ca_toi,so_ca_cn

def tinh_luong_thang(muc_luong, so_ca_sang, so_ca_toi, so_ca_cn):
    luong_thang = muc_luong*so_ca_sang + (muc_luong+40)*so_ca_toi + (muc_luong+60)*so_ca_cn 
    return luong_thang
    
def main():
    muc_luong,so_ca_sang,so_ca_toi,so_ca_cn = nhap_du_lieu()
    print(tinh_luong_thang(muc_luong,so_ca_sang,so_ca_toi,so_ca_cn))

if __name__ == "__main__":
    main()

