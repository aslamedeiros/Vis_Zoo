def collector_year_dash(data, app_version, colors):

    alt.data_transformers.disable_max_rows()

    teste = data.copy()
    teste.family=teste.family.fillna('Non-identified')
    teste['collector_full_name']=teste['collector_full_name'].fillna('Non-Identified')
    teste['collector_full_name']=teste['collector_full_name'].replace('  ', 'Non-Identified')
    teste['collector_full_name']=teste['collector_full_name'].str.strip()

    teste = teste.groupby(['collector_full_name','year_collected', 'family','order']).count()['class'].reset_index().rename(columns=
                                                                                               {'class':'counts'})

    teste0 = teste.copy()
    teste0.sort_values(['year_collected', 'collector_full_name'], inplace=True)
    sorting2 = list(teste0['collector_full_name'].unique())
    sorting2.remove('Non-Identified')
    sorting2.append('Non-Identified')

    x_labels = teste.sort_values('year_collected')['year_collected'].unique()
    y_labels = sorting2

    x_lab=["N/A"]+list(x_labels)
    counts = list(range(min(teste['counts']), max(teste['counts'])+50, 50))

    #select_family = alt.selection_multi(fields= ['family'], bind= 'legend')
    #select_family = alt.selection_multi(fields= ['family'], bind= 'legend')
    click = alt.selection_multi( fields=['collector_full_name'],empty='none')
    click_year = alt.selection_multi(fields=['collector_full_name','year_collected'],empty='none')

    g2 = alt.Chart(teste,width=15.5*len(x_labels), height=900#15.5*len(y_labels),
                  ).mark_circle().encode(
            x= alt.X('year_collected', type='ordinal', title='Collected Year',
                 scale= alt.Scale(domain= x_labels),axis=alt.Axis(grid=True,gridOpacity=.3)),
            y= alt.Y('collector_full_name', type='nominal', title='Collector Name', 
                 scale= alt.Scale(domain= y_labels),
                sort=sorting2,axis=alt.Axis(grid=True,gridOpacity=.3)),
            size= alt.Size('counts', type="quantitative",  title= 'Counts',
                       legend= alt.Legend(orient= 'right', direction='horizontal', tickCount= 4),
                       scale=alt.Scale(domain= counts,range=[20, 100], zero=True)),  # range ajusta tamanho do circulo
            order= alt.Order('counts', sort='descending'),  # smaller points in front    
            color=  alt.Color('family:N', title="Family", 
                         scale=alt.Scale(domain=list(colors[0].keys()), range=list(colors[0].values())),
                         legend= None, #alt.Legend(columns=2, symbolLimit= 58)
                         ),
            tooltip= alt.Tooltip(['collector_full_name', 'year_collected', 'counts', 'family'])
        ).add_selection(click,click_year)#.transform_filter(select_family)

    g_9 = alt.Chart(teste,width=15.5*len(x_labels), height=900).mark_bar(fill='none', stroke='lightgray',strokeOpacity=0.7,size=55).encode(
        y=alt.Y('collector_full_name:O',scale= alt.Scale(domain= y_labels),
                axis=alt.Axis(grid=True,gridOpacity=0.5)),
    ).transform_filter(click)

    g_19 = alt.Chart(teste,width=15.5*len(x_labels), height=900).mark_point( stroke='#FF174b',strokeWidth=1,size=500).encode(
        y=alt.Y('collector_full_name:O',scale= alt.Scale(domain= y_labels),
                axis=alt.Axis(grid=True,gridOpacity=0.5),),
        x=alt.X('year_collected:O',scale= alt.Scale(domain= x_labels)),
    ).transform_filter(click_year)

    # Coletor
    g_0= alt.Chart(teste,
                                #height=100,
                                width=400,
                            ).mark_text(
                                size=12, text= 'COLLECTED YEAR:', opacity=0
                            ).encode(
                                )

    g_a0= alt.Chart(teste,
                                #height=100,
                                width=400,
                            ).mark_text(
                                size=18, text= 'COLLECTOR NAME:',
                            ).encode(
                                )

    g_a= alt.Chart(teste,
                                #height=100,
                                width=400,
                            ).mark_text(
                                size=16
                            ).encode(
                                text="collector_full_name").transform_filter(click)

    # Abertura
    g_esp = alt.Chart(teste,height=250.0,width=400).mark_circle(opacity=0.7).encode(
        y=alt.Y("id:O",
            title=None,
            axis=alt.Axis(ticks=False, grid=True,gridOpacity=0.3,domain=False,labels=False),
            scale=alt.Scale(reverse=True),),
        x=alt.X('year_collected:O',title='Collected Year',scale= alt.Scale(domain= x_labels),
                axis=alt.Axis(grid=True,gridOpacity=0.3,domain=False,ticks=False)),
        color= alt.Color('family:N', title="Family", 
                         scale=alt.Scale(domain=list(colors[0].keys()), range=list(colors[0].values())),
                         legend= None, #alt.Legend(columns=2, symbolLimit= 58)
                         ),
        size= alt.Size('counts', type="quantitative",  title= 'Counts',
                       legend= None, #alt.Legend(orient= 'right', direction='horizontal', tickCount= 4),
                       scale=alt.Scale(domain= counts,range=[20, 100], zero=True)),
        order= alt.Order('counts', sort='descending'),
        tooltip= alt.Tooltip(['collector_full_name', 'year_collected',  'family','counts'])
        ).transform_window(
        id='rank()',
        groupby=['collector_full_name','year_collected']
        ).transform_filter(
        click
    ).add_selection(click_year)#.transform_filter(select_family)

    g_6 = alt.Chart(teste,height=250.0,width=400).mark_bar(fill='none', stroke='#FF174B',size=15).encode(
        x=alt.X('year_collected:O',scale= alt.Scale(domain= x_labels),
                axis=alt.Axis(grid=True,gridOpacity=0.5)),
    ).transform_filter(click_year)

    # Year

    g_l0= alt.Chart(teste,
                                #height=100,
                                width=400,
                            ).mark_text(
                                size=18, text= 'COLLECTED YEAR:',
                            ).encode(
                                )

    g_l= alt.Chart(teste,
                                #height=100,
                                width=400,
                            ).mark_text(
                                size=16
                            ).encode(
                                text="year_collected").transform_filter(click_year)


    # parte2
    g_7 = alt.Chart(teste,height=320.0,width=400).mark_bar().encode(
        y=alt.Y('family:O',title='Family',axis=alt.Axis(domain=False,ticks=False,),sort='-x'),
        x =alt.X('counts',stack='zero',scale=alt.Scale(type='sqrt'),
                 title='Counts(sqrt)',axis=alt.Axis(domain=False,ticks=False)),
        color= alt.Color('family:N', title="Family", 
                         scale=alt.Scale(domain=list(colors[0].keys()), range=list(colors[0].values())),),
        opacity= alt.condition(click_year,alt.value(.9),alt.value(.4)),
        tooltip=['family','year_collected','counts']
    ).transform_filter(click_year)


    g2 = (g_9+g2+g_19)|( g_a0&g_a&(g_6+g_esp)&g_0 &g_l0&g_l&g_7)

    g2.configure_axis(
            labelFontSize=10,
            titleFontSize=12
        ).configure_legend(
            labelFontSize=12,
            titleFontSize=12
        ).configure_facet(
        spacing=-140
        ).configure_view(
            height=15.0,width=150,stroke=None
    ).configure_title(anchor="middle",fontSize=24)#.save('./graphs/t5_3.html')

    return g2