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
file = 'training_data.npy'

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
    print("{}".format(k))
    time.sleep(1)
pause = False

#  Joystick Controller setup
pygame.init()
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
print(joystick_count)
controller = pygame.joystick.Joystick(1)
controller.init()
name = controller.get_name()
print("Controller Name: ", name)

while True:
    if not pause:
        screen = grab_screen(region=(0, 35, 800, 630))
        # screen = cv2.cvtColor(screen, cv2.COLOR_BGR2HLS)
        # new_img = screen/255 - 0.1
        new_img = cv2.resize(new_img, (400, 300))
        cv2.imshow('screen', new_img)

        curr_time = time.time()
        FPS = 1/(curr_time - prev_time)
        # print("FPS:", FPS)
        prev_time = time.time()
        pygame.event.pump()
        steering_angle = controller.get_axis(0) * 100

        # key = key_check()
        # if key:
        #     if key[0] == "A":
        #         steer = -10
        #     else:
        #         steer = 10
        # else:
        #     steer = 0

        plt.show()
        training_data.append([new_img, steering_angle])
        # if len(training_data) % 1000 == 0:

        if cv2.waitKey(25) & 0xFF == ord('q'):
            print(len(training_data))
            np.save(file, training_data)
            cv2.destroyAllWindows()
            break

    keys = key_check()
    if 'T' in keys:
        if pause:
            pause = False
            print('unpaused!')
            time.sleep(1)
        else:
            print('Pausing!')
            pause = True
            time.sleep(1)


