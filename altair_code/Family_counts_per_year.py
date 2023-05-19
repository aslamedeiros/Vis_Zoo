# graph structures by **Franklin Oliveira**

import numpy as np
import pandas as pd

# visualization
import altair as alt
import streamlit as st
from data_utils import *


def timeX_family_countY(NewTable, app_version, colors):

    cores_familia = colors[0]
    alt.renderers.enable('default')
    alt.data_transformers.disable_max_rows()

    teste = NewTable.groupby(['family','year_collected']).count()['class'].reset_index().rename(
                                                                                        columns={'class':'counts'})

    teste = teste.dropna(subset=['year_collected'])
    teste['family'] = teste['family'].astype(str)
    teste['year_collected'] = teste['year_collected'].astype(int)

    sort_list = teste.sort_values('year_collected')['year_collected'].unique()
    time_min = sort_list.min()
    time_max = sort_list.max()

    graph = alt.Chart(teste,
                width=500, height=500, title='Registers by Families').mark_circle(
                                                                                    size=60).encode(
        x= alt.X('year_collected', title='Collected Year', scale=alt.Scale(domain=[time_min, time_max])),
        y= alt.Y('family', type='nominal', title='Family',
                sort= alt.EncodingSortField(field='year_collected', op='min', order='ascending')),
        size= alt.Size('counts', title='Counts',
                    legend= None, scale=alt.Scale(range=[15,100])),
        color = alt.Color('family:O', title= 'Family',
                        legend= None, scale= alt.Scale(domain= list(cores_familia.keys()), range=list(cores_familia.values()))),
        tooltip = alt.Tooltip(['family', 'year_collected', 'counts'])
    )

    graph = graph.configure_title(fontSize=16).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    ).configure_legend(
        labelFontSize=12,
        titleFontSize=12
    )

    return graph

