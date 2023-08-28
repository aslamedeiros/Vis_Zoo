import numpy as np
import pandas as pd
import streamlit as st


import altair as alt

from data_utils import *

# Novo teste
alt.data_transformers.enable('default', max_rows=None)


def typeY_by_timeX(db,app_version,colors):
    # Transform Data
    teste = db[['min_depth','family','order', 'year_cataloged', 'qualifier', 'catalog_number', 
                  'genus', 'species', 'type_status']].copy()

    temp = teste.groupby(['type_status','year_cataloged', 'family', 'order']).count()['genus'].reset_index().rename(columns={
        'genus':'counts'
    })

    select_type = alt.selection_multi(fields= ['type_status'], bind='legend')
    select_family = alt.selection_multi(fields= ['family'], bind='legend')

    base = temp[(temp['type_status'] != 'nan') & (temp['type_status'] != 'Non-type')].sort_values('year_cataloged')

    x_labels = list(base.sort_values('year_cataloged')['year_cataloged'].unique())
    y_labels = base['family'].unique()
    types = base['type_status'].unique()
    counts = base['counts'].unique()
    counts = [counts.min(), counts.max()]
    families = base['family'].unique()

    if x_labels[0]==0:
        x_labels=x_labels[1:]

    # Base Info
    colorBase = alt.Color('family:N', title='Family',
                        scale= alt.Scale(domain=y_labels, range=[colors[0][a] for a in y_labels]),
                        legend= None)
    sizeBase = alt.Size('counts:Q', title='Counts', scale=alt.Scale(domain= counts, range=[30,270]),legend= None)
    shapeBase = alt.Shape('type_status:N', title='Types', legend= None,)
    tooltipBase = [alt.Tooltip('family', title='family'),
                alt.Tooltip('type_status', title='type'),
                alt.Tooltip('year_cataloged', title='year_cataloged'),
                alt.Tooltip('counts', title='#registers')]
    orderBase = alt.Order('types_status:N', sort='descending')  # smaller points in front

    # Select
    select_all = alt.selection_multi(fields = ['type_status','year_cataloged', 'family', 'order'], empty='none')

    # Graphs
    tipo = alt.Chart(base, height=40, width= 400, title='Types per Family').mark_point(filled=False).encode(
        x = alt.X('year_cataloged:O', title='',
                scale= alt.Scale(domain=x_labels),
                axis=alt.Axis(grid=True,gridOpacity=0.2,orient='top')),
        y = alt.Y("id:O",
            title=y_labels[0],
            axis=alt.Axis(ticks=False, grid=True,gridOpacity=0.1,labels=False,titleAngle=0,titleAlign='right',domain=False),
            scale=alt.Scale(),),
        color= colorBase, size= sizeBase, order= orderBase, 
        shape= shapeBase, tooltip= tooltipBase,
    ).transform_window(
        id='rank()',
        groupby=['family','year_cataloged'],
        ).add_selection(select_type, select_family,select_all).transform_filter(select_type).transform_filter(select_family).transform_filter(
        alt.FieldEqualPredicate(field='family', equal=y_labels[0])
    )


    for a in range(len(y_labels)-2):
        t1 = alt.Chart(base, height=40, width= 400,).mark_point(filled=False).encode(
        x = alt.X('year_cataloged:O', title='',
                scale= alt.Scale(domain=x_labels),
                axis=alt.Axis(grid=True,gridOpacity=0.2,labels=False,domain=False,ticks=False,)),
        y = alt.Y("id:O",
            title=y_labels[a+1],
            axis=alt.Axis(ticks=False, grid=True,gridOpacity=0.1,labels=False,titleAngle=0,titleAlign='right',domain=False),
            scale=alt.Scale(),),
        color= colorBase, size= sizeBase, order= orderBase,
        shape= shapeBase, tooltip= tooltipBase,
        ).transform_window(
        id='rank()',
        groupby=['family','year_cataloged'],
        ).add_selection(select_type, select_family,select_all).transform_filter(select_type).transform_filter(select_family).transform_filter(
        alt.FieldEqualPredicate(field='family', equal=y_labels[a+1])
        )
        
        if a%2==0:
            t1 = alt.Chart(base,height=40, width= 400,).mark_rect(color='#F3FBE7').encode(x = alt.X('year_cataloged:O', 
                                                                                                    title='',
                scale= alt.Scale(domain=x_labels)),)+t1
        
        tipo = alt.vconcat(tipo,t1,spacing=-50)
        

    t1 = alt.Chart(base, height=40, width= 400,).mark_point(filled=False).encode(
        x = alt.X('year_cataloged:O', title='',
                scale= alt.Scale(domain=x_labels),
                axis=alt.Axis(grid=True,gridOpacity=0.2,)),
        y = alt.Y("id:O",
            title=y_labels[a+2],
            axis=alt.Axis(ticks=False, grid=True,gridOpacity=0.1,labels=False,titleAngle=0,titleAlign='right',domain=False),
            scale=alt.Scale(),),
        color= colorBase, size= sizeBase, order= orderBase,
        shape= shapeBase, tooltip= tooltipBase,
        ).transform_window(
        id='rank()',
        groupby=['family','year_cataloged'],
        ).add_selection(select_type, select_family,select_all).transform_filter(select_type).transform_filter(select_family).transform_filter(
        alt.FieldEqualPredicate(field='family', equal=y_labels[a+2])
        )
        
    if a%2!=0:
        t1 = alt.Chart(base,height=40, width= 400,).mark_rect(color='#F3FBE7').encode(x = alt.X('year_cataloged:O', 
                                                                                                    title='',
                scale= alt.Scale(domain=x_labels)),)+t1
        
    tipo = alt.vconcat(tipo,t1,spacing=-50)

    # Part II
    point = alt.Chart(db,height=400, width=10).mark_point(opacity=0.7,size=30,filled=False).encode(
            y=alt.Y("id:O",
                title=None,
                axis=alt.Axis(ticks=False, grid=True,gridOpacity=0.3,domain=False,labels=False),                ),
            x=alt.X('family', type='ordinal',title=None,
                    axis=alt.Axis(grid=True,gridOpacity=0.3,domain=False,ticks=False,labels=False)),
            color= colorBase,
            shape= shapeBase,
            tooltip= alt.Tooltip(['year_cataloged', 'family', 'genus', 'species'  ,'catalog_number','type_status'])
            ).transform_window(
            id='rank()',
            groupby=['year_cataloged','family']
            ).add_selection(select_family).transform_filter(select_all)

    regs = alt.Chart(db,height=401,width=80).mark_text(opacity=0.7,).encode(
            y=alt.Y("id:O",
                title=None,
                axis=alt.Axis(ticks=False, grid=True,gridOpacity=0.3,domain=False,labels=False),
                ),
            text='catalog_number',
            tooltip= alt.Tooltip(['year_cataloged', 'family',  'family', 'genus', 'species'  ,'catalog_number','type_status'])
            ).transform_window(
            id='rank()',
            groupby=['year_cataloged','family']
            ).transform_filter(select_all)

    regs_auth = alt.Chart(db,height=401,width=150).mark_text(opacity=0.7,).encode(
            y=alt.Y("id:O",
                title=None,
                axis=alt.Axis(ticks=False, grid=True,gridOpacity=0.3,domain=False,labels=False),
                ),
            text='author_full',
            tooltip= alt.Tooltip(['year_cataloged', 'family', 'family', 'genus', 'species'  ,'catalog_number','type_status'])
            ).transform_window(
            id='rank()',
            groupby=['year_cataloged','family']
            ).transform_filter(select_all)

    chart2 = alt.Chart(db,height=30, width=90+150+10).mark_text(text='REGISTERS:',fontSize=20,align='right').transform_filter(select_all)
    chart3 = alt.hconcat(point,regs,regs_auth,spacing=5)

    # Aggregate 
    tipo = alt.hconcat(tipo,alt.vconcat(chart2, chart3, spacing=5)
           ).configure_title(fontSize=16).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    ).configure_legend(
        labelFontSize=12,
        titleFontSize=12
    ).configure_view(stroke=None
    ).configure_legend(
        orient='right',
        direction='vertical',
        offset=-360,
        symbolDirection='vertical')

    return tipo
