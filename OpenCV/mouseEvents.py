import math
import cv2 as cv
import numpy as np

cizim = False
xi, yi = -1, -1
mod = 0

def draw(event, x, y, flags, param):
    global cizim, xi, yi, mod
    if event == cv.EVENT_LBUTTONDOWN:
        xi, yi = x, y
        cizim = True
    if event == cv.EVENT_MOUSEMOVE:
        if cizim:
            if mod:
                cv.circle(img, (xi, yi), int(math.sqrt((xi - x) ** 2 + (yi - y) ** 2)), (100, 50, 0), 2)
            else:
                cv.rectangle(img, (xi, yi), (x, y), (100, 50, 0), -1)
    if event == cv.EVENT_LBUTTONUP:
        cizim = False

img = np.ones([512, 512, 3], np.uint8)

cv.namedWindow("Paint")
cv.setMouseCallback("Paint", draw)

while True:
    cv.imshow("Paint", img)
    key = cv.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("m"):
        mod = not mod

cv.destroyAllWindows()






