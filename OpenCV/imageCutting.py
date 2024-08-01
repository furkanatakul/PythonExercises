import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread("Images/sudoku.png")
rows, cols = img.shape[:2]

cv.namedWindow("img", cv.WINDOW_NORMAL)
clickCount = 0
a = []

dstPoints = np.float32([
    [0, 0],
    [cols - 1, 0],
    [0, rows - 1],
    [cols - 1, rows - 1]
])


def draw(event, x, y, flags, param):
    global clickCount, a

    if clickCount < 4:
        if event == cv.EVENT_LBUTTONDBLCLK:
            clickCount += 1
            a.append((x,y))
    else:
        srcPoints = np.float32([
            [a[0][0], a[0][1]],
            [a[1][0], a[1][1]],
            [a[2][0], a[2][1]],
            [a[3][0], a[3][1]]
        ])
        clickCount = 0
        a = []

        m = cv.getPerspectiveTransform(srcPoints,dstPoints)
        imageOutput = cv.warpPerspective(img, m, (cols, rows))
        cv.imshow("output", imageOutput)


cv.setMouseCallback("img", draw)


while 1:
    cv.imshow("img", img)
    #cv.imshow("imgOutput", output)
    if cv.waitKey(1) & 0xFF == 27:
        break
cv.destroyAllWindows()