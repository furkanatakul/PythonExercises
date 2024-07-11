import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# Veri setini yükle
data = pd.read_csv("Datasets/odev_tenis.csv")
dataFrame = pd.DataFrame(data=data)

# LabelEncoder kullanarak kategorik verileri sayısal verilere çevir
le = preprocessing.LabelEncoder()
outlook = data.iloc[:, 0].values
outlook = le.fit_transform(outlook).reshape(-1, 1)

# OneHotEncoder kullanarak 'outlook' sütununu dönüştür
ohe = preprocessing.OneHotEncoder()
outlook = ohe.fit_transform(outlook).toarray()
outlook = pd.DataFrame(outlook, index=range(len(outlook)), columns=["overcast", "rainy", "sunny"])

# 'windy' ve 'play' sütunlarını LabelEncoder ile dönüştür
windy = data.iloc[:, -2].values
windy = le.fit_transform(windy).reshape(-1, 1)
windy = pd.DataFrame(windy, index=range(len(windy)), columns=["windy"])

play = data.iloc[:, -1].values
play = le.fit_transform(play).reshape(-1, 1)
play = pd.DataFrame(play, index=range(len(play)), columns=["play"])

# 'temperature' ve 'humidity' sütunlarını seç
temputure_humidity = dataFrame[["temperature", "humidity"]]

# Yeni veri çerçevesini oluştur
dataFrame2 = pd.concat([outlook, temputure_humidity, windy, play], axis=1)

# Hedef ve özellik değişkenlerini ayır
y = dataFrame2["humidity"]
x = dataFrame2.drop(["humidity"], axis=1)

# Veriyi eğitim ve test olarak ayır
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.33)

# Lineer regresyon modelini oluştur ve eğit
lr = LinearRegression()
lr.fit(xTrain, yTrain)

# Test verisiyle tahmin yap
tahmin = lr.predict(xTest)
print(yTest, "\n", tahmin)

# OLS modeli oluştur
X = np.append(arr=np.ones((len(x), 1)).astype(int), values=x, axis=1)
X = pd.DataFrame(X)
xList = X.iloc[:, [0, 1, 2, 3, 4, 5]]
xList = np.array(xList, dtype=float)
model = sm.OLS(y, xList).fit()

# Geriye doğru eleme işlemi
column_to_drop = xTrain.columns[-2]
column_to_drop2 = xTest.columns[-2]
xTrain = xTrain.drop(columns=[column_to_drop])
xTest = xTest.drop(columns=[column_to_drop2])
lr.fit(xTrain, yTrain)
tahmin2 = lr.predict(xTest)
print(tahmin2)

xList = x.iloc[:, [0, 1, 2, 3, 5]]
xList = np.array(xList, dtype=float)
model = sm.OLS(y, xList).fit()
column_to_drop = xTrain.columns[2]
column_to_drop2 = xTest.columns[2]
xTrain = xTrain.drop(columns=[column_to_drop])
xTest = xTest.drop(columns=[column_to_drop2])
lr.fit(xTrain, yTrain)
tahmin3 = lr.predict(xTest)
print(tahmin3)

xList = x.iloc[:, [0, 1, 3, 5]]
xList = np.array(xList, dtype=float)
model = sm.OLS(y, xList).fit()
column_to_drop = xTrain.columns[0]
column_to_drop2 = xTest.columns[0]
xTrain = xTrain.drop(columns=[column_to_drop])
xTest = xTest.drop(columns=[column_to_drop2])
lr.fit(xTrain, yTrain)
tahmin4 = lr.predict(xTest)
print(tahmin4)

xList = x.iloc[:, [1, 3, 5]]
xList = np.array(xList, dtype=float)
model = sm.OLS(y, xList).fit()
column_to_drop = xTrain.columns[-1]
column_to_drop2 = xTest.columns[-1]
xTrain = xTrain.drop(columns=[column_to_drop])
xTest = xTest.drop(columns=[column_to_drop2])
lr.fit(xTrain, yTrain)
tahmin5 = lr.predict(xTest)
print(tahmin5)

xList = x.iloc[:, [1, 3]]
xList = np.array(xList, dtype=float)
model = sm.OLS(y, xList).fit()
column_to_drop = xTrain.columns[0]
column_to_drop2 = xTest.columns[0]
xTrain = xTrain.drop(columns=[column_to_drop])
xTest = xTest.drop(columns=[column_to_drop2])
lr.fit(xTrain, yTrain)
tahmin6 = lr.predict(xTest)
print(tahmin6)


xList = x.iloc[:, [3]]
xList = np.array(xList, dtype=float)
model = sm.OLS(y, xList).fit()
print(model.summary())

