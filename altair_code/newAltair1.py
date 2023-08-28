import numpy as np
import pandas as pd
import streamlit as st


import altair as alt

from data_utils import *

# Novo teste
alt.data_transformers.enable('default', max_rows=None)

def titulo(var):
    if 'year' in var:
        return (var.replace('year','')+'_year').replace('_',' ').strip().title()
    else:
        return var.replace('_full_','_').replace('_',' ').title()

def cx_alta(var):
    if 'year' in var:
        return (var.replace('year','')+'_year').replace('_',' ').strip().upper()
    else:
        return var.replace('_full_','_').replace('_',' ').upper()

def dash(dados:pd.DataFrame, varX:str,x_labels, varY:str, y_labels, varColor:str, colors:dict, varSize:str, limSize:list, db:pd.DataFrame):
    # Selects
    select_family = alt.selection_multi(fields= [varColor], bind= 'legend')
    selectX = alt.selection_multi( fields=[varY],empty='none')
    selectXY = alt.selection_multi(fields=[varY,varX],empty='none')

    # Transform Data
    x_labels = [str(x) for x in x_labels]
    dados[varX]=dados[varX].astype('str')

    # Height and width
    h_1 = 13*len(y_labels)
    w_1 = 15.5*len(x_labels)
    w_2 = len(x_labels)*11.5

    colorBase = alt.Color(varColor, type ='nominal', title=titulo(varColor), 
                         scale=alt.Scale(domain=list(colors[0].keys()), range=list(colors[0].values())),
                         legend=None,)

    # Graph 1 - Base
    gBase  = alt.Chart(dados,width=w_1, height=h_1,
                  ).mark_circle().encode(
            x= alt.X(varX, type='ordinal', title = titulo(varX),
                 scale= alt.Scale(domain= x_labels),axis=alt.Axis(grid=True,gridOpacity=.3)),
            y= alt.Y(varY, type='nominal', title = titulo(varY), 
                scale= alt.Scale(domain= y_labels),
                sort=y_labels,axis=alt.Axis(grid=True,gridOpacity=.3)),
            size= alt.Size(varSize, type="quantitative",  title= titulo(varSize),
                       legend=None,
                       scale=alt.Scale(domain= limSize,range=[20, 100], zero=True)),  # range ajusta tamanho do circulo
            order= alt.Order(varSize, sort='descending'),  # smaller points in front    
            color= colorBase,
            tooltip= alt.Tooltip([varY, varX, varSize, varColor])
        ).add_selection(select_family,selectX,selectXY).transform_filter(select_family)

    # Marks
    yMark = alt.Y(varY, type='ordinal',scale= alt.Scale(domain= y_labels),
                axis=alt.Axis(grid=True,gridOpacity=0.5))
    
    gBaseMark1 = alt.Chart(dados,width=w_1, height=h_1).mark_bar(fill='none', stroke='lightgray',strokeOpacity=0.7,size=55).encode(
        y= yMark,
    ).transform_filter(selectX)

    gBaseMark2 = alt.Chart(dados,width=w_1, height=h_1).mark_point( stroke='#FF174b',strokeWidth=1,size=500).encode(
        y=yMark,
        x=alt.X(varX, type='ordinal',scale= alt.Scale(domain= x_labels)),
    ).transform_filter(selectXY)

    
    # Text
    ## Empty
    gTextEmpty= alt.Chart(dados, width=w_2,).mark_text(
                                size=12, text= cx_alta(varY), opacity=0
                            ).encode()

    ## Y
    gTextNameY= alt.Chart(dados, width=w_2,).mark_text(
                                size=18, text= cx_alta(varY),
                            ).encode()
    gTextVarY= alt.Chart(dados, width=w_2,).mark_text(
                                size=16
                            ).encode(
                                text=varY).transform_filter(selectX)
    
    ## X
    gTextNameX= alt.Chart(dados, width=w_2,).mark_text(
                                size=18, text= cx_alta(varX),
                            ).encode()
    gTextVarX= alt.Chart(dados, width=w_2,).mark_text(
                                size=16
                            ).encode(
                                text=varX).transform_filter(selectXY)

    # Graph 2 - Year vs ID
    gYearId = alt.Chart(dados,height=250, width=w_2).mark_circle(opacity=0.7).encode(
        y=alt.Y("id:O", title=None,
            axis=alt.Axis(ticks=False, grid=True,gridOpacity=0.3,domain=False,labels=False),
            scale=alt.Scale(reverse=True),),
        x=alt.X(varX, type='ordinal',title=titulo(varX),scale= alt.Scale(domain= x_labels),
                axis=alt.Axis(grid=True,gridOpacity=0.3,domain=False,ticks=False)),
        color= colorBase,
        size= alt.Size(varSize, type="quantitative",  title= titulo(varSize),
                       legend=None,
                       scale=alt.Scale(domain= limSize,range=[20, 100], zero=True)),
        order= alt.Order(varSize, sort='descending'),
        tooltip= alt.Tooltip([varY, varX,  varColor, varSize])
        ).transform_window(
        id='rank()',
        groupby=[varY,varX]
        ).transform_filter(
        selectX
    ).add_selection(select_family,selectXY).transform_filter(select_family)

    gYearMark = alt.Chart(dados,height=250, width=w_2).mark_bar(fill='none', stroke='#FF174B',size=15).encode(
        x=alt.X(varX, type='ordinal',scale= alt.Scale(domain= x_labels),
                axis=alt.Axis(grid=True,gridOpacity=0.5)),
    ).transform_filter(selectXY)

    # Transforms Data - Registers Level
    db_dash = db.copy()
    db_dash =  db_dash.rename(columns={'determinator_full_name':'Identified_by','year_collected':'year_sampling'})

    db_dash[varX]=db_dash[varX].astype('str')
    db_dash[varX].fillna('N/A', inplace=True)
    db_dash[varX].replace('0','N/A', inplace=True)
    db_dash[varY].fillna('Non-Identified', inplace=True)
    db_dash[varColor].fillna('Non-identified', inplace=True)

    for var in ['order', 'genus', 'species', 'type_status','qualifier']:
        db_dash[var].fillna('Non-Identified', inplace=True) 

    if varY=='collector_full_name':
        base = db_dash[['catalog_number', 'year_cataloged', 'month_cataloged', 'year_sampling',
                        'month_collected', 'lat', 'long', 'state', 'country', 'continent',
                        'region', 'locality', 'min_depth', 'max_depth', 'kingdom', 'phylum',
                        'class', 'order', 'family', 'genus', 'species', 'type_status',
                        'qualifier', 'Identified_by', 'collector_full_name', 'author_full']]

        if 'collector_full_name2' in db_dash.columns:
            base = pd.concat([base,
                    db_dash[['catalog_number', 'year_cataloged', 'month_cataloged', 'year_sampling',
                        'month_collected', 'lat', 'long', 'state', 'country', 'continent',
                        'region', 'locality', 'min_depth', 'max_depth', 'kingdom', 'phylum',
                        'class', 'order', 'family', 'genus', 'species', 'type_status',
                        'qualifier', 'Identified_by','collector_full_name2', 'author_full']][db_dash['collector_full_name2'].notna(
                    )].rename({'collector_full_name2':'collector_full_name'},axis=1)
                    ],
                    ignore_index=True)
        
        if 'collector_full_name3' in db_dash.columns:
            base = pd.concat([base,
                    db_dash[['catalog_number', 'year_cataloged', 'month_cataloged', 'year_sampling',
                        'month_collected', 'lat', 'long', 'state', 'country', 'continent',
                        'region', 'locality', 'min_depth', 'max_depth', 'kingdom', 'phylum',
                        'class', 'order', 'family', 'genus', 'species', 'type_status',
                        'qualifier', 'Identified_by', 'collector_full_name3', 'author_full']][db_dash['collector_full_name3'].notna(
                    )].rename({'collector_full_name3':'collector_full_name'},axis=1)
                    ],
                    ignore_index=True)


        base['collector_full_name']=base['collector_full_name'].str.strip()
        db_dash = base

    # Graph 3 - Family vs Register
    gFamilyId = alt.Chart(db_dash,height=250, width=w_2).mark_circle(opacity=0.7).encode(
        y=alt.Y("number:O", title=None,
            axis=alt.Axis(ticks=False, grid=True,gridOpacity=0.3,domain=False,labels=False),),
        x=alt.X(varColor, type='ordinal',title=titulo(varColor),
                axis=alt.Axis(grid=True,gridOpacity=0.3,domain=False,ticks=True,orient='top'),
                scale=alt.Scale(reverse=True),),
        color= colorBase,
        tooltip= alt.Tooltip(['catalog_number', 'year_cataloged', 'year_sampling','class', 'order', 'family', 
                              'genus', 'species', 'type_status','qualifier', varY, varX,  varColor,'number:O'])
        ).transform_window(
        number='rank()',
        groupby=[varColor,varX,varY]
    ).transform_filter(selectXY)
    
    # Graph
    graph = ((gBaseMark1+ gBase +gBaseMark2)|(gTextNameY & gTextVarY & (gYearMark+gYearId) & gTextEmpty & gTextNameX & gTextVarX & (gFamilyId)))

    return graph.configure_view(stroke=None)


