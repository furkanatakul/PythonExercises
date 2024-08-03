import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

resim = cv.imread("Images/kus.jpg")

kernel = np.ones((5,5), np.float32) / 25

# Softening

dst = cv.filter2D(resim, -1, kernel)
dst2 = cv.blur(resim, (10,10))
dst3 = cv.GaussianBlur(resim, (11,11), 0)
dst4 = cv.medianBlur(resim, 11)

# Sharpening

filter = np.array([
    [-1,-1,-1],
    [-1,9,-1],
    [-1,-1,-1]
])

filterMexicanHat = np.array([
    [0,0,-1,0,0],
    [0,-1,-2,-1,0],
    [-1,-2,16,-2,-1],
    [0,-1,-2,-1,0],
    [0,0,-1,0,0]
])

filterRandom = np.array([
    [2,5,-9,2],
    [-9,-6,-6,-9],
    [9,6,6,9],
    [2,5,-9,2]
])

filterSepia = np.array([
    [0.272,0.534,0.131],
    [0.349,0.686,0.168],
    [0.393,0.769,0.189]
])

filter2 = np.array([
    [0,1,0],
    [0,0,0],
    [0,-1,0]
])

dst5 = cv.filter2D(resim, -1, filter)
dst6 = cv.filter2D(resim, -1, filterMexicanHat)
dst7 = cv.filter2D(resim, -1, filterRandom)
dst8 = cv.transform(resim, filterSepia)
dst9 = cv.filter2D(resim, -1, filter2)


cv.imshow("resim",resim)
cv.imshow("img",dst8)

cv.waitKey()
cv.destroyAllWindows()