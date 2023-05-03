import random

data = []

#TODO: lấy dữ liệu
with open('so_so.txt','r') as f:
    line = f.readline().split(' ')

for num in line:
    data.append(int(num))

print(data)

data_1 = [int(num/10) for num in data]
data_2 = [int(num%10) for num in data]

def xac_suat(data):
    # Tính toán xác suất xuất hiện của từng số trong dãy số
    probability_distribution = [1/len(data) for _ in range(len(data))]

    # Dự đoán số tiếp theo dựa trên xác suất xuất hiện của từng số
    next_number = random.choices(data, weights=probability_distribution)[0]

    return next_number

so_dau = xac_suat(data_1)
so_cuoi = xac_suat(data_2)

print(so_dau,so_cuoi)



