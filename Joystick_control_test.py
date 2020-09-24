from vjoy import vJoy, ultimate_release
import numpy as np
import time
from getKeys import key_check

"""
    Run this code to check the connection between the virtual controller and the game.
    The vehicle should keep making circles in counter clock direction when the connection is successful
    ** Note that you need to press P to break the connection rather than terminating the code, as this could result in 
    crashing the vjoy driver  
"""

vj = vJoy()

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

while True:
    vj.open()
    btn = 1
    joystickPosition = vj.generateJoystickPosition(wAxisX=12000, wAxisZ=32000, wAxisZRot=0)
    vj.update(joystickPosition)
    print("running")
    time.sleep(0.1)
    vj.sendButtons(0)

    keys = key_check()
    if 'P' in keys:
        joystickPosition = vj.generateJoystickPosition(wAxisX=16000, wAxisY=16000)
        vj.update(joystickPosition)
        vj.sendButtons(0)
        vj.close()
        break


