import matplotlib.pyplot as plt 
import numpy as np 

# Khởi tạo các giá trị ban đầu
y0 = 0  # Vị trí ban đầu (m)
v0 = 0  # Vận tốc ban đầu (m/s)
g = 9.81  # Gia tốc trọng trường (m/s^2)
t_max = 5  # Thời gian tối đa (s)
num_steps = 1000  # Số lượng bước tính toán

# Tính toán các giá trị mới cho vị trí và vận tốc sau mỗi bước thời gian
t = np.linspace(0, t_max, num_steps)
y = np.zeros_like(t)
v = np.zeros_like(t)
y[0] = y0
v[0] = v0
dt = t[1] - t[0]

for i in range(1, num_steps):
    y[i] = y[i-1] + v[i-1] * dt
    v[i] = v[i-1] - g * dt

# Vẽ đồ thị biểu diễn vị trí của quả bóng theo thời gian
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Free Fall Motion')
plt.show()

