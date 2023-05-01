import matplotlib.pyplot as plt 
import numpy as np 

class Pendulum:
    def __init__(self,length, mass, initial_angle, initial_angular_velocity):
        self.length = length
        self.mass = mass 
        self.initial_angle = initial_angle
        self.initial_angular_velocity = initial_angular_velocity
    def angular_acceleration(self):
        gravity = 9.8
        return (-gravity/self.length) * np.sin(self.angle)
    def update(self, time_step):
        angular_acceleration = self.angular_acceleration()
        self.angular_velocity += angular_acceleration * time_step
        self.angle += self.angular_velocity * time_step

pendulum = Pendulum(length=1, mass=1, initial_angle=np.pi/4, initial_angular_velocity=0)

time_step = 0.01
num_steps = int(10 / time_step)

angles = np.zeros(num_steps)
times = np.zeros(num_steps)

for i in range(num_steps):
    angles[i] = pendulum.angle
    times[i] = i * time_step
    pendulum.update(time_step)

plt.plot(times, angles)
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.title('Simple Pendulum Motion')
plt.show()

