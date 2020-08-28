import pyvjoy
import time
import math
import pygame

pygame.init()
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
print(joystick_count)
controller = pygame.joystick.Joystick(1)
controller.init()

name = controller.get_name()
print(name)
num_axis = controller.get_numaxes()
print(num_axis)
while True:
    pygame.event.pump()
    output = controller.get_axis(0) * 100
    print(int(output))
