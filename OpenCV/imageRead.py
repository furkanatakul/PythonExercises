import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
resim = cv.imread("Images/kedi.jpg", 0)

cv.namedWindow("resim", cv.WINDOW_NORMAL)
print(resim)
cv.imshow("resim", resim)
cv.imshow("resim penceresi", resim)
plt.imshow(resim, cmap="gray")
plt.show()


sifir= np.zeros([300,300])
bir= np.ones([300,300])

cv.imshow("sıfır", sifir)
cv.imshow("bir", bir)
cv.namedWindow("sıfır", cv.WINDOW_NORMAL)
cv.namedWindow("bir", cv.WINDOW_NORMAL)

key = cv.waitKey(0)
cv.destroyAllWindows()

if key == ord("s"):
    cv.imwrite("Images/kedi2.jpg", resim)

