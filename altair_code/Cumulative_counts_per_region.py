#!/usr/bin/env python
# coding: utf-8

# # Cumulative counts per geographical region
# 
# By **Franklin Oliveira**
# 
# -----
# This notebook contains all code necessary to make charts from `repteis` database with focus on collection's cumulative spacial increments. Here you'll find some basic data treatment and charts' code. 
# 
# Database: <font color='blue'>'Compilacao Livros Repteis - 2 a 10 - 2020_04_28.xls'</font>.m
#     

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


NewTable = pd.read_csv('./data/treated_db.csv', sep=';', encoding='utf-8-sig', low_memory=False)


# <br>
# 
# <font size=5>**Color palette**</font>
# 
# Importing customized color palettes.
# 
# 
# <!-- <img src="./src/paleta_cores.jpeg" width='500px'>
#  -->
# <!-- Cores: 
# 
# - verde_escuro: #284021
# - verde_claro: #88BF11
# - amarelo: #D9CB0B
# - laranja: #D99311
# - laranja_escuro: #BF4417
# - marrom-_laro: #BF8D7A -->

# In[20]:


# importing customized color palettes
from src.MNViz_colors import *


# In[21]:


# p.s.: Caudata is an error and should be removed
# cores_ordem = {
#     'Squamata': '#BF4417',
#     'Testudines': '#D9CB0B', 
#     'Crocodylia': '#284021'
# }

ordens = list(cores_ordem.keys())
cores = list(cores_ordem.values())


# <br>
# 
# ## Counting per continent

# In[22]:


# corrects a typo (Améica do Sul)
NewTable['continent'] = NewTable['continent'].apply(lambda x: 'América do Sul' if x=='Améica do Sul' else x)


# In[23]:


# forces Country column to be in string format
NewTable['country'] = NewTable['country'].apply(lambda x:str(x))


# In[24]:


# looking good...
# NewTable['continent'].value_counts()


# In[25]:


# grouping per Year and Continent
teste = NewTable.groupby(['year_collected','continent']).count()['class'].reset_index().rename(columns={
    'class':'counts'
})

# sorting...
teste = teste.sort_values(['continent', 'year_collected'])


# In[26]:


# cumulatively counting
cumSum = []
for continente in teste['continent'].unique():
    cumSum.extend(list(teste[teste['continent'] == continente]['counts'].cumsum()))
    
teste['cumulative_sum'] = cumSum


# ### Chart: all continents

# In[27]:


select_continent = alt.selection_multi(fields=['continent'], bind='legend')

g1 = alt.Chart(teste, title="Collection's temporal evolution per continent", 
               width=600).mark_line(point=True).encode(
    x= alt.X('year_collected', type="ordinal", title='Sampling Year'),
    y= alt.Y('cumulative_sum', title='', 
             sort=alt.EncodingSortField('counts', op="count", order='descending')),
    color= alt.Color('continente:N', title='Continent',
                     scale=alt.Scale(domain=list(cores_continente.keys()), range=list(cores_continente.values()))),
    tooltip= alt.Tooltip(['continent','year_collected','counts', 'cumulative_sum']),
    opacity= alt.condition(select_continent, alt.value(1), alt.value(0))
).add_selection(select_continent)

g1 = g1.configure_title(fontSize=16).configure_axis(
    labelFontSize=12,
    titleFontSize=12
).configure_legend(
    labelFontSize=12,
    titleFontSize=12
)

# g1.save('./graphs/cumCounts/time-spacial/temporal_evolution_per_continent.html')
# g1


# ### Chart: all continents (ex. South America)

# In[35]:


select_continent = alt.selection_multi(fields=['continent'], bind='legend')

# removing South America from domain and range colors
continents_exSA = [c for c in teste['continent'].unique() if c != 'América do Sul']
colors_exSA = [cores_continente[c] for c in continents_exSA]

g1 = alt.Chart(teste[teste['continent']!='América do Sul'],
               title="Collection's temporal evolution per continent (ex. South America)", 
width=600).mark_line(point=True).encode(
    x= alt.X('year_collected', type="ordinal", title='Sampling Year'),
    y= alt.Y('cumulative_sum', title='', 
             sort=alt.EncodingSortField('counts', op="count", order='descending'),
             scale= alt.Scale(domain=[0,150])),
    color= alt.Color('continente:N', title='Continent',
                     scale=alt.Scale(domain= continents_exSA, range= colors_exSA)),
    tooltip= alt.Tooltip(['continent','year_collected','counts', 'cumulative_sum']),
    opacity= alt.condition(select_continent, alt.value(1), alt.value(0))
).add_selection(select_continent).configure_point(
    size=50
)

g1 = g1.configure_title(fontSize=16).configure_axis(
    labelFontSize=12,
    titleFontSize=12
).configure_legend(
    labelFontSize=12,
    titleFontSize=12
)

# g1.save('./graphs/cumCounts/time-spacial/temporal_evolution_OTHER_continents.html')
# g1


# <br>
# 
# ## Counting per Country

# In[39]:


# grouping per year, continent and country
teste = NewTable.groupby(['year_collected','continent','country']).count()['class'].reset_index().rename(columns={
    'class':'counts'
})

teste = teste.sort_values(['country', 'year_collected'])


# In[40]:


# cumulatively counting
cumSum = []
for pais in teste['country'].unique():
    cumSum.extend(list(teste[teste['country'] == pais]['counts'].cumsum()))
    
teste['cumulative_sum'] = cumSum


# ### Chart: all countries

# In[43]:


select_country = alt.selection_multi(fields=['country'], bind='legend')

g1 = alt.Chart(teste, title="Collection's temporal evolution per country", 
width=600).mark_line(point=True).encode(
    x= alt.X('year_collected', type="ordinal", title='Sampling Year',
            scale= alt.Scale(domain=list(sorted(teste['year_collected'].unique())))), # fixed x-axis
    y= alt.Y('cumulative_sum', title='', 
             sort=alt.EncodingSortField('counts', op="count", order='descending'),
             scale= alt.Scale(domain=[0,20000])),
    color= alt.Color('pais:N', title='Country',
                     legend= alt.Legend(columns=2, symbolLimit=42),
                     scale= alt.Scale(domain=list(cores_pais.keys()), range=list(cores_pais.values()))),
    tooltip= alt.Tooltip(['country','year_collected','counts', 'cumulative_sum']),
#     opacity= alt.condition(select_country, alt.value(1), alt.value(0))
).add_selection(select_country).transform_filter(select_country)

g1 = g1.configure_title(fontSize=16).configure_axis(
    labelFontSize=12,
    titleFontSize=12
).configure_legend(
    labelFontSize=12,
    titleFontSize=12
)

# g1.save('./graphs/cumCounts/time-spacial/temporal_evolution_per_country.html')
# g1


# <font color='red' size=4>TEST: multiple selectors (for country and continent)</font>

# In[54]:


# selectors
select_continent = alt.selection_multi(fields=['continent'], bind='legend')
select_country = alt.selection_multi(fields=['country'], bind='legend')

# database
db = teste[teste['country'] != 'Brasil']

# aux. variables
family_legend = [p for p in cores_pais.keys() if p in db['country'].unique()]
colors_legend = [cores_pais[p] for p in family_legend]

# charts
g1 = alt.Chart(db, title="Collection's temporal evolution per country (ex. Brazil)", 
               width=600, height=300).mark_line(point=True).encode(
    x= alt.X('year_collected', type="ordinal", title='Sampling Year',
             scale= alt.Scale(domain=sorted(list(teste['year_collected'].unique())))),
    y= alt.Y('cumulative_sum', title='', 
             sort=alt.EncodingSortField('counts', op="count", order='descending'),
             scale= alt.Scale(domain=[0,150])
            ),
    color= alt.Color('pais:N', title='Country', 
                legend= alt.Legend(columns=2, symbolLimit=42),
                scale= alt.Scale(domain=family_legend, 
                                 range=colors_legend)),
    tooltip= alt.Tooltip(['continent', 'country','year_collected','counts', 'cumulative_sum']),
    detail= alt.Detail('pais:N'),
    opacity= alt.condition(select_country, alt.value(1), alt.value(0.05))
).add_selection(select_country).transform_filter(select_country).transform_filter(select_continent)

