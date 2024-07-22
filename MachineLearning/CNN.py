import os
import numpy as np
import pandas as pd
from tensorflow.keras import Sequential, Input
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix

# TensorFlow log seviyesini ayarlama
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Modelin ilklemesi
classifier = Sequential([
    Input(shape=(64, 64, 3)),
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(units=128, activation='relu'),
    Dense(units=1, activation='sigmoid')
])

# CNN
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# CNN ve resimler
train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('Datasets/veriler/training_set',
                                                 target_size=(64, 64),
                                                 batch_size=32,
                                                 class_mode='binary')

test_set = test_datagen.flow_from_directory('Datasets/veriler/test_set',
                                            target_size=(64, 64),
                                            batch_size=32,
                                            class_mode='binary')

classifier.fit(training_set,
               steps_per_epoch=training_set.samples // training_set.batch_size,
               epochs=1,
               validation_data=test_set,
               validation_steps=test_set.samples // test_set.batch_size)

# Tahminler
test_set.reset()
pred = classifier.predict(test_set, verbose=1)
pred = (pred > 0.5).astype(int)

# Test etiketlerini toplama
test_labels = []
for i in range(len(test_set)):
    test_labels.extend(np.array(test_set[i][1]))

# Dosya isimlerini toplama
dosyaisimleri = test_set.filenames

# Sonuçların DataFrame olarak tutulması
sonuc = pd.DataFrame()
sonuc['dosyaisimleri'] = dosyaisimleri
sonuc['tahminler'] = pred.flatten()
sonuc['test'] = test_labels[:len(pred)]  # Test etiketlerini tahminlerle aynı uzunlukta olacak şekilde kesme

# Confusion Matrix
cm = confusion_matrix(test_labels[:len(pred)], pred)
print(cm)