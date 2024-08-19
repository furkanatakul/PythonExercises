import cv2 as cv
import numpy as np
import pickle
import random
from tensorflow.keras.preprocessing.image import img_to_array
import tensorflow as tf

image = cv.imread("Images/mnist.png")
cv.imshow("image",image)

ss = cv.ximgproc.segmentation.createSelectiveSearchSegmentation()
ss.setBaseImage(image)
ss.switchToSelectiveSearchQuality()

print("start")
rects = ss.process()

proposals = []
boxes = []
output = image.copy()

for (x,y,w,h) in rects:
    color = [random.randint(0,255) for j in range(3)]
    cv.rectangle(output, (x,y), (x+w,y+h), color, 2, cv.LINE_AA)

    roi = image[y:y+h,x:x+w]
    roi = cv.resize(roi, (32,32), interpolation=cv.INTER_LANCZOS4)
    roi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)

    roi = img_to_array(roi)

    proposals.append(roi)
    boxes.append((x,y,x+w,y+h))

proposals = np.array(proposals, dtype=np.float64)
boxes = np.array(boxes, dtype=np.int32)

print("Siniflandirma")
pickleIn = open("model_trained.p", "rb")
model = pickle.load(pickleIn)
proba = model.predict(proposals)

numberList = []
idx = []

for i in range(len(proba)):
    maxProba = np.max(proba[i])

    if maxProba > 0.95:
        idx.append(i)
        numberList.append(np.argmax(proba[i]))
cv.namedWindow("Image", cv.WINDOW_NORMAL)
for i in range(len(numberList)):

    j = idx[i]
    cv.rectangle(image, (boxes[j,0], boxes[j,1]), (boxes[j,2], boxes[j,3]), (0,0,255), 2, cv.LINE_AA)
    cv.putText(image, str(np.argmax(proba[j])), (boxes[j, 0] + 5, boxes[j, 1] + 5), cv.FONT_HERSHEY_SIMPLEX, 1.5,
               (255, 0, 0), 1)
    cv.imshow("Image", image)




cv.waitKey(0)
cv.destroyAllWindows()