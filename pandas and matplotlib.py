#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[65]:


#load the dataset
data1=pd.read_csv('D:\jayashrinidhi\gapminder_full.csv')


# In[66]:


#display dataset
data1


# In[45]:


#display the head of the dataset(shows only 5 rows)
data1.head()


# In[46]:


#get number of rows and columns
print(data1.shape)


# In[47]:


#get columns names
data1.columns


# In[48]:


#get the dtype of each column
data1.dtypes


# In[49]:


#get more information about data
data1.info()


# In[50]:


#looking at columns,rows and cells
#get the countrycolumn and save it in a new variable
country_data=data1['country']
#show the first 5 observation
country_data.head()


# In[51]:


country_data.tail()


# In[52]:


subset=data1[['country','continent','year']]
subset.head()


# In[53]:


subset.tail()


# In[54]:


#analtics summary of the dataset
data1.describe(include='all')


# In[55]:


data1.hist(figsize=(10,5))


# In[56]:


sns.boxplot(x="year",y="life_exp",data=data1)


# In[57]:


data1=data1.drop(['year'],axis='columns')
data1.head(5)


# In[58]:


data1=data1.rename(columns={"country": "countries"})
data1.head(5)


# In[68]:


duplicate_rows=data1[data1.duplicated()]
print('number of duplicate rows:',duplicate_rows.shape)


# In[69]:


data1.count()


# In[ ]:




