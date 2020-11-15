#!/usr/bin/env python
# coding: utf-8

# ## ASSIGNMENT-2

# ## Problem Statement:
# ### 1. Create a single .xlsx file with 10 sheets inside filled with dummy data.
# ### 2. Read the .xlsx file using pandas
# ### 3. Export every single sheet of the .xlsx file as a .csv file. (The Output should produce 10 .csv files that contains values of each sheet of .xlsx file respectively)

# ### IMPORTING THE NECESSARY LIBRARIES

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ### INSTALLING PACKAGES TO LOAD 'xlsx' FILE

# In[2]:


get_ipython().system('pip install xlrd')
get_ipython().system('pip install openpyxl')


# 

# ### Task-1: TO CREATE A SINGLE '.xlsx' FILE WITH 10 SHEETS FILLED WITH DUMMY DATA

# 

# ### Task-2 (A): TO IMPORT THE ENTIRE 'xlsx' WORKBOOK/FILE CONTAINING MANY SHEETS

# In[3]:


excelfile = pd.ExcelFile('Assignment-2--Dummy_Data.xlsx')


# ### Task-2 (B): TO IMPORT ONLY A PARTICULAR SHEET OF THE WORKBOOK

# #### DATA-1: Sold_Price

# In[4]:


sold_price_data  = excelfile.parse('Sold_Price')
sold_price_data


# #### DATA-2: Sales_Profit

# In[5]:


sales_profit_data  = excelfile.parse('Sales_Profit')
sales_profit_data


# #### DATA-3: Sales_Cat

# In[6]:


sales_cat_data = excelfile.parse('Sales_Cat')
sales_cat_data


# #### DATA-4: Profit_Cat

# In[7]:


profit_cat_data = excelfile.parse('Profit_Cat')
profit_cat_data


# #### DATA-5: Gender_Salary

# In[8]:


gender_salary_data = excelfile.parse('Gender_Salary')
gender_salary_data


# #### DATA-6: Disc_Seg

# In[9]:


disc_seg_data = excelfile.parse('Disc_Seg')
disc_seg_data


# #### DATA-7: Calls_State

# In[10]:


calls_states_data = excelfile.parse('Calls_State')
calls_states_data


# #### DATA-8: GPA_Student

# In[11]:


gpa_student_data = excelfile.parse('GPA_Student')
gpa_student_data


# #### DATA-9: Products_Cust

# In[12]:


products_cust_data = excelfile.parse('Products_Cust')
products_cust_data


# #### DATA-10: Stock_Price

# In[13]:


stock_price_data = excelfile.parse('Stock_Price')
stock_price_data


# 

# ### Task-3: EXPORTING THE 'xlsx' FILES AS 'csv' FILES

# #### COMMA SEPARATED VALUES (CSV): * The values are separated by commas & each line in the file as a row. It is in the tabular form.

# #### DATA-1: Sold_Price

# In[14]:


sold_price_data.to_csv('sold_price_data_output.csv',sep=',')


# #### DATA-2: Sales_Profit

# In[15]:


sales_profit_data.to_csv('sales_profit_data_output.csv',sep=',')


# #### DATA-3: Sales_Cat

# In[16]:


sales_cat_data.to_csv('sales_cat_data_output.csv',sep=',')


# #### DATA-4: Profit_Cat

# In[17]:


profit_cat_data.to_csv('profit_cat_data_output.csv',sep=',')


# #### DATA-5: Gender_Salary

# In[18]:


gender_salary_data.to_csv('gender_salary_data_output.csv',sep=',')


# #### DATA-6: Disc_Seg

# In[19]:


disc_seg_data.to_csv('disc_seg_data_output.csv',sep=',')


# #### DATA-7: Calls_States

# In[20]:


calls_states_data.to_csv('calls_states_data_output.csv',sep=',')


# #### DATA-8: GPA_Student

# In[21]:


gpa_student_data.to_csv('gpa_student_data_output.csv',sep=',')


# #### DATA-9: Products_Cust

# In[22]:


products_cust_data.to_csv('products_cust_data_output.csv',sep=',')


# #### DATA-10: Stock_Price

# In[23]:


stock_price_data.to_csv('stock_price_data_output.csv',sep=',')


# 

# ## THANK YOU
