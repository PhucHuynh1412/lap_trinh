import numpy as np
from hmmlearn import hmm

data = []
#TODO: lấy dữ liệu
with open('so_so_55.txt','r') as f:
    line = f.readline().split(' ')
for num in line:
    data.append(int(num))
data = np.array([[num] for num in data])

# Dữ liệu đầu vào
X = data

# Khởi tạo mô hình HMM với 6 trạng thái ẩn và sử dụng thuật toán Baum-Welch
model = hmm.GaussianHMM(n_components=6, covariance_type="diag", n_iter=100)
model.fit(X)

# Dự đoán 6 số liên tiếp tiếp theo trong dãy số
next_numbers = model.sample(n_samples=6)[0].astype(int)

print(next_numbers)

