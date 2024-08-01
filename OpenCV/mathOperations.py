import cv2 as cv
import numpy as np

# NumPy array'leri tanımla
y = 10*np.ones((1,1,1), np.uint8)
x = 250*np.ones((1,1,1), np.uint8)

# OpenCV add fonksiyonunu kullanarak toplama işlemi yap
result_cv = cv.add(x, y)
print("cv.add result:", result_cv)  # Beklenen çıktı: [255]

img = np.zeros((512,512,3),np.uint8)
img[:] = [255,0,0]
img2 = np.zeros((512,512,3),np.uint8)
img2[:] = [0,0,255]



summ = cv.addWeighted(img,0.7,img2,0.3,0)

# cv.imshow("resim", summ)

imgg = cv.imread("Images/elephent.jpg")
imgg2 = cv.imread("Images/kus.jpg")

imggGrey= cv.cvtColor(imgg, cv.COLOR_BGR2GRAY)

ret, mask = cv.threshold(imggGrey, 10, 255, cv.THRESH_BINARY)
x, y,z = imgg.shape
roi = imgg2[0:x, 0:y]

maskInvert = cv.bitwise_not(mask)

imgg_bg = cv.bitwise_and(roi,roi,mask=maskInvert)
#imgg2_fg = cv.bitwise_and(imgg,imgg,mask=mask)

toplam = cv.add(imgg_bg,imgg)
imgg2[0:x, 0:y] = toplam
cv.namedWindow("resim", cv.WINDOW_NORMAL)

cv.imshow("resim", toplam)




cv.waitKey(0)
cv.destroyAllWindows()


