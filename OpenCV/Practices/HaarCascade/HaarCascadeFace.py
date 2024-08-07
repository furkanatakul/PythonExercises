import cv2

face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

img = cv2.imread("yuzler.jpg")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(img_gray, 1.05, 2)


for x, y, w, h in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)
    roi_gray = img_gray[y:y+h, x:x+w]
    
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.02,1)
    
    for ex, ey, ew, eh in eyes:
        cv2.rectangle(img, (ex+x, ey+y), (ex+ew+x, ey+eh+y), (0,255,0),2)
        
        
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()
