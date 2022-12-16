import pyinputplus as pin 
import numpy as np 

# TODO: Nhập cơ sở dữ liệu ban đầu 
muc_luong = pin.inputInt("Nhập mức lương 1 ca: ")
so_ca_sang_trong_tuan = pin.inputInt("Số ca sáng trong tuần (không tính chủ nhật): ")
so_ca_toi_trong_tuan = pin.inputInt("SỐ ca tối trong tuần (không tính chủ nhật): ")
so_ca_chu_nhat_trong_tuan = pin.inputInt("Số ca chủ nhật trong tuần: ")

# TODO: Mức lương quy định 
muc_sang = muc_luong
muc_toi = muc_luong + 40
muc_chu_nhat = muc_luong + 60

# TODO: Tính lương 
luong = so_ca_sang_trong_tuan * 4 * muc_sang + so_ca_toi_trong_tuan * 4 * muc_toi + so_ca_chu_nhat_trong_tuan * 4 * muc_chu_nhat
print(f"Tiền lương tháng này: {luong} đồng.")

# TODO: Tính tiền tiết kiệm
tien_no = 9100
tien_tiet_kiem = (luong - tien_no)*0.15
print(f"Tiền tiết kiệm tháng này là: {tien_tiet_kiem}")

# TODO: Tính tiền xài trong tháng
tien_ba_me = 1500
tien_con = pin.inputFloat("Nhập tiền đóng học phí cho con: ")
tien_xai = luong - tien_no - tien_ba_me - tien_tiet_kiem - tien_con 
print(f"Tiền xài tháng này là: {tien_xai}")


