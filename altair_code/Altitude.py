
import numpy as np
import pandas as pd
import streamlit as st


import altair as alt

from data_utils import *


from itertools import compress

def familyX_altitudeY(NewTable, app_version, colors):

  cores_familia = colors[0]
  alt.data_transformers.disable_max_rows()

  # subsetting
  teste = NewTable[['altitude','family','order',
                    #'suborder',
                    'year_collected', 
                    #'qualifier',
                    'catalog_number', 
                    'genus', 'species', 
                    #'subspecies'
                    ]].copy()

  # sorting
  teste = teste.sort_values(['altitude','family'])

  # dropping na
  teste.dropna(subset=['altitude'], inplace=True)

  # making sure altitude is a floating point number
  teste['altitude'] = teste['altitude'].astype(float)

  # removing outlier
  teste = teste[teste['altitude'] < 7000].copy()

  # database
  db = teste[teste['family'] != "#n/d"]

  # aux. variables
  ordens = list(cores_ordem.keys())
  cores = list(cores_ordem.values())

  #color_pal = alt.condition(alt.FieldOneOfPredicate("familia",new_fam), alt.Color('family:N', title= 'Family', legend = None, scale=alt.Scale(domain= list(cores_familia.keys()), range= list(cores_familia.values()))), alt.value('lightgray'))

  temp = alt.Chart(db, title='Altitude per Family').mark_circle().encode(
      x = alt.X('family', type='nominal', title='Family', 
                sort= alt.EncodingSortField('altitude', op='mean', order='ascending')),
      y = alt.Y('altitude', type='quantitative', title='Altitude (in meters)'),
      color= alt.Color('family:N', title= 'Family', 
                    legend = None,
                    scale=alt.Scale(domain= list(cores_familia.keys()), 
                                    range= list(cores_familia.values()))),
      tooltip = [alt.Tooltip('catalog_number', title='number in catalogue'),
              alt.Tooltip('genus', title='Genus'),
              alt.Tooltip('species', title='Species'),
              #alt.Tooltip('subspecies', title='Subspecies'),
              #alt.Tooltip('qualifier', title='qualifier'),
              alt.Tooltip('year_collected', title='year collected'),
              alt.Tooltip('altitude', title='altitude')],

  )

  return temp


def genusX_altitudeY(data, app_version, colors):

  cores_familia = colors[0]
  data = data[['altitude','species','genus','order', 
                #'suborder',
                 'family', 'year_collected', 
                 #'qualifier',
                  'catalog_number', 
                 #'subspecies'
                  ]]

  # dropping na
  data = data.dropna(subset=['altitude'])
  # making sure altitude is a floating point number
  data['altitude'] = data['altitude'].astype(float)
  # removing outlier
  data = data[data['altitude'] < 7000].copy()

  # ordering x-axis per mean altitude - OUTLIER: ordem nula
  graph = alt.Chart(data, title='Altitude per Genus',
                  width= 900, height=300).mark_circle().encode(
      x = alt.X('genus', type='nominal', title='Genus',
              sort=alt.EncodingSortField('altitude', op="mean", order="ascending")),
      y = alt.Y('altitude:Q', title='Altitude (in meters)'),
      color = alt.Color('family:N', title='Family',
                      legend=None,
                      scale= alt.Scale(domain=list(cores_familia.keys()), range= list(cores_familia.values()))),
      tooltip = alt.Tooltip(['catalog_number', 'genus','species',
                          #'subspecies', 
                          'order',
                          #'suborder',
                          #'qualifier',
                          'year_collected','altitude'])
  )

  graph = graph.configure_title(fontSize=16).configure_axis(
      labelFontSize=12,
      titleFontSize=12
  ).configure_legend(
      labelFontSize=12,
      titleFontSize=12
  )

  # g.save('./graphs/altitude/genus/altitude-per-genus.html')
  # g
  return graph

def familyX_depthY(data, app_version, colors):

  cores_familia = colors[0]
  # subsetting
  teste = data[['min_depth','family','infraorder', 'year_collected', 'qualifier', 'catalog_number', 
                    'genus', 'species', 'collector_full_name', 'country','state','locality', 'type_status']].copy()

  # sorting
  teste = teste.sort_values(['min_depth','family'])

  # dropping na
  teste.dropna(subset=['min_depth'], inplace=True)

  # making sure altitude is a floating point number
  teste['min_depth'] = teste['min_depth'].astype(float)

  # extremes for scale
  max_y = teste['min_depth'].max()
  min_y = teste['min_depth'].min()

  temp = alt.Chart(teste, title='Depth per Family', width=800, height=400).mark_circle().encode(
    x = alt.X('family', type='nominal', title='Family', 
              sort= alt.EncodingSortField('min_depth', op='max', order='ascending')),
    y = alt.Y('min_depth', type='quantitative', title='Depth (in meters)',
              scale = alt.Scale(domain=[max_y, min_y])),
        color= alt.Color('family:N', title='Family', 
                     scale=alt.Scale(domain=list(cores_familia.keys()), 
                                     range=list(cores_familia.values())),
                      legend=None),
    tooltip = alt.Tooltip(['catalog_number', 'infraorder','family','genus','species', 'type_status',
                            'qualifier', 'year_collected','collector_full_name',
                            'country', 'state', 'locality', 'min_depth'])
  )

  temp = temp.configure_title(fontSize=16).configure_axis(
      labelFontSize=12,
      titleFontSize=12
  ).configure_legend(
      labelFontSize=12,
      titleFontSize=12
  )

  return temp


def familyX_depthY_pol(data, app_version, colors):

  cores_familia = colors[0]
  # subsetting
  teste = data[['min_depth','family', 'year_collected', 'qualifier', 'catalog_number', 
                    'genus', 'species', 'collector_full_name', 'country','state','locality', 'type_status']].copy()

  # sorting
  teste = teste.sort_values(['min_depth','family'])

  # dropping na
  teste.dropna(subset=['min_depth'], inplace=True)

  # making sure altitude is a floating point number
  teste['min_depth'] = teste['min_depth'].astype(float)

  # extremes for scale
  max_y = teste['min_depth'].max()
  min_y = teste['min_depth'].min()

  temp = alt.Chart(teste, title='Depth per Family', width=800, height=400).mark_circle().encode(
    x = alt.X('family', type='nominal', title='Family', 
              sort= alt.EncodingSortField('min_depth', op='max', order='ascending')),
    y = alt.Y('min_depth', type='quantitative', title='Depth (in meters)',
              scale = alt.Scale(domain=[max_y, min_y])),
        color= alt.Color('family:N', title='Family', 
                     scale=alt.Scale(domain=list(cores_familia.keys()), 
                                     range=list(cores_familia.values())),
                      legend=None),
    tooltip = alt.Tooltip(['catalog_number', 'family','genus','species', 'type_status',
                            'qualifier', 'year_collected','collector_full_name',
                            'country', 'state', 'locality', 'min_depth'])
  )

  temp = temp.configure_title(fontSize=16).configure_axis(
      labelFontSize=12,
      titleFontSize=12
  ).configure_legend(
      labelFontSize=12,
      titleFontSize=12
  )

  return temp