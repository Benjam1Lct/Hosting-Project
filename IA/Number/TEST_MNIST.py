import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

if __name__ == '__main__':
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = tf.keras.utils.normalize(x_train, axis=1)
    x_test = tf.keras.utils.normalize(x_test, axis=1)

    new_model = tf.keras.models.load_model("nn.h5")

    for x in range(1,6):
        filename = f'{x}.png'
        if os.path.isfile(filename):
            img = cv.imread(filename)[:,:,0]
            img = np.invert(np.array([img]))
            prediction = new_model.predict(img)
            print(f'Le resultat est probablement {np.argmax(prediction)}')
            plt.imshow(img[0], cmap=plt.cm.binary)
            plt.show()
        else:
            print(f"File {filename} not found.")
