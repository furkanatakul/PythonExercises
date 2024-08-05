import cv2 as cv
import numpy as np


cam = cv.VideoCapture(0)

def nothing(x):
    pass

cv.namedWindow("frame")
cv.createTrackbar("H1", "frame", 0, 359, nothing)
cv.createTrackbar("H2", "frame", 0, 359, nothing)
cv.createTrackbar("S1", "frame", 0, 255, nothing)
cv.createTrackbar("S2", "frame", 0, 255, nothing)
cv.createTrackbar("V1", "frame", 0, 255, nothing)
cv.createTrackbar("V2", "frame", 0, 255, nothing)

while cam.isOpened():
    _ , frame = cam.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    h1 = int(cv.getTrackbarPos("H1","frame") / 2)
    h2 = int(cv.getTrackbarPos("H2", "frame") / 2)
    s1 = cv.getTrackbarPos("S1", "frame")
    s2 = cv.getTrackbarPos("S2", "frame")
    v1 = cv.getTrackbarPos("V1", "frame")
    v2 = cv.getTrackbarPos("V2", "frame")


    lower = np.array([h1, s1, v1])
    upper = np.array([h2, s2, v2])

    mask = cv.inRange(hsv, lower, upper)

    res = cv.bitwise_and(frame, frame, mask= mask)

    cv.namedWindow("frame", cv.WINDOW_NORMAL)
    cv.namedWindow("frame2", cv.WINDOW_NORMAL)
    cv.namedWindow("frame3", cv.WINDOW_NORMAL)
    cv.imshow("frame", frame)
    cv.imshow("frame2", mask)
    cv.imshow("frame3", res)

    if cv.waitKey(1) & 0xFF == 27:
        break


cam.release()
cv.destroyAllWindows()






