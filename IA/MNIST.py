# Enregistrez le code dans le fichier « keras-test.py » dans le dossier « keras-test »
from __future__ import print_function
# Télécharger Keras 
import keras
# Télécharger les dossiers de formation et de test MNIST
from keras.datasets import mnist
# Télécharger le modèle séquentiel 
from keras.models import Sequential
# Télécharger les couches des cellules neuronales 
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
# Nombre de caractéristiques de données différentes : chiffres 0-9
num_classes = 10
# Nombre de laissez-passer pour la formation du réseau de neurones
epochs = 12
# Nombre de données utilisées lors d’un passage
batch_size = 128
# Dimensions des images d’entrée (28 x 28 pixels par image)
img_rows, img_cols = 28, 28
# Télécharger les formations et les tests 
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
if K.image_data_format() == 'channels_first':
    train_images = train_images.reshape(train_images.shape[0], 1, img_rows, img_cols)
    test_images = test_images.reshape(test_images.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    train_images = train_images.reshape(train_images.shape[0], img_rows, img_cols, 1)
    test_images = test_images.reshape(test_images.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)
# Définir le type de données en nombre décimal 
train_images = train_images.astype('float32')
test_images = test_images.astype('float32')
# Normaliser les données des images
# c'est à dire normalisation des valeurs. Puisque l'idéal pour l'IA est de travailler sur 
# des valeurs comprises entre 0 et 1, ainsi on divise par 255 (la valeur maximale pouvant être prise).
train_images /= 255
test_images /= 255
print('train_images shape:', train_images.shape)
print(train_images.shape[0], 'train samples')
print(test_images.shape[0], 'test samples')
# Convertir les vecteurs de classe en matrices de classe binaires
train_labels = keras.utils.to_categorical(train_labels, num_classes)
test_labels = keras.utils.to_categorical(test_labels, num_classes)
# Créer un modèle
model = Sequential()
# Ajouter des couches au modèle
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))
# Compiler le modèle
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])
# Former le modèle
model.fit(train_images, train_labels,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(test_images, test_labels))
# Évaluer le modèle
score = model.evaluate(test_images, test_labels, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])