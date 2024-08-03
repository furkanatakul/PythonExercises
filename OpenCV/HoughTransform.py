import cv2 as cv
import numpy as np

img = cv.imread("Images/chess.jpg")

gray_ = img.copy()
gray = cv.cvtColor(gray_, cv.COLOR_BGR2GRAY)

edges = cv.Canny(gray, 30,50)

lines = cv.HoughLines(edges, 1, np.pi/180, 500)

if not isinstance(lines, type(None)):
    for line in lines:
         for rho, theta in line:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

            cv.line(gray_, (x1,y1) , (x2,y2), color=(0,0,255), thickness=2 )

cv.imshow("resim", img)
cv.imshow("edges", edges)
cv.imshow("copy", gray_)




cv.waitKey()
cv.destroyAllWindows()