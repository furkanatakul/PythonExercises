import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Resmi oku
resim = cv.imread("Images/image.jpg")

# Resme çerçeve ekle
constant = cv.copyMakeBorder(resim, 50, 50, 50, 50  , cv.BORDER_CONSTANT, value=[255, 0, 0])

# Pikseli oku ve değiştir
print(resim.shape)
px = resim[100, 100]
resim[100, 100, 0] = 255
resim[100, 100, 1:3] = [0, 100]
print(px)
print(resim.size)

# Bir kısmı kırp
kirp = resim[500:700, 600:800]

# BGR'den RGB'ye dönüştür
resim_rgb = cv.cvtColor(resim, cv.COLOR_BGR2RGB)
kirp_rgb = cv.cvtColor(kirp, cv.COLOR_BGR2RGB)
constant_rgb = cv.cvtColor(constant, cv.COLOR_BGR2RGB)

# Görüntüleri plot et
plt.subplot(131)
plt.imshow(resim_rgb)
plt.subplot(132)
plt.imshow(kirp_rgb)
plt.subplot(133)
plt.imshow(constant_rgb)
plt.show()
















