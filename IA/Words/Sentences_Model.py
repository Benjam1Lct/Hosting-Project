import os
import cv2
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, LSTM, Bidirectional, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

# Chemin vers le dossier contenant les images de la base de données IAM
data_dir = '\iam_data'

# Chargement du fichier de métadonnées contenant les transcriptions
metadata_file = os.path.join(data_dir, 'ascii', 'lines.txt')
metadata = pd.read_csv(metadata_file, sep=' ', header=None, names=['filename', 'index', 'text'], usecols=[0, 1, 8])

# Création d'un dictionnaire pour mapper les caractères à des entiers
charset = set(' '.join(str(text) for text in metadata['text'].tolist()))
char_to_idx = {c: i + 1 for i, c in enumerate(charset)}
idx_to_char = {i + 1: c for i, c in enumerate(charset)}

# Chargement des images et prétraitement
images = []
labels = []
for i, row in metadata.iterrows():
    # Chemin vers l'image
    img_path = os.path.join(data_dir, 'lines', row['filename'] + '.png')

    # Lecture de l'image en niveaux de gris
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Normalisation de l'image
    img = img / 255.

    # Redimensionnement de l'image
    img = cv2.resize(img, (128, 32))

    # Ajout de l'image et de la transcription à la liste
    images.append(img)
    labels.append([char_to_idx[c] for c in row['text']])

# Conversion des listes en tableaux numpy
images = np.array(images)
labels = np.array(labels)

# Création d'un modèle de reconnaissance de phrases basé sur un réseau de neurones récurrents (LSTM)
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=images.shape[1:]))
model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 1)))
model.add(Flatten())
model.add(Dropout(0.2))
model.add(Bidirectional(LSTM(256, return_sequences=True)))
model.add(Dropout(0.2))
model.add(Bidirectional(LSTM(256, return_sequences=True)))
model.add(Dense(len(charset) + 1, activation='softmax'))

# Compilation du modèle
model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(1e-4), metrics=['accuracy'])

# Entraînement du modèle
model.fit(images, labels,
          batch_size=32,
          epochs=20,
          validation_split=0.2,
          callbacks=[EarlyStopping(patience=5, restore_best_weights=True)])

# Sauvegarde du modèle
model.save('./model.h5')
