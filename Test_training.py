import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from getKeys import key_check
import cv2
from grabscreen import grab_screen
from DNN_model import vgg_16
from directkeys import PressKey, ReleaseKey, W, A, D
import time

t_time = 0.05
pause = False
prev_time = time.time()

def left():
    PressKey(W)
    PressKey(A)
    ReleaseKey(D)
    time.sleep(t_time)
    ReleaseKey(A)


def right():
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)
    time.sleep(t_time)
    ReleaseKey(D)


def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)


model = load_model("Test_model.h5")
print("code starts in..")
time.sleep(0.5)
for i in range(0, 4):
    k = 3 - i
    print("{}".format(k))
    time.sleep(1)
while True:
    if not pause:
        screen = grab_screen(region=(0, 35, 800, 630))
        wawdscreen = cv2.cvtColor(screen, cv2.COLOR_BGR2HLS)
        new_img = screen/255 - 0.1
        new_img = cv2.resize(new_img, (400, 300))
        # cv2.imshow('screen', new_img)
        steering_angle = float(model.predict(new_img[None, :, :, :], batch_size=1))
        key_press = 0
        if steering_angle < -0.05:
            key_press = "A"
        elif steering_angle > 0.05:
            key_press = "D"
        else:
            key_press = "W"
        print("==================")
        print(steering_angle)
        # print(key_press)
        if key_press == "A":
            left()
        elif key_press == "D":
            right()
        else:
            straight()
        curr_time = time.time()
        FPS = 1/(curr_time - prev_time)
        # print("FPS:", FPS)
        prev_time = time.time()

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

    keys = key_check()
    if 'T' in keys:
        if pause:
            pause = False
            print('Unpaused!')
            time.sleep(1)
        else:
            print('Pausing!')
            pause = True
            time.sleep(1)



