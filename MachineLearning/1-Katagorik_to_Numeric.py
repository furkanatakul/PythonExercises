#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


pd.read_csv("Datasets/veriler.csv")


# In[3]:


dataFrame1 = pd.read_csv("Datasets/eksikveriler.csv")


# In[4]:


from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")


# In[5]:


yas = dataFrame1.iloc[:,1:4].values


# In[6]:


yas


# In[7]:


imputer = imputer.fit(yas[:,1:4])
yas[:,1:4]  = imputer.transform(yas[:,1:4])
yas


# In[8]:


#dataFrame1.loc[:,"yas"].mean()


# In[9]:


#dataFrame1.loc[dataFrame1.yas.isnull(),"yas"] = dataFrame1.loc[:,"yas"].mean()


# In[10]:


dataFrame1


# In[11]:


ulke = dataFrame1.loc[:,"ulke"]


# In[12]:


from sklearn import preprocessing


# In[13]:


le = preprocessing.LabelEncoder()


# In[14]:


ulke = le.fit_transform(ulke).reshape(-1, 1)


# In[15]:


ulke


# In[16]:


ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()


# In[17]:


ulke


# In[18]:


sonuc = pd.DataFrame(data=ulke,columns=["fr","tr","us"])


# In[19]:


sonuc


# In[22]:


yas =pd.DataFrame(data=yas,index=range(22),columns=["boy","kilo","yas"])
s = pd.concat([sonuc,yas],axis=1)


# In[26]:


cinsiyet = dataFrame1.loc[:,"cinsiyet"]
dataFrame2 = pd.concat([s,cinsiyet],axis=1)


# In[24]:


from sklearn.model_selection import train_test_split


# In[27]:


y = dataFrame2["cinsiyet"].values
x = dataFrame2.drop("cinsiyet", axis = 1).values


# In[30]:


xTrain,xtest,yTrain,yTest = train_test_split(x,y,test_size=0.33)


# In[31]:


from sklearn.preprocessing import StandardScaler


# In[35]:


sc = StandardScaler()
XTrain = sc.fit_transform(xTrain)
XTest = sc.fit_transform(xtest)
XTrain


# In[ ]:




