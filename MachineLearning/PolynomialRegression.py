#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


# In[6]:


dataFrame = pd.read_csv("Datasets/maaslar.csv")
dataFrame


# In[29]:


x = dataFrame.iloc[:,1]
y = dataFrame.iloc[:,-1]
X = x.values.reshape(-1,1)
Y = y.values.reshape(-1,1)


# In[30]:


lr  = LinearRegression()
lr.fit(X,Y)


# In[31]:


plt.scatter(X,Y)
plt.plot(X,lr.predict(X),"r")


# In[49]:


from sklearn.preprocessing import PolynomialFeatures
pr = PolynomialFeatures(degree= 20)
xPoly = pr.fit_transform(X)


# In[50]:


lr2 = LinearRegression()
lr2.fit(xPoly,Y)


# In[51]:


plt.scatter(X,Y)
plt.plot(X,lr2.predict(xPoly),"r")


# In[48]:


print(lr2.predict(xPoly))


# In[ ]:




