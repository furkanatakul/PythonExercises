import cv2 as cv
import numpy as np
from random import randint as rnd

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

kernel = np.ones((5,5), np.uint8)

while cam.isOpened():
    _ , frame = cam.read()
    img = frame.copy()
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
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE ,kernel)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN ,kernel)

    res = cv.bitwise_and(frame, frame, mask=mask)

    # Kenar tespiti yapmaya yarar.
    # cv.RETR_TREE YERİNE cv.RETR_LIST kullanılırsa hiyerarşi ilişkisini kaldırır. çocukları tespit etmez
    # cv.CHAIN_APPROX_SIMPLE yerine cv.CHAIN_APPROX_NONE kullanılırsa gereksiz kenarları da tespit eder
    contours, hierarchy = cv.findContours(mask, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    for i, cnt in enumerate(contours):
        area = cv.contourArea(cnt)
        if area > 50000 or area < 200:
            continue
        x, y, w, h = cv.boundingRect(cnt)
        print(x,y,w,h)
        color = (rnd(0, 256), rnd(0, 256), rnd(0, 256))

        #cv.drawContours(img, contours, i, color, 2, cv.LINE_8, hierarchy, 0)

        try:
            ellipse = cv.fitEllipse(cnt)
            cv.ellipse(img, ellipse, color, -1)
        except cv.error as e :
            print(e)


        cv.putText(img, str((w,h)), (x,y), cv.FONT_HERSHEY_PLAIN, 1, color, 2)

    cv.namedWindow("frame", cv.WINDOW_NORMAL)
    cv.namedWindow("frame2", cv.WINDOW_NORMAL)
    cv.namedWindow("frame3", cv.WINDOW_NORMAL)
    cv.imshow("frame", frame)
    cv.imshow("frame2", mask)
    cv.imshow("frame3", img)

    if cv.waitKey(1) & 0xFF == 27:
        break


cam.release()
cv.destroyAllWindows()
