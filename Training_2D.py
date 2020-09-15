import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Lambda, Cropping2D, MaxPooling2D, Conv2D, Activation, Dropout
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import tensorflow as tf
from sklearn.utils import shuffle

import cv2

train_data = np.load('tf_data.npy', allow_pickle=True)

images = []
controls = []
i = 0
print(len(train_data))
for data in train_data:
    i = i+1
    source_image = data[0]
    new_image = cv2.resize(source_image, (100, 100))
    new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2HLS)
    new_image = cv2.GaussianBlur(new_image, (3, 3), 0)
    new_image = new_image/255 - 0.1
    control = data[1]

    if control[1] <= -0.5 or control[1] == 0:
        if control[1] == 0.5:
            pass
        elif i % 2 == 0:
            images.append(new_image)
            controls.append(control)
        else:
            pass
    elif control[1] > 0.2:
        images.append(new_image)
        flip_image = np.fliplr(new_image)
        images.append(flip_image)
        controls.append(control)
        flip_control = [-control[0], control[1]]
        controls.append(flip_control)


X_train = np.array(images)
y_train = np.array(controls)

X_train, y_train = shuffle(X_train, y_train)

print("the image is being trained on {} samples".format(len(X_train)))
epochs = 10
batch_size = 64

vgg_model = VGG16(weights='imagenet', include_top=False, input_shape=(100, 100, 3))
for layer in vgg_model.layers:
    layer.trainable = False

data_input = Input(shape=(100, 100, 3))
vgg = vgg_model(data_input)
drop_1 = Dropout(0.2)(vgg)
flat_1 = Flatten()(drop_1)
dense = Dense(512, activation='relu')(flat_1)
drop_2 = Dropout(0.4)(dense)
dense_2 = Dense(256, activation='relu')(drop_2)
drop_3 = Dropout(0.4)(dense_2)
dense_3 = Dense(64, activation='relu')(drop_3)
drop_4 = Dropout(0.4)(dense_3)
prediction = Dense(2, activation='linear')(drop_4)

model = Model(inputs=data_input, outputs=prediction)

model.compile(optimizer='Adam', loss='mse')
print('training...')
model.fit(X_train, y_train, validation_split=0.2, shuffle=True, epochs=epochs, verbose=2, batch_size=batch_size)

print()
print('training complete')

model.save('tf_model2.h5')
print()
print('model saved')
