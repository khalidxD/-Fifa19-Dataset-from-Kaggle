#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv('/Users/immortal/Desktop/DataScience/DataScienceCourse/Analysis/data/imdb_movies.csv')
df


# In[38]:


df.info()


# In[32]:


df.columns # We find That there is spaces in columns so we want to replace it.
    


# In[36]:


df.rename(columns=lambda s: s.replace(" ", ""),inplace=True) #Removing  Columns Spaces ..
df.columns # DONE!


# In[37]:


df # The new data frame 


# In[42]:


#What is the top five directors that has more rating in his films ?
df.groupby(['DIRECTOR'])['RATING'].mean().sort_values(ascending=False).iloc[0:5] # This is not mean he has the better grosscollection !


# In[77]:


#How many films the top 5 directors made ?
df[(df['DIRECTOR']=='Francis Ford Coppola')|(df['DIRECTOR']=='Frank Darabont')|(df['DIRECTOR']=='Peter Jackson')|(df['DIRECTOR']=='Jon Watts')|(df['DIRECTOR']=='T.J. Gnanavel')]['DIRECTOR'].value_counts()


# In[67]:


df['GROSSCOLLECTION'] = df['GROSSCOLLECTION'].replace(np.nan, '$0.0M') #Fill the Nan values to $0.0M
df


# In[72]:


#Convert the GROSSCOLLECTION to int for better analysis

def coverttoint(x):
    return float(x['GROSSCOLLECTION'].split('$')[1].split('M')[0])
df['GROSSCOLLECTION']=df.apply(coverttoint , axis=1)
df


# In[86]:


# how much GROSSCOLLECTION that top five directors make ?
df[(df['DIRECTOR']=='Francis Ford Coppola')|(df['DIRECTOR']=='Frank Darabont')|(df['DIRECTOR']=='Peter Jackson')|
   (df['DIRECTOR']=='Jon Watts')|(df['DIRECTOR']=='T.J. Gnanavel')].groupby(['DIRECTOR'])['GROSSCOLLECTION'].sum().sort_values(ascending=False)


# In[73]:


#What is the most grossCollection of directors made?
df.groupby(['DIRECTOR'])['GROSSCOLLECTION'].sum().sort_values(ascending=False)


# In[93]:


#Which the movie has more votes ?
df.groupby(['moviename'])['votes'].sum().sort_values(ascending=False)


# In[94]:


df.corr() # There is a corr between raiting and ranking of movie


# In[ ]:




