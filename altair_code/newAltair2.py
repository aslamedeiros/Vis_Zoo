import numpy as np
import pandas as pd
import streamlit as st


import altair as alt

from data_utils import *

# Novo teste
alt.data_transformers.enable('default', max_rows=None)


def typeY_by_timeX(db,app_version,colors):
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
    # x_labels = x_labels + ['N/A']
    # base.year_cataloged.replace(0,'N/A', inplace=True)
    # db.year_cataloged.replace(0,'N/A', inplace=True)
    # base.year_cataloged.fillna('N/A')
    # db.year_cataloged.fillna('N/A')


    select_all = alt.selection_multi(fields = ['type_status','year_cataloged', 'family', 'order'], empty='none')#,on="mouseover")

    tipo = alt.Chart(base, height=40, width= 400, title='Types per Family').mark_point(filled=False).encode(
        x = alt.X('year_cataloged:O', title='',
                scale= alt.Scale(domain=x_labels),
                axis=alt.Axis(grid=True,gridOpacity=0.2,orient='top')),
        y = alt.Y("id:O",
            title=y_labels[0],
            axis=alt.Axis(ticks=False, grid=True,gridOpacity=0.1,labels=False,titleAngle=0,titleAlign='right',domain=False),
            scale=alt.Scale(),),
        color= alt.Color('family:N', title='Family',
                        scale= alt.Scale(domain=y_labels, 
                                        range=[colors[0][a] for a in y_labels]),
                        legend= None),#alt.Legend(columns=2, symbolLimit=102,orient= 'right')), 
        size= alt.Size('counts:Q', title='Counts', scale=alt.Scale(domain= counts, range=[30,270]),
                    legend= None), #alt.Legend(orient= 'right', direction= 'horizontal')),
        order= alt.Order('type_status', sort='descending'),  # smaller points in front
        shape= alt.Shape('type_status:N', title='Types', 
                        legend= None,#alt.Legend(columns=4,orient='right'),
                        #scale= alt.Scale(domain=['Holotype', 'Neotype','Paratype'],
                        #                range=['triangle', 'square', 'cross'])
                        ),
        tooltip= [alt.Tooltip('family', title='family'),
                alt.Tooltip('type_status', title='type'),
                alt.Tooltip('year_cataloged', title='year_cataloged'),
                alt.Tooltip('counts', title='#registers')]
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
            color= alt.Color('family:N', title='Family',
                        scale= alt.Scale(domain=y_labels, 
                                        range=[colors[0][a] for a in y_labels]),
                        #legend= alt.Legend(columns=2, symbolLimit=102,orient= 'left')
                            ), 
        size= alt.Size('counts:Q', title='Counts', scale=alt.Scale(domain= counts, range=[30,270]),
                    #legend= alt.Legend(orient= 'left', direction= 'horizontal')
                    ),
        order= alt.Order('type_status', sort='descending'),  # smaller points in front
        shape= alt.Shape('type_status:N', title='Types', 
                        #legend= alt.Legend(columns=4),
                        #scale= alt.Scale(domain=['Holotype', 'Neotype','Paratype'],
                        #                range=['triangle', 'square', 'cross'])
                        ),
        tooltip= [alt.Tooltip('family', title='family'),
                alt.Tooltip('type_status', title='type'),
                alt.Tooltip('year_cataloged', title='year_cataloged'),
                alt.Tooltip('counts', title='#registers')]
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
            color= alt.Color('family:N', title='Family',
                        scale= alt.Scale(domain=y_labels, 
                                        range=[colors[0][a] for a in y_labels]),
                        #legend= alt.Legend(columns=2, symbolLimit=102,orient='left')
                            ), 
        size= alt.Size('counts:Q', title='Counts', scale=alt.Scale(domain= counts, range=[30,270]),
                    #legend= alt.Legend(orient= 'left', direction= 'horizontal')
                    ),
        order= alt.Order('type_status', sort='descending'),  # smaller points in front
        shape= alt.Shape('type_status:N', title='Types', 
                        #legend= alt.Legend(columns=4),
                        #scale= alt.Scale(domain=['Holotype', 'Neotype','Paratype'],
                        #                range=['triangle', 'square', 'cross'])
                        ),
        tooltip= [alt.Tooltip('family', title='family'),
                alt.Tooltip('type_status', title='type'),
                alt.Tooltip('year_cataloged', title='year_cataloged'),
                alt.Tooltip('counts', title='#registers')]
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

    varX = 'family'
    varY = 'year_cataloged'
    varColor =  'family'

    point = alt.Chart(db,height=400, width=10).mark_point(opacity=0.7,size=30,filled=False).encode(
            y=alt.Y("id:O",
                title=None,
                axis=alt.Axis(ticks=False, grid=True,gridOpacity=0.3,domain=False,labels=False),
                scale=alt.Scale(#reverse=True
                ),
                ),
            x=alt.X('family', type='ordinal',title=None,#scale= alt.Scale(domain=['n']),
                    axis=alt.Axis(grid=True,gridOpacity=0.3,domain=False,ticks=False,labels=False)),
            color= alt.Color(varColor, type ='nominal', title='Family', 
                            scale=alt.Scale(domain=y_labels, 
                                        range=[colors[0][a] for a in y_labels]),
                            #legend= alt.Legend(columns=2, symbolLimit= 58,orient='bottom-left')
                            ),
            shape= alt.Shape('type_status:N', title='Types', 
                        #legend= alt.Legend(columns=4),
                        #scale= alt.Scale(domain=['Holotype', 'Neotype','Paratype'],
                        #                range=['triangle', 'square', 'cross'])
                        ),
            tooltip= alt.Tooltip([varY, varX,  'family', 'genus', 'species'  ,'catalog_number','type_status'])
            ).transform_window(
            id='rank()',
            groupby=[varY,varX]
            ).add_selection(select_family).transform_filter(select_all)

    regs = alt.Chart(db,height=401,width=80).mark_text(opacity=0.7,).encode(
            y=alt.Y("id:O",
                title=None,
                axis=alt.Axis(ticks=False, grid=True,gridOpacity=0.3,domain=False,labels=False),
                #scale=alt.Scale(reverse=True),
                ),
            #x=alt.X(varX, type='ordinal',title=None,#scale= alt.Scale(domain= x_labels),
            #        axis=alt.Axis(grid=False,gridOpacity=0.3,domain=False,ticks=False,labels=False)),
            text='catalog_number',
            tooltip= alt.Tooltip([varY, varX,  'family', 'genus', 'species'  ,'catalog_number','type_status'])
            ).transform_window(
            id='rank()',
            groupby=[varY,varX]
            ).transform_filter(select_all)

    regs_auth = alt.Chart(db,height=401,width=150).mark_text(opacity=0.7,).encode(
            y=alt.Y("id:O",
                title=None,
                axis=alt.Axis(ticks=False, grid=True,gridOpacity=0.3,domain=False,labels=False),
                #scale=alt.Scale(reverse=True),
                ),
            #x=alt.X(varX, type='ordinal',title=None,#scale= alt.Scale(domain= x_labels),
            #        axis=alt.Axis(grid=False,gridOpacity=0.3,domain=False,ticks=False,labels=False)),
            text='author_full',
            tooltip= alt.Tooltip([varY, varX, 'family', 'genus', 'species'  ,'catalog_number','type_status'])
            ).transform_window(
            id='rank()',
            groupby=[varY,varX]
            ).transform_filter(select_all)

    # chart3 = alt.Chart(height=250, width=90+150+10).mark_circle(opacity=0)
    chart5 = alt.Chart(db,height=30, width=90+150+10).mark_text(text='REGISTERS:',fontSize=20,align='right').transform_filter(select_all)
    chart4 = alt.hconcat(point,regs,regs_auth,spacing=5)

    #tipo = tipo|regs+point

    tipo = alt.hconcat(tipo,alt.vconcat(chart5, chart4, spacing=5)
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
