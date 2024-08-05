import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

print(cam.get(3))
print(cam.get(4))

# cam.set(3,320)
# cam.set(4, 240)
# 
# print(cam.get(3))
# print(cam.get(4))

if not cam.isOpened():
    print("Kamera Tanınmadı")
    exit()

fourcc = cv.VideoWriter_fourcc(*"XVID")
out = cv.VideoWriter("Videos/nesneler.avi", fourcc, 30.0, (640,480))

while cam.isOpened():
    ret, frame = cam.read()

    #frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    if not ret:
        print("Kameradan Görüntü Okunamıyor!!")
        break
    out.write(frame)
    cv.imshow("kamera", frame)
    if cv.waitKey(1) == ord("q"):
        print("Görüntü Sonlandırıldı.")
        break



cam.release()
out.release()
cv.destroyAllWindows()