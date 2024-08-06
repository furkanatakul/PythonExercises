import cv2
import numpy as np
from matplotlib import pyplot as plt


trainData = np.random.randint(0, 100, (25,2)).astype(np.float32)
responses = np.random.randint(0, 2, (25,1)).astype(np.float32)

red = trainData[responses.ravel() == 0]
blue = trainData[responses.ravel() == 1]

plt.scatter(red[:,0], red[:,1], 80, 'r', '^', 
            label = "red-0", alpha = 0.4)
plt.scatter(blue[:,0], blue[:,1], 80, 'b', 'o', 
            label = "blue-1", alpha = 0.4)

new_data = np.random.randint(0, 100, (1,2)).astype(np.float32)
plt.scatter(new_data[:,0], new_data[:,1], 80, 'g', 's', 
            label = "new", alpha = 1)

knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)
ret, results, neighbours, distance = knn.findNearest(new_data, 3)

print("*"*40)
print("""
      ret: {}
      results: {}
      neighbours: {}
      distance: {}
      """.format(ret,results,neighbours, distance))
print("*"*40)

plt.legend()
plt.show()