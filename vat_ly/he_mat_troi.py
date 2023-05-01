import pygame
import math

# Kích thước cửa sổ
WIDTH, HEIGHT = 800, 600

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Khởi tạo Pygame
pygame.init()

# Tạo cửa sổ
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Thiết lập tiêu đề
pygame.display.set_caption("Solar System")

# Tạo hình ảnh
sun_img = pygame.image.load("sun.png")
earth_img = pygame.image.load("earth.png")
mars_img = pygame.image.load("mars.png")

# Vị trí và bán kính của các hành tinh và sao
sun_pos = [WIDTH//2, HEIGHT//2]
sun_radius = 50
earth_pos = [sun_pos[0]+200, sun_pos[1]]
earth_radius = 20
mars_pos = [sun_pos[0]+300, sun_pos[1]]
mars_radius = 15

# Góc xoay ban đầu của các hành tinh
earth_angle = 0
mars_angle = 0

# Tốc độ xoay của các hành tinh (đơn vị là radian/giây)
earth_speed = math.radians(2)
mars_speed = math.radians(1)

# Vòng lặp chính
running = True
clock = pygame.time.Clock()
while running:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Xoay hành tinh
    earth_angle += earth_speed
    mars_angle += mars_speed

    # Tính toán vị trí mới của hành tinh
    earth_x = int(sun_pos[0] + math.cos(earth_angle) * 200)
    earth_y = int(sun_pos[1] + math.sin(earth_angle) * 200)
    mars_x = int(sun_pos[0] + math.cos(mars_angle) * 300)
    mars_y = int(sun_pos[1] + math.sin(mars_angle) * 300)

    # Vẽ hình ảnh
    screen.fill(BLACK)
    screen.blit(sun_img, (sun_pos[0]-sun_radius, sun_pos[1]-sun_radius))
    screen.blit(earth_img, (earth_x-earth_radius, earth_y-earth_radius))
    screen.blit(mars_img, (mars_x-mars_radius, mars_y-mars_radius))
    pygame.display.flip()

    # Điều chỉnh tốc độ
    clock.tick(60)

# Kết thúc Pygame
pygame.quit()

