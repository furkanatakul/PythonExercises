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

paint = np.ones((480,640,3), np.uint8) * 255

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
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for i, cnt in enumerate(contours):
        area = cv.contourArea(cnt)
        if area > 50000 or area < 200:
            continue
        x, y, w, h = cv.boundingRect(cnt)
        print(x,y,w,h)
        color = (rnd(0, 256), rnd(0, 256), rnd(0, 256))

        #Kontür için çeşitli momentleri hesaplar. Bu momentler, konturun geometrik özelliklerini anlamak için kullanılır.
        M = cv.moments(cnt)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # Şeklin çevresini çizen - çevreleyen  çizgi çizer
        perimeter = cv.arcLength(cnt, True)
        epsilon = 0.1 * perimeter
        approx = cv.approxPolyDP(cnt, epsilon, True)
        cv.drawContours(img, [approx], -1,(0,0,0), 15)
        # Yukardaki siyah, şeklin çevresini tamamen dolaşırken alttaki beyaz çizgi en yakın kenarları birleştirir
        # Yani bir atnalı tarzında şekli tıpkı su bardağının çevresini çizer gibi çevreler
        hull = cv.convexHull(cnt)
        cv.drawContours(img, [hull], -1, (255,255,255), 8)

        (x2,y2), radius = cv.minEnclosingCircle(cnt)

        cv.circle(img, (x,y), 5, (0,0,255), -1)
        cv.circle(img, center, 5, (255, 0, 0), -1)
        #cv.circle(img, (int(x2), int(y2)), int(radius), (0, 255, 0), -1)
        cv.drawContours(img, contours, i, color, 4)

        cv.circle(paint, (int(x2), int(y2)), 15, color, -1)

        if len(approx) == 3:
            cv.putText(img, "Ucgen", (x,y), cv.FONT_HERSHEY_PLAIN, 1, 0, 2)
        elif len(approx) == 4:
            cv.putText(img, "Dortgen", (x,y), cv.FONT_HERSHEY_PLAIN, 1, 0, 2)
        elif len(approx) == 5:
            cv.putText(img, "Besgen", (x,y), cv.FONT_HERSHEY_PLAIN, 1, 0, 2)
        elif len(approx) > 6 and len(approx) < 11:
            cv.putText(img, "Cokgen", (x,y), cv.FONT_HERSHEY_PLAIN, 1, 0, 2)
        else:
            cv.putText(img, "Daire", (x, y), cv.FONT_HERSHEY_PLAIN, 1, 0, 2)

    cv.namedWindow("frame", cv.WINDOW_NORMAL)
    cv.namedWindow("frame2", cv.WINDOW_NORMAL)
    cv.namedWindow("frame3", cv.WINDOW_NORMAL)
    cv.namedWindow("frame4", cv.WINDOW_NORMAL)
    cv.imshow("frame", frame)
    cv.imshow("frame2", mask)
    cv.imshow("frame3", img)
    cv.imshow("frame4", paint)
    if cv.waitKey(1) & 0xFF == 27:
        break
    elif cv.waitKey(1) & 0xFF == ord("e"):
        paint [:] = 255

cam.release()
cv.destroyAllWindows()