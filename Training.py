
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Lambda, Cropping2D, MaxPooling2D, Conv2D, Activation, Dropout
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import tensorflow as tf
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from math import ceil
from random import shuffle
import matplotlib.pyplot as plt
import cv2
fpv = False
allow_pickle = True
if fpv:
    train_data = np.load('fpv_data.npy', allow_pickle=True)
else:
    train_data = np.load('3pv_data.npy', allow_pickle=True)
images = []
steer = []
for data in train_data:
    source_image = data[0]
    # print(source_image.shape)
    new_image = source_image
    images.append(new_image)
    # flip_image = np.fliplr(new_image)
    # images.append(flip_image)
    steering_angle = data[1]
    steer.append(steering_angle)
    # steer.append(-steering_angle)

X_train = np.array(images)
print(len(X_train))
y_train = np.array(steer)

# X_train, y_train = shuffle(X_train, y_train)

epochs = 5
batch_size = 250
# input_size = 64
activation_relu = 'relu'

vgg_model = VGG16(weights='imagenet', include_top=False, input_shape=(100, 100, 3))
for layer in vgg_model.layers:
    layer.trainable = False

data_input = Input(shape=(100, 100, 3))
# resize_input = Lambda(lambda image: tf.image.resize(image, (66, 200)))(data_input)
vgg = vgg_model(data_input)
drop_1 = Dropout(0.2)(vgg)
flat_1 = Flatten()(drop_1)
dense = Dense(512, activation='relu')(flat_1)
drop_2 = Dropout(0.2)(dense)
dense_2 = Dense(256, activation='relu')(drop_2)
drop_3 = Dropout(0.2)(dense_2)
dense_3 = Dense(64, activation='relu')(drop_3)
drop_4 = Dropout(0.2)(dense_3)
prediction = Dense(1)(drop_4)

model = Model(inputs=data_input, outputs=prediction)
adam = Adam(lr=0.0001)
model.compile(optimizer='Adam', loss='mse')
print('training...')
model.fit(X_train, y_train, validation_split=0.2, shuffle=True, epochs=epochs, verbose=2, batch_size=batch_size)

print()
print('training complete')

model.save('3pv_model2.h5')
print()
print('model saved')


