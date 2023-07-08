#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[4]:


#'r' used for ignoring underscore or dash and to avoid encoding error, use unicode_escape
df = pd.read_csv(r'D:\Data_Science Project\Python_Diwali_Sales_Analysis-main\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv', encoding='unicode_escape')


# In[5]:


df.shape


# In[6]:


df.head() # by default 5 and for more row view enter value in ()


# In[7]:


df.info() # gives full information


# In[8]:


# Drop unrelated / blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)  # axis means delete full column and inplace for save everything


# In[9]:


# check full null values
pd.isnull(df).sum()   # sum() gives count of null value
df.shape


# In[10]:


# Drop null value
df.dropna(inplace=True)
df.shape


# In[11]:


# Change data type
df['Amount'] = df['Amount'].astype('int')


# In[12]:


# Checking the data type changed or not
df['Amount'].dtypes


# In[13]:


# Checking columns
df.columns


# In[14]:


# Rename columns name
df.rename(columns={'Marital_Status':'Shaadi'})


# In[15]:


# describe() method returns description of the data in the datafrrame (i.e Count, mean, std, etc)
df.describe()


# In[16]:


# Use describe() for specific columns
df[['Age', 'Orders', 'Amount']].describe()


# # Exploitry Data Analysis (EDA)

# # Gender

# In[17]:


df.columns


# In[19]:


ax = sns.countplot(x = 'Gender', data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[22]:


# Checking who purchase the product more either men or women
sales_gen = df.groupby(['Gender'], as_index=False) ['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x = 'Gender', y = 'Amount', data = sales_gen)


# From above graphs we can see that most of the buyers are females as compare to the men

# # Age

# In[23]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[24]:


# Total amount Vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False) ['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x = 'Age Group', y = 'Amount', data = sales_age)


# From above graph we can see that most of the buyers are of age group between 26-35 yrs female

# # State

# In[32]:


# Total numbers of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False) ['Orders'].sum().sort_values(by='Orders', ascending=False). head(10)
sns.set(rc={'figure.figsize':(18,5)})

sns.barplot(x = 'State', y = 'Orders', data = sales_state)


# In[33]:


# total amount/ sales from top 10 states

sales_state = df.groupby(['State'], as_index=False) ['Amount'].sum().sort_values(by='Amount', ascending=False). head(10)
sns.set(rc={'figure.figsize':(18,5)})

sns.barplot(x = 'State', y = 'Amount', data = sales_state)


# From above graphs we can see that most of the orders are from Uttar Pradesh, Maharastra, Karnataka respectively

# # Marital Status

# In[47]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(5,5)})

for bars in ax.containers:
    ax.bar_label(bars)


# In[51]:


sales_marital = df.groupby(['Marital_Status', 'Gender'], as_index=False) ['Amount'].sum().sort_values(by='Amount', ascending=False). head(10)
sns.set(rc={'figure.figsize':(7,5)})

sns.barplot(data = sales_marital, x = 'Marital_Status', y = 'Amount', hue = 'Gender')


# From above graphs we can see that most of the buyers are married (Women) and they have a high purchasing power

# # Occupation

# In[52]:


sns.set(rc={'figure.figsize':(20,5)})

ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[62]:


occupation = df.groupby(['Occupation'], as_index=False) ['Amount'].sum().sort_values(by='Amount', ascending=False). head(10)
sns.set(rc={'figure.figsize':(20,5)})

sns.barplot(data = occupation, x = 'Occupation', y = 'Amount')


# From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation Sector

# # Product Category

# In[64]:


sns.set(rc={'figure.figsize':(25,5)})

ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[65]:


product_status = df.groupby(['Product_Category'], as_index=False) ['Amount'].sum().sort_values(by='Amount', ascending=False). head(10)
sns.set(rc={'figure.figsize':(20,5)})

sns.barplot(data = product_status, x = 'Product_Category', y = 'Amount')


# From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category

# In[68]:


# Checking the maximum order from product id

product_id_status = df.groupby(['Product_ID'], as_index=False) ['Orders'].sum().sort_values(by='Orders', ascending=False). head(10)
sns.set(rc={'figure.figsize':(20,5)})

sns.barplot(data = product_id_status, x = 'Product_ID', y = 'Orders')


# # Conclusion

# * Married women age group 26-35 yrs from Up, Maharastra and Karnatka working in IT, Healthcare and Aviation sectors are more likely to buy products from Food, Clothing and Electronics Gadgets*

# In[ ]:




