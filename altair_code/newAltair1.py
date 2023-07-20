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
    select_family = alt.selection_multi(fields= [varColor], bind= 'legend')
    click = alt.selection_multi( fields=[varY],empty='none')
    click_year = alt.selection_multi(fields=[varY,varX],empty='none')

    x_labels = [str(x) for x in x_labels]
    dados[varX]=dados[varX].astype('str')


    w_1 = 15.5*len(x_labels)
    h_1 = 13*len(y_labels)
    # Prancheta
    g2 = alt.Chart(dados,width=w_1, height=h_1,
                  ).mark_circle().encode(
            x= alt.X(varX, type='ordinal', title = titulo(varX),
                 scale= alt.Scale(domain= x_labels),axis=alt.Axis(grid=True,gridOpacity=.3)),
            y= alt.Y(varY, type='nominal', title = titulo(varY), 
                scale= alt.Scale(domain= y_labels),
                sort=y_labels,axis=alt.Axis(grid=True,gridOpacity=.3)),
            size= alt.Size(varSize, type="quantitative",  title= titulo(varSize),
                       legend=None,# None, #alt.Legend(orient= 'right', direction='horizontal', tickCount= 4),
                       scale=alt.Scale(domain= limSize,range=[20, 100], zero=True)),  # range ajusta tamanho do circulo
            order= alt.Order(varSize, sort='descending'),  # smaller points in front    
            color=  alt.Color(varColor,type='nominal', title = titulo(varColor), 
                         scale=alt.Scale(domain=list(colors[0].keys()), range=list(colors[0].values())),
                         legend=None,#None, #alt.Legend(columns=2, symbolLimit= 60)
                         ),
            tooltip= alt.Tooltip([varY, varX, varSize, varColor])
        ).add_selection(select_family,click,click_year).transform_filter(select_family)

    g_9 = alt.Chart(dados,width=w_1, height=h_1).mark_bar(fill='none', stroke='lightgray',strokeOpacity=0.7,size=55).encode(
        y=alt.Y(varY, type='ordinal',scale= alt.Scale(domain= y_labels),
                axis=alt.Axis(grid=True,gridOpacity=0.5)),
    ).transform_filter(click)

    g_19 = alt.Chart(dados,width=w_1, height=h_1).mark_point( stroke='#FF174b',strokeWidth=1,size=500).encode(
        y=alt.Y(varY, type='ordinal',scale= alt.Scale(domain= y_labels),
                axis=alt.Axis(grid=True,gridOpacity=0.5),),
        x=alt.X(varX, type='ordinal',scale= alt.Scale(domain= x_labels)),
    ).transform_filter(click_year)

    w_2 = len(x_labels)*11.5
    # Coletor
    g_0= alt.Chart(dados,
                                #height=100,
                                width=w_2,
                            ).mark_text(
                                size=12, text= cx_alta(varY), opacity=0
                            ).encode(
                                )

    g_a0= alt.Chart(dados,
                                #height=100,
                                width=w_2,
                            ).mark_text(
                                size=18, text= cx_alta(varY),
                            ).encode(
                                )

    g_a= alt.Chart(dados,
                                #height=100,
                                width=w_2,
                            ).mark_text(
                                size=16
                            ).encode(
                                text=varY).transform_filter(click)

    # Abertura
    g_esp = alt.Chart(dados,height=250, width=w_2).mark_circle(opacity=0.7).encode(
        y=alt.Y("id:O",
            title=None,
            axis=alt.Axis(ticks=False, grid=True,gridOpacity=0.3,domain=False,labels=False),
            scale=alt.Scale(reverse=True),),
        x=alt.X(varX, type='ordinal',title=titulo(varX),scale= alt.Scale(domain= x_labels),
                axis=alt.Axis(grid=True,gridOpacity=0.3,domain=False,ticks=False)),
        color= alt.Color(varColor, type ='nominal', title=titulo(varColor), 
                         scale=alt.Scale(domain=list(colors[0].keys()), range=list(colors[0].values())),
                         legend=None,# alt.Legend(columns=2, symbolLimit= 60)
                         ),
        size= alt.Size(varSize, type="quantitative",  title= titulo(varSize),
                       legend=None,# alt.Legend(orient= 'right', direction='horizontal', tickCount= 4),
                       scale=alt.Scale(domain= limSize,range=[20, 100], zero=True)),
        order= alt.Order(varSize, sort='descending'),
        tooltip= alt.Tooltip([varY, varX,  varColor, varSize])
        ).transform_window(
        id='rank()',
        groupby=[varY,varX]
        ).transform_filter(
        click
    ).add_selection(select_family,click_year).transform_filter(select_family)

    g_6 = alt.Chart(dados,height=250, width=w_2).mark_bar(fill='none', stroke='#FF174B',size=15).encode(
        x=alt.X(varX, type='ordinal',scale= alt.Scale(domain= x_labels),
                axis=alt.Axis(grid=True,gridOpacity=0.5)),
    ).transform_filter(click_year)

    # Year

    g_l0= alt.Chart(dados,
                                #height=100,
                                width=w_2,
                            ).mark_text(
                                size=18, text= cx_alta(varX),
                            ).encode(
                                )

    g_l= alt.Chart(dados,
                                #height=15,
                                width=w_2,
                            ).mark_text(
                                size=16
                            ).encode(
                                text=varX).transform_filter(click_year)


    # parte2
    db_dash = db.copy()
    db_dash =  db_dash.rename(columns={'determinator_full_name':'Identified_by','year_collected':'year_sampling'})
    #db_dash[varX]=db_dash[varX].to_string()
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

    #print(db_dash[varX].unique())
    g_7 = alt.Chart(db_dash,height=250, width=w_2).mark_circle(opacity=0.7).encode(
        y=alt.Y("number:O",
            title=None,
            axis=alt.Axis(ticks=False, grid=True,gridOpacity=0.3,domain=False,labels=False),
               ),
        x=alt.X(varColor, type='ordinal',title=titulo(varColor),
                axis=alt.Axis(grid=True,gridOpacity=0.3,domain=False,ticks=True,orient='top'),
                scale=alt.Scale(reverse=True),
                ),
        color= alt.Color(varColor, type ='nominal', title=titulo(varColor), 
                         scale=alt.Scale(domain=list(colors[0].keys()), range=list(colors[0].values())),
                         legend=None,# alt.Legend(columns=2, symbolLimit= 60)
                         ),
        tooltip= alt.Tooltip(['catalog_number', 'year_cataloged', 'year_sampling',
       'class', 'order', 'family', 'genus', 'species', 'type_status',
       'qualifier', varY, varX,  varColor,'number:O'])
        ).transform_window(
        number='rank()',
        groupby=[varColor,varX,varY]
    ).transform_filter(click_year)
    
    # Legenda barras

    #g_7labels = g_7.mark_text(align = 'right',color='black',size=8
    #                    ).encode(text=varColor#y=alt.Y(varColor,sort=alt.SortField('counts:Q'))
    #                    )

    g2 = ((g_9+g2+g_19)|(g_a0 & g_a & (g_6+g_esp) & g_0 & g_l0 & g_l & (g_7)))

    return g2.configure_view(stroke=None)


def time_catalogedX_determinatorY_dash(banco,app_version,colors):
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
    #base = base.rename(columns={'determinator_full_name':'determinator_name','year_cataloged':'cataloged_year'})
    
    x_labels=list(x_labels[:-1])+['N/A']
    
    registers = list(range(min(base.registers), max(base.registers)+50, 50))
    
    for a in base.family.unique():
        if a not in colors[0].keys():
            colors[0][a]='black'
            
    base =  base.rename(columns={'determinator_full_name':'Identified_by'})####
    
    g2 = dash(base,'year_cataloged',x_labels, 'Identified_by',y_labels, 'family', colors, 'registers', registers, db = banco)
    
    return g2.properties(title='Counts by Identifier')

def time_collectedX_collectorY_dash(db,app_version,colors):   
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
    
    g2 = dash(teste,'year_sampling',x_labels,'collector_full_name',y_labels,'family',colors,'registers',registers,db)
    
    return g2.properties(title='Collector')