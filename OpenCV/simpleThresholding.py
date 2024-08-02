import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


resim = cv.imread("Images/whiteToBlack.jpg", 0)

_, resimThresh1 = cv.threshold(resim, 182, 255, cv.THRESH_BINARY)
_, resimThresh2 = cv.threshold(resim, 182, 255, cv.THRESH_BINARY_INV)
_, resimThresh3 = cv.threshold(resim, 182, 255, cv.THRESH_TRUNC)
_, resimThresh4 = cv.threshold(resim, 182, 255, cv.THRESH_TOZERO)
_, resimThresh5 = cv.threshold(resim, 182, 255, cv.THRESH_TOZERO_INV)

resimler = [resim ,resimThresh1,resimThresh2,resimThresh3,resimThresh4,resimThresh5]
basliklar = ["ORIGINAL", "THRESH_BINARY", "THRESH_BINARY_INV", "THRESH_TRUNC",
             "THRESH_TOZERO", "THRESH_TOZERO_INV"]
p = 0
fig, axes = plt.subplots(2, 3, figsize=(10, 8))
for i in range(2):
    for j in range(3):
        axes[i,j].imshow(resimler[p], "gray")
        axes[i, j].set_title(basliklar[p])
        p += 1
#plt.show()

def nothing(x):
    pass
cv.namedWindow("resim")
cv.createTrackbar("esik", "resim", 0, 255, nothing)


while 1 :
    thresh = cv.getTrackbarPos("esik", "resim")

    _, thresholdImage = cv.threshold(resim, thresh, 255, cv.THRESH_BINARY)

    cv.imshow("resim", thresholdImage)
    if cv.waitKey(1) & 0xFF == 27:
        break


cv.waitKey()
cv.destroyAllWindows()



















