import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import tensorflow as tf
from tensorflow.keras.models import model_from_json
import numpy as np
from PIL import Image
import keyboard
import time
from mss import mss

mon = {"top" : 525, "left" : 685, "width" : 250, "height" : 130}
sct = mss()

width = 125
height = 50

model = model_from_json(open("model_new.json", "r").read())
model.load_weights("trex_weight_new.weights.h5")

labels = ["Down", "Right", "Up"]

framerateTime = time.time()
counter = 0
i = 0
delay = 0.4
keyDownPressed = False

while True:
    img = sct.grab(mon)
    im = Image.frombytes("RGB", img.size, img.rgb)
    im2 = np.array(im.convert("L").resize((width, height)))
    im2 = im2 / 255

    X = np.array([im2])
    X = X.reshape(X.shape[0], width, height, 1)
    r = model.predict(X)
    result = np.argmax(r)

    if result == 0:
        keyboard.press(keyboard.KEY_DOWN)
        keyDownPressed = True
    if result == 2:
        if keyDownPressed:
            keyboard.release(keyboard.KEY_UP)
        time.sleep(delay)
        keyboard.press(keyboard.KEY_UP)

        if i < 1500:
            time.sleep(0.3)
        elif 1500 < i < 5000:
            time.sleep(0.2)
        else:
            time.sleep(0.17)
        keyboard.press(keyboard.KEY_DOWN)
        keyboard.release(keyboard.KEY_DOWN)

    counter += 1
    if time.time() - framerateTime > 1 :
        counter = 0
        framerateTime = time.time()

        if i <= 1500:
            delay -= 0.003
        else:
            delay -= 0.005
        if delay < 0 :
            delay = 0

        print("---------------------")
        print("Down: {} \nRight:{} \nUp: {} \n".format(r[0][0],r[0][1],r[0][2]))
        i += 1