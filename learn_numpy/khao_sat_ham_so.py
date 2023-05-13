import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Khai báo biến và hàm số
x = sp.Symbol('x')
f = x**3 - 3*x**2 + 2

# Tính đạo hàm của hàm số
df = sp.diff(f, x)

# Tìm các điểm cực trị của hàm số
critical_points = sp.solve(df, x)
print("Các điểm cực trị của hàm số: ", critical_points)

# Tạo biểu đồ hàm số và đường tiệm cận ngang
a, b = -2, 3
x_vals = np.linspace(a, b, 1000)
y_vals = np.array([f.subs(x, i) for i in x_vals])
hline = np.zeros(len(x_vals))

plt.plot(x_vals, y_vals, label='f(x)')
plt.plot(x_vals, hline, linestyle='--', color='gray')

# Tìm chiều tăng/giảm của hàm số trên các khoảng xác định
increasing_intervals = []
decreasing_intervals = []
for i in range(len(critical_points) + 1):
    if i == 0:
        interval = [a, critical_points[i]] if len(critical_points) > 0 else [a, b]
    elif i == len(critical_points):
        interval = [critical_points[i-1], b]
    else:
        interval = [critical_points[i-1], critical_points[i]]
    interval_df = sp.diff(f, x).subs(x, interval)
    if interval_df > 0:
        increasing_intervals.append(interval)
        plt.fill_between(interval, hline, y_vals[(x_vals>=interval[0]) & (x_vals<=interval[1])], alpha=0.2, color='green')
    elif interval_df < 0:
        decreasing_intervals.append(interval)
        plt.fill_between(interval, hline, y_vals[(x_vals>=interval[0]) & (x_vals<=interval[1])], alpha=0.2, color='red')
    else:
        plt.axvline(interval[0], linestyle='--', color='gray')
plt.title("Biểu đồ hàm số và khảo sát chiều biến thiên")
plt.legend()
plt.show()

print("Các khoảng tăng của hàm số: ", increasing_intervals)
print("Các khoảng giảm của hàm số: ", decreasing_intervals)

