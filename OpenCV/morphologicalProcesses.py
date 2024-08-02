import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

resim = cv.imread("Images/i.jpg", 0)
_, thresholdImage = cv.threshold(resim, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

kernel = np.ones((3,3), dtype=np.uint8)


#Farklı kernel oluşturma yöntemleri
kernelRectengular = cv.getStructuringElement(cv.MORPH_RECT, (5,5))
kernelEllipse = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
kernelCross = cv.getStructuringElement(cv.MORPH_CROSS, (5,5))


erosion = cv.erode(thresholdImage, kernelCross, iterations=1)
dilation = cv.dilate(thresholdImage, kernelCross, iterations=3)

oppening = cv.morphologyEx(thresholdImage, cv.MORPH_OPEN, kernelCross)
closing = cv.morphologyEx(thresholdImage, cv.MORPH_CLOSE, kernelCross)
tophat = cv.morphologyEx(thresholdImage, cv.MORPH_TOPHAT, kernelCross)
blackhat = cv.morphologyEx(thresholdImage, cv.MORPH_BLACKHAT, kernelCross)
gradient = cv.morphologyEx(thresholdImage, cv.MORPH_GRADIENT, kernelCross)

plt.subplot(241), plt.imshow(thresholdImage, "gray" ), plt.title("Original")
plt.subplot(242), plt.imshow( erosion, "gray"), plt.title("Erosion")
plt.subplot(243), plt.imshow(dilation, "gray"), plt.title("Dilation")
plt.subplot(244), plt.imshow(oppening, "gray" ), plt.title("Openning")
plt.subplot(245), plt.imshow(closing, "gray" ), plt.title("Closing")
plt.subplot(246), plt.imshow(tophat, "gray" ), plt.title("Tophat") # Orijinal giriş resmiyle oppeningin farkını alır
plt.subplot(247), plt.imshow(blackhat, "gray" ), plt.title("Blackhat") # Orijinal giriş resmiyle closing in farkını alır
plt.subplot(248), plt.imshow(gradient, "gray" ), plt.title("Gradient") # Dilation ile Erosion un farkını alır

plt.tight_layout()
plt.show()



cv.waitKey()
cv.destroyAllWindows()