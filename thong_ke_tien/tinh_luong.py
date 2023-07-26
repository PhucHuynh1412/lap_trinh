import pyinputplus as pin 
import datetime as dtt 

muc_luong = 120
so_ca_sang = 33
so_ca_toi = 18
so_ca_chu_nhat = 3
thang_hien_tai = dtt.datetime.now().month

def tinh_tong_so_ca_trong_thang():
    tong_ca_sang = 4 * so_ca_sang 
    tong_ca_toi = 4 * so_ca_toi
    tong_ca_cn = 4 * so_ca_chu_nhat

    tong_ca_trong_thang = tong_ca_sang + tong_ca_toi + tong_ca_cn
    luong = tong_ca_sang * muc_luong + tong_ca_toi * (muc_luong + 40) + tong_ca_cn * (muc_luong + 60)

    print(f"=====* Thông tin ca day trong tháng {thang_hien_tai} *=====")
    print(f"   - Tổng ca tháng {thang_hien_tai} là {tong_ca_trong_thang}, trong đó: ")
    print(f"        - Tổng số ca sáng trong tháng {thang_hien_tai} là: {tong_ca_sang}")
    print(f"        - Tổng số ca tối trong tháng {thang_hien_tai} là: {tong_ca_toi}")
    print(f"        - Tổng số ca chủ nhật trong tháng {thang_hien_tai} là: {tong_ca_cn}")
    print(f"   ==> Lương dự định của tháng {thang_hien_tai} là: {luong}")
    

def main():
    tinh_tong_so_ca_trong_thang()

if __name__ == "__main__":
    main()