def time_catalogedX_determinatorY_dash(banco,app_version,colors):
    # transforms data
    teste1 = banco.copy()
    teste1.year_cataloged=teste1.year_cataloged.fillna(20000)
    teste1.year_cataloged=teste1.year_cataloged.replace(0,20000)
    teste1.family=teste1.family.fillna('Non-identified')
    teste1['determinator_full_name']=teste1['determinator_full_name'].fillna('Non-Identified')
    teste1['determinator_full_name']=teste1['determinator_full_name'].replace('  ', 'Non-Identified')
    
    base = teste1[['year_cataloged','family','determinator_full_name','class']]
    if 'determinator_full_name2' in teste1.columns:
        base = pd.concat([base,
                  teste1[['year_cataloged','family','determinator_full_name2','class']][teste1['determinator_full_name2'].notna(
                  )].rename({'determinator_full_name2':'determinator_full_name'},axis=1)
                 ],
                 ignore_index=True)

        base = pd.concat([base,
                  teste1[['year_cataloged','family','determinator_full_name3','class']][teste1['determinator_full_name3'].notna(
                  )].rename({'determinator_full_name3':'determinator_full_name'},axis=1)
                 ],
                 ignore_index=True)
    base['determinator_full_name']=base['determinator_full_name'].str.strip()
    
    base = base.groupby(['determinator_full_name','year_cataloged','family']
                         ).count()['class'].reset_index().rename(columns={'class':'registers'})
    
    temp2 = base.copy()
    temp2.sort_values(['year_cataloged', 'determinator_full_name'], inplace=True)
    sorting = list(temp2['determinator_full_name'].unique())
    if 'Non-Identified' in sorting:
        sorting.remove('Non-Identified')
        sorting.append('Non-Identified')
    
    x_labels = list(base.sort_values('year_cataloged')['year_cataloged'].unique())
    y_labels = sorting
    
    base.year_cataloged=base.year_cataloged.replace(20000,'N/A')
    
    x_labels=list(x_labels[:-1])+['N/A']
    
    registers = list(range(min(base.registers), max(base.registers)+50, 50))
    
    for a in base.family.unique():
        if a not in colors[0].keys():
            colors[0][a]='black'
            
    base =  base.rename(columns={'determinator_full_name':'Identified_by'})####
    
    # Creates Graph
    graph = dash(base,'year_cataloged',x_labels, 'Identified_by',y_labels, 'family', colors, 'registers', registers, db = banco)
    
    return graph.properties(title='Counts by Identifier')

