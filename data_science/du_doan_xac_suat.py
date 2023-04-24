import random

#TODO: create data base
with open('so_so.txt','r') as f:
    line = f.readline().split(' ')

for i , num in enumerate(line):
    line[i] = int(num)

print(line)

data_1 = [int(num/100) for num in line]

data_2 = [int((num%100)/10) for num in line]

data_3 = [int(num%10) for num in line]

def xac_suat(data):
    # Tính toán xác suất xuất hiện của từng số trong dãy số
    probability_distribution = [1/len(data) for _ in range(len(data))]

    # Dự đoán số tiếp theo dựa trên xác suất xuất hiện của từng số
    next_number = random.choices(data, weights=probability_distribution)[0]

    return next_number

so_dau = xac_suat(data_1)
so_giua = xac_suat(data_2)
so_cuoi = xac_suat(data_3)

print("="*30)
print(so_dau,so_giua,so_cuoi)
