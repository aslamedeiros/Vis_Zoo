import altair as alt
import pandas as pd
import streamlit as st
from column_dict import *


def custom_chart(data:pd.DataFrame, app_version, colors):

  axisoptions = data.columns

  cores_familia = colors[0]

  yaxis = st.selectbox(label='y axis', options=axisoptions, index=0)
  groupcount = st.multiselect(label='group by', options=axisoptions)

  data = data.dropna(subset=[yaxis])
  data = data.dropna(subset=groupcount)

  sorted = data.sort_values('year_collected')['year_collected'].unique()
  xmin = sorted.min()
  xmax = sorted.max()

  axis_aggreg = groupcount+['year_collected']
  if yaxis not in axis_aggreg:
    axis_aggreg.append(yaxis)

  show_tooltip = axis_aggreg

  if len(groupcount) > 0:
    data = data.groupby(axis_aggreg).count()['class'].reset_index().rename(columns={'class':'counts'})
    show_tooltip.append('counts')

  if 'family' in axis_aggreg:
    color_pal = alt.Color('family:N', title= 'Family', 
                    legend = None,
                    scale=alt.Scale(domain= list(cores_familia.keys()), 
                                    range= list(cores_familia.values())))
  else:
    color_pal = alt.value('blue')

  graph = alt.Chart(data).mark_point().encode(
    x = alt.X('year_collected', scale=alt.Scale(domain=[xmin,xmax])),
    y = alt.Y(yaxis),
    tooltip = alt.Tooltip(show_tooltip),
    color = color_pal
  )

  if len(groupcount) > 0:
    graph = graph.encode(size = alt.Size('counts', scale=alt.Scale(range=[30,250]), legend=None))

  return graph
