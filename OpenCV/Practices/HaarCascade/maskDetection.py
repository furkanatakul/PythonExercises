import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml")
mouth_cascade = cv2.CascadeClassifier(
    "haarcascade_mcs_mouth.xml")


korona = cv2.imread("aa.png")
yazi_maskeli = cv2.imread("yazi.png")
yazi_maskesiz = cv2.imread("yazi2.png")

korona_gray = cv2.cvtColor(korona,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(korona_gray,5,255,cv2.THRESH_BINARY)



cv2.namedWindow("Mask Detection")

cam = cv2.VideoCapture(0)

cam_x, cam_y = int(cam.get(3)), int(cam.get(4))

cerceve = np.zeros((cam_y+200, cam_x, 3), np.uint8)

yazi_maskeli = cv2.resize(yazi_maskeli, (cam_x, 200))
yazi_maskesiz = cv2.resize(yazi_maskesiz, (cam_x, 200))

while cam.isOpened():
    ret, frame = cam.read()
    video = frame.copy()
    
    if not ret:
        print("haydaa")
        
    cerceve[-200:,:] = yazi_maskeli
    cerceve[:-200,:] = video
    
    gray_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray_image, 1.1, 7)
    
    if(len(faces) == 0):
        print("no face found")
    else:
        for x, y, w, h in faces:
            roi_gray = gray_image[y:y+h, x:x+w]
            roi = frame[y:y+h, x:x+w]
            
            mouth = mouth_cascade.detectMultiScale(roi_gray,
                                                   1.4, 15)
            
            if(len(mouth) == 0):
                print("maske takılı")
            else:
                print("maskenizi takın")
                cerceve[-200:,:] = yazi_maskesiz
                dsize = (w, h)
                
                korona_resize = cv2.resize(korona, dsize)
                mask_resize = cv2.resize(mask, dsize)
                mask_inv = cv2.bitwise_not(mask_resize)
                
                
                img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)

                img2_fg = cv2.bitwise_and(korona_resize,
                                          korona_resize,
                                          mask=mask_resize)
                
                toplam = cv2.add(img1_bg,img2_fg)
                
                video[y:y+h, x:x+w] = toplam
                
                cerceve[:-200,:] = video
                
                
    cv2.imshow("Mask Detection",cerceve)
    
    if cv2.waitKey(33) & 0xFF == ord("q"):
        print("by")
        break



cam.release()
cv2.destroyAllWindows()