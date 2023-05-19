from curses import color_pair
import numpy as np
import pandas as pd

# visualization
import altair as alt

def geographic_alt(NewTable: pd.DataFrame, app_version, colors):

    cores_familia = colors[0]


    from vega_datasets import data

    source = alt.topo_feature(data.world_110m.url, 'countries')

    world = alt.Chart(source).mark_geoshape(
        fill='white',
        stroke='gray'
    ).project('naturalEarth1')

    tipos = NewTable['type_status'].astype(str).unique()

    #color_pal = alt.condition(alt.FieldOneOfPredicate("familia",new_fam),alt.Color('family:N', title='Family', 
    #                    legend=None, 
    #                    scale= alt.Scale(domain= list(cores_familia.keys()), range= list(cores_familia.values()))),
    #                    alt.value('lightgray'))

    teste = alt.Chart(NewTable).mark_point(filled=True).encode(
        longitude = alt.X('long:Q', title='Longitude'),
        latitude = alt.Y('lat:Q', title='Latitude'),
        color= alt.Color('family:N', title='Family', 
                        legend=None, 
                        scale= alt.Scale(domain= list(cores_familia.keys()), range= list(cores_familia.values()))),
        shape = alt.Shape('type_status:N', title='Type', scale= alt.Scale(domain=tipos), 
                        legend=None),
        tooltip = alt.Tooltip(['lat','long','country',
                            #'region',
                            'state',
                            'year_collected',
                            'month_collected',
                            'genus','order', 'family', 'type_status'])
    ).project(type='naturalEarth1')


    temp = (world + teste).configure_title(fontSize=16).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    )

    return temp

def timeX_family_continentY(data, app_version, colors):

    cores_familia = colors[0]
    teste = data.groupby(['year_collected','continent', 'family']).count()['class'].reset_index().rename(columns={
    'class':'counts'
    })

    # database
    db = teste

    db = db.dropna(subset=['year_collected'])
    db['year_collected'] = db['year_collected'].astype(int)
    db[['continent','family']] = db[['continent','family']].astype(str)

    # auxiliar variables for encoding fields
    x_labels = db.sort_values('year_collected')['year_collected'].unique()
    xmin = x_labels.min()
    xmax = x_labels.max()
    y_labels = db['continent'].unique()
    print(y_labels)

    graph = alt.Chart(db, title='Registers Family by Continent', height=300, width=1400).mark_circle().encode(
        x= alt.X('year_collected', title='Sampling Year', 
                scale= alt.Scale(domain= [xmin,xmax])),
        y= alt.Y('continent:N', title='Continent', 
                scale= alt.Scale(domain= y_labels),
                sort=alt.EncodingSortField('counts', op="count", order='descending')), 
        size=alt.Size('counts', title='Counts',
                    legend= None,
                    scale= alt.Scale(range=[20,120])), 
        order= alt.Order('counts', sort='descending'),  # smaller points in front
    #     color= alt.Color('order', scale=alt.Scale(domain=ordens, range=cores)),  # old palette per order
        color= alt.Color('family',title= 'Family', 
                        legend= None,
                        scale= alt.Scale(domain= list(cores_familia.keys()), range= list(cores_familia.values()))),
        tooltip= alt.Tooltip(['continent','year_collected','family','counts'])
    )

    graph = graph.configure_title(fontSize=16).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    ).configure_legend(
        labelFontSize=12,
        titleFontSize=12
    )

    return graph

def timeX_family_countryY(data, app_version, colors):

    cores_familia = colors[0]
    teste = data.groupby(['year_collected','country', 'family']).count()['class'].reset_index().rename(columns={
    'class':'counts'
    })

    # database
    db = teste

    # auxiliar variables for encoding fields
    x_labels = db.sort_values('year_collected')['year_collected'].unique()
    xmin = x_labels.min()
    xmax = x_labels.max()
    y_labels = db['country'].unique()

    graph = alt.Chart(db, title='Registers Family by Country', height=500, width=1400).mark_circle().encode(
        x= alt.X('year_collected', title='Sampling Year', 
                scale= alt.Scale(domain= [xmin,xmax])),
        y= alt.Y('country:N', title='country', 
                scale= alt.Scale(domain= y_labels),
                sort=alt.EncodingSortField('counts', op="count", order='descending')), 
        size=alt.Size('counts', title='Counts',
                    legend= None,
                    scale= alt.Scale(range=[20,120])), 
        order= alt.Order('counts', sort='descending'),  # smaller points in front
    #     color= alt.Color('order', scale=alt.Scale(domain=ordens, range=cores)),  # old palette per order
        color= alt.Color('family',title= 'Family', 
                        legend= None,
                        scale= alt.Scale(domain= list(cores_familia.keys()), range= list(cores_familia.values()))),
        tooltip= alt.Tooltip(['country','year_collected','family','counts'])
    )

    graph = graph.configure_title(fontSize=16).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    ).configure_legend(
        labelFontSize=12,
        titleFontSize=12
    )

    return graph

def timeX_family_statesY(data, app_version, colors):

    cores_familia = colors[0]
    teste = data.groupby(['year_collected','state', 'family']).count()['class'].reset_index().rename(columns={
    'class':'counts'
    })

    # database
    db = teste

    # auxiliar variables for encoding fields
    x_labels = db.sort_values('year_collected')['year_collected'].unique()
    xmin = x_labels.min()
    xmax = x_labels.max()
    y_labels = db['state'].unique()

    if app_version=='GBIF':
        color_palette = None
    else:
        color_palette = alt.Color('family',title= 'Family', 
                        legend= None,
                        scale= alt.Scale(domain= list(cores_familia.keys()), range= list(cores_familia.values())))

    graph = alt.Chart(db, title='Registers Family by Brazilian States', height=1500, width=1400).mark_circle().encode(
        x= alt.X('year_collected', title='Sampling Year', 
                scale= alt.Scale(domain= [xmin,xmax])),
        y= alt.Y('state:N', title='states', 
                scale= alt.Scale(domain= y_labels),
                sort=alt.EncodingSortField('counts', op="count", order='descending')), 
        size=alt.Size('counts', title='Counts',
                    legend= None,
                    scale= alt.Scale(range=[20,120])), 
        order= alt.Order('counts', sort='descending'),  # smaller points in front
    #     color= alt.Color('order', scale=alt.Scale(domain=ordens, range=cores)),  # old palette per order
        color= color_palette,
        tooltip= alt.Tooltip(['state','year_collected','family','counts'])
    )

    graph = graph.configure_title(fontSize=16).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    ).configure_legend(
        labelFontSize=12,
        titleFontSize=12
    )

    return graph