g2 = alt.Chart(db, title="Collection's temporal evolution per country (ex. Brazil)", 
               width=600, height=300).mark_line(point=True).encode(
    x= alt.X('year_collected', type="ordinal", title='Sampling Year',
             scale= alt.Scale(domain=sorted(list(teste['year_collected'].unique())))),
    y= alt.Y('cumulative_sum', title='', 
             sort=alt.EncodingSortField('counts', op="count", order='descending'),
             scale= alt.Scale(domain=[0,150])
            ),
    color= alt.Color('continente:N', title='Continent', 
                legend= alt.Legend(columns=2, symbolLimit=42),
                scale= alt.Scale(domain=list(cores_continente.keys()), 
                                 range=list(cores_continente.values()))),
    tooltip= alt.Tooltip(['continent', 'country','year_collected','counts', 'cumulative_sum']),
    detail= alt.Detail('pais:N'),
    opacity= alt.condition(select_country, alt.value(1), alt.value(0.05))
).add_selection(select_continent).transform_filter(select_continent)


# creating layers (to make different selectors work together)
chart = alt.layer(g2, g1).resolve_scale('independent').configure_title(fontSize=16).configure_axis(
    labelFontSize=12,
    titleFontSize=12
).configure_legend(
    labelFontSize=12,
    titleFontSize=12
)

# chart.save('./graphs/cumCounts/time-spacial/evolution_per_country-TEST.html')
# chart


# ### Chart: all countries (ex. Brasil)

# In[30]:


# database - filtering out Brazil
db = teste[teste['country'] != 'Brasil']

# country selector
select_country = alt.selection_multi(fields=['country'], bind='legend')

# chart
g1 = alt.Chart(db, title="Collection's temporal evolution per country (ex. Brazil)", 
width=600).mark_line(point=True).encode(
    x= alt.X('year_collected', type="ordinal", title='Sampling Year',
            scale= alt.Scale(domain=list(sorted(teste['year_collected'].unique())))),
    y= alt.Y('cumulative_sum', title='', 
             sort=alt.EncodingSortField('counts', op="count", order='descending'),
            scale= alt.Scale(domain=[0,120])),
    color= alt.Color('pais:N', title='Country',
                     legend= alt.Legend(columns=2, symbolLimit=42),
                     scale= alt.Scale(domain=list(cores_pais.keys()), range=list(cores_pais.values()))),
    tooltip= alt.Tooltip(['country','year_collected','counts', 'cumulative_sum']),
#     opacity= alt.condition(select_country, alt.value(1), alt.value(0))
).add_selection(select_country).transform_filter(select_country)

g1 = g1.configure_title(fontSize=16).configure_axis(
    labelFontSize=12,
    titleFontSize=12
).configure_legend(
    labelFontSize=12,
    titleFontSize=12
)

# g1.save('./graphs/cumCounts/time-spacial/temporal_evolution_per_country-exBrazil.html')
# g1


# <br>
# 
# ### Chart: only South America countries

# In[34]:


# database
db = teste[teste['continent'] == 'América do Sul']

# country selector
select_country = alt.selection_multi(fields=['country'], bind='legend')


g1 = alt.Chart(db, 
               title="Collection's temporal evolution per South America countries",
width=600).mark_line(point=True).encode(
    x= alt.X('year_collected', type="ordinal", title='Sampling Year',
            scale= alt.Scale(domain=list(sorted(teste['year_collected'].unique())))),
    y= alt.Y('cumulative_sum', title='', 
             sort=alt.EncodingSortField('counts', op="count", order='descending'),
            scale= alt.Scale(domain=[0,20000])),
    color= alt.Color('pais:N', title='Country',
                     legend= alt.Legend(columns=2),
                     scale= alt.Scale(domain=list(cores_AS.keys()), range=list(cores_AS.values()))),
    tooltip= alt.Tooltip(['country','year_collected','counts']),
#     opacity= alt.condition(select_country, alt.value(1), alt.value(0))
).add_selection(select_country).transform_filter(select_country)

