import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

data = pd.read_excel('Datasets/Iris.xls')

x = data.iloc[:,1:4].values
y = data.iloc[:,4].values

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)

sc=StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)

#Logistic Regression
logr = LogisticRegression(random_state=0)
logr.fit(x_train,y_train)
y_pred = logr.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
print("Logistic Regression")
print(cm)

#KNN
knn = KNeighborsClassifier(n_neighbors=7, metric='nan_euclidean')
knn.fit(x_train,y_train)
y_pred = knn.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
print("KNN")
print(cm)

#SVC
svc = SVC(kernel='rbf')
svc.fit(x_train,y_train)
y_pred = svc.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
print('SVC')
print(cm)

#Naive Bayes
gnb = GaussianNB()
gnb.fit(x_train, y_train)
y_pred = gnb.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
print('GNB')
print(cm)

# Decision Tree Classifier
dtc = DecisionTreeClassifier(criterion = 'entropy')
dtc.fit(x_train,y_train)
y_pred = dtc.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
print('DTC')
print(cm)

#Random Forest Classifier
rfc = RandomForestClassifier(n_estimators=10, criterion = 'gini')
rfc.fit(x_train,y_train)
y_pred = rfc.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
print('RFC')
print(cm)

# 7. ROC , TPR, FPR değerleri
y_proba = rfc.predict_proba(X_test)
print(y_test)
print(y_proba[:,0])
fpr , tpr , thold = metrics.roc_curve(y_test,y_proba[:,0],pos_label='Iris-setosa')
print(fpr)
print(tpr)