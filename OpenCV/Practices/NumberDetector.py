import cv2
import numpy as np

img = cv2.imread("Images/digits.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# DATAMIZI HAZIRLIYORUZ

cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
x = np.array(cells)

train = x[:,:90].reshape(-1,400).astype(np.float32)
test = x[:,90:100].reshape(-1,400).astype(np.float32)

k = np.arange(10)
train_responses = np.repeat(k,450).reshape(-1,1)
# test_responses = train_responses.copy()
test_responses = np.repeat(k,50).reshape(-1,1)

# DATA KAYIT ETME
np.savez("knn_data.npz", train_data = train,
         train_label = train_responses)

# DATA OKUMA
with np.load("knn_data.npz") as data:
    print(data.files)
    train = data["train_data"]
    train_responses = data["train_label"]

# EĞİTİM

knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_responses)
ret, results, neighbours, distance = knn.findNearest(test, 5)

matches = test_responses == results
correct = np.count_nonzero(matches)
accuracy = correct*100.0 / results.size

print("accuracy: ",accuracy)

# Eğitilen modeli kayıt etmek
# video'da yok sonradan ekledim :(
knn.save('KNN_Trained_Model.yml')
#%%
#modeli okuma
knn = cv2.ml.KNearest_load('KNN_Trained_Model.yml')

# Kendimiz Test Edelim

def test(img):
    img = cv2.medianBlur(img, 21)
    img = cv2.dilate(img, np.ones((15,15),np.uint8))
    cv2.imshow("img",img)
    img = cv2.resize(img, (20,20)).reshape(-1,400).astype(np.float32)
    ret, results, neighbours, distance = knn.findNearest(img, 
                                                         5)
    cv2.putText(img2, str(int(ret)), (100,300), 
                font, 10, 255, 4, cv2.LINE_AA)
    return ret


cizim = False
mod = False
xi,yi = -1,-1
font = cv2.FONT_HERSHEY_SIMPLEX
img = np.ones((400,400),np.uint8)

def draw(event, x, y, flags, param):
    global cizim,xi,yi,mod
    
    if event == cv2.EVENT_LBUTTONDOWN:
        xi,yi = x,y
        cizim = True
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if cizim:
            if mod:
                cv2.circle(img,(x,y),10,255,-1)
            else:
                cv2.rectangle(img,(xi,yi),(x,y),255,-1)
        else:
            pass
    
    elif event == cv2.EVENT_LBUTTONUP:
        cizim = False

    elif event == cv2.EVENT_LBUTTONDBLCLK:
        img[:,:] = 0


cv2.namedWindow("paint")
cv2.setMouseCallback("paint",draw)

while(1):
    img2 = np.ones((400,400),np.uint8)
    key = cv2.waitKey(33) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("m"):
        mod = not mod
    
    print(test(img))
    cv2.imshow("paint",img)
    cv2.imshow("result",img2)
    
cv2.destroyAllWindows()





