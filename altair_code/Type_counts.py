#!/usr/bin/env python
# coding: utf-8

# # Type charts
# 
# By **Franklin Oliveira**

import numpy as np
import pandas as pd


# pacote para visualização principal
import altair as alt
import streamlit as st
from data_utils import *


# habilitando renderizador para notebook
# alt.renderers.enable('notebook')
# alt.renderers.enable('default')


def timeX_collector_countTypeY(NewTable: pd.DataFrame, app_version, colors):

    cores_familia = colors[0]
        # database
    db = NewTable.groupby(['year_collected', 'collector_full_name', 'type_status', 'family']).count()['class'].reset_index().rename(columns={'class':'counts'})

    sort_list = db.sort_values('year_collected')['year_collected'].unique()
    time_min = sort_list.min()
    time_max = sort_list.max()

    graph = alt.Chart(db, height=900, width= 400, title='Registers Type by collector').mark_point(filled=False).encode(
        x = alt.X('year_collected:Q', title='Description Year',
                scale= alt.Scale(domain=[time_min, time_max])),
        y = alt.Y('collector_full_name:N', title= 'Collector name', sort=alt.EncodingSortField('year_collected',op='min',order='ascending')),
    #               sort=genus_order),
        color= alt.Color('family:N',
                        legend=None,
                        scale= alt.Scale(domain= list(cores_familia.keys()), range=list(cores_familia.values()))), 
        size= alt.Size('counts', title='Counts',
                    legend= None,
                    scale=alt.Scale(range=[30,500])),
        order= alt.Order('counts', sort='descending'),  # smaller points in front
        shape= alt.Shape('type_status:N', title='Type',
                        legend=None), 
        tooltip= [alt.Tooltip('family', title='family'),
                alt.Tooltip('type_status', title='type'),
                alt.Tooltip('year_collected', title='description year'),
                alt.Tooltip('counts', title='counts'),
                alt.Tooltip('collector_full_name', title='collector')]
    )

    graph = graph.configure_title(fontSize=16).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    ).configure_legend(
        labelFontSize=12,
        titleFontSize=12
    )

    return graph

def timeX_countTypeY(NewTable: pd.DataFrame, app_version, colors):

    cores_familia = colors[0]
        # database
    db = NewTable.groupby(['year_collected', 'type_status']).count()['class'].reset_index().rename(columns={'class':'counts'})

    sort_list = db.sort_values('year_collected')['year_collected'].unique()
    time_min = sort_list.min()
    time_max = sort_list.max()

    graph = alt.Chart(db, height=900, width= 400, title='Registers by Type').mark_point(filled=False).encode(
        x = alt.X('year_collected:Q', title='Year Collected',
                scale= alt.Scale(domain=[time_min, time_max])),
        y = alt.Y('type_status:N', title= 'Type', sort=alt.EncodingSortField('year_collected',op='min',order='ascending')),
    #               sort=genus_order), 
        size= alt.Size('counts', title='Counts',
                    legend= None,
                    scale=alt.Scale(range=[30,500])),
        order= alt.Order('counts', sort='descending'),  # smaller points in front
        shape= alt.Shape('type_status:N', title='Type',
                        legend=None), 
        tooltip= [alt.Tooltip('type_status', title='type'),
                alt.Tooltip('year_collected', title='description year'),
                alt.Tooltip('counts', title='counts')]
    )

    graph = graph.configure_title(fontSize=16).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    ).configure_legend(
        labelFontSize=12,
        titleFontSize=12
    )

    return graph
