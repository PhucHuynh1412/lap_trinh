import random
import numpy as np 

#TODO: create data base
with open('so_so.txt','r') as f:
    line = f.readline().split(' ')

for i , num in enumerate(line):
    line[i] = int(num)

#TODO: danh sach cac so
data = line 
print(data)
data_1 = [int(num/100) for num in line]
data_2 = [int((num%100)/10) for num in line]
data_3 = [int(num%10) for num in line]

#TODO: ham xu ly
def xac_suat(data):
    # Tính toán xác suất xuất hiện của từng số trong dãy số
    probability_distribution = [1/len(data) for _ in range(len(data))]

    # Dự đoán số tiếp theo dựa trên xác suất xuất hiện của từng số
    next_number = random.choices(data, weights=probability_distribution)[0]

    return next_number

def so_trung(data):
    count_dict = {}
    for num in data:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1 
    print('số trùng nhau và sô lần trùng')
    for num, count in count_dict.items():
        if count > 1:
            print(f"{num}: {count} times.")
def in_ki_so_so_va_day_so(data):
    dt = {}
    ki = 248
    count = len(data)
    hang = int(count/20)
    np_arr = np.array(data).reshape(hang,20)
    #print(np_arr)
    for i in range(hang):
        dt[ki] = np_arr[i]
        ki += 1
    print(dt)


#TODO: in ra man hinh so du đoán
so_dau = xac_suat(data_1)
so_giua = xac_suat(data_2)
so_cuoi = xac_suat(data_3)

print("="*30)
print(so_dau,so_giua,so_cuoi)

print("*"*20)
so_trung(data)

in_ki_so_so_va_day_so(data)

