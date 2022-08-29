#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt


# In[3]:


df1=pd.read_excel("D:/jayashrinidhi/TRUCKING.xlsx")
df1


# In[5]:


import matplotlib.pyplot as plt
plt.scatter(df1["x1"],df1["travel_time"],color="green")
plt.ylabel("travel time")
plt.title("simple linear regression with miles travelled")


# In[6]:


plt.scatter(df1["n_of_deliveries"],df1["travel_time"],color="red")
plt.ylabel("travel time")
plt.title("simple linear regression with number of deliveries")


# In[10]:


import matplotlib.pyplot as plt
plt.figure()
plt.scatter(df1["x1"],df1["travel_time"],color="green")
plt.scatter(df1["n_of_deliveries"],df1["travel_time"],color="red")
plt.ylabel("travel time")
plt.title("Multiple regression")
plt.xlabel("x1 in green and x2 in red")


# In[12]:


Reg1=ols(formula="travel_time~ x1",data=df1)
fit1=Reg1.fit()
print(fit1.summary())


# In[15]:


from statsmodels.formula.api import ols
model=ols("travel_time~ x1 +n_of_deliveries",data=df1).fit()
model.summary()


# In[18]:


print(anova_lm(fit1))


# In[19]:


anova_table=anova_lm(model,type=1)
anova_table


# In[ ]:




