import glob
import os
import matplotlib.pyplot as plt
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from PIL import Image
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")
imgs = glob.glob("./img/*.png")

width = 125
height = 50

X = []
Y = []

for img in imgs:
    filename = os.path.basename(img)
    label = filename.split("_")[0]
    im = np.array(Image.open(img).convert("L").resize((width,height)))
    im = im / 255
    X.append(im)
    Y.append(label)

X = np.array(X)
X = X.reshape(X.shape[0], width, height, 1)

def oneHatLabels(values):
    labelEncoder = LabelEncoder()
    intEncoded = labelEncoder.fit_transform(values)
    oneHotEncoder = OneHotEncoder(sparse_output=False)
    oneHotEncoded = oneHotEncoder.fit_transform(intEncoded.reshape(-1,1))
    return oneHotEncoded

Y = oneHatLabels(Y)

trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.25, random_state=2)

#Model İnşası:

model = Sequential([
    Conv2D(filters=32, kernel_size=(3, 3), activation="relu", input_shape=(width, height, 1),
           kernel_regularizer=tf.keras.regularizers.l2(0.02)),
    Conv2D(filters=64, kernel_size=(3, 3), activation="relu",
           kernel_regularizer=tf.keras.regularizers.l2(0.02)),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.25),
    Flatten(),
    Dense(128, activation="relu", kernel_regularizer=tf.keras.regularizers.l2(0.02)),
    Dropout(0.4),
    Dense(3, activation="softmax")  # softmax  yerine
])
model.compile(
    loss=tf.keras.losses.CategoricalCrossentropy(from_logits=False),
    optimizer=tf.keras.optimizers.Adam(0.001),
    metrics=["accuracy"]
)
model.fit(
    trainX, trainY, epochs=30, batch_size = 64
)
#     probabilities = tf.nn.softmax(r)
scoreTrain = model.evaluate(trainX, trainY)
print("Accuracy Train: %", scoreTrain[1]*100)

scoreTest = model.evaluate(testX, testY)
print("Accuracy Test: %", scoreTest[1]*100)

with open("model_new.json", "w") as json_file:
    json_file.write(model.to_json())
model.save_weights("trex_weight_new.weights.h5")