import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

resim = cv.imread("Images/noisy2.jpeg", 0)
resim = cv.resize(resim, None, fx=3,fy=3, interpolation=cv.INTER_CUBIC)

#Simple Thresholding
_, th1 = cv.threshold(resim, 127, 255, cv.THRESH_BINARY)

#Otsu Thresholding
_, th = cv.threshold(resim, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

#Otsu Thresholding after filtering
blur = cv.GaussianBlur(resim, (15,15), 0)
_, th2 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

plt.subplot(3,3,1), plt.imshow(resim, "gray"), plt.title("Original Image")
plt.subplot(3,3,2), plt.hist(resim.ravel(), 256), plt.title("Histogram")
plt.subplot(3,3,3), plt.imshow(th, "gray"), plt.title("Simple Thresholding")
plt.subplot(3,3,4), plt.imshow(resim, "gray"), plt.title("Original Image")
plt.subplot(3,3,5), plt.hist(resim.ravel(), 256), plt.title("Histogram")
plt.subplot(3,3,6), plt.imshow(th1, "gray"), plt.title("Otsu Thresholding")
plt.subplot(3,3,7), plt.imshow(blur, "gray"), plt.title("Original Image")
plt.subplot(3,3,8), plt.hist(blur.ravel(), 256), plt.title("Histogram")
plt.subplot(3,3,9), plt.imshow(th2, "gray"), plt.title("Otsu Thresholding after filtering")
plt.tight_layout()
plt.show()


plt.hist(blur.ravel(), 256)
plt.show()
cv.imshow("resim", th)









cv.waitKey()


cv. destroyAllWindows()