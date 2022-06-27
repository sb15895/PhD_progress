#!/usr/bin/env python
# coding: utf-8

# # Gantt chart 

# In[1]:


from IPython.display import Image, display
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff

# df = pd.DataFrame([
#     dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
#     dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
#     dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')
# ])

# fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task")
# fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
# fig.show()


df = [dict(Task="Third Year Review", Start='2023-12-01', Finish='2023-11-01'),
      dict(Task="Second Year Review", Start='2021-12-01', Finish='2021-11-01'),
      dict(Task="First Year Review", Start='2021-2-01', Finish='2021-1-01')]

fig = ff.create_gantt(df)
fig.show()



# # Plots 
# https://plotly.com/python/gantt/
# 
# ## 1st May 
# 
# Blah blah 
# 
# ## 22 June 
# Jupyter book 
# https://sphinx-inline-tabs.readthedocs.io/en/latest/
# https://sphinx-book-theme.readthedocs.io/en/stable/customize/index.html
# 
# 
# 

# In[ ]:





# In[ ]:





# In[ ]:




