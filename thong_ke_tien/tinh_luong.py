import pyinputplus as pin 

#TODO: Nhập dữ liệu
bac_luong = 120
muc_1 = 120
muc_2 = 140
muc_3 = 160 

so_ca_sang = 9
so_ca_toi = 15
so_ca_thu_7_cn = 15 

#TODO: tính lương tạm 1 tháng
def tinh_luong():
    luong_tam = (so_ca_sang*muc_1 + so_ca_toi*muc_2 + so_ca_thu_7_cn*muc_3)*4
    return luong_tam

if __name__ == "__main__":
    print(f"Lương tạm tính tháng này là: {tinh_luong()} ngàn đồng")

