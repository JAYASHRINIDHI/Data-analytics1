#!/usr/bin/env python
# coding: utf-8

# In[2]:


from scipy.optimize import minimize
import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


tbl=pd.read_excel("D:/jayashrinidhi/regr.xlsx")
tbl


# In[5]:


import statsmodels.api as sm
x=tbl["TV Ads"]
y=tbl["car Sold"]
x2=sm.add_constant(x)
mod1=sm.OLS(y,x2)
mod2=mod1.fit()
print(mod2.summary())


# In[7]:


e=mod2.resid
e


# In[8]:


np.std(e)


# In[11]:


def lik(parameters):
    m=parameters[0]
    b=parameters[1]
    sigma=parameters[2]
    for i in np.arange(0,len(x)):
        y_exp=m*x+b
    L=(len(x)/2*np.log(2*np.pi)+len(x)/2*np.log(sigma**2)+1/(2*sigma**2)*sum((y-y_exp)**2))
    return L


# In[14]:


lik_model=minimize(lik,np.array([5,5,5]),method="Nelder-Mead")
lik_model.x


# In[16]:


plt.scatter(x,y)
plt.plot(x,lik_model['x'][0]*x+lik_model["x"][1])
plt.show()


# In[ ]:





# In[ ]:




