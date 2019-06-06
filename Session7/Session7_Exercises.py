#!/usr/bin/env python
# coding: utf-8

# # Python for Data Science, Level I
# ### *Session \#7*
# ---
# 
# ### Helpful shortcuts
# ---
# 
# **SHIFT** + **ENTER** ----> Execute Cell
# 
# **TAB** ----> See autocomplete options
# 
# **ESC** then **b** ----> Create Cell 
# 
# **ESC** then **dd** ----> Delete Cell
# 
# **\[python expression\]?** ---> Explanation of that Python expression
# 
# **ESC** then **m** then __ENTER__ ----> Switch to Markdown mode

# ## I. Calling APIs
# 
# ### Warm Ups
# 
# ---
# 
# **Import requests package:** `import requests`

# In[ ]:





# **GET request:** `response = requests.get('https://api.iextrading.com/1.0/stock/aapl/financials')`

# In[136]:


response = requests.get('https://api.iextrading.com/1.0/stock/aapl/financials')


# **Response as string:** `response.text`

# In[139]:


response.text


# **Response as dictionary:** `data = response.json()`

# In[ ]:





# **Accessing nested data:** `data['financials'][0]['totalCash']`

# In[ ]:





# **Dataframe from dictionaries:** `pd.DataFrame.from_dict(data['financials'])`

# In[ ]:





# ### Exercises
# ---

# **1.**

# In[ ]:





# **2.**

# In[ ]:





# **3.**

# In[ ]:





# ### Extra Credit
# ---

# In[ ]:





# ## II. Merging Data
# 
# ### Warm Ups
# ---

# **Appending to a DataFrame:** `df1.append(df2)`

# In[ ]:





# **Using concat on a list of DataFrames:** `pd.concat([df1, df2])`

# In[ ]:





# **Merging two DataFrames:** `pd.merge(df1, df2)`

# In[ ]:





# In[ ]:


two more kinds of joins


# In[ ]:





# ### Exercises
# ---

# In[ ]:





# ### Extra Credit
# ---

# In[ ]:





# In[91]:


import requests
import pandas as pd

symbols = ['aapl', 'gs']
symbols_string = ",".join(symbols)

# historical_url = "https://api.iextrading.com/1.0/stock/market/chart/3m?symbols=" + symbols_string
news_url = "https://api.iextrading.com/1.0/stock/market/batch?last=1&types=news&symbols=" + symbols_string
previous_url = "https://api.iextrading.com/1.0/stock/market/batch?types=previous&symbols=" + symbols_string
# Start with historical data
# overlay news headlines, join on symbol and date

# start with latest data for a bunch of stocks
# overlay latest headline
# overlay with sector performance
# overlay with company data

# sector_url = "https://api.iextrading.com/1.0/stock/market/sector-performance"
stats_url = "https://api.iextrading.com/1.0/stock/market/batch?symbols=aapl&types=stats"
previous_data = requests.get(previous_url).json()
financials_url = "https://api.iextrading.com/1.0/stock/aapl/financials"
historical_data = requests.get(historical_url).json()
news_data = requests.get(news_url).json()
sector_data = requests.get(sector_url).json()
# stats_data = requests.get(stats_url).json()
# financials_data = requests.get(financials_url).json()['financials']


# In[95]:


previous_df = pd.DataFrame.from_dict(previous_data)
previous_data
# json_normalize(previous_data[''])


# **Merge on same column:** `pd.merge(best_df, live_df, on="url")`
# 
# *Note: Input string can be a URL or a local file path*

# In[11]:


pd.merge(best_df, live_df, on="title")


# **Contatenate dataframes:** `pd.concat([live_df, best_df])`

# ## III. Running and Scheduling Scripts
# 
# ### Warm Ups
# ---

# In[140]:


get_ipython().system('jupyter nbconvert --to script *.ipynb')


# ### Exercises
# ---

# In[ ]:





# ### Extra Credit
# ---

# In[ ]:




