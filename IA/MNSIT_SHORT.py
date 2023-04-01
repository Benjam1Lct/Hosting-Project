import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=60)

model.summary()

model.evaluate(x_test, y_test)

model.save("./nn.h5")
model.save("./neural_net")

"""new_model = tf.keras.models.load_model("nn.h5")"""

model.save("./nn_weights.h5")

"""model.load_weights("nn_weights.h5")

json_string = model.to_json()
with open("nn_model.json", "w") as f:
    f.write(json_string)

with open("nn_model.json", "r") as f:
    loaded_json_string = f.read()

new_model = tf.keras.models.model_from_json(loaded_json_string)
new_model.summary()
new_model.evaluate(x_test, y_test, verbose=2)"""
