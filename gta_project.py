from grabscreen import grab_screen
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pyautogui

import cv2
import time

prev_time = time.time()

while True:
    screen = grab_screen(region=(0, 40, 800, 640))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2HLS)
    new_img = screen/255
    cv2.imshow('screen', screen)
    curr_time = time.time()
    FPS = 1/(curr_time - prev_time)
    print("FPS:", FPS)
    prev_time = time.time()
    plt.show()
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

    # current_time = time.time()
    # print("frame took {} seconds".format(current_time - seconds))
    # seconds = time.time()
