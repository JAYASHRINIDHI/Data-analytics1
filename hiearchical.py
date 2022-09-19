#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist


# In[4]:


data=pd.read_excel("D:/jayashrinidhi/hierarchical_clustering.xlsx")
data


# In[7]:


x=data["Variable 1"]
y=data["Variable 2"]
n=range(1,8)

fig,ax=plt.subplots()
ax.scatter(x,y,marker='*',c="red",alpha=0.5)
plt.grid()
plt.xlabel("Variable 1")
plt.ylabel("Variable 2")
for i,txt in enumerate(n):
    ax.annotate(txt,(x[i],y[i]))


# In[12]:


from scipy.cluster.hierarchy import dendrogram,linkage

linked=linkage(data,"single")

labelList=range(1,8)

plt.figure(figsize=(10,7))
dendrogram(linked,
         orientation="top",
         labels=labelList,
         distance_sort="descending",
         show_leaf_counts=True)
plt.axhline(y=2.5)
plt.show()


# In[14]:


import sklearn
from sklearn.cluster import AgglomerativeClustering

k=3
Hclustering=AgglomerativeClustering(n_clusters=k,affinity="euclidean",linkage="single")
Hclustering.fit(data)


# In[15]:


Hclustering.fit_predict(data)


# In[16]:


print(Hclustering.labels_)


# In[18]:


x=data["Variable 1"]
y=data["Variable 2"]
n=range(1,8)

fig,ax=plt.subplots()
ax.scatter(x,y,c=Hclustering.labels_,cmap="rainbow")
plt.grid()
plt.xlabel("Variable 1")
plt.ylabel("Variable 2")
for i,txt in enumerate(n):
    ax.annotate(txt,(x[i],y[i]))


# In[ ]:




