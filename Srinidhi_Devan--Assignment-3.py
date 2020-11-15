#!/usr/bin/env python
# coding: utf-8

# ## ASSIGNMENT-3

# ### Create a HeatMap Plot for the following plot with Seaborn:
#  
# 1. Download the DataSet from the GitHub link: Click to Download -> https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv to solve this problem.
# The dataset has 5 columns namely: country,year,pop,continent,lifeExp and gdpPercap
#  
# 2. Create a pivot table dataframe with year along x-axes, country along y-axes and lifeExp filled within cells.
#  
# 3. Plot a heatmap using seaborn for the pivot table that was just created.
# 

# ### IMPORTING THE NECESSARY LIBRARIES

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import savefig


# ### Step-1: READING THE DATASET

# In[2]:


data = pd.read_csv('FiveYearData.csv')


# ### Since we require only three variables: 'country', 'year' and 'lifeExp', we can drop the rest from the data

# In[3]:


data_1 = data.drop(['pop','continent','gdpPercap'],axis=1)


# ### Step-2: CREATING a PIVOT TABLE WITH 'year' ALONG x-AXIS, 'country' ALONG y-AXIS & 'lifeExp' FILLED WITHIN CELLS

# In[4]:


data_table = pd.pivot_table(data_1,index=['country'],columns=['year'],values=['lifeExp'])
data_table


# ### Step-3: HEAT MAP OF THE PIVOT TABLE

# In[5]:


fig, ax = plt.subplots(figsize=(20,70))  
heatmap = sns.heatmap(data_table)
figure = heatmap.get_figure()   
figure.savefig('Srinidhi_Devan--Assignment-3.png', dpi=400)

