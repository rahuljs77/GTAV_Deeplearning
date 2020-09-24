from grabscreen import grab_screen
import cv2

"""
    > This code test the screen recording 
    > Place the "800 x 600" GTA V game window on the top right corner of your screen
    > Note that the screen should be of the resolution 1920 X 1080
    > Correct recording should return the entire GTA V window with the sky region cropped out
    > In case of incorrect screen recording change the recording region accordingly
"""
print("Press 'q' to quit recording")
while True:
    """
    The recording coordinates are in the form (x1, y1, x2, y2) where x1, y1 represent the top left corner and x2, y2 
    represent the bottom right corner
    """

    screen = grab_screen(region=(1170, 290, 1870, 430))
    screen = cv2.resize(screen, (500, 400))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    cv2.imshow('screen', screen)
    screen = cv2.resize(screen, (100, 100))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
