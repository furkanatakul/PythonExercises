import cv2 as cv
import numpy as np

img = np.zeros([512,512,3],np.uint8)


#çizgi çizme:
cv.line(img,(0,0),(511,511),(255,0,0), 5)
cv.line(img,(50,400),(400,50),(0,255,0), 5)

#Dikdörtgen Çizme
cv.rectangle(img,(50,50),(300,300),(0,0,255), 5)
cv.rectangle(img,(300,300),(511,511),(0,255,255), -1)

#Çember-Daire Çizme
cv.circle(img, (255,255), 60, (120,120,120), 2)
cv.circle(img, (100,100), 90, (255,255,120), -1)

#Elips Çizme:
cv.ellipse(img, (255,255), (100,50), 0,0,180, (255,100,0), 3)
cv.ellipse(img, (100,100), (100,50), 0,0,180, (255,100,0), -1)

#Belirtilen noktalara şekil çizme:
pts = np.array([[20, 30], [100, 120], [255, 255], [10, 400]], np.int32)
pts.reshape(-1,1,2)
cv.polylines(img,[pts],True,(255,255.255))

#Yazı Yazma:

cv.putText(img,"Selam Dunya", (50,50), cv.FONT_HERSHEY_PLAIN, 4, (0,155,255), 2, cv.LINE_AA)



cv.imshow("resim",img)
cv.waitKey(0)
cv.destroyAllWindows()


