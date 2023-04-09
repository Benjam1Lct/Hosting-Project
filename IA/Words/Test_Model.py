import os
import cv2
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, LSTM, Bidirectional, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

# Chargement du modèle sauvegardé
model = load_model('model.h5')


# Fonction pour prédire la transcription d'une image
def predict_image(image_path):
    # Lecture de l'image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Normalisation de l'image
    img = img / 255.

    # Redimensionnement de l'image
    img = cv2.resize(img, (128, 32))

    # Prédiction de la transcription
    pred = model.predict(np.array([img]))

    # Conversion des prédictions en texte
    text = ''
    for p in pred[0]:
        if idx_to_char[np.argmax(p)] != ' ':
            text += idx_to_char[np.argmax(p)]

    return text