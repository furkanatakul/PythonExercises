#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data = pd.read_csv("Datasets/veriler.csv")


# In[5]:


from sklearn import preprocessing
le = preprocessing.LabelEncoder()
cinsiyet = data.iloc[:,-1].values
cinsiyet = le.fit_transform(cinsiyet).reshape(-1, 1)


# In[8]:


ohe = preprocessing.OneHotEncoder()
cinsiyet = ohe.fit_transform(cinsiyet).toarray()


# In[9]:


cinsiyet


# In[10]:


cinsiyet = pd.DataFrame(data=cinsiyet[:,0],columns=["cinsiyet"],index=range(len(cinsiyet)))


# In[11]:


cinsiyet


# In[14]:


ulke = data.iloc[:,0].values
yas = data.iloc[:,1:4].values
ulke = le.fit_transform(ulke).reshape(-1, 1)
ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
sonuc = pd.DataFrame(data=ulke,columns=["fr","tr","us"])
yas =pd.DataFrame(data=yas,index=range(22),columns=["boy","kilo","yas"])
s = pd.concat([sonuc,yas],axis=1)


# In[15]:


dataFrame2 = pd.concat([s,cinsiyet],axis=1)


# In[16]:


dataFrame2


# In[21]:


from sklearn.model_selection import train_test_split
y = dataFrame2["cinsiyet"].values
x = dataFrame2.drop("cinsiyet", axis = 1).values
xTrain,xTest,yTrain,yTest = train_test_split(x,y,test_size=0.33)


# In[22]:


from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(xTrain,yTrain)
tahmin = lr.predict(xTest)


# In[23]:


tahmin


# In[25]:


yTest


# In[38]:


boy = dataFrame2.iloc[:,3]
boy


# In[39]:


veri = dataFrame2.drop(["boy"],axis=1)


# In[40]:


veri


# In[56]:


xTrain,xTest,yTrain,yTest = train_test_split(veri,boy,test_size=0.33)


# In[54]:


lr2 = LinearRegression()
lr2.fit(xTrain,yTrain)
tahmin2 = lr2.predict(xTest)
tahmin2


# In[63]:


yTest


# In[71]:


import statsmodels.api as sm

x = np.append(arr = np.ones((22,1)).astype(int), values=veri.to_numpy(), axis=1)


# In[72]:


x


# In[73]:


xList = veri.iloc[:,[0,1,2,3,4,5]]


# In[76]:


xList= np.array(xList,dtype=float)


# In[77]:


model = sm.OLS(boy,xList).fit()


# In[78]:


model.summary()


# In[79]:


xList = veri.iloc[:,[0,1,2,3,5]]
xList= np.array(xList,dtype=float)
model = sm.OLS(boy,xList).fit()
model.summary()


# In[80]:


xList = veri.iloc[:,[0,1,2,3]]
xList= np.array(xList,dtype=float)
model = sm.OLS(boy,xList).fit()
model.summary()


# In[ ]:




