import cv2 as cv
import os
from os.path import isfile, join
import matplotlib.pyplot as plt

pathIn = r"img1"
pathOut = "deneme.mp4"

files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f)) ]

fps = 25
size= (1920, 1080)

fourcc = cv.VideoWriter_fourcc(*"MP4V")
out = cv.VideoWriter(pathOut, fourcc, fps, size, True)

for i in files :
    print(i)

    fileName = pathIn + "\\" + i

    img = cv.imread(fileName)

    out.write(img)

out.release()















