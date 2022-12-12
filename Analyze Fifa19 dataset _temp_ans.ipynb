#!/usr/bin/env python
# coding: utf-8

# # Fifa19 Exercise - Solutions
# 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [Fifa19 Dataset](https://www.kaggle.com/winterbreeze/fifa19eda) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# #### Read fifa_eda.csv 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv('/Users/immortal/Desktop/DataScience/DataScienceCourse/Analysis/data/fifa_eda.csv')
df


# In[29]:


df.info()


# ### New Part Visualiztion Questions

# #### Draw the outliers of players value

# In[3]:


sns.set(rc={'figure.figsize':(25,5)})

sns.boxenplot(df['Value']) # It seems like the outliers between 90000 to 120000


# #### find the average wage for each Nationality and draw the outliers in value for the top 5 nationality

# In[56]:


df.groupby(['Nationality'])['Wage'].mean().sort_values(ascending=False).head() # The top average wage Nationality


# In[75]:


df[(df['Nationality']=='Dominican Republic')|(df['Nationality']=='United Arab Emirates')|(df['Nationality']=='Gabon')|(df['Nationality']=='Armenia')|(df['Nationality']=='Croatia')] # data frame for the top 5


# In[82]:


sns.set(rc={'figure.figsize':(10,5)})
sns.boxplot(data=df[(df['Nationality']=='Dominican Republic')|(df['Nationality']=='United Arab Emirates')|(df['Nationality']=='Gabon')|(df['Nationality']=='Armenia')|(df['Nationality']=='Croatia')],x='Nationality',y='Wage')


# #### Draw the distripution of players Height

# In[4]:


sns.displot(df['Height'],kind="kde")


# #### What are the top 10 clubs in the wage and visualize the results ?

# In[140]:


df.groupby(['Club'])['Wage'].sum().sort_values(ascending=False).iloc[0:10]


# In[143]:


df.groupby(['Club'])['Wage'].sum().sort_values(ascending=False).iloc[0:10].index
    


# In[11]:


top_df=df[(df['Club']=='Real Madrid')|(df['Club']=='FC Barcelona')|(df['Club']=='Manchester City')|(df['Club']=='Manchester United')|(df['Club']=='Juventus')
  |(df['Club']=='Chelsea')|(df['Club']=='Liverpool')|(df['Club']=='Tottenham Hotspur')|(df['Club']=='Arsenal')|(df['Club']=='FC Bayern München') ]

top_df


# In[12]:


sns.barplot(x='Club' , y='Wage' , data=top_df , estimator=sum )


# #### is there any outlier in the Age find it with 1- visualization 2-  with pandas ?

# In[15]:


sns.boxenplot(df['Age']) # from the graph the outlier begins from 40 to 45


# In[16]:


IQR=df['Age'].quantile(0.75)-df['Age'].quantile(0.25)
IQR


# In[17]:


upper_limit=df['Age'].quantile(0.75)+(1.5*IQR)
lower_limit=df['Age'].quantile(0.25)-(1.5*IQR)
upper_limit,lower_limit


# In[33]:


df_clean=df[(df['Age']<=upper_limit)|(df['Age']<=lower_limit)] # New data frame with remove all the outliers
df_clean


# In[34]:


sns.boxenplot(df_clean['Age']) #New grapgh without outliers


# In[45]:





# In[ ]:





# In[ ]:





# #### Is there a correlation between Value and Overall and viusalize the results with two graphs?**

# In[53]:


df[['Wage','Value' ,'Overall','Height']].corr() # There is a correlation between wage and value and overall


# In[50]:


sns.barplot(x='Overall' , y='Value', data=df)


# In[ ]:





# #### what are the ratio of the Preferred Foot and visualize with a graph ?

# In[62]:


df['Preferred Foot'].value_counts()


# In[66]:


sns.displot(x='Preferred Foot', data=df)


# #### what are the top 10 average overall clubs and visualize with a graph ?

# In[77]:


df.groupby('Club')['Overall'].mean().sort_values(ascending=False).iloc[0:10]


# In[81]:


top2_df=df[(df['Club']=='Juventus')|(df['Club']=='Napoli')|(df['Club']=='Inter')|(df['Club']=='Real Madrid')|(df['Club']=='Milan')
  |(df['Club']=='FC Barcelona')|(df['Club']=='Paris Saint-Germain')|(df['Club']=='Roma')|(df['Club']=='Manchester United')|(df['Club']=='FC Bayern München') ]
top2_df # The new data frame for top overall clubs


# In[82]:


sns.barplot(x='Club', y='Overall' , data=top2_df)


# In[ ]:





# In[83]:


df


# **What are the top 5 most common nationality and visualize them with a graph?**

# In[85]:


df['Nationality'].value_counts().head()


# In[88]:


new_df3=df[(df['Nationality']=='England')|(df['Nationality']=='Germany')|(df['Nationality']=='Spain')|(df['Nationality']=='Argentina')|(df['Nationality']=='France')]
new_df3 #New data frame for the 5 most common nationality


# In[89]:


sns.displot(x='Nationality', data=new_df3)


# # Great Job!