g1 = g1.configure_title(fontSize=16).configure_axis(
    labelFontSize=12,
    titleFontSize=12
).configure_legend(
    labelFontSize=12,
    titleFontSize=12
)

# g1.save('./graphs/cumCounts/time-spacial/temporal_evolution_per_country-SouthAmerica.html')
# g1


# ### Chart: South America countries (ex. Brasil)

# In[37]:


# removing Brasil from country list
countries_AS_exBr = [c for c in cores_AS.keys() if c != 'Brasil']
cores_AS_exBr = [cores_AS[c] for c in countries_AS_exBr]

# country selector
select_country = alt.selection_multi(fields=['country'], bind='legend')

g1 = alt.Chart(teste[(teste['continent'] == 'América do Sul') & (teste['country'] != 'Brasil')], 
               title="Collection's temporal evolution per South America country (ex. Brazil)",
width=600).mark_line(point=True).encode(
    x= alt.X('year_collected', type="ordinal", title='Sampling Year',
            scale= alt.Scale(domain=list(sorted(teste['year_collected'].unique())))),
    y= alt.Y('cumulative_sum', title='', 
             sort=alt.EncodingSortField('counts', op="count", order='descending'),
            scale= alt.Scale(domain=[0,120])),
    color= alt.Color('pais:N', title='Country',
                     legend= alt.Legend(columns=2),
                     scale= alt.Scale(domain=countries_AS_exBr, range=cores_AS_exBr)),
    tooltip= alt.Tooltip(['country','year_collected','counts']),
#     opacity= alt.condition(select_country, alt.value(1), alt.value(0))
).add_selection(select_country).transform_filter(select_country)

g1 = g1.configure_title(fontSize=16).configure_axis(
    labelFontSize=12,
    titleFontSize=12
).configure_legend(
    labelFontSize=12,
    titleFontSize=12
)

# g1.save('./graphs/cumCounts/time-spacial/temporal_evolution_per_country-SouthAmerica-exBrazil.html')
# g1


# <br>
# 
# ## Counting per Brazilian State

# In[38]:


# filtering for Brazil, only
teste2 = NewTable[NewTable['country'] == 'Brasil']
teste2 = teste2.groupby(['year_collected','state', 'order']).count()['class'].reset_index().rename(columns={
    'class':'counts'
})


# ### creating column with brazilian regions

# In[39]:


regioes = {
    'Rio de Janeiro':'SE',
    'São Paulo':'SE',
    'Espírito Santo': 'SE',
    'Pernambuco':'NE',
    'Santa Catarina':'S',
    'Amazonas':'N',
    'Goiás':'CO',
    'Roraima':'N',
    'Pará':'N',
    'Mato Grosso':'CO',
    'Acre': 'N',
    'Bahia': 'NE',
    'Minas Gerais': 'SE',
    'Mato Grosso do Sul': 'CO',
    'Paraná': 'S',
    'Rondônia': 'N',
    'Ceará': 'NE',
    'Maranhão': 'N',
    'Rio Grande do Sul': 'S',
    'Paraíba': 'NE',
    'Distrito Federal': 'CO',
    'Alagoas': 'NE',
    'Amapá':'N',
    'Piauí': 'NE',
    'Brasília': 'CO',
    'Tocantins': 'N',
    'Rio Grande do Norte': 'NE',
    'Sergipe': 'NE',
    'Minas Gerais/Goiás/Distrito Federal': 'CO',
    'Santa Catarina-Rio Grande do Sul': 'S'
}

# criando coluna com as regiões
teste2['region'] = teste2['state'].apply(lambda x: regioes[str(x)])

# coluna com estado, regiao
teste2['regiao_e_estado'] = teste2['state'] + ', ' + teste2['region']

# ordenando por região e soma das contagens
sorting = teste2.groupby(['regiao_e_estado', 'region']).sum()['counts'].reset_index(
                                                                ).rename(columns={'counts':'soma'})
sorting = sorting.sort_values(['region','soma'], ascending=False)['regiao_e_estado'].unique()


# In[40]:


# OBS: variável teste2 tem as informações que precisamos (vide gráfico de contagem por região - time_spacial)
teste = teste2.groupby(['year_collected','regiao_e_estado']).count()['order'].reset_index().rename(columns={
    'order':'counts'
})

teste = teste.sort_values(['regiao_e_estado', 'year_collected'])


# In[41]:


# cumulatively counting
cumSum = []
for reg_est in teste['regiao_e_estado'].unique():
    cumSum.extend(list(teste[teste['regiao_e_estado'] == reg_est]['counts'].cumsum()))
    
teste['cumulative_sum'] = cumSum


# In[42]:


teste['estado'] = teste['regiao_e_estado'].apply(lambda x:x.split(',')[0])
teste['region'] = teste['regiao_e_estado'].apply(lambda x:x.split(',')[1].strip())


# ### Chart: cumulative counts per Brazilian State

# In[43]:


# independent legend (use only if needed)
# teste['ones'] = 1
# 
# select_region = alt.selection_multi(fields=['region'], bind='legend')
# 
# legend_reg = alt.Chart(teste).mark_point(filled=True, size=100).encode(
#     x= alt.X('ones:O', title='', axis=None),
#     y= alt.Y('regiao:N', title='', sort= ['N', 'NE', 'CO', 'SE', 'S'],
#             axis= alt.Axis(orient= 'right', labels=True, grid=False, ticks=False, domain=False)),
#     color= alt.condition(select_region, 
#                          alt.Color('regiao:N',
#                            scale= alt.Scale(domain= list(cores_regioes.keys()),
#                                range= list(cores_regioes.values()))),
#                          alt.value('lightgray'))
# #     opacity= alt.condition(select_region, alt.value(1), alt.value(0.5))
# ).add_selection(select_region)
# 
# legend_reg


# In[49]:


select_state = alt.selection_multi(fields=['estado'], bind='legend')

g1 = alt.Chart(teste, title="Collection's temporal evolution per Brazilian State", 
               width=600).mark_line(point=True).encode(
    x= alt.X('year_collected', type="ordinal", title='Sampling Year',
             scale= alt.Scale(domain=sorted(list(teste['year_collected'].unique())))),
    y= alt.Y('cumulative_sum', title='', 
             sort=alt.EncodingSortField('counts', op="count", order='descending'),
             scale= alt.Scale(domain=[0,140])),
    color= alt.Color('estado:N', title='State', 
                legend= alt.Legend(columns=2, symbolLimit=42),
                scale= alt.Scale(domain=list(cores_estados.keys()), range=list(cores_estados.values()))),
    tooltip= alt.Tooltip(['region', 'estado','year_collected','counts', 'cumulative_sum']),
#     opacity= alt.condition(select_region, alt.value(1), alt.value(0.2))
).add_selection(select_state).transform_filter(select_state)

g1 = g1.configure_title(fontSize=16).configure_axis(
    labelFontSize=12,
    titleFontSize=12
).configure_legend(
    labelFontSize=12,
    titleFontSize=12
).configure_view(strokeWidth=0)

# g1.save('./graphs/cumCounts/time-spacial/temporal_evolution_per_state.html')
# g1


# <br>
# 
# <font color='red' size='5'>TEST</font>
# 
# Chart with multiple selectors

# In[53]:


# selectors
select_region = alt.selection_multi(fields=['region'], bind='legend')
select_state = alt.selection_multi(fields=['estado'], bind='legend')


# charts
g1 = alt.Chart(teste, title="Collection's temporal evolution per Brazilian State", width=600).mark_line(point=True).encode(
    x= alt.X('year_collected', type="ordinal", title='Sampling Year',
             scale= alt.Scale(domain=sorted(list(teste['year_collected'].unique())))),
    y= alt.Y('cumulative_sum', title='', 
             sort=alt.EncodingSortField('counts', op="count", order='descending'),
             scale= alt.Scale(domain=[0,140])),
    color= alt.Color('estado:N', title='State', 
                legend= alt.Legend(columns=2, symbolLimit=42),
                scale= alt.Scale(domain=list(cores_estados.keys()), range=list(cores_estados.values()))),
    tooltip= alt.Tooltip(['region', 'estado','year_collected','counts', 'cumulative_sum']),
    detail= alt.Detail('estado:N'),
    opacity= alt.condition(select_state, alt.value(1), alt.value(0.05))
).add_selection(select_state).transform_filter(select_state).transform_filter(select_region)

g2 = alt.Chart(teste, title="Collection's temporal evolution per Brazilian State", width=600).mark_line(point=True).encode(
    x= alt.X('year_collected', type="ordinal", title='Sampling Year',
             scale= alt.Scale(domain=sorted(list(teste['year_collected'].unique())))),
    y= alt.Y('cumulative_sum', title='', 
             sort=alt.EncodingSortField('counts', op="count", order='descending'),
             scale= alt.Scale(domain=[0,140])),
    color= alt.Color('regiao:N', title='Region', 
                legend= alt.Legend(columns=5, symbolLimit=42),
                scale= alt.Scale(domain=list(cores_regioes.keys()), range=list(cores_regioes.values()))),
    tooltip= alt.Tooltip(['region', 'estado','year_collected','counts', 'cumulative_sum']),
    detail= alt.Detail('estado:N'),
    opacity= alt.condition(select_state, alt.value(1), alt.value(0.05))
).add_selection(select_region).transform_filter(select_region)


# creating layers (to make different selectors work together)
chart = alt.layer(g2, g1).resolve_scale('independent').configure_title(fontSize=16).configure_axis(
    labelFontSize=12,
    titleFontSize=12
).configure_legend(
    labelFontSize=12,
    titleFontSize=12
)

# chart.save('./graphs/cumCounts/time-spacial/temporal_evolution_per_state_and_region.html')
# chart


# <br>
# 
# ### Chart: cumulative counts per Brazilian Region

# In[54]:


temp = teste2.groupby(['year_collected','region']).count()['order'].reset_index().rename(columns={
    'order':'counts'
})

temp = temp.sort_values(['region', 'year_collected'])


# In[55]:


# cumulatively counting
cumSum = []
for reg in temp['region'].unique():
    cumSum.extend(list(temp[temp['region'] == reg]['counts'].cumsum()))
    
temp['cumulative_sum'] = cumSum


# In[58]:


select_region = alt.selection_multi(fields=['region'], bind='legend')

g1 = alt.Chart(temp, title="Collection's temporal evolution per Brazilian Region", 
               width=600).mark_line(point=True).encode(
    x= alt.X('year_collected', type="ordinal", title='Sampling Year',
             scale= alt.Scale(domain=sorted(list(teste['year_collected'].unique())))),
    y= alt.Y('cumulative_sum', title='', 
             sort=alt.EncodingSortField('counts', op="count", order='descending'),
             scale= alt.Scale(domain=[0,350])),
    color= alt.Color('regiao:N', title='Region', 
                        legend= alt.Legend(columns=1, symbolLimit=42),
                     scale= alt.Scale(domain=list(cores_regioes.keys()), range=list(cores_regioes.values()))),
    tooltip= alt.Tooltip(['region','year_collected','counts', 'cumulative_sum']),
#     opacity= alt.condition(select_country, alt.value(1), alt.value(0))
).add_selection(select_region).transform_filter(select_region)

g1 = g1.configure_title(fontSize=16).configure_axis(
    labelFontSize=12,
    titleFontSize=12
).configure_legend(
    labelFontSize=12,
    titleFontSize=12
)

# g1.save('./graphs/cumCounts/time-spacial/temporal_evolution_per_region.html')
# g1


# <br>
# 
# **That's it!**
