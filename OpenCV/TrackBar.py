import cv2 as cv
import numpy as np

img = np.zeros([512,512,3], np.uint8)
cv.namedWindow("resim")

def nothing(x):
    pass


cv.createTrackbar("Track","resim", 0, 255, nothing)
cv.createTrackbar("Track1","resim", 0, 255, nothing)
cv.createTrackbar("Track2","resim", 0, 255, nothing)

cv.createTrackbar("ON/OFF", "resim", 0,1,nothing)



while 1:
    cv.imshow("resim", img)

    if cv.waitKey(1) & 0xFF == 27:
        break

    r = cv.getTrackbarPos("Track", "resim")
    g = cv.getTrackbarPos("Track1", "resim")
    b = cv.getTrackbarPos("Track2", "resim")

    switch = cv.getTrackbarPos("ON/OFF", "resim")

    if switch:
        img[:] = [b,g,r]
    else:
        img[:]= 0
cv.destroyAllWindows()












