import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


kus = cv.imread("Images/kus.jpg")
img = cv.imread("Images/sudoku.png")
print(kus.shape)
res = cv.resize(kus, (300,300))
res2 = cv.resize(kus, None, fx=0.5,fy=0.5, interpolation=cv.INTER_CUBIC)

print(res2.shape)

# RESMİN KENARINDA BOŞLUK BIRAKMA

rows, cols = kus.shape[:2]

translationMatrix = np.float32([
    [1,0,50],
    [0,1,50]
])

imgTranslation = cv.warpAffine(kus, translationMatrix, (cols, rows) )


# RESİM DÖNDÜRME

rotationMatrix = cv.getRotationMatrix2D((cols/2, rows/2), 30,1)

imgRotated = cv.warpAffine(kus, rotationMatrix, (cols, rows))



# RESİM NOKTALARININ KOORDİNATLARINI DEĞİŞTİRME


srcPoints = np.float32([
    [0,0],
    [cols-1,0],
    [0,rows-1]
])

dstPoints = np.float32([
    [0,0],
    [int(0.6*(cols-1)), 0],
    [int(0.4*(cols-1)), rows-1]
])

affineMatrix = cv.getAffineTransform(srcPoints,dstPoints)

output = cv.warpAffine(kus, affineMatrix, (cols, rows))


# Kuş Resmi perspektif alma

srcPoints = np.float32([
    [0,0],
    [cols-1,0],
    [0,rows-1],
    [cols-1, rows-1]
])

dstPoints = np.float32([
    [0, 0],
    [cols - 1, 0],
    [int(0.33*(cols - 1)), rows - 1],
    [int(0.66*(cols - 1)), rows - 1]
])

projectiveMatrix = cv.getPerspectiveTransform(srcPoints, dstPoints)

output = cv.warpPerspective(kus, projectiveMatrix, (cols,rows))


# Bir resmin belirli bir alanını kırpma

srcPoints = np.float32([
    [365,85],
    [478,87],
    [366,224],
    [493,230]
])

dstPoints = np.float32([
    [0, 0],
    [cols - 1, 0],
    [0, rows - 1],
    [cols - 1, rows - 1]
])

projectiveMatrix = cv.getPerspectiveTransform(srcPoints, dstPoints)

output = cv.warpPerspective(img, projectiveMatrix, (cols,rows))



cv.imshow("img", output)



cv.waitKey()
cv.destroyAllWindows()