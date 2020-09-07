from vjoy import vJoy, test, ultimate_release
import numpy as np
import time
from getKeys import key_check
from grabscreen import grab_screen
from tensorflow.keras.models import load_model
import cv2

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

while True:
    vj.open()
    btn = 1

    joystickPosition = vj.generateJoystickPosition(wAxisX=16000, wAxisZ=16000)
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


