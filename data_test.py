import numpy as np
import matplotlib.pyplot as plt


allow_pickle = True
train_data = np.load('3pv_data.npy', allow_pickle=True)
images = []
steer = []
for data in train_data:
    images.append(data[0])
    steer.append(data[1])
    flip_image = np.fliplr(data[0])
    images.append(flip_image)
    steer.append(-data[1])

X_train = np.array(images)
plt.imshow(X_train[0])
plt.show()
print(len(X_train))
y_train = np.array(steer)
print(y_train)
