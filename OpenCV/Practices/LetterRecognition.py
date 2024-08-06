import cv2
import numpy as np


#DATA HAZIRLAMA

data = np.loadtxt("letter-recognition.data", dtype="float32",
                  delimiter=",",
                  converters={0: lambda x: ord(x)-65})

# for i, k in enumerate(data[:,0]):
#     data[:,0][i] = ord(k)-65
# data = np.float32(data)

train, test = np.vsplit(data, 2)
train_responses, trainData = np.hsplit(train, [1])
test_responses, testData = np.hsplit(test, [1])

#EĞİTİM

knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, train_responses)

#TEST
ret, results, neighbours, distance = knn.findNearest(testData, 5)

matches = test_responses == results
correct = np.count_nonzero(matches)
accuracy = correct*100.0 / results.size

print("accuracy: ",accuracy)
