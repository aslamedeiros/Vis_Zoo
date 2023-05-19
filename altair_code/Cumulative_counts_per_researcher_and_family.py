#!/usr/bin/env python
# coding: utf-8

# # Cumulative Counts per researcher & family
# 
# By **Franklin Oliveira**
# 
# -----
# This notebook contains all code necessary to make the cumulative counts line charts for `repteis` database. Here you'll find some basic data treatment and charts' code. 
# 
# Database: <font color='blue'>'Compilacao Livros Repteis - 2 a 10 - 2020_04_28.xls'</font>.

# In[1]:


import datetime
import numpy as np
import pandas as pd

from collections import defaultdict

# quick visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Waffle Charts
# from pywaffle import Waffle 
# docs: https://pywaffle.readthedocs.io/en/latest/examples/block_shape_distance_location_and_direction.html

# visualization
import altair as alt

# enabling notebook renderer
# alt.renderers.enable('notebook')
# alt.renderers.enable('default')

# disabling rows limit
alt.data_transformers.disable_max_rows()


# ## Importing data...

# In[2]:


NewTable = pd.read_csv('./data/treated_db.csv', sep=';', encoding='utf-8-sig', low_memory= False)


# <br>
# 
# <font size=5>**Color Palette**</font>
# 
# <!-- <img src="./src/paleta_cores.jpeg" width='500px'> -->

# In[3]:


# importing customized color palettes
from src.MNViz_colors import *


# <br>
# 
# 
# ## Graphs
# 
# ---
# 
# ### Creating chart: counts per determiner per year
# 
# To calculate the cumulative counts, we need to consider ALL determiner's columns, in this case:
# 
#     - 'determinator_full_name'
#     - 'determinator_full_name2': as I'm writing this script, it's all empty

# In[4]:


determiner_columns = ['determinator_full_name', 'determinator_full_name2']

# name of all determiners (first and second)
determiners = set(NewTable['determinator_full_name'].str.strip()).union(set(NewTable['determinator_full_name2']))

determiners = [name for name in determiners if 'nan' not in str(name)]  # removing NaN and parsing into a list


# In[5]:


# subsetting (p.s.: kingdom is a non-empty column used only for counting)
df = NewTable[[determiner_columns[0], 'ano_determinacao', 'kingdom']].copy()

# concatenating all columns into just one to make grouping per determiner and year easier
if len(determiner_columns) > 1:
    for det_col in determiner_columns[1:]:
        temp = NewTable[[det_col, 'ano_determinacao', 'kingdom']].copy()
        temp.columns = [determiner_columns[0], 'ano_determinacao', 'kingdom']
        
        df = pd.concat([df, temp])
        
# parsing columns into strings so we don't lose information while grouping
df[determiner_columns[0]] = df[determiner_columns[0]].astype(str)
df['ano_determinacao'] = df['ano_determinacao'].astype(str)


# In[6]:


# grouping
grouped = df.groupby([determiner_columns[0], 'ano_determinacao']).count().reset_index().rename(columns=
                                                        {'kingdom':'count'})

# sorting
grouped.sort_values('ano_determinacao', inplace=True)

# cumulatively counting for each determiner
counts = pd.DataFrame()
for det in determiners:
    temp = grouped[grouped[determiner_columns[0]] == det].copy()
    temp['cumulative_sum'] = temp['count'].cumsum()
    
    counts = pd.concat([counts, temp])
    
# grouped['cumulative_sum'] = cumCounts


# In[7]:


# temporary adjustment for axis labels only
counts['ano_determinacao'] = counts['ano_determinacao'].apply(lambda x:str(x).split('.')[0])


# In[8]:


select = alt.selection(type='single', on='mouseover', nearest=True, fields=['determinator_full_name'])

base = alt.Chart(counts, title='Cumulative contribution of each determiner', width=800,
              height=500).encode(
    x= alt.X('ano_determinacao', type="ordinal", title='Determination Year'),
    y= alt.Y('cumulative_sum', title='', 
             sort=alt.EncodingSortField('counts', op="count", order='descending')),
    color= alt.Color('determinator_full_name:N', title='', legend=None,
                     scale= alt.Scale(scheme= 'warmgreys')),
    
)

points = base.mark_circle(size=40).encode(
    opacity=alt.value(0.5),
    tooltip= alt.Tooltip(['determinator_full_name','ano_determinacao','count','cumulative_sum'])
).add_selection(
    select
)

