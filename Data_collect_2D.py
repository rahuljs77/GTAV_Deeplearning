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

prev_time = time.time()

file = 'tf_data.npy'
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
        screen = grab_screen(region=(1170, 290, 1870, 430))
        screen = cv2.resize(screen, (400, 400))
        cv2.imshow('screen', screen)
        screen = cv2.resize(screen, (100, 100))
        curr_time = time.time()
        FPS = 1 / (curr_time - prev_time)
        prev_time = time.time()
        pygame.event.pump()
        steering_angle = controller.get_axis(0)
        throttle = controller.get_axis(2)
        throttle = round(throttle, 2)
        if throttle < -0.5:
            throttle = -0.49
        steering_angle = round(steering_angle, 2)
        print('steering_angle = {}, throttle = {}'.format(steering_angle, throttle))
        control = [steering_angle, throttle]
        train_data.append([screen, control])
        # print("FPS:", FPS)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            print(("{} images collected".format(len(train_data))))
            np.save(file, train_data)
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
