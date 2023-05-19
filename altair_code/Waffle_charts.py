#!/usr/bin/env python
# coding: utf-8

# # Waffle Charts
# 
# By **Franklin Oliveira**
# 
# -----
# This notebook contains all code necessary to make charts from `repteis` database with focus on time and space exploration. Here you'll find some basic data treatment and charts' code. 
# 
# Database: <font color='blue'>'Compilacao Livros Repteis - 2 a 10 - 2020_04_28.xls'</font>.m
#     

# ## Basic imports

# In[1]:


import datetime
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

from collections import defaultdict

# this package does most of the heavy work of constructing the Waffle Charts
# docs: https://pywaffle.readthedocs.io/en/latest/examples/block_shape_distance_location_and_direction.html
from pywaffle import Waffle 

# alt.renderers.enable('default')


# ## Importing data...

# In[2]:


NewTable = pd.read_csv('./data/treated_db.csv', sep=';', encoding='utf-8-sig', low_memory= False)


# <br>
# 
# <font size=5>**Color Palette**</font>
# 
# <!-- <img src="./src/paleta_cores.jpeg" width='500px'> -->
# 
# <!-- Cores: 
# 
# - verde_escuro: #284021
# - verde_claro: #88BF11
# - amarelo: #D9CB0B
# - laranja: #D99311
# - laranja_escuro: #BF4417
# - marrom-_laro: #BF8D7A -->

# In[3]:


# importing customized color palettes
from src.MNViz_colors import *


# In[4]:


# p.s.: Caudata is an error and should be removed
# cores_ordem = {
#     'Squamata': '#BF4417',
#     'Testudines': '#D9CB0B', 
#     'Crocodylia': '#284021'
# }

ordens = list(cores_ordem.keys())
cores = list(cores_ordem.values())


# a few comments on the rationale behind the color palette (to see this, uncomment the content in this cell)
# 
# <!-- **Paleta de Cores - Família:**
# 
# - grupo 1: 1 cor  (verde escuro)
# <ul>
#     <li style="color:#142611"><b>centroide 1</b></li>
# </ul>
# - grupo 2: 8 cores
# <ul>
#     <li style="color:#85D907"><b>centroide 2</b></li>
# </ul>
# 
# ['#d7ff81', '#bafd62', '#9feb3f', '#85d907', '#6cc700', '#52b700', '#35a600', '#0b9700', '#008800']
# 
# <font color="#d7ff81"><b>cor 1</b> (ficou fora)</font>
# <font color="#bafd62"><b>cor 2</b></font>
# <font color="#9feb3f"><b>cor 3</b></font>
# <font color="#85d907"><b>cor 4</b></font>
# <font color="#6cc700"><b>cor 5</b></font>
# <font color="#52b700"><b>cor 6</b></font>
# <font color="#35a600"><b>cor 7</b></font>
# <font color="#0b9700"><b>cor 8</b></font>
# <font color="#008800"><b>cor 9</b></font>
# 
# 
# - grupo 3: 2 cores
# #888C03
# <ul>
#     <li style="color:#22401E"><b>centroide 3 (puxando para tons frios mais claros)</b></li>
# </ul>
# 
# <font color="#99b6b2"><b>cor 1</b></font>
# <font color="#81a58b"><b>cor 2</b></font>
# 
# 
# - grupo 4: 1 cor  (amarelo)
# <ul>
#     <li style="color:#F2CB07"><b>centroide 4</b></li>
# </ul>
# 
# - grupo 5: 10 cores
# <ul>
#     <li style="color:#cb97d4"><b>centroide 5 (puxando para o roxo)</b></li>
# </ul>
# 
# ['#f8dcf9', '#ebc5ed', '#ddafe2', '#ce9ad6', '#bf86cc', '#af73c2', '#a160b8', '#924fae', '#833fa4'] #803da1
# 
# <font color="#f8dcf9"><b>cor 1</b></font>
# <font color="#ebc5ed"><b>cor 2</b></font>
# <font color="#ddafe2"><b>cor 3</b></font>
# <font color="#ce9ad6"><b>cor 4</b></font>
# <font color="#bf86cc"><b>cor 5</b></font>
# <font color="#af73c2"><b>cor 6</b></font>
# <font color="#a160b8"><b>cor 7</b></font>
# <font color="#924fae"><b>cor 8</b></font>
# <font color="#833fa4"><b>cor 9</b></font>
# <font color="#803da1"><b>cor 10</b></font>
# 
# 
# - grupo 6: 12 cores
# <ul>
#     <li style="color:#91F2E9"><b>centroide 6</b></li>
# </ul>
# 
# ['#c9fff9', '#b3eff2', '#9cdcea', '#83c9e2', '#68b7da', '#4aa6d2', '#2096ca', '#0087c1', '#0079b7']
# 
# ['#cee5d8', '#b3d2d1', '#9bbfc9', '#83adc2', '#6d9bba', '#568ab2', '#3e7baa', '#226ca2', '#005e98']
# 
# 
# <font color="#c9fff9"><b>cor 1</b></font>
# <font color="#b3eff2"><b>cor 2</b></font>
# <font color="#9cdcea"><b>cor 3</b></font>
# <font color="#83c9e2"><b>cor 4</b></font>
# <font color="#68b7da"><b>cor 5</b></font>
# <font color="#4aa6d2"><b>cor 6</b></font>
# <font color="#2096ca"><b>cor 7</b></font>
# <font color="#0087c1"><b>cor 8</b></font>
# <font color="#0079b7"><b>cor 9</b></font>
# <font color="#3e7baa"><b>cor 10</b></font>
# <font color="#226ca2"><b>cor 11</b></font>
# <font color="#005e98"><b>cor 12</b></font>
# 
# 
# - grupo 7: 3 cores
# <ul>
#     <li style="color:#8C1A0F"><b>centroide 7 (puxando para o marrom)</b></li>
# </ul>
# 
# ['#fde5bf', '#efd09f', '#e1bb82', '#d3a767', '#c6934d', '#b98033', '#ac6f18', '#9e5e00', '#914e00']
# 
# <font color="#ac6f18"><b>cor 1</b></font>
# <font color="#9e5e00"><b>cor 2</b></font>
# <font color="#914e00"><b>cor 3</b></font>
# 
# 
# - grupo 8: 13 cores
# <ul>
#     <li style="color:#D9430D"><b>centroide 8</b></li>
# </ul>
# 
# ['#ffce9f', '#ffb683', '#ff9f69', '#ff8851', '#f5723b', '#e75b25', '#d9430d', '#cb2800', '#bc0000']
# 
# ['#ff8f68', '#ff7e56', '#ff6b40', '#ee5829', '#d9430d', '#c62f00', '#b41b00', '#a40300', '#930000']
# 
# <font color="#ffce9f"><b>cor 1</b></font>
# <font color="#ffb683"><b>cor 2</b></font>
# <font color="#ff9f69"><b>cor 3</b></font>
# <font color="#ff8851"><b>cor 4</b></font>
# <font color="#f5723b"><b>cor 5</b></font>
# <font color="#e75b25"><b>cor 6</b></font>
# <font color="#d9430d"><b>cor 7</b></font>
# <font color="#cb2800"><b>cor 8</b></font>
# <font color="#bc0000"><b>cor 9</b></font>
# <font color="#c62f00"><b>cor 10</b></font>
# <font color="#b41b00"><b>cor 11</b></font>
# <font color="#a40300"><b>cor 12</b></font>
# <font color="#930000"><b>cor 13</b></font>
# 
# <br>
# 
# **TOTAL: 50 cores** -->

# In[5]:


# cores por grupo
cores_grupo = {
    'grupo 1':'#142611',
    'grupo 2':'#85D907',
    'grupo 3':'#F2CB07',
    'grupo 4':'#cb97d4',
    'grupo 5':'#91F2E9',
    'grupo 6':'#8a8a8a',
    'grupo 7':'#D9430D'
}


# ### <br>
# 
# ### identificadores por grupo
# 
# preciso criar listas para identificar em qual grupo cada família está. 

# In[6]:


grupo1 = ['Alligatoridae']
grupo2 = ['Chelidae', 'Chelydridae', 'Dermochelyidae', 'Cheloniidae', 'Emydidae', 'Geoemydidae', 
          'Testudinidae', 'Kinosternidae', 'Trionychidae', 'Podocnemididae']
grupo3 = ['Amphisbaenidae']
grupo4 = ['Dactyloidae','Agamidae','Chamaeleonidae','Iguanidae','Hoplocercidae','Leiosauridae',
          'Polychrotidae','Liolaemidae','Phrynosomatidae','Tropiduridae']
grupo5 = ['Scincidae','Anguidae','Lacertidae','Gymnophthalmidae','Helodermatidae','Xantusiidae',
          'Gekkonidae','Phyllodactylidae','Sphaerodactylidae','Varanidae','Teiidae']
grupo6 = ['Anomalepididae','Leptotyphlopidae','Typhlopidae']
grupo7 = ['Dipsadidae','Natricidae','Homalopsidae','Colubridae','Lamprophiidae','Pythonidae',
          'Boidae','Aniliidae','Loxocemidae','Elapidae','Tropidophiidae','Xenopeltidae','Viperidae']

# todos os grupos
grupos = [grupo1, grupo2, grupo3, grupo4, grupo5, grupo6, grupo7]

# nomes dos grupos para exibição
nomes_grupos = {
    'grupo 1':'Crocodylia',
    'grupo 2':'Testudines',
    'grupo 3':'Amphisbaenia', 
    'grupo 4':'Sauria - Iguania',
    'grupo 5':'Sauria - Scleroglossa',
    'grupo 6':'Serpentes - Scolecophidia',
    'grupo 7':'Alethinophidia'
}


# ## Waffle Charts
# 
# ----
# 
# ### 1- Orders

# In[7]:


def calcPercentages(df, col='order', discard_col= 'index'):
    
    if discard_col == 'index':
        temp = df.reset_index()
    else:
        temp = df
    
    percent = temp.groupby(col).count()[discard_col].reset_index().rename(
                                                                    columns={discard_col:'counts'})
    percent['percent'] = percent['counts'] / percent['counts'].sum()
    percent['percent'] = percent['percent'] * 100
    
    return percent


# In[8]:


percent = calcPercentages(NewTable, col='order')
percent = percent[percent['order'].isin(ordens)].copy()

percent


# In[9]:


# adicionando coluna com as cores por ordem
percent['cores'] = percent['order'].apply(lambda x: cores_ordem[x])


# In[10]:


percent.sort_values('percent', inplace=True)


# In[11]:


# standard figure
fig1 = plt.figure(
    FigureClass=Waffle, 
    rows=10, 
#     columns=10, 
#     rounding_rule='nearest',
    values=[round(i) for i in percent['percent']],
    colors=list(percent['cores']),
    title={
        'label': 'Orders', 
        'loc': 'center',
        'fontdict': {
            'fontsize':20
        }
    },
    labels=["{0} ({1}%)".format(k, round(v, 2)) for k, v in zip(percent['order'], percent['percent'])],
    legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1), 'fontsize':12},
    icon_size=18,
    vertical= True,
    icon_legend=True,
#     legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data), 'framealpha': 0},
    figsize=(10, 6)  # figsize is a parameter of matplotlib.pyplot.figure
)

plt.savefig('./graphs/waffles/orders.svg')
plt.savefig('./graphs/waffles/orders.png')

plt.show()


# <br>
# 
# ## Idea:
# 
# 
# make one waffle per group of the color palette and, then, another waffle to the families of each group.

# In[12]:


def identificaGrupo(grupos, familia):
    for i in range(len(grupos)):
        if familia in grupos[i]:
            return f'grupo {i+1}'
    return 'Nan'


# In[13]:


NewTable['grupo'] = NewTable['family'].apply(lambda x: identificaGrupo(grupos, x))


# In[14]:


percent = calcPercentages(NewTable, col='grupo')
percent = percent[percent['grupo'] != 'Nan']

# adicionando coluna com as cores por ordem
percent['cores'] = percent['grupo'].apply(lambda x: cores_grupo[x])

# ordenando percentuais
# percent.sort_values('percent', inplace=True)


# In[15]:


percent['nomes_exibicao'] = percent['grupo'].apply(lambda x: nomes_grupos[x])


# In[16]:


# standard figure
fig1 = plt.figure(
    FigureClass=Waffle, 
    rows=10, 
#     columns=10, 
#     rounding_rule='nearest',
    values=[round(i,2) for i in percent['percent']],
    colors=list(percent['cores']),
    title={
        'label': '"% per groups (Total: 23096 specimens)"', 
        'loc': 'center',
        'fontdict': {
            'fontsize':20
        }
    },
    labels=["{0} ({1}%)".format(k, round(v, 2)) for k, v in zip(percent['nomes_exibicao'], percent['percent'])],
    legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1), 'fontsize':12},
    icon_size=18,
    vertical= True,
    icon_legend=True,
#     legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data), 'framealpha': 0},
    figsize=(10, 6)  # figsize is a parameter of matplotlib.pyplot.figure
)

plt.savefig('./graphs/waffles/groups.svg')
plt.savefig('./graphs/waffles/groups.png')

plt.show()


# <br>
# 
# ### a waffle for the families within each group

# In[17]:


NewTable['grupo'].value_counts()


# In[18]:


# 1. filtrar tabela por grupo
temp = NewTable[NewTable['grupo'] == 'grupo 7'].copy()

# 2. calcular percentagens
percent = calcPercentages(temp, col='family')

# 3. identificar cores
percent['cores'] = percent['family'].apply(lambda x: cores_familia[x])

# ordenando percentuais
# percent.sort_values('percent', inplace=True)
total = percent['counts'].sum()

# nome do grupo para exibição
nome = nomes_grupos['grupo 7']

# standard figure
fig1 = plt.figure(
    FigureClass=Waffle, 
    rows=10, 
#     columns=10, 
#     rounding_rule='nearest',
    values=[round(j,2) for j in percent['percent']],
    colors=list(percent['cores']),
    title={
        'label': f'{nome} (Total: {total} specimens)', 
        'loc': 'center',
        'fontdict': {
            'fontsize':20
        }
    },
    labels=["{0} ({1}%)".format(k, round(v, 2)) for k, v in zip(percent['family'], percent['percent'])],
    legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1), 'fontsize':12},
    icon_size=18,
    vertical= True,
    icon_legend=True,
#     legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data), 'framealpha': 0},
    figsize=(10, 6)  # figsize is a parameter of matplotlib.pyplot.figure
)

plt.savefig('./graphs/waffles/groups/group7.svg')
plt.savefig('./graphs/waffles/groups/group7.png')

plt.show()


# In[19]:


for i in range(len(grupos)-2):
    
    # 1. filtrar tabela por grupo
    temp = NewTable[NewTable['grupo'] == f'grupo {i+1}'].copy()

    # 2. calcular percentagens
    percent = calcPercentages(temp, col='family')

    # 3. identificar cores
    percent['cores'] = percent['family'].apply(lambda x: cores_familia[x])

    # ordenando percentuais
#     percent.sort_values('percent', inplace=True)
    total = percent['counts'].sum()
    
    # nome do grupo para exibição
    nome = nomes_grupos[f'grupo {i+1}']
    
    # standard figure
    fig1 = plt.figure(
        FigureClass=Waffle, 
        rows=10, 
    #     columns=10, 
    #     rounding_rule='nearest',
        values=[j for j in percent['percent']],
        colors=list(percent['cores']),
        title={
            'label': f'{nome} (Total: {total} specimens)', 
            'loc': 'center',
            'fontdict': {
                'fontsize':20
            }
        },
        labels=["{0} ({1}%)".format(k, round(v, 2)) for k, v in zip(percent['family'], percent['percent'])],
        legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1), 'fontsize':12},
        icon_size=18,
        vertical= True,
        icon_legend=True,
    #     legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data), 'framealpha': 0},
        figsize=(10, 6)  # figsize is a parameter of matplotlib.pyplot.figure
    )

#     plt.savefig(f'./graphs/waffles/grupos/group{i+1}.svg')
    plt.savefig(f'./graphs/waffles/groups/group{i+1}.png')

# plt.show()


# <br>
# 
# -----
# 
# ### 2- Orders per family

# In[20]:


family_counts = NewTable['family'].value_counts().reset_index()
family_counts.columns = ['family', 'count']


# In[21]:


NewTable.sort_values('order', inplace=True)


# In[22]:


NewTable[NewTable['family'] == '#n/d']['order']


# In[23]:


d = defaultdict()

index=0
for family in NewTable['family'].unique():
    
    # comentar na reunião (ordem Caudata e Serpentes)
    if family == 'Nan' or family == '#n/d' or family == 'Plethodontidae':
        continue
    # filtrando a base e calculando percentuais
    temp = calcPercentages(NewTable[NewTable['family']==family], col='order')
    temp.sort_values('percent', inplace=True)
    temp = temp[temp['order'].isin(ordens)]
    
    # criando coluna de cores
    temp['cores'] = temp['order'].apply(lambda x:cores_ordem[x])
    
    # contagem
    count = family_counts[family_counts['family'] == family]['count'].values[0] 
       
    index +=1
    
    #dict for chart
    d[(5,10,index)]= { 
        'rows':10, 
    #     columns=10, 
    #     rounding_rule='floor',
        'values':list(temp['percent']),
        'colors':list(temp['cores']),
        # p.s.: thousands separator is: ,
        'title':{
            'label': f'Family: {family}\nTotal of registers: {count}'.replace(',','.'),
            'loc': 'left', 'fontsize':18},
        'icon_legend':True,
    }
        
d = dict(d)
# d


# #### Making `waffle charts`

# In[24]:


teste = plt.figure(
    FigureClass= Waffle,
    plots= d,
    rows=10, 
#     columns=10, 
    vertical=True, 
    block_aspect_ratio=1.2,
    legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)},
    figsize=(35, 35)  # figsize is a parameter of matplotlib.pyplot.figure
    
)

# saving charts
plt.savefig('./graphs/waffles/families.svg')
plt.savefig('./graphs/waffles/families.png')


# <br>
# 
# **The end!**
# 
# -----
