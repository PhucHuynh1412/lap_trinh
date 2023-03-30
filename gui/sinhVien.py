class SinhVien:
    'Cơ sở dữ liệu chung của sinh viên'
    svCount = 0

    def __init__(self, ten, HocPhi):
        self.ten = ten
        self.HocPhi = HocPhi
        SinhVien.svCount += 1

    def displayCount(self):
        print(f'Tổng số sinh viên đã đóng học phí: {SinhVien.svCount}')
    
    def displaySinhVien(self):
        print(f'Tên sinh viên: {self.ten}, học phí: {self.HocPhi}')

sv1 = SinhVien('Phúc',4000)
sv2 = SinhVien('Hiếu', 5000)

sv1.displaySinhVien()
sv2.displaySinhVien()

SinhVien.displayCount



