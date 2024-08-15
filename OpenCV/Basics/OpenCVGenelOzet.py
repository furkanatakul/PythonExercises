# opencv kütüphanesini içe aktaralım
import cv2
import cv2 as cv
# matplotlib kütüphanesini içe aktaralım
import matplotlib.pyplot as plt
# resmi siyah beyaz olarak içe aktaralım
resim = cv.imread("Images/kus.jpg")
# resmi çizdirelim

# resmin boyutuna bakalım

print(resim.shape)

# resmi 4/5 oranında yeniden boyutlandıralım ve resmi çizdirelim
newRows = int(resim.shape[0] * 4/5)
newCols = int(resim.shape[1] * 4/5)
resim = cv.resize(resim, (newCols, newRows))
resim_rgb = cv.cvtColor(resim, cv.COLOR_BGR2RGB)
resim_gray = cv.cvtColor(resim, cv.COLOR_BGR2GRAY)
plt.subplot(221), plt.imshow(resim_rgb), plt.title("Original")

# orijinal resme bir yazı ekleyelim mesela "kopek" ve resmi çizdirelim
cv.putText(resim,"Kus", (0,0), cv.FONT_HERSHEY_PLAIN, 4, (0,0,0), 2, cv.LINE_AA)


# orijinal resmin 50 threshold değeri üzerindekileri beyaz yap altındakileri siyah yapalım, 
# binary threshold yöntemi kullanalım ve resmi çizdirelim
_, threshold  = cv.threshold(resim_gray, 50, 255, cv.THRESH_BINARY)
plt.subplot(222), plt.imshow(threshold, "gray"), plt.title("Threshold")

# orijinal resme gaussian bulanıklaştırma uygulayalım ve resmi çizdirelim
gauss = cv2.GaussianBlur(resim_rgb, ksize = (3,3), sigmaX = 7)
plt.subplot(223), plt.imshow(gauss, ), plt.title("GaussianBlur")

# orijinal resme Laplacian  gradyan uygulayalım ve resmi çizdirelim

laplacian = cv.Laplacian(resim, -1, ksize=3)
plt.subplot(224), plt.imshow(gauss, ), plt.title("Laplacian")
plt.tight_layout()
plt.show()
# orijinal resmin histogramını çizdirelim

color = ("b", "g", "r")
plt.figure()
for i, c in enumerate(color):
    hist = cv2.calcHist([resim], channels = [i], mask = None, histSize = [256], ranges = [0,256])
    plt.plot(hist, color = c)

plt.tight_layout()
plt.show()