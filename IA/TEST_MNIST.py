import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Recreate the exact same model, including its weights and the optimizer
new_model = tf.keras.models.load_model('../digits.model/saved_model.pb')

# Show the model architecture
new_model.summary()