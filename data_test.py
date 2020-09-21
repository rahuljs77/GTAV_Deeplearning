import numpy as np
import matplotlib.pyplot as plt
import cv2
from sklearn.utils import shuffle

allow_pickle = True
train_data = np.load('data/data.npy', allow_pickle=True)
print(len(train_data))
images = []
# while True:
for i in range(0, 200):
    data = train_data[i]
    source_image = data[0]
    new_image = source_image
    width = new_image.shape[0]
    height = new_image.shape[1]
    new_image = cv2.resize(new_image, (width*5, height*5))
    new_image = cv2.GaussianBlur(new_image, (3, 3), 0)
    new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2YUV)
    new_image = new_image/255 - 0.1
    images.append(new_image)


X_train = np.array(images, dtype="float")
X1_train = np.array(images)
plt.imshow(X_train[50])
plt.show()
print(X_train[10])
print(X1_train[10])

    # control = data[1]
    # print(control)
    # cv2.imshow("image", new_image)
    # if cv2.waitKey(25) & 0xFF == ord('q'):
    #     cv2.destroyAllWindows()
    #     break

#
# x = [1, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 8, 8, 8]
# y = len(x)
# indices = list(range(y))
# np.random.shuffle(indices)
# print(indices)
# print(np.floor(9.7))


