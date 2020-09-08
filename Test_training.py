import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from getKeys import key_check
import cv2
from grabscreen import grab_screen
from DNN_model import vgg_16
from directkeys import PressKey, ReleaseKey, W, A, D
from vjoy import vJoy, test, ultimate_release
import time
from getKeys import key_check

gain = 20
vj = vJoy()
# JOYSTICK INPUT
x_range = 16393
z_range = 32786

wAxisX = 16393
wAxisY = 16393
wAxisZ = 0
wAxisXRot = 16393
wAxisYRot = 16393
wAxisZRot = 0

keys = key_check()
ultimate_release()

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


model = load_model("3pv_model.h5")
print("code starts in..")
time.sleep(0.5)
for i in range(0, 4):
    k = 3 - i
    print("{}".format(k))
    time.sleep(1)
while True:
    if not pause:
        vj.open()
        btn = 1
        screen = grab_screen(region=(0, 280, 800, 430))
        screen = cv2.resize(screen, (200, 66))
        # cv2.imshow('screen', screen)
        # screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2YUV)
        screen = (screen / 255 - 0.2)

        # steering_angle = float(model.predict(screen[None, :, :, :], batch_size=1))
        # steering_correction = int(steering_angle * 16000) * gain
        # print(steering_correction)

        joystickPosition = vj.generateJoystickPosition(wAxisX=16000, wAxisZ=22000)
        vj.update(joystickPosition)
        time.sleep(0.01)
        vj.sendButtons(0)

        curr_time = time.time()
        FPS = 1/(curr_time - prev_time)
        print("FPS:", FPS)
        prev_time = time.time()

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

    keys = key_check()
    if 'T' in keys:
        # if pause:
        #     pause = False
        #     print('Unpaused!')
        #     time.sleep(1)
        # else:
        #     print('Pausing!')
        #     pause = True
        #     time.sleep(1)
        joystickPosition = vj.generateJoystickPosition(wAxisX=16000, wAxisY=16000)
        vj.update(joystickPosition)
        vj.sendButtons(0)
        # ultimate_release()
        vj.close()
        break