def timeX_family_countTypeY(NewTable: pd.DataFrame, app_version, colors):

    cores_familia = colors[0]
    alt.renderers.enable('default')
    alt.data_transformers.disable_max_rows()

    NewTable = NewTable.dropna(subset=['type_status'])
    teste = NewTable.groupby(['family','year_collected','type_status']).count()['class'].reset_index().rename(
                                                                                        columns={'class':'counts'})

    teste = teste.dropna(subset=['year_collected'])
    teste['family'] = teste['family'].astype(str)
    teste['year_collected'] = teste['year_collected'].astype(int)
    teste['type_status'] = teste['type_status'].astype(str)

    teste = teste.sort_values(['year_collected'])

    sort_list = teste['year_collected'].unique()
    time_min = sort_list.min()
    time_max = sort_list.max()


    #color_pal = alt.condition(alt.FieldOneOfPredicate("familia",new_fam), alt.Color('family:O', title= 'Family',
    #                    legend= None, scale= alt.Scale(domain= list(cores_familia.keys()), range=list(cores_familia.values())))#, alt.value('lightgray'))

    graph = alt.Chart(teste, height=500, width=250, title='Registers Type by Family').mark_point(filled=False).encode(
    x = alt.X('year_collected:Q', title='Description Year', 
              scale= alt.Scale(domain=[time_min, time_max])),
    y = alt.Y('family:N', title= 'Family', sort= alt.EncodingSortField('year_collected', op='min', order='ascending')),
    color= alt.Color('family:N', title='Family', legend=None,
                    scale= alt.Scale(domain= list(cores_familia.keys()), 
                                     range= list(cores_familia.values()))), 
    size= alt.Size('counts', title='Counts', legend= None,
                   scale=alt.Scale(range=[30,500])),
    order= alt.Order('counts', sort='descending'),  # smaller points in front
    shape= alt.Shape('type_status:N', title='Type', legend= None), 
    tooltip= [alt.Tooltip('family', title='family'),
              alt.Tooltip('type_status', title='type'),
              alt.Tooltip('year_collected:T', title='description year'),
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


def timeX_genus_countTypeY(NewTable: pd.DataFrame, app_version, colors):

    cores_familia = colors[0]
        # database
    db = NewTable.groupby(['year_collected', 'genus', 'type_status', 'family']).count()['class'].reset_index().rename(columns={'class':'counts'})

    db = db.dropna(subset=['year_collected'])
    db['family'] = db['family'].astype(str)
    db['year_collected'] = db['year_collected'].astype(int)
    db['type_status'] = db['type_status'].astype(str)
    db['genus'] = db['genus'].astype(str)

    sort_list = db.sort_values('year_collected')['year_collected'].unique()
    time_min = sort_list.min()
    time_max = sort_list.max()

    graph = alt.Chart(db, height=500, width= 400, title='Registers Type by Genus').mark_point(filled=False).encode(
        x = alt.X('year_collected:Q', title='Description Year',
                scale= alt.Scale(domain=[time_min, time_max])),
        y = alt.Y('genus:N', title= 'Genus', sort=alt.EncodingSortField('year_collected',op='min',order='ascending')),
    #               sort=genus_order),
        color= alt.Color('family:N', title='Family',
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

def timeX_order_countY(NewTable, app_version, colors):

    cores_familia = colors[1]
    alt.renderers.enable('default')
    alt.data_transformers.disable_max_rows()

    teste = NewTable.groupby(['order','year_collected']).count()['class'].reset_index().rename(
                                                                                        columns={'class':'counts'})

    teste = teste.dropna(subset=['year_collected'])
    teste['order'] = teste['order'].astype(str)
    teste['year_collected'] = teste['year_collected'].astype(int)

    sort_list = teste.sort_values('year_collected')['year_collected'].unique()
    time_min = sort_list.min()
    time_max = sort_list.max()

    graph = alt.Chart(teste,
                width=500, height=500, title='Registers by Order').mark_circle(
                                                                                    size=60).encode(
        x= alt.X('year_collected', title='Collected Year', scale=alt.Scale(domain=[time_min, time_max])),
        y= alt.Y('order', type='nominal', title='Order',
                sort= alt.EncodingSortField(field='year_collected', op='min', order='ascending')),
        size= alt.Size('counts', title='Counts',
                    legend= None, scale=alt.Scale(range=[15,100])),
        color = alt.Color('order:O', title= 'Family',
                        legend= None, scale= alt.Scale(domain= list(cores_ordem.keys()), range=list(cores_ordem.values()))),
        tooltip = alt.Tooltip(['order', 'year_collected', 'counts'])
    )

    graph = graph.configure_title(fontSize=16).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    ).configure_legend(
        labelFontSize=12,
        titleFontSize=12
    )

    return graph

def timeX_infraorder_countY(NewTable, app_version, colors):

    cores_ordem = colors[1]
    alt.renderers.enable('default')
    alt.data_transformers.disable_max_rows()

    teste = NewTable.groupby(['infraorder','year_collected']).count()['class'].reset_index().rename(
                                                                                        columns={'class':'counts'})

    teste = teste.dropna(subset=['year_collected'])
    teste['infraorder'] = teste['infraorder'].astype(str)
    teste['year_collected'] = teste['year_collected'].astype(int)

    sort_list = teste.sort_values('year_collected')['year_collected'].unique()
    time_min = sort_list.min()
    time_max = sort_list.max()

    graph = alt.Chart(teste,
                width=500, height=500, title='Registers by Infraorder').mark_circle(
                                                                                    size=60).encode(
        x= alt.X('year_collected', title='Collected Year', scale=alt.Scale(domain=[time_min, time_max])),
        y= alt.Y('infraorder', type='nominal', title='Infraorder',
                sort= alt.EncodingSortField(field='year_collected', op='min', order='ascending')),
        size= alt.Size('counts', title='Counts',
                    legend= None, scale=alt.Scale(range=[15,100])),
        color = alt.Color('infraorder:O', title= 'Family',
                        legend= None, scale= alt.Scale(domain= list(cores_ordem.keys()), range=list(cores_ordem.values()))),
        tooltip = alt.Tooltip(['infraorder', 'year_collected', 'counts'])
    )

    graph = graph.configure_title(fontSize=16).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    ).configure_legend(
        labelFontSize=12,
        titleFontSize=12
    )

    return graph
