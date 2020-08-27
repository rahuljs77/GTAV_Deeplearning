
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Lambda, Cropping2D, MaxPooling2D, Conv2D, Activation, Dropout
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import tensorflow as tf
import sklearn
from sklearn.model_selection import train_test_split
from math import ceil
from random import shuffle
import matplotlib.pyplot as plt
import cv2

allow_pickle = True
train_data = np.load('training_data.npy', allow_pickle=True)
images = []
steer = []
for data in train_data:
    images.append(data[0])
    flip_image = np.fliplr(data[0])
    images.append(flip_image)
    steer.append(data[1])
    steer.append(-data[1])

X_train = np.array(images)
print(len(X_train))
y_train = np.array(steer)

epochs = 10
batch_size = 200
input_size = 64
activation_relu = 'relu'

vgg_model = VGG16(weights='imagenet', include_top=False, input_shape=(66, 200, 3))
for layer in vgg_model.layers:
    layer.trainable = False

data_input = Input(shape=(300, 400, 3))
resize_input = Lambda(lambda image: tf.image.resize(image, (66, 200)))(data_input)
vgg = vgg_model(resize_input)
# vgg = vgg_model(data_input)
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

model.save('Test_model.h5')
print()
print('model saved')


