import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Resmi yükleyin ve gri tonlamalı hale getirin
image = cv.imread("Images/chess.jpg", cv.IMREAD_GRAYSCALE)
image_float = np.float32(image)

# Orijinal resmi gösterin
plt.subplot(221), plt.imshow(image, cmap='gray'), plt.title("Original")

# Harris köşe tespiti
dst = cv.cornerHarris(image_float, blockSize=2, ksize=3, k=0.04)
dst = cv.dilate(dst, None)

# Köşe noktalarını işaretleyin
image_harris = image.copy()
image_harris[dst > 0.2 * dst.max()] = 255

plt.subplot(222), plt.imshow(dst, cmap='gray'), plt.title("Corner Detected")
plt.subplot(223), plt.imshow(image_harris, cmap='gray'), plt.title("Corner Detected ++")

# Shi-Tomasi köşe tespiti
image_color = cv.imread("Images/chess.jpg")
corners = cv.goodFeaturesToTrack(image, 100, 0.01, 10)
if corners is not None:
    corners = np.int0(corners)
    for i in corners:
        x, y = i.ravel()
        cv.circle(image_color, (x, y), 5, (0, 255, 0), -1)

plt.subplot(224), plt.imshow(cv.cvtColor(image_color, cv.COLOR_BGR2RGB)), plt.title("Shi-Tomasi Corner Detection")

plt.tight_layout()
plt.show()
