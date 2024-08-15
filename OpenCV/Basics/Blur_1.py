import cv2
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")

# blurring (detayı azaltır, gürültüyü engeller)
img = cv2.imread("Images/kus.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("orijinal"),plt.show()

"""
ortalama bulanıklaştırma yöntemi

"""
dst2 = cv2.blur(img, ksize = (3,3))
plt.figure(), plt.imshow(dst2), plt.axis("off"), plt.title("Ortalama Blur")

"""
gaussian blur

"""

gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
plt.figure(), plt.imshow(gb), plt.axis("off"), plt.title("Gauss Blur")

"""
medyan blur

"""
mb = cv2.medianBlur(img, ksize = 3)
plt.figure(), plt.imshow(mb), plt.axis("off"), plt.title("Medyan Blur")


def gaussianNoise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5

    gauss = np.random.normal(mean, sigma, (row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    normalized_image = np.clip(noisy, 0, 1)
    return normalized_image

# içe aktar normalize et
img = cv2.imread("Images/kus.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("orijinal"),plt.show()

gaussianNoisyImage = gaussianNoise(img)
plt.figure(),plt.imshow(gaussianNoisyImage),plt.axis("off"),plt.title("Gauss Noisy"),plt.show()

# gauss blur
gb2 = cv2.GaussianBlur(gaussianNoisyImage, ksize = (3,3), sigmaX = 7)
plt.figure(), plt.imshow(gb2), plt.axis("off"), plt.title("with Gauss Blur")


def saltPepperNoise(image):
    image = cv2.resize(image, (1000, 1000))
    row, col, ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    noisy = np.copy(image)

    # Salt (beyaz) gürültü
    num_salt = np.ceil(amount * image.size * s_vs_p)
    salt_coords = [np.random.randint(0, i, int(num_salt)) for i in image.shape]
    noisy[salt_coords[0], salt_coords[1], :] = [255, 255, 255]  # Beyaz renkli piksel için

    # Pepper (siyah) gürültü
    num_pepper = np.ceil(amount * image.size * (1 - s_vs_p))
    pepper_coords = [np.random.randint(0, i, int(num_pepper)) for i in image.shape]
    noisy[pepper_coords[0], pepper_coords[1], :] = [0, 0, 0]  # Siyah renkli piksel için

    return noisy

file_path = 'Images/kus.jpg'
img = cv2.imread(file_path)

# Gürültü ekle
spImage = saltPepperNoise(img)

# Görüntüleme
plt.figure(), plt.imshow(cv2.cvtColor(spImage, cv2.COLOR_BGR2RGB)), plt.axis("off"), plt.title("SP Image")

# Median blur uygulama
spImage_uint8 = np.uint8(spImage)  # Median blur için uint8 formatına çevir
mb2 = cv2.medianBlur(spImage_uint8, ksize=3)

plt.figure(), plt.imshow(cv2.cvtColor(mb2, cv2.COLOR_BGR2RGB)), plt.axis("off"), plt.title("with Median Blur")
plt.show()