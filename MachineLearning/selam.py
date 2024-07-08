import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from sklearn.metrics import r2_score
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

dataFrame = pd.read_csv("Datasets/maaslar_yeni.csv")

dataFrame.drop(["Calisan ID"], axis=1, inplace=True)

dataFrame.drop(["unvan"], axis=1, inplace=True)
print(dataFrame.corr())

y = dataFrame.loc[:,"maas"].values
x = dataFrame.drop(["maas"], axis=1).values
# xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.33)
lr = LinearRegression()
lr2 = LinearRegression()
pr = PolynomialFeatures(degree= 4)

X = pd.DataFrame(x)
xList = X.iloc[:, [0,2]].values

x_poly = pr.fit_transform(xList)

lr2.fit(x_poly, y)

predictions = lr2.predict(x_poly)
lr.fit(xList, y)

tahmin = lr.predict(xList)

model = sm.OLS(tahmin, xList).fit()

model2 = sm.OLS(predictions, xList).fit()

sc1 = StandardScaler()
xOlcekli = sc1.fit_transform(xList)
sc2 = StandardScaler()
yOlcekli = sc2.fit_transform(y.reshape(-1,1))

sr = SVR(kernel="rbf",degree=4)
sr.fit(xOlcekli,yOlcekli)

tahmin3 = sr.predict(xOlcekli)
model3 = sm.OLS(tahmin3, xOlcekli).fit()


dtr = DecisionTreeRegressor(random_state=0)
dtr.fit(xList,y)
tahmin4 = dtr.predict(xList)
model4 = sm.OLS(tahmin4, xList).fit()

rfr = RandomForestRegressor(random_state=0, n_estimators=10)
rfr.fit(xList,y)
tahmin5 = rfr.predict(xList)
model5 = sm.OLS(tahmin5, xList).fit()
print(model.summary())
print(model2.summary())
print(model3.summary())
print(model4.summary())
print(model5.summary())

from sklearn.preprocessing import PolynomialFeatures
print(r2_score(y,tahmin))
pr = PolynomialFeatures(degree=4)
xPolyTrain = pr.fit_transform(x)
xPolyTest = pr.transform(x)

lr2 = LinearRegression()
lr2.fit(xPolyTrain, x)

# Tahminleri yap
poly_predictions = lr2.predict(xPolyTest)

print("Eğitim Verileri:\n", y)
print("\nPolinomal Tahminler:\n", poly_predictions)

