from grabscreen import grab_screen
import math
import pygame
import pyvjoy
from getKeys import key_check
import pyautogui
import numpy as np
import os
import cv2
import time

"""
    The following code records the gameplay and the corresponding controller input and stores them into a .npy file
"""
prev_time = time.time()

file = 'data/tf_data.npy'
if os.path.isfile(file):
    train_data = list(np.load(file, allow_pickle=True))
else:
    train_data = []

print("recording starts in..")
time.sleep(0.5)
for i in range(0, 3):
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
        # Screen recording data
        screen = grab_screen(region=(1170, 290, 1870, 430))
        screen = cv2.resize(screen, (400, 400))
        cv2.imshow('screen', screen)
        screen = cv2.resize(screen, (100, 100))

        # FPS
        curr_time = time.time()
        FPS = 1 / (curr_time - prev_time)
        prev_time = time.time()

        # Controller input
        pygame.event.pump()
        steering_angle = controller.get_axis(0)
        throttle = -controller.get_axis(2)
        throttle = round(throttle, 2)
        if throttle > 0.8:
            throttle = 0.8
        steering_angle = round(steering_angle, 2)
        print('steering_angle = {}, throttle = {}'.format(steering_angle, throttle))
        control = [steering_angle, throttle]
        train_data.append([screen, control])

    keys = key_check()
    if 'P' in keys:
        if pause:
            pause = False
            print('Playing')
        else:
            pause = True
            print('Paused!')
            print(("{} images collected".format(len(train_data))))
            np.save(file, train_data)
            print("File saved!!")

