import cv2
import numpy as np

cam = cv2.VideoCapture("vtest.avi")

tum_vucud = cv2.CascadeClassifier("haarcascade_fullbody.xml")
alt_vucud = cv2.CascadeClassifier("haarcascade_lowerbody.xml")
ust_vucud = cv2.CascadeClassifier("haarcascade_upperbody.xml")

ret, resim = cam.read()

detect = np.zeros((resim.shape[0],resim.shape[1],3), np.uint8)

def nothing(x):
    pass

cv2.namedWindow("resim", cv2.WINDOW_NORMAL)
cv2.createTrackbar("one_param", "resim", 0, 100, nothing)
cv2.createTrackbar("two_param", "resim", 0, 100, nothing)
cv2.createTrackbar("switch", "resim", 0, 1, nothing)

while cam.isOpened():
    
    detect[:] = 0
    
    if cv2.getTrackbarPos("switch", "resim") == 1:
        cv2.waitKey(1)
        continue
        
    ret, resim = cam.read()
    
    if not ret:
        print("done")
        break
    
    resim_gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
    
    
    one_param = cv2.getTrackbarPos("one_param", "resim")/100+1.01
    two_param = cv2.getTrackbarPos("two_param", "resim")+1
    
    print("ilk parametre: {}, ikinci parametre: {} ".format(
        one_param,two_param))
    
    vucudlar = tum_vucud.detectMultiScale(resim_gri, 
                                          one_param, 
                                          two_param,
                                          minSize=(40,40),
                                          maxSize=(110,110))
    alt_vucudlar = alt_vucud.detectMultiScale(resim_gri,
                                              one_param, 
                                              two_param,
                                              minSize=(40,40),
                                              maxSize=(80,80))
    ust_vucudlar = ust_vucud.detectMultiScale(resim_gri, 
                                              one_param, 
                                              two_param,
                                              minSize=(40,40),
                                              maxSize=(80,80))
    
    for x, y, w, h in vucudlar:
        detect[y:y+h, x:x+w] = resim[y:y+h, x:x+w]
        cv2.rectangle(resim, (x,y), (x+w, y+h), (255,0,0), 3)
        resim[y:y+h, x:x+w, 0] = 255
    
    for x, y, w, h in alt_vucudlar:
        cv2.rectangle(resim, (x,y), (x+w, y+h), (0,255,0), 2)
        resim[y:y+h, x:x+w, 1] = 255
    
    for x, y, w, h in ust_vucudlar:
        cv2.rectangle(resim, (x,y), (x+w, y+h), (0,0,255), 2)
        resim[y:y+h, x:x+w, 2] = 255
    
    cv2.imshow("resim",resim)
    cv2.imshow("detect",detect)
    
    if cv2.waitKey(5) == ord("q"):
        print("by")
        break
    
cv2.destroyAllWindows()
cam.release()