import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

resim = cv.imread("Images/chess.jpg", 0)

# Y eksenindeki kenarları belirginleştirir
sobelX  = cv.Sobel(resim, -1, 1, 0, ksize= 5)
# Schar Filter
sobelX_  = cv.Sobel(resim, -1, 1, 0, ksize= -1)
# X eksenindeki kenarları belirginleştirir
sobelY  = cv.Sobel(resim, -1, 0, 1, ksize= 5)
# Her iki eksendeki  kenarları belirginleştirir
sobel  = cv.Sobel(resim, -1, 1, 1, ksize= 5)

laplacian = cv.Laplacian(resim, -1, )
#Canny Yöntemi
canny = cv.Canny(resim, 50, 150)

plt.subplot(241), plt.imshow(resim, "gray"), plt.title("Original")
plt.subplot(242), plt.imshow(sobelX, "gray"), plt.title("SobelX")
plt.subplot(243), plt.imshow(sobelY, "gray"), plt.title("SobelY")
plt.subplot(244), plt.imshow(sobel, "gray"), plt.title("Sobel")
plt.subplot(245), plt.imshow(sobelX_, "gray"), plt.title("Schar")
plt.subplot(246), plt.imshow(laplacian, "gray"), plt.title("Laplacian")
plt.subplot(247), plt.imshow(canny, "gray"), plt.title("Canny")

plt.tight_layout()
plt.show()



















cv.waitKey()
cv.destroyAllWindows()