lines = base.mark_line(point=True).encode(
    size=alt.condition(~select, alt.value(1), alt.value(4)),
    opacity= alt.value(1),
#     color = alt.condition(~select, alt.value('lightgray'), alt.value('black'))
#     tooltip= alt.Tooltip(['determinator_full_name','det_year','cumulative_sum'])
)

g1 = points + lines

g1 = g1.configure_title(fontSize=16).configure_axis(
    labelFontSize=12,
    titleFontSize=12
).configure_legend(
    labelFontSize=12,
    titleFontSize=12
)

# g1.save('./graphs/cumCounts/determiner/cumCount-per-year.html')
# g1


# <br>
# 
# ### Collector's cumulative contribution per year
# 
# <font color='red' size='5'> Collectors name is sensitive data. Do not publish it without curator's permission </font>
# 
# To calculate the cumulative counts, we need to consider ALL collector's columns, in this case:
# 
#     - 'collector_full_name'
#     - 'collector_full_name2' ... 'collector_full_name6'

# In[9]:


collector_columns = ['collector_full_name', 'collector_full_name2', 
                     'collector_full_name3', 'collector_full_name4', 
                     'collector_full_name5', 'collector_full_name6']

# name of all collectors (first through sixth)
collectors = set(NewTable['collector_full_name'].str.strip())

for col in collector_columns[1:]:
    collectors = collectors.union(set(NewTable[col]))

collectors = [name for name in collectors if 'nan' not in str(name)]  # removing NaN and parsing into a list


# In[10]:


# subsetting (p.s.: kingdom is a non-empty column used only for counting)
df = NewTable[[collector_columns[0], 'year_collected', 'kingdom']].copy()

# concatenating all columns into just one to make grouping per determiner and year easier
if len(collector_columns) > 1:
    for col in collector_columns[1:]:
        temp = NewTable[[col, 'year_collected', 'kingdom']].copy()
        temp.columns = [collector_columns[0], 'year_collected', 'kingdom']
        
        df = pd.concat([df, temp])
        
# parsing columns into strings so we don't lose information while grouping
df[collector_columns[0]] = df[collector_columns[0]].astype(str)
df['year_collected'] = df['year_collected'].astype(str)


# In[11]:


# grouping
grouped = df.groupby([collector_columns[0], 'year_collected']).count().reset_index().rename(columns=
                                                        {'kingdom':'count'})

# sorting
grouped.sort_values('year_collected', inplace=True)

# cumulatively counting for each determiner
counts = pd.DataFrame()
for col in collectors:
    temp = grouped[grouped[collector_columns[0]] == col].copy()
    temp['cumulative_sum'] = temp['count'].cumsum()
    
    counts = pd.concat([counts, temp])
    
# grouped['cumulative_sum'] = cumCounts


# In[12]:


# temporary adjustment for axis labels only
counts['year_collected'] = counts['year_collected'].apply(lambda x:str(x).split('.')[0])


# In[13]:


select = alt.selection(type='single', on='mouseover', nearest=True, fields=['collector_full_name'])

base = alt.Chart(counts, title='Cumulative contribution of each Collector', width=800,
              height=500).encode(
    x= alt.X('year_collected', type="ordinal", title='Sampling Year'),
    y= alt.Y('cumulative_sum', title='', 
             sort=alt.EncodingSortField('counts', op="count", order='descending')),
    color= alt.Color('collector_full_name:N', title='', legend=None, 
                     scale= alt.Scale(scheme='warmgreys')),
)

points = base.mark_circle(size=40).encode(
    opacity=alt.value(0.5),
    tooltip= alt.Tooltip(['collector_full_name','year_collected','count', 'cumulative_sum'])
).add_selection(
    select
)

front = base.mark_line(point=True).encode(
    size=alt.condition(~select, alt.value(1), alt.value(4)),
    opacity= alt.value(1),
)

g1 = points + front

g1 = g1.configure_title(fontSize=16).configure_axis(
    labelFontSize=12,
    titleFontSize=12
).configure_legend(
    labelFontSize=12,
    titleFontSize=12
)

# g1.save('./graphs/cumCounts/collector/cumCount-per-year.html')
# g1


# <br>
# 
# ## Cumulative counts per Family
# 

# In[22]:


# grouping per Year and Family
teste = NewTable.groupby(['year_collected','family']).count()['class'].reset_index().rename(columns={
    'class':'counts'
})

