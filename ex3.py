#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data={'state':['ohio','ohio','ohio','nevada','nevada','nevada'],'year':[2000,2001,2002,2001,2002,2003],'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}
frame=pd.DataFrame(data)
frame


# In[3]:


frame.head()


# In[4]:


frame2=pd.DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three','four','five','six'])
frame2


# In[5]:


frame2.columns


# In[6]:


frame2['state']


# In[7]:


frame2.year


# In[8]:


frame2.loc['three']


# In[10]:


frame2['dept']=16.5
frame2


# In[11]:


frame2['dept']=np.arange(6.)
frame2


# In[13]:


val=pd.Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame2['debt']=val
frame2


# In[14]:


frame2['eastern']=frame2.state=='ohio'
frame2


# In[15]:


del frame2['eastern']
frame2.columns


# In[16]:


pop={'nevada':{2001:2.4,2002:2.9},'ohio':{2000:1.5,2001:1.7,2002:3.6}}
frame3=pd.DataFrame(pop)
frame3


# In[18]:


frame3.T


# In[20]:


pd.DataFrame(pop,index=[2001,2002,2003])


# In[21]:


frame3.index.name='year';frame.columns.name='state'
frame3


# In[22]:


frame3.values


# In[23]:


frame.values


# In[ ]:




