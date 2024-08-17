import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd

OPENCV_OBJECT_TRACKERS = {"csrt"      : cv.legacy.TrackerCSRT.create(),
		                  "kcf"       : cv.legacy.TrackerKCF.create(),
		                  "boosting"  : cv.legacy.TrackerBoosting.create(),
		                  "mil"       : cv.legacy.TrackerMIL.create(),
		                  "tld"       : cv.legacy.TrackerTLD.create(),
		                  "medianflow": cv.legacy.TrackerMedianFlow.create(),
		                  "mosse"     : cv.legacy.TrackerMOSSE.create()}

trackerName = "kcf"
tracker = OPENCV_OBJECT_TRACKERS[trackerName]
print(tracker)

gt = pd.read_csv("gt_new.txt")

videoPath = "deneme.mp4"
cap = cv.VideoCapture(videoPath)

# genel parametreler
initBB = None
fps = 25
frame_number = []
f = 0
success_track_frame_success = 0
track_list = []
start_time = time.time()

while True:
    ret, frame = cap.read()

    if ret:
        frame = cv.resize(frame,(960,540))
        (H,W) = frame.shape[:2]

        carGt = gt[gt["frame_no"] == f]
        if len(carGt) != 0:
            x = carGt.x.values[0]
            y = carGt.y.values[0]
            w = carGt.w.values[0]
            h = carGt.h.values[0]
            center_x = carGt.center_x.values[0]
            center_y = carGt.center_y.values[0]

            cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
            cv.circle(frame, (center_x,center_y), 2, (0,0,255), -1)

        if initBB is not None:
            (success, box) = tracker.update(frame)

            if f <= np.max(gt.frame_no):
                (x,y,w,h) = [int(i) for i in box]
                cv.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
                success_track_frame_success += 1
                trackCenterX = int(x+w/2)
                trackCenterY = int(y + h / 2)
                track_list.append([f,trackCenterX,trackCenterY])

            info = [("Tracker",trackerName),
                    ("Success", "Yes" if success else "No")]
            for (i, (o, p)) in enumerate(info):
                text = "{}: {} ".format(o, p)
                cv.putText(frame, text, (10, H - (i * 20) - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        cv.putText(frame, "Frame Num: " + str(f), (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv.imshow("frame", frame)

        frame_number.append(f)
        f = f + 1
        key = cv.waitKey(1) & 0xFF

        if key == ord("t"):
            initBB = cv.selectROI("Frame", frame, fromCenter=False)
            cv.destroyWindow("Frame")
            tracker.init(frame, initBB)

        elif key == ord("q"):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()

stop_time = time.time()

timeDiff = stop_time - start_time

#Değerlendirme:
trackDf = pd.DataFrame(track_list, columns = ["frame_no","center_x", "center_y"])

if len(trackDf) != 0:
    print("Tracking method: ", tracker)
    print("Time: ", timeDiff)
    print("Number of frame to track (gt): ", len(gt))
    print("Number of frame to track (track success): ", success_track_frame_success)

    track_df_frame = trackDf.frame_no

    gt_center_x = gt.center_x[track_df_frame].values
    gt_center_y = gt.center_y[track_df_frame].values

    track_df_center_x = trackDf.center_x.values
    track_df_center_y = trackDf.center_y.values

    plt.plot(np.sqrt((gt_center_x - track_df_center_x) ** 2 + (gt_center_y - track_df_center_y) ** 2))
    plt.xlabel("frame")
    plt.ylabel("Öklid mesafesi btw gt ve track")
    error = np.sum(np.sqrt((gt_center_x - track_df_center_x) ** 2 + (gt_center_y - track_df_center_y) ** 2))
    print("Toplam hata: ", error)
    plt.show()