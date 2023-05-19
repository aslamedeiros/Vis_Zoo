
import numpy as np
import pandas as pd

# pacote para visualização principal
import altair as alt
from src.MNViz_colors import *

from itertools import compress

def timeX_monthY(data):

    # desabilitando limite de linhas
    alt.data_transformers.disable_max_rows()



    # droping NAN
    counts = data.dropna(subset=['year_collected', 'month_collected'], how='all')
    # grouping per time and order
    counts = counts.groupby(['year_collected', 'month_collected']).count()['class'].reset_index().rename(
                                                                                columns={'class':'counts'})

    # making sure month and year cols are int
    counts['year_collected'] = counts['year_collected'].astype(int)
    counts['month_collected'] = counts['month_collected'].astype(int)

    total = alt.Chart(counts, title='Total of collected specimens per month/year', width=1200, height=200).mark_rect().encode(
            y = alt.Y('month_collected', type='ordinal', title='Collected Month',
                    sort= alt.EncodingSortField('month_collected', order='descending')),
            x = alt.X('year_collected:O', title='Collected Year',),
            color= alt.Color('counts', title='Counts', scale=alt.Scale(scheme="yellowgreenblue"),legend=None),
            tooltip = alt.Tooltip(['counts', 'year_collected', 'month_collected'])
    )

    total.configure_title(fontSize=16).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    ).configure_legend(
        labelFontSize=12,
        titleFontSize=12
    )

    return total