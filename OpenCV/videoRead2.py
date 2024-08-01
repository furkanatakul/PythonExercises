import cv2 as cv
import numpy as np

cam = cv.VideoCapture("Videos/bolt-detection.mp4")

if not cam.isOpened():
    print("Video dosyası açılamadı.")
    exit()

frame_count = int(cam.get(cv.CAP_PROP_FRAME_COUNT))
print(f"Toplam kare sayısı: {frame_count}")

current_frame = 0
while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        if current_frame >= frame_count:
            print("Video sona erdi.")
        else:
            print(f"Görüntü Okunamıyor!!! Kare: {current_frame}")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("goruntu", gray)

    if cv.waitKey(30) & 0xFF == ord('q'):
        print("Video Kapatıldı")
        break

    current_frame += 1
cam.release()
cv.destroyAllWindows()


