from hmmlearn import hmm
import numpy as np

# Tạo dữ liệu ví dụ
X = np.random.randint(low=0, high=10, size=(100, 12))

# Tạo và huấn luyện mô hình HMM với 10 trạng thái ẩn
model = hmm.GaussianHMM(n_components=10)
model.fit(X)

# Dự đoán số tiếp theo trong dãy số
next_number = model.predict(X[-1].reshape(1, -1))[0]
print("Số tiếp theo trong dãy số là:", next_number)

