from vjoy import vJoy, test, ultimate_release
import numpy as np
import time
from getKeys import key_check
from grabscreen import grab_screen
from tensorflow.keras.models import load_model
import cv2

"""
    The following code takes in the current screenshot of the game and feeds it to the trained neural network
    The neural network returns the predicted steering and throttle value. The steering and throttle values are 
    passed to the game via a virtual controller
"""

prev_time = time.time()
s_gain = 1.8
t_gain = 2

vj = vJoy()
pause = False
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

model = load_model("models/tf_model1.h5")

print("Autonomous mode in T minus-")
time.sleep(0.5)
for i in range(0, 3):
    k = 3 - i
    print(k)
    time.sleep(1)

while True:
    if not pause:
        vj.open()
        btn = 1
        screen = grab_screen(region=(1170, 290, 1870, 430))
        screen = cv2.resize(screen, (100, 100))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2HLS)  # Converting image HLS for better detection of lanes
        screen = cv2.GaussianBlur(screen, (3, 3), 0)  # Blurring the image to remove noise
        screen = screen/255 - 0.1  # Normalizing the image

        curr_time = time.time()
        FPS = 1 / (curr_time - prev_time)
        FPS = round(FPS, 2)
        prev_time = time.time()

        control = (model.predict(screen[None, :, :, :], batch_size=1))  # Predicted steering and throttle value

        print("Steering angle: {}   Throttle: {}   FPS: {}".format(control[0][0], control[0][1], FPS))

        # Converting the steering and throttle values to corresponding joystick axis values

        steering_angle = control[0][0]
        steering_correction = (steering_angle * 16000)
        steering_correction = int(steering_correction * s_gain)

        throttle = control[0][1]
        if throttle < 0:
            throttle = throttle * 2
        else:
            pass

        if throttle > 0.1:
            forward = int(throttle*32000*1.5)
            backward = 0

        elif 0 < throttle <= 0.1:
            forward = 0
            backward = int(throttle*32000*t_gain)
        else:
            forward = 0
            backward = 32000  # Full reverse throttle for instant braking at high speeds

        joystickPosition = vj.generateJoystickPosition(wAxisX=16000 + steering_correction,
                                                       wAxisZ=forward, wAxisZRot=backward)  # Joystick axis values
        vj.update(joystickPosition)

        time.sleep(0.1)
        vj.sendButtons(0)

    keys = key_check()
    if 'P' in keys:
        joystickPosition = vj.generateJoystickPosition(wAxisX=16000, wAxisY=16000)
        vj.update(joystickPosition)
        vj.sendButtons(0)
        if pause:
            pause = False
            print('Play!')
        else:
            print('Pause!')
            pause = True


