import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

resim = cv.imread("Images/kus.jpg", 0)

thresh = cv.adaptiveThreshold(resim, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 0)
thresh2 = cv.adaptiveThreshold(resim, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 0)

plt.subplot(1,3,1), plt.imshow(resim, "gray"), plt.title("Original")
plt.subplot(1,3,2), plt.imshow(thresh, "gray"), plt.title("ADAPTIVE_THRESH_MEAN_C")
plt.subplot(1,3,3), plt.imshow(thresh2, "gray"), plt.title("ADAPTIVE_THRESH_GAUSSIAN_C")
plt.show()

cv.waitKey()
cv.destroyAllWindows()