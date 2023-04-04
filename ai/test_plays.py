import pygame 
import os
data = []

for name in os.listdir('./Music'):
    data.append(name)

pygame.init()
for name in data:
    pygame.mixer.music.load(f"./Music/{name}")

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass

