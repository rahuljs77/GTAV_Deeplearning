from vjoy import vJoy, test, ultimate_release
import numpy as np
import time
from getKeys import key_check
from grabscreen import grab_screen
from tensorflow.keras.models import load_model
import cv2
gain = 15
vj = vJoy()


x_range = 16393
z_range = 32786

wAxisX = 16393
wAxisY = 16393
wAxisZ = 0
wAxisXRot = 16393
wAxisYRot = 16393
wAxisZRot = 0

throttle = 0
turn = 0.9
keys = key_check()
ultimate_release()
xPos = 0
yPos = 16000
model = load_model("3pv_model.h5")
while True:
    vj.open()
    btn = 1
    screen = grab_screen(region=(0, 280, 800, 430))
    screen = cv2.resize(screen, (100, 100))
    # cv2.imshow('screen', screen)
    # screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2HLS)
    screen = (screen / 255 - 0.2)
    steering_angle = float(model.predict(screen[None, :, :, :], batch_size=1))
    steering_correction = int(steering_angle * 16000) * gain

    joystickPosition = vj.generateJoystickPosition(wAxisX=16000 + steering_correction, wAxisZ=16000)
    vj.update(joystickPosition)
    print("running")
    time.sleep(0.1)
    vj.sendButtons(0)

    keys = key_check()
    if 'T' in keys:
        joystickPosition = vj.generateJoystickPosition(wAxisX=16000, wAxisY=16000)
        vj.update(joystickPosition)
        vj.sendButtons(0)
        # ultimate_release()
        vj.close()
        break




