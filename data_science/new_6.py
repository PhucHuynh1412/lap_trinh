import numpy as np
from hmmlearn import hmm

data = []
with open('so_so_6.txt','r') as f:
    for line in f.readlines():
        data.append(int(line))
print(data)
data = np.array(data)

# Khởi tạo mô hình HMM với 12 trạng thái ẩn
model = hmm.GaussianHMM(n_components=12)

# Đọc dữ liệu đầu vào từ file
data = np.loadtxt('so_so_6.txt')

# Huấn luyện mô hình trên dữ liệu đầu vào
model.fit(data)

# Dự đoán số tiếp theo trong dãy số
next_number = model.sample(1)[0][0][-1]

print('Số tiếp theo trong dãy số:', int(next_number))
