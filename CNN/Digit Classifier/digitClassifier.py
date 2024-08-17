import os
import matplotlib.pyplot as plt
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import numpy as np
import cv2 as cv
from tensorflow.keras import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, BatchNormalization
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sns
import pickle

path = "myData"

myList = os.listdir(path)
noofClasses = len(myList)
print("Label Sayısı :", noofClasses)

images = list()
classNo = list()

for i in range(noofClasses):
    myImageList = os.listdir(path + "\\" + str(i))

    for j in myImageList:
        img = cv.imread(path + "\\" + str(i) + "\\" + j)
        img = cv.resize(img, (32,32))
        images.append(img)
        classNo.append(i)

print(len(images))

images = np.array(images)
classNo = np.array(classNo)

# Veri Ayırma

xtrain, xtest, ytrain, ytest = train_test_split(images, classNo, test_size=0.5, random_state=42)
xtrain, xcv, ytrain, ycv = train_test_split(xtrain, ytrain, test_size=0.5, random_state=42)


def preProcess(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.equalizeHist(img)
    img = img /255

    return img

xtrain = np.array(list(map(preProcess, xtrain)))
xtest = np.array(list(map(preProcess, xtest)))
xcv = np.array(list(map(preProcess, xcv)))

xtrain = xtrain.reshape(-1, 32, 32, 1)
xtest = xtest.reshape(-1, 32, 32, 1)
xcv = xcv.reshape(-1, 32, 32, 1)

dataGenerate = ImageDataGenerator(width_shift_range= 0.1,
                                  height_shift_range= 0.1,
                                  zoom_range= 0.1,
                                  rotation_range= 10)
dataGenerate.fit(xtrain)

ytrain = to_categorical(ytrain, noofClasses)
ytest = to_categorical(ytest, noofClasses)
ycv = to_categorical(ycv, noofClasses)

model = Sequential([
    Conv2D(filters=16, kernel_size=(3,3), activation="relu", padding="same"), # (32,32,1),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.2),
    Flatten(),
    Dense(units=256, activation="relu"),
    Dropout(0.2),
    Dense(units=noofClasses, activation="softmax")
])
model.compile(
    loss="categorical_crossentropy",
    optimizer="Adam",
    metrics = ["accuracy"]
)
hist = model.fit(
    dataGenerate.flow(xtrain, ytrain, batch_size=250), validation_data=(xcv,ycv), epochs=15,
                      steps_per_epoch=xtrain.shape[0] // 250, shuffle = 1
)

pickleOut = open("model_trained.p", "wb")
pickle.dump(model, pickleOut)
pickleOut.close()

#Değerlendirme

plt.figure()
plt.plot(hist.history["loss"], label="Egitim Kaybı")
plt.plot(hist.history["val_loss"], label="Validation Kaybı")
plt.legend()

plt.figure()
plt.plot(hist.history["accuracy"], label="Egitim Accuracy")
plt.plot(hist.history["val_accuracy"], label="Validation Accuracy")
plt.legend()

score = model.evaluate(xtest, ytest, verbose = 0)
print("Test Loss: ", score[0])
print("Test Accuracy: ", score[1])


yPred = model.predict(xcv)
yPredClass = np.argmax(yPred, axis=1)
yTrue = np.argmax(ycv, axis=1)

cm = confusion_matrix(yTrue, yPredClass)

f, ax = plt.subplots(figsize=(8,8))
sns.heatmap(cm, annot=True, linewidths=0.01, cmap="Greens", linecolor="gray", fmt=".1f", ax=ax)
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix")

plt.legend()
plt.show()