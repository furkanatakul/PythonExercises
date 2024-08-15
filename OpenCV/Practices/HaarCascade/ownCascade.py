import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

path = "images"

imgWidth = 180
imgHeight = 120

cam= cv.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
cam.set(10,180) # kameranın aydınlık seviyesi

global countFolder
def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists(path + str(countFolder)):
        countFolder += 1
    os.makedirs(path + str(countFolder))

saveDataFunc()

count = 0
countSave = 0

while True:
    ret, img = cam.read()

    if ret:
        img = cv.resize(img, (imgWidth, imgHeight))

        if count % 5 == 0:
            cv.imwrite(path+str(countFolder)+"/"+str(countSave)+".png", img)
            countSave +=1
            print(countSave)
        count += 1

        cv.imshow("Image", img)
    key = cv.waitKey(1) & 0xFF

    if key == ord("q"): break

cam.release()
cv.destroyAllWindows()