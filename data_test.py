import numpy as np
import matplotlib.pyplot as plt
import cv2
from sklearn.utils import shuffle


allow_pickle = True
train_data = np.load('3pv_data.npy', allow_pickle=True)
images = []
steer = []
# while True:
for data in train_data:
    source_image = data[0]
    new_image = source_image
    new_image = cv2.resize(new_image, (400, 132))
    new_image = cv2.GaussianBlur(new_image, (3, 3), 0)
    new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2HLS)
    new_image = new_image/255 - 0.1
    steering_angle = data[1]
    if -0.1 < steering_angle < 0.1:
        steering_angle = 0
    steer.append(steering_angle)
    cv2.imshow("image", new_image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

# X_train = np.array(images)
# print(len(X_train))
# y_train = np.array(steer)
# print(y_train)
#
# X_train, y_train = shuffle(X_train, y_train)



