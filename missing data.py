#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df=pd.read_csv("D:\jayashrinidhi\emp.csv")
print(df.head())


# In[2]:


print(df.dtypes)
print(df.describe)


# In[3]:


print('Salary')
print(df['Salary'].head(10))


# In[4]:


print(df['Gender'].head(10))


# In[5]:


missing_value_formats=["n.a","?","NA","n/a","na","--"]
df=pd.read_csv("D:\jayashrinidhi\emp.csv",na_values=missing_value_formats)
print(df['Gender'].head(10))


# In[22]:


import pandas as pd
missing_value_formats=["n.a","?","NA","n/a","na","--"]
df=pd.read_csv("D:\jayashrinidhi\emp.csv",na_values=missing_value_formats)

def make_int(i):
    try:
        return int(i)
    except:
        return pd.np.nan
    
df["Salary"]=df["Salary"].map(make_int)
print(df["Salary"].head())


# In[21]:


print(df["Gender"].isnull().head(10))
print(df["Gender"].notnull().head(10))


# In[8]:


null_filter=df["Gender"].notnull()
print(df[null_filter].head())


# In[9]:


print(df.isnull().values.any())


# In[10]:


print(df.isnull().sum())


# In[39]:


new_df=df.dropna(axis=0)

print(new_df.isnull().values.any())


# In[41]:


new_df=df.dropna(axis=0,how="any")
new_df


# In[44]:


new_df=df.dropna(axis=0,how="all")
new_df


# In[46]:


new_df=df.dropna(axis=1,how="any")
new_df


# In[47]:


new_df=df.dropna(axis=1,how="all")
new_df


# In[34]:


df["Salary"].fillna(0)


# In[14]:


df["Gender"].fillna("No Gender")


# In[15]:


df["Salary"].fillna(method='pad')


# In[16]:


df["Salary"].fillna(method="bfill")


# In[23]:


df["Salary"].fillna(df["Salary"].median())


# In[24]:


df["Salary"].fillna(int(df["Salary"].mean()))


# In[28]:


df["Salary"].replace(to_replace=np.nan,value=0)


# In[30]:


df["Salary"].interpolate(method="linear",direction="forward")


# In[ ]:




