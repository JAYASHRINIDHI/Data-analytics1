#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


acad=pd.read_excel('D:/jayashrinidhi/acad.xlsx')
acad


# In[3]:


obs=pd.pivot_table(acad[['g','sm']],index='g',columns='sm',aggfunc=len)
obs


# In[4]:


from scipy.stats import chi2_contingency


# In[5]:


chi2,p,dof,tbl=chi2_contingency(obs)


# In[6]:


chi2


# In[7]:


p


# In[8]:


dof


# In[9]:


tbl


# In[10]:


import scipy
from scipy.stats import chi2
from scipy.stats import poisson


# In[11]:


import pandas as pd
import numpy as np


# In[13]:


data=pd.read_excel('D:/jayashrinidhi/P_distribution.xlsx')
data


# In[18]:


observed_freq=data['Frequency']
observed_freq


# In[20]:


total_arrival = 600
total_time_period = 100
mu = total_arrival/total_time_period


# In[21]:


mu


# In[22]:


expected_freq=[]
for i in range(len(observed_freq)):
    e_freq=100*poisson.pmf(i,mu)
    expected_freq.append(e_freq)


# In[23]:


expected_freq


# In[24]:


expected_freq_round_off=[round(elem,2)for elem in expected_freq]
expected_freq_round_off


# In[27]:


df=pd.DataFrame(list(zip(observed_freq,expected_freq_round_off)),columns=['observed frequency','expected frequency'])
df


# In[30]:


obs_freq=[5,10,14,20,12,12,9,8,10]
expected_freq=[6.20,8.92,13.39,16.06,16.06,13.77,10.33,6.88,8.39]


# In[31]:


scipy.stats.chisquare(obs_freq,expected_freq)


# In[ ]:




