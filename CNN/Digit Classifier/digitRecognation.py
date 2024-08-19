import cv2 as cv
import pickle
import numpy as np


def preProcess(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Görüntüyü gri tonlamaya çevir
    img = cv.equalizeHist(img)  # Histogram eşitleme
    img = img / 255.0  # Normalize etme (0-1 aralığına dönüştürme)
    return img


# Kamera açma
cam = cv.VideoCapture(0)
cam.set(3, 480)
cam.set(4, 480)

# Modeli yükleme
pickleIn = open("../Object Tracking/model_trained.p", "rb")
model = pickle.load(pickleIn)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    # Görüntüyü işleme
    img = cv.resize(frame, (32, 32))  # Görüntüyü yeniden boyutlandır
    img = preProcess(img)  # Görüntüyü işleme
    img = img.reshape(1, 32, 32, 1)  # Model giriş şekline dönüştürme

    # Tahmin
    predictions = model.predict(img)
    classIndex = np.argmax(predictions, axis=1)[0]  # En yüksek olasılığa sahip sınıfı bul
    prob = np.max(predictions)  # Maksimum olasılığı hesapla

    print(classIndex, prob)

    # Sonuçları ekranda göster
    if prob > 0.7:
        cv.putText(frame, f"{classIndex} {prob:.2f}", (50, 50), cv.FONT_HERSHEY_SIMPLEX,
                   1, (0, 255, 0), 2, cv.LINE_AA)

    cv.imshow("Siniflandirma Sonucu", frame)

    if cv.waitKey(1) & 0xFF == 27:  # ESC tuşuna basarak çıkış
        break

# Kaynakları serbest bırak
cam.release()
cv.destroyAllWindows()