import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

cam = cv.VideoCapture(0)

lower = np.array([105, 50, 50])
upper = np.array([135, 255, 255])

_,background = cam.read()

kernel = np.ones((3,3), np.uint8)
kernel1 = np.ones((11,11), np.uint8)
kernel2 = np.ones((13,13), np.uint8)
while cam.isOpened():

    _, frame = cam.read()

    hsv = cv. cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower, upper)

    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel )
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel1)
    mask  = cv.dilate(mask, kernel2, iterations=1)

    mask_not = cv.bitwise_not(mask)

    bg = cv.bitwise_and(background,background,mask=mask)
    fg = cv.bitwise_and(frame, frame, mask=mask_not)

    dst = cv.addWeighted(bg,1,fg,1,0)

    #dst = np.vstack((dst, frame
    # ))

    cv.imshow("goruntu",frame)
    cv.imshow("msak", mask)
    cv.imshow("cloak", fg)
    if cv.waitKey(1) & 0xFF == 27:
        break

cam.release()
cv.destroyAllWindows()