from grabscreen import grab_screen
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
import pygame
import pyvjoy
from getKeys import key_check
import pyautogui
import numpy as np
import os
import cv2
import time

prev_time = time.time()

image_data = []
steer_data = []

fpv = False

if fpv:
    file = 'fpv_data.npy'
    if os.path.isfile(file):
        print('File exists, loading previous data!')
        training_data = list(np.load(file, allow_pickle=True))
    else:
        print('File does not exist, starting fresh!')
        training_data = []
else:
    file = '3pv_data.npy'
    if os.path.isfile(file):
        print('File exists, loading previous data!')
        training_data = list(np.load(file, allow_pickle=True))
    else:
        print('File does not exist, starting fresh!')
        training_data = []

print("code starts in..")
time.sleep(0.5)
for i in range(0, 4):
    k = 3 - i
    print(k)
    time.sleep(1)
pause = False

#  Joystick Controller setup
pygame.init()
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
print("{} joysticks detected".format(joystick_count))
controller = pygame.joystick.Joystick(1)
controller.init()
name = controller.get_name()
print("Controller Name: ", name)

while True:
    if not pause:
        screen = grab_screen(region=(0, 280, 800, 430))
        screen = cv2.resize(screen, (100, 100))
        cv2.imshow('screen', screen)
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2HLS)
        screen = screen/255 - 0.2

        curr_time = time.time()
        FPS = 1/(curr_time - prev_time)
        prev_time = time.time()
        pygame.event.pump()
        steering_angle = controller.get_axis(0)
        steering_angle = round(steering_angle, 2)
        print(steering_angle)
        training_data.append([screen, steering_angle])
        # print("FPS:", FPS)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            print(("{} images collected".format(len(training_data))))
            np.save(file, training_data)
            print("File saved!!")
            cv2.destroyAllWindows()
            break

    keys = key_check()
    if 'T' in keys:
        if pause:
            pause = False
            print('Play!')
            time.sleep(1)
        else:
            print('Pause!')
            pause = True
            time.sleep(1)


