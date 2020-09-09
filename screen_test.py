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

print("code starts in..")
time.sleep(0.5)
for i in range(0, 4):
    k = 3 - i
    print("{}".format(k))
    time.sleep(1)
pause = False
while True:
    if not pause:
        screen = grab_screen(region=(0, 280, 800, 430))
        screen = cv2.resize(screen, (200, 66))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2YUV)
        screen = screen / 255 - 0.2
        cv2.imshow('screen', screen)
        screen = cv2.resize(screen, (100, 100))

        print(screen.shape)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
