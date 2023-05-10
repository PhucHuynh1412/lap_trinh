from hmmlearn import hmm
import numpy as np 

#TODO: lấy dữ liệu
data = []
with open('so_so.txt','r') as f:
    line = f.readline().split(' ')

for num in line:
    data.append(int(num))
data = np.array(data)
print(data)

# Chuyển đổi dữ liệu sang dạng số nguyên và tạo ma trận quan sát
obs = data.reshape(-1, 1)
obs_seq = np.hstack([obs[:-1], obs[1:]])

# Tạo và đào tạo mô hình HMM
n_states = 5  # số trạng thái ẩn
model = hmm.MultinomialHMM(n_components=n_states, n_iter=1000, verbose=True)
model.fit(obs_seq)

# Dự đoán giá trị tiếp theo
last_obs = np.array([data[-2], data[-1]]).reshape(1, -1)
predicted_obs = model.predict_proba(last_obs)[0].argmax()
predicted_value = predicted_obs + 10  # chuyển đổi về giá trị thực tế
print(predicted_value)
