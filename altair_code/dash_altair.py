import datetime
import numpy as np
import pandas as pd

import altair as alt

def titulo(var):
    return var.replace('_full_','_').replace('_',' ').title()

def cx_alta(var):
    return var.replace('_full_','_').replace('_',' ').upper()

def dash(dados:pd.DataFrame, varX:str,x_labels, varY:str, y_labels, varColor:str, colors:dict, varSize:str, limSize:list):
    select_family = alt.selection_multi(fields= [varColor], bind= 'legend')
    click = alt.selection_multi( fields=[varY],empty='none')
    click_year = alt.selection_multi(fields=[varY,varX],empty='none')

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
                       legend=None, #alt.Legend(orient= 'right', direction='horizontal', tickCount= 4),
                       scale=alt.Scale(domain= limSize,range=[20, 100], zero=True)),  # range ajusta tamanho do circulo
            order= alt.Order(varSize, sort='descending'),  # smaller points in front    
            color=  alt.Color(varColor,type='nominal', title = titulo(varColor), 
                         scale=alt.Scale(domain=list(colors[0].keys()), range=list(colors[0].values())),
                         legend=None), #alt.Legend(columns=2, symbolLimit= 58)),
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
                         legend= alt.Legend(columns=2, symbolLimit= 58)),
        size= alt.Size(varSize, type="quantitative",  title= titulo(varSize),
                       legend= alt.Legend(orient= 'right', direction='horizontal', tickCount= 4),
                       scale=alt.Scale(domain= limSize,range=[20, 100], zero=True)),
        order= alt.Order(varSize, sort='descending'),
        tooltip= alt.Tooltip([varY, varX,  varColor,varSize])
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
    g_7 = alt.Chart(dados,height=320,width=w_2).mark_bar().encode(
        y=alt.Y(varColor,type='ordinal',title=titulo(varColor),axis=alt.Axis(domain=False,ticks=False,labels=False),sort='-x'),
        x =alt.X(varSize,stack='zero',scale=alt.Scale(type='sqrt'),
                 title=titulo(varSize)+'(sqrt)',axis=alt.Axis(domain=False,ticks=False)),
        tooltip=[varColor,varX,varSize]
    ).transform_filter(click_year)

    # Legenda barras

    #g_7labels = g_7.mark_text(align = 'right',color='black',size=8
    #                    ).encode(text=varColor#y=alt.Y(varColor,sort=alt.SortField('counts:Q'))
    #                    )

    g_7 = g_7.encode(
            color= alt.Color(varColor, type='nominal', title=titulo(varColor),
                         scale=alt.Scale(domain=list(colors[0].keys()), range=list(colors[0].values())),),
    )


    g2 = ((g_9+g2+g_19)|(g_a0 & g_a & (g_6+g_esp) & g_0 & g_l0 & g_l & (g_7))).configure_view(stroke=None)


    return g2