#!/usr/bin/env python
# coding: utf-8

# ## ASSIGNMENT-4 : DECISION TREE ALGORITHM

# ### For the given ‘Iris’ dataset, in this task, we shall create the Decision Tree classifier.

# ### Importing the necessary libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split


# ### Reading the Dataset 'Iris' and dropping 'ID' variable

# In[2]:


data = pd.read_csv('Iris.csv')
data = data.drop(['Id'],axis=1)


# ### Separating the Independent & Dependent variables

# In[3]:


x = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
#independent variable

y = data['Species']
#dependent variable


# ### Splitting the data into Train & Test dataset

# In[4]:


# splitting data into training and test set for independent attributes

(x_train, x_test, y_train, y_test) = train_test_split(x, y, train_size=0.7, random_state=1)
#'random_state'--> to ensure that there is always uniformity in splitting


# ### Decision Tree Classifier

# In[5]:


dt_model = DecisionTreeClassifier(criterion = 'gini' )


# In[6]:


dt_model.fit(x_train, y_train)


# ### Finding the Feature Importance

# In[7]:


print (pd.DataFrame(dt_model.feature_importances_, columns = ["Imp"], index = x_train.columns))


# In[8]:


clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)


# ### Plotting the Decision Tree

# In[9]:


fig = plt.figure(figsize=(10,6))
fig = tree.plot_tree(dt_model,feature_names=data.columns,filled='True')


# ### Prediction on Train & Test Data

# In[10]:


ytrain_predict = dt_model.predict(x_train)
ytest_predict = dt_model.predict(x_test)


# ### Creating Classification Report

# In[11]:


from sklearn.metrics import classification_report,confusion_matrix


# ### Classification Report for Train Data

# In[12]:


print(classification_report(y_train, ytrain_predict))


# ### Classification Report for Test Data

# In[13]:


print(classification_report(y_test, ytest_predict))


# ### Accuracy Score for Train Data

# In[14]:


dt_model.score(x_train,y_train)


# ### Accuracy Score for Test Data

# In[15]:


dt_model.score(x_test,y_test)