# sorting...
teste = teste.sort_values(['family', 'year_collected'])


# In[23]:


# cumulatively counting
cumSum = []
for family in teste['family'].unique():
    cumSum.extend(list(teste[teste['family'] == family]['counts'].cumsum()))
    
teste['cumulative_sum'] = cumSum


# ### Chart: per collected year

# In[24]:


# filtering out some families lost while grouping
# familias = [f for f in cores_familia.keys() if f in teste['family'].unique()]
# cores_temp = [cores_familia[f] for f in familias] 

# selector
select_family = alt.selection_multi(fields=['family'], bind='legend')

# aux. variables for encoding fields
x_labels = teste.sort_values('year_collected')['year_collected'].unique()
# x_labels = [str(y).split('.')[0] for y in x_labels]
y_max = np.ceil(max(teste['cumulative_sum'].unique()))

g1 = alt.Chart(teste, title='Cumulative amount of specimens per family', 
               width=600, height=400).mark_line(point=True).encode(
    x= alt.X('year_collected', type="ordinal", title='Sampling Year',
             scale= alt.Scale(domain= x_labels)),
    y= alt.Y('cumulative_sum', title='', 
             scale= alt.Scale(domain=[0, y_max]),
             sort=alt.EncodingSortField('counts', op="count", order='descending')),
    color= alt.Color('family:N', title='Family',
                     legend= alt.Legend(columns=2, symbolLimit=50),
                     scale=alt.Scale(domain=list(cores_familia.keys()), 
                                     range= list(cores_familia.values()))),
    tooltip= alt.Tooltip(['family','year_collected','counts', 'cumulative_sum']),
    opacity= alt.condition(select_family, alt.value(1), alt.value(0))
).add_selection(select_family).transform_filter(select_family)

g1 = g1.configure_title(fontSize=16).configure_axis(
    labelFontSize=12,
    titleFontSize=12
).configure_legend(
    labelFontSize=12,
    titleFontSize=12
)

# g1.save('./graphs/cumCounts/family/temporal_evolution_per_family.html')
# g1


# <br>
# 
# ### Chart: per determination year

# In[17]:


# grouping per Year and Family
teste = NewTable.groupby(['ano_determinacao','family']).count()['class'].reset_index().rename(columns={
    'class':'counts'
})

# sorting...
teste = teste.sort_values(['family', 'ano_determinacao'])


# In[18]:


# cumulatively counting
cumSum = []
for family in teste['family'].unique():
    cumSum.extend(list(teste[teste['family'] == family]['counts'].cumsum()))
    
teste['cumulative_sum'] = cumSum


# In[20]:


# filtering out some families lost while grouping
# familias = [f for f in cores_familia.keys() if f in teste['family'].unique()]
# cores_temp = [cores_familia[f] for f in familias] 

# selector
select_family = alt.selection_multi(fields=['family'], bind='legend')

# aux. variables for encoding fields
x_labels = teste.sort_values('ano_determinacao')['ano_determinacao'].unique()
# x_labels = [str(y).split('.')[0] for y in x_labels]
y_max = np.ceil(max(teste['cumulative_sum'].unique()))


g1 = alt.Chart(teste, title='Cumulative amount of specimens per family', 
               width=600, height=400).mark_line(point=True).encode(
    x= alt.X('ano_determinacao', type="ordinal", title='Determination Year',
             scale= alt.Scale(domain= x_labels)),
    y= alt.Y('cumulative_sum', title='', 
             scale= alt.Scale(domain= [0, y_max]),
             sort=alt.EncodingSortField('counts', op="count", order='descending')),
    color= alt.Color('family:N', title='Família',
                     legend= alt.Legend(columns=2, symbolLimit=50),
                     scale=alt.Scale(domain=list(cores_familia.keys()), 
                                     range= list(cores_familia.values()))),
    tooltip= alt.Tooltip(['family','ano_determinacao','counts', 'cumulative_sum']),
    opacity= alt.condition(select_family, alt.value(1), alt.value(0))
).add_selection(select_family).transform_filter(select_family)

g1 = g1.configure_title(fontSize=16).configure_axis(
    labelFontSize=12,
    titleFontSize=12
).configure_legend(
    labelFontSize=12,
    titleFontSize=12
)

# g1.save('./graphs/cumCounts/family/temporal_evolution_per_family-det_year.html')
# g1


# <br>
# 
# **The end!**
# 
# -----