def time_collectedX_collectorY_dash(db,app_version,colors): 
    # transforms data  
    teste = db.copy()
    teste.family=teste.family.fillna('Non-identified')
    teste.year_collected=teste.year_collected.fillna(20000)
    teste.year_collected=teste.year_collected.replace(0,20000)
    teste['collector_full_name']=teste['collector_full_name'].fillna('Non-Identified')
    teste['collector_full_name']=teste['collector_full_name'].replace('  ', 'Non-Identified')

    base = teste[['collector_full_name','year_collected', 'family','order','class']]

    if 'collector_full_name2' in teste.columns:
        base = pd.concat([base,
                  teste[['collector_full_name2','year_collected', 'family','order','class']][teste['collector_full_name2'].notna(
                  )].rename({'collector_full_name2':'collector_full_name'},axis=1)
                 ],
                 ignore_index=True)
    
    if 'collector_full_name3' in teste.columns:
        base = pd.concat([base,
                  teste[['collector_full_name3','year_collected', 'family','order','class']][teste['collector_full_name3'].notna(
                  )].rename({'collector_full_name3':'collector_full_name'},axis=1)
                 ],
                 ignore_index=True)


    base['collector_full_name']=base['collector_full_name'].str.strip()

    teste = base.groupby(['collector_full_name','year_collected', 'family','order']).count()['class'].reset_index().rename(columns=
                                                                                               {'class':'registers'})

    teste0 = teste[teste.year_collected!='N/A'].copy()
    teste0.sort_values(['year_collected', 'collector_full_name'], inplace=True)
    sorting2 = list(teste0['collector_full_name'].unique())
    if 'Non-Identified' in sorting2:
        sorting2.remove('Non-Identified')
        sorting2.append('Non-Identified')

    x_labels = teste0.sort_values('year_collected')['year_collected'].unique()
    y_labels = sorting2

    teste.year_collected=teste.year_collected.replace(20000,'N/A')
    x_labels=list(x_labels[:-1])+['N/A']
    registers = list(range(min(teste['registers']), max(teste['registers'])+50, 50))
    
    for a in teste.family.unique():
        if a not in colors[0].keys():
            colors[0][a]='black'
    
    teste = teste.rename(columns={'year_collected':'year_sampling'})
    
    # Create Graph
    graph = dash(teste,'year_sampling',x_labels,'collector_full_name',y_labels,'family',colors,'registers',registers,db)
    
    return graph.properties(title='Collector')