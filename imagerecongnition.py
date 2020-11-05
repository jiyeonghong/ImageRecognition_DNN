# -*- coding: utf-8 -*-
"""ImageRecongnition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12WF5RJQgikfsdPhtfb7dR5XXQdqz2v0F
"""

from keras.datasets import cifar10
import matplotlib.pyplot as plt

cifar10_class_names = {
    0: "Plane",
    1: "Car",
    2: "Bird",
    3: "Cat",
    4: "Deer",
    5: "Dog",
    6: "Frog",
    7: "Horse",
    8: "Boat",
    9: "Truck"
}

# Load the entire data set
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Loop thorugh each pictures in the data set 
for i in range(1000):
    # Grab an image from the data set
    sample_image = x_train[i]
    # Grab the image's expected class id
    image_class_number = y_train[i][0]

    # Look up the class name from the class id
    image_class_name = cifar10_class_names[image_class_number]

    # Draw the image as a plot
    plt.imshow(sample_image)
    # Label the image
    plt.title(image_class_name)
    # Show the plot on the screen
    plt.show()

import keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from pathlib import Path

# Load data Set
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Normalize data set to 0-to-1 range
x_train = x_train.astype("float32")
x_test = x_test.astype("float32")
x_train = x_train / 255
x_test = x_test / 255

# Convert class vectors to binary class matrices
# Out labels are single values from 0 to 9
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

# Create a model and add layers
model = Sequential() # Input_shape은 첫번째 레이어에서 넣어야 함. 

model.add(Conv2D(32, (3, 3), padding="same", activation="relu", input_shape = (32, 32, 3)))
model.add(Conv2D(32, (3, 3), activation = "relu"))

model.add(Conv2D(64, (3, 3), padding = "same", activation = "relu"))
model.add(Conv2D(64, (3, 3), activation = "relu"))

model.add(Flatten())

model.add(Dense(512, activation = "relu"))
model.add(Dense(10, activation = "softmax"))

# Print a summary of the model
model.summary()