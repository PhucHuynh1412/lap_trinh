import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Khởi tạo vòng tròn
circle = plt.Circle((0, 0), 0.2, color='r')

# Thêm vòng tròn vào trục
ax.add_artist(circle)

# Hàm cập nhật hình ảnh
def update(frame):
    # Tính toán vị trí mới cho vòng tròn
    x = frame * 0.1
    y = 0

    # Cập nhật vị trí của vòng tròn
    circle.center = (x, y)

    return circle,

# Tạo hình ảnh động
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

# Hiển thị hình ảnh
plt.show()

