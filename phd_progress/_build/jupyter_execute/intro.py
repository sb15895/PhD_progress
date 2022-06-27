#!/usr/bin/env python
# coding: utf-8

# <!-- 
# # Gantt chart 
# 
# A book about my work in PhD.  -->
# <!-- ```{tableofcontents}
# ``` 
#  -->

# In[1]:


from IPython.display import Image, display
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff

df = [dict(Task="Third Year Review", Start='2022-11-01', Finish='2022-12-01'),
      dict(Task="HPC IO tuner", Start='2022-07-10', Finish='2022-07-30'),
      dict(Task="SC deadline", Start='2022-08-1', Finish='2022-08-10'),
      dict(Task="Threads utilisation", Start='2022-07-25', Finish='2022-07-30'),
      dict(Task="Add fenicsX", Start='2022-07-25', Finish='2022-07-30'),
      dict(Task="SC deadline", Start='2022-08-1', Finish='2022-08-10'),
      dict(Task="Second Year Review", Start='2021-11-01', Finish='2021-12-01'),
      dict(Task="CIUK 21", Start='2021-10-01', Finish='2021-11-01'),
      dict(Task="First Year Review", Start='2021-1-01', Finish='2021-2-01')]

fig = ff.create_gantt(df) 
fig.update_layout(
    autosize=False,
    margin=dict(l=20, r=20, t=20, b=20),)

fig.layout.title = None

fig.show()

