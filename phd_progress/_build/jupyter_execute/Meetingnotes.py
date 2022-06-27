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
    width=1000,
    height=800,
    margin=dict(l=20, r=20, t=20, b=20),)

fig.layout.title = None

fig.show()

# import plotly.express as px
# import pandas as pd
# import math

# string1 = f"""<a href="/_build/html/Markdown_files/CRESCENDO_DOLFINX.html", target="_black">o</a>"""

# df = pd.DataFrame([
#     dict(Task="Job A", Start='2009-01-01', Finish='2009-01-04', Filename=string1),
#     dict(Task="Job A", Start='2009-01-06', Finish='2009-01-09', Filename=string1),
#     dict(Task="Job A", Start='2009-01-10', Finish='2009-01-15', Filename=string1),
#     dict(Task="Job A", Start='2009-01-16', Finish='2009-01-19', Filename=string1),
#     dict(Task="Job A", Start='2009-01-21', Finish='2009-01-25', Filename=string1),
#     dict(Task="Job A", Start='2009-01-28', Finish='2009-01-31', Filename=string1),
#     dict(Task="Job A", Start='2009-02-01', Finish='2009-02-08', Filename=string1),
#     dict(Task="Job A", Start='2009-02-11', Finish='2009-02-15', Filename=string1),
#     dict(Task="Job A", Start='2009-02-17', Finish='2009-02-20', Filename=string1),
#     dict(Task="Job A", Start='2009-02-22', Finish='2009-02-24', Filename=string1),
#     dict(Task="Job A", Start='2009-02-25', Finish='2009-02-28', Filename=string1),
#     dict(Task="Job B", Start='2009-03-05', Finish='2009-03-15', Filename=string1),
#     dict(Task="Job C", Start='2009-02-20', Finish='2009-04-30', Filename=string1)
# ])

# fig = px.timeline(df, 
#                   x_start="Start",
#                   x_end="Finish",
#                   y="Task",
#                   color="Task",
#                   color_discrete_sequence=px.colors.qualitative.Pastel)

# for idx, row in df.iterrows():
#     periods = pd.date_range(row["Start"],row["Finish"], freq='1D')
#     center_pos = math.floor(len(periods) / 2)
#     x_dates = periods[center_pos]
#     fig.add_annotation(
#         {
#             "x": x_dates,#row["Finish"],
#             "y": row["Task"],
#             "text": row["Filename"],
#             "align": "center",
#             "showarrow":False,
#         }
#     )

# fig.show()
# fig.write_html("test_gantt.html", include_plotlyjs="cdn")


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

# ```python
# note = "Python syntax highlighting"
# print(node)
# ```

# In[ ]:





# In[ ]:




