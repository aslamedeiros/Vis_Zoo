from altair_code.dash_altair import dash 

import numpy as np
import pandas as pd

# visualization
import altair as alt





def timeX_collectorY_top50(data:pd.DataFrame, app_version, colors):

    cores_familia = colors[0]
    # disabling rows limit
    alt.data_transformers.disable_max_rows()

    inter_data = data.groupby(['collector_full_name','year_collected', 'family']).count()['class'].reset_index().rename(columns=
                                                                                {'class':'counts'})
    # getting range
    time_domain = inter_data.sort_values(['year_collected'])['year_collected'].unique()
    time_max = time_domain.max()
    time_min = time_domain.min()

    # summing and sorting contributions of each collector
    sumed_collector = inter_data.groupby('collector_full_name').sum()['counts'].reset_index().rename(
        columns={'counts':'sum'})
    sorted_collector = sumed_collector.sort_values('sum', ascending=False)

    # sorted names
    sort_list = sorted_collector['collector_full_name'].unique()

    # database
    data_vis = inter_data.where(inter_data['collector_full_name'].isin(sort_list[0:50]))

    counts = data_vis['counts']

    #color_pal = alt.condition(alt.FieldOneOfPredicate("familia",new_fam), alt.Color('family', type="nominal", title="Family", legend = None,
    #                scale=alt.Scale(domain=familias, range=list(cores_familia.values()))), alt.value('lightgray'))


    graph = alt.Chart(data_vis, title= 'collection Registers by Top 50 collectors',
                width=800, height=700).mark_circle().encode(
        x= alt.X('year_collected', title='Sampling Year', scale=alt.Scale(domain=[time_min, time_max])),
        y= alt.Y('collector_full_name', type='nominal', title='Collector Name',
                sort= sort_list[0:50]),
        size= alt.Size('counts', title='Counts', scale= alt.Scale(range=[20,200]),
                    legend= None),
        order= alt.Order('counts', sort='descending'),  # smaller points in front
        color= alt.Color('family', type="nominal", title="Family", legend = None,
                    scale=alt.Scale(domain= list(cores_familia.keys()), range=list(cores_familia.values()))),
        tooltip= alt.Tooltip(['collector_full_name', 'year_collected', 'counts', 'family'])
    )

    graph = graph.configure_title(fontSize=16).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    ).configure_legend(
        labelFontSize=12,
        titleFontSize=12
    )

    return graph

def timeX_collectorY(data, app_version, colors):

    cores_familia = colors[0]
    teste = data.groupby(['collector_full_name','year_collected','family']).count()['class'].reset_index().rename(columns=
                                                                                            {'class':'counts'})


    sort_list = teste.sort_values('year_collected')['year_collected'].unique()
    time_min = sort_list.min()
    time_max = sort_list.max()

    graph = alt.Chart(teste, title='collection Registers by collector', width=800, height=10000).mark_circle().encode(
    x= alt.X('year_collected', title='Collected Year', scale=alt.Scale(domain=[time_min,time_max])),
    y= alt.Y('collector_full_name', type='nominal', title='Collector Name', 
            sort=alt.EncodingSortField('year_collected', op="min", order='ascending')),
    size= alt.Size('counts', scale=alt.Scale(range=[20, 350]), legend=None),  # range ajusta tamanho do circulo
    order= alt.Order('counts', sort='descending'),  # smaller points in front
    color = alt.Color('family', type="nominal", title="Family", legend = None,
                    scale=alt.Scale(domain= list(cores_familia.keys()), range=list(cores_familia.values()))),
    tooltip= [alt.Tooltip('collector_full_name', title='collector name'),
            alt.Tooltip('year_collected', title='year collected'),
            alt.Tooltip('counts', title='count'),
            alt.Tooltip('family',title='family')],
    )

    graph = graph.configure_title(fontSize=16).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    ).configure_legend(
        labelFontSize=12,
        titleFontSize=12
    )

    return graph


def timeX_determinerY(data, app_version, colors):

    cores_familia = colors[0]
    teste = data.groupby(['determinator_full_name','year_collected','family']).count()['class'].reset_index().rename(columns=
                                                                                            {'class':'counts'})


    sort_list = teste.sort_values('year_collected')['year_collected'].unique()
    time_min = sort_list.min()
    time_max = sort_list.max()

    graph = alt.Chart(teste, title='description Registers by determiner', width=800, height=2000).mark_circle().encode(
    x= alt.X('year_collected', title='Collected Year', scale=alt.Scale(domain=[time_min,time_max])),
    y= alt.Y('determinator_full_name', type='nominal', title='Determiner Name', 
            sort=alt.EncodingSortField('year_collected', op="min", order='ascending')),
    size= alt.Size('counts', scale=alt.Scale(range=[20, 350]), legend=None),  # range ajusta tamanho do circulo
    order= alt.Order('counts', sort='descending'),  # smaller points in front
    color = alt.Color('family', type="nominal", title="Family", legend = None,
                    scale=alt.Scale(domain= list(cores_familia.keys()), range=list(cores_familia.values()))),
    tooltip= alt.Tooltip(['determinator_full_name', 'year_collected', 'counts']),
    )

    graph = graph.configure_title(fontSize=16).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    ).configure_legend(
        labelFontSize=12,
        titleFontSize=12
    )

    return graph

def timeX_determinerY_top50(data, app_version, colors):

    cores_familia = colors[0]
    # disabling rows limit
    alt.data_transformers.disable_max_rows()

    inter_data = data.groupby(['determinator_full_name','year_collected', 'family']).count()['class'].reset_index().rename(columns=
                                                                                {'class':'counts'})
    # getting range
    time_domain = inter_data.sort_values(['year_collected'])['year_collected'].unique()
    time_max = time_domain.max()
    time_min = time_domain.min()

    # summing and sorting contributions of each collector
    sumed_collector = inter_data.groupby('determinator_full_name').sum()['counts'].reset_index().rename(
        columns={'counts':'sum'})
    sorted_collector = sumed_collector.sort_values('sum', ascending=False)

    # sorted names
    sort_list = sorted_collector['determinator_full_name'].unique()

    # database
    data_vis = inter_data.where(inter_data['determinator_full_name'].isin(sort_list[0:50]))

    counts = data_vis['counts']

    #color_pal = alt.condition(alt.FieldOneOfPredicate("familia",new_fam), alt.Color('family', type="nominal", title="Family", legend = None,
    #                scale=alt.Scale(domain=familias, range=list(cores_familia.values()))), alt.value('lightgray'))


    graph = alt.Chart(data_vis, title= 'description Registers by Top 50 determiners',
                width=800, height=700).mark_circle().encode(
        x= alt.X('year_collected', title='Sampling Year', scale=alt.Scale(domain=[time_min, time_max])),
        y= alt.Y('determinator_full_name', type='nominal', title='Determiner Name',
                sort= sort_list[0:50]),
        size= alt.Size('counts', title='Counts', scale= alt.Scale(range=[20,200]),
                    legend= None),
        order= alt.Order('counts', sort='descending'),  # smaller points in front
        color= alt.Color('family', type="nominal", title="Family", legend = None,
                    scale=alt.Scale(domain= list(cores_familia.keys()), range=list(cores_familia.values()))),
        tooltip= alt.Tooltip(['determinator_full_name', 'year_collected', 'counts', 'family'])
    )

    graph = graph.configure_title(fontSize=16).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    ).configure_legend(
        labelFontSize=12,
        titleFontSize=12
    )

    return graph

def collector_year_dash(data, app_version, colors):

    alt.data_transformers.disable_max_rows()

    teste = data.copy()
    teste.family=teste.family.fillna('Non-identified')
    teste.year_collected = teste.year_collected.fillna('N/A')
    teste.year_collected = teste.year_collected.replace(0,'N/A')
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
                                                                                               {'class':'counts'})

    teste0 = teste[teste.year_collected!='N/A'].copy()
    teste0.sort_values(['year_collected', 'collector_full_name'], inplace=True)
    sorting2 = list(teste0['collector_full_name'].unique())
    sorting2.remove('Non-Identified')
    sorting2.append('Non-Identified')

    x_labels = teste0.sort_values('year_collected')['year_collected'].unique()
    y_labels = sorting2

    x_lab=list(x_labels)+['N/A']
    counts = list(range(min(teste['counts']), max(teste['counts'])+50, 50))

    g2 = dash(teste,'year_collected',x_lab,'collector_full_name',y_labels,'family',colors,'counts',counts)
    return g2
