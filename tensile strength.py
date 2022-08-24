#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
from sklearn import linear_model
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error


# In[6]:


data=pd.read_excel("D:/jayashrinidhi/HARDNESS.xls")


# In[7]:


data


# In[8]:


from sklearn.model_selection import train_test_split


# In[13]:


x=data["Hardness"].values.reshape(-1,1)
y=data["Tensile strength"].values.reshape(-1,1)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=88)


# In[14]:


x_train.shape,x_test.shape,y_train.shape,y_test.shape


# In[15]:


len(x_train)


# In[16]:


len(x_test)


# In[17]:


x_train


# In[18]:


from sklearn.linear_model import LinearRegression
reg=LinearRegression()


# In[20]:


reg.fit(x_train,y_train)


# In[21]:


reg.intercept_


# In[22]:


reg.coef_


# In[23]:


y_predict=reg.predict(x_test)


# In[24]:


y_predict


# In[25]:


mean_squared_error(y_test,y_predict)


# In[26]:


reg.score(x_test,y_test)


# In[28]:


mean_squared_error(y_test,y_predict)


# In[29]:


reg.score(x_test,y_test)


# In[30]:


reg.score(x_train,y_train)


# In[ ]:




