import pandas as pd
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

colList = ["frame_number","identity_number","left","top","width","height","score","class","visibility"]

data = pd.read_csv("gt.txt", names=colList)

car = data[data["class"] == 3]

videoPath = "deneme.mp4"

cap = cv.VideoCapture(videoPath)
id1 = 29

numberOfImage = np.max(data["frame_number"])

fps = 25
boundBoxList = list()

for i in range(numberOfImage+1):
    ret, frame = cap.read()

    if ret:
        frame = cv.resize(frame, dsize=(960,540))

        filterId1 = np.logical_and(car["frame_number"] == i+1, car["identity_number"] == id1)

        if len(car[filterId1]) != 0:

            x = int(car[filterId1]["left"].values[0] / 2)
            y = int(car[filterId1].top.values[0] / 2)
            w = int(car[filterId1].width.values[0] / 2)
            h = int(car[filterId1].height.values[0] / 2)
            cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            cv.circle(frame, (int(x+(w/2)), int(y+(h/2))), 2, (0,0,255,),-1)

            # frame, x, y, genis, yuksek, center_x, center_y
            boundBoxList.append([i, x, y, w, h, int(x+(w/2)), int(y+(h/2))])

        cv.putText(frame, "Frame Num: "+str(i+1), (10,30), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 1,(0,0,255), 2)
        cv.imshow("Frame",frame)

        if cv.waitKey(1) & 0xFF == ord("q"): break

    else : break

cap.release()
cv.destroyAllWindows()

df = pd.DataFrame(boundBoxList, columns = ["frame_no", "x", "y", "w", "h", "center_x", "center_y"])
df.to_csv("gt_new.txt",index=False)