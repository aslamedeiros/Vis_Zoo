import pandas as pd
import numpy as np
import colorsys
from src.MNViz_colors import * #cores_familia_crustacea, cores_familia_reptiles, cores_ordem, cores_infraordem, cores_ordem_polychaete, cores_familia_polychaete

sepoptions = [',',';','\t']

def get_file_extension(app_version):
  if app_version == 'reptiles' or app_version=='crustaceas' or app_version=='polychaeta' or app_version=='annelida':
    ext = 'xlsx'
  elif app_version == 'GBIF':
    ext = 'csv'
  return ext

#there are 5 positional arguments
def filter_data(data:pd.DataFrame, list_filter_out, time1, time2):

  data[['family','type_status']] = data.loc[:,['family','type_status']].astype(str)

  filtered_data =  data.where((data['year_collected'] <= time2) & (data['year_collected'] >= time1))

  for filt in list_filter_out:
    filtered_data = filtered_data.where((~filtered_data[filt['name_column']].isin(filt['filter'])))

  return filtered_data

# this functions creates color_palettes for orders and families 
def create_color_palettes(data, app_version , base = ''):

  if app_version == 'reptiles':
    core_family = cores_familia_reptiles
    core_ordem = cores_ordem
  elif app_version == 'crustaceas' and base == 'Decapoda':
    core_family = cores_familia_crustacea
    core_ordem = cores_infraordem
  elif app_version == 'polychaeta':
    core_family = cores_familia_polychaete
    core_ordem = cores_ordem_polychaete
  elif app_version == 'annelida':
    core_family = cores_familia_annelida
    core_ordem = cores_ordem_annelida
  else:
    data.dropna(subset=['order','family'], inplace=True)
    order_groups = data.groupby(['order','family']).count()['class']
    orders = data.groupby(['order','family']).count().reset_index().groupby(['order']).count()['class']

    orders_name = orders.index
    orders_counts = orders.to_numpy()

    core_ordem = dict()
    core_family = dict()

    order_colors, order_intervals = counts_to_color(orders_counts, [0,0.95], centered_values=False, return_interval=True, equidistant=False)

    for i in range(len(order_colors)):
      core_ordem[orders_name[i]] = order_colors[i]
      
      family_names = order_groups[orders_name[i]].index
      family_counts = order_groups[orders_name[i]].to_numpy()
      
      family_colors = counts_to_color(family_counts, order_intervals[i], centered_values=True, return_interval=False, equidistant=True, changeSaturation=True)
      # changeSaturation=True means that the saturation is going to change between the colors
      for k in range(len(family_colors)):

        core_family[family_names[k]] = family_colors[k]
    
  return core_family, core_ordem

#this function is used to create color palettes with color ranges proportionnal to the number of families and orders
def counts_to_color(counts, interval, centered_values=False, return_interval=True, equidistant=False, changeSaturation=False):
    
    if centered_values:
      col_range = interval[1] - interval[0]
      interval[0] = interval[0] + col_range/10
      interval[1] = interval[1] - col_range/10

    bounds = (counts/np.sum(counts)).cumsum()*(interval[1]-interval[0])+interval[0]
    if equidistant:
      bounds = np.linspace(interval[0], interval[1], len(bounds)+1)[1:]
    
    intervals = list()
    colors = list()

    saturation = 0.7
    if changeSaturation:
      sat_min = 0.5
      sat_max = 0.9
      saturation = sat_min

    for i in range(len(bounds)):

      if i == 0:
          intervals.append([interval[0],bounds[i]])
          colors.append(zero_one_to_hex((interval[0]+bounds[i])/2, saturation))
      else:
          intervals.append([bounds[i-1],bounds[i]])
          colors.append(zero_one_to_hex((bounds[i-1]+bounds[i])/2, saturation))
        
      if changeSaturation:
        saturation += (sat_max - sat_min)/len(bounds)
    
    if return_interval:
        return colors, intervals
    else:
        return colors

# from a value between 0 and 1 for hue, and between 0 and 1 for saturation (which also impacts value), returns an rgb hexadecimal color for the custom components css 
def zero_one_to_hex(value, sat):
  h = value
  s = sat
  v = 1.15 - sat/2

  rgb = colorsys.hsv_to_rgb(h,s,v)

  res = '#{:02x}{:02x}{:02x}'.format(int(rgb[0]*255),int(rgb[1]*255),int(rgb[2]*255))
  return res