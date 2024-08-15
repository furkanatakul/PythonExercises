# opencv kütüphanesini içe aktaralım
import cv2 as cv
# numpy kütüphanesini içe aktaralım
import numpy as np
import matplotlib.pyplot as plt
# resmi siyah beyaz olarak içe aktaralım resmi çizdirelim
img = cv.imread("Images/ozet.jpg", 0)
plt.subplot(221), plt.imshow(img, cmap="gray"), plt.title("Original")
# resim üzerinde bulunan kenarları tespit edelim ve görselleştirelim edge detection
blured = cv.blur(img, ksize = (3,3))
canny = cv.Canny(blured, 50, 150)
plt.subplot(222), plt.imshow(canny, cmap="gray"), plt.title("Edge Detected")

# yüz tespiti için gerekli haar cascade'i içe aktaralım
cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

# yüz tespiti yapıp sonuçları görselleştirelim
faces = cascade.detectMultiScale(img, scaleFactor=1.15, minNeighbors=12)

for x,y,w,h in faces:
    cv.rectangle(img, (x,y), (x+w,y+h), 255, 3)
plt.subplot(223), plt.imshow(img, cmap="gray"), plt.title("Face Detected")

# HOG ilklendirelim insan tespiti algoritmamızı çağıralım ve svm'i set edelim
hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())
img = cv.imread("Images/ozet.jpg", 0)
(rects, weights) = hog.detectMultiScale(img, padding=(8, 8), scale=1.05)

for (x, y, w, h) in rects:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
plt.subplot(224), plt.imshow(img, cmap="gray"), plt.title("Human Detected")

plt.tight_layout()
plt.show()
cv.destroyAllWindows()