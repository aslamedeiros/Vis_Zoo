import unidecode
import numpy as np
import pandas as pd

from src.MNViz import *

def get_depth(d):
    '''
    Treats known errors in Depth columns
    '''
    
    d = str(d)
    
    if d.lower() == 'nan' or d.lower() == 'none':
        return np.NAN
    else:
        return d.replace(',','.').replace('m','').strip()

# function to define type
def define_type(t):
    t = str(t).strip().lower().capitalize()

    if t == 'Nan' or t=='Null':
        return np.NAN
    else:
        return t

def correct_type(t):
    '''
    Given a type input, it correctly returns the name of the type (Corrects for spelling mistakes 
    and some known errors)
    '''
    # list of known types
    types = ['Parátipo', 'Holótipo', 'Alótipo', 'Neótipo', 'Paralectótipo', 'Topótipo', 'Síntipo', 'Lectótipo']
    normalized_types = {unidecode.unidecode(j):j for j in types}  # corrects for accents errors
    
    t = str(t).strip().capitalize()
    if t in types:
        return t
    elif t in normalized_types.keys():
        return normalized_types[t]
    elif t == 'None' or t == 'Nan':
        return np.NAN
    else:  # still don't know what to do with 'Tipo, Co-tipo and Material tipo'.
        return t


def catch_year(row,sep='/', return_month=False):
        if not str(row).find(sep)==-1:
            dates_values = str(row).split(sep)
            year = int(dates_values[0])
            month = int(dates_values[1])
            if return_month:
                return month
            else:
                return year
        else:
            return np.NaN

# function to apply new types with respect to NaN
def apply_type_with_nan(value, new_type):
    try:
        if str(value).lower() == 'nan' or str(value).lower() == ' ' :
            return np.NaN
        else:
            return new_type(value)
    except:
        return np.NAN

# function to determine if the instance was lost to fire
def lost_in_fire(description):
    '''
    Returns 1 if that specimen was lost in the fire, 0 otherwise.
    '''
    description = str(description)
    
    # removing accents
    description = unidecode.unidecode(description)
    
    if 'perdido no incendio' in description:
        return 1
    else:
        return 0            

#from a column of first_name and a column of last_name, creates a new full_name columns and erases the two previous columns
def create_column_full_name(data:pd.DataFrame, column_first_name, column_last_name, column_full_name):

    def capitalize(a):
        return a.title().strip()
    
    data[column_first_name] = data[column_first_name].fillna('') ###
    data[column_last_name] = data[column_last_name].fillna('') ###

    data[column_first_name] = data[column_first_name].apply(capitalize) ### treat_names
    data[column_last_name] = data[column_last_name].apply(treat_names, args=['last'])

    data[column_full_name] = data[column_first_name].astype(str).str.strip() + ' ' + data[column_last_name].astype(str).str.strip()
    data[column_full_name].apply(apply_type_with_nan, args=[str])
    data.drop(columns=[column_first_name,column_last_name], inplace=True)

    return data
    
def correct_lat(l):
    l = str(l).lower().replace(',','.').strip().replace('\n','')
    
    if l == 'nan':
        return np.NAN
    elif np.abs(float(l.split(' ')[0])) > 90:  # abnormally large values indicate a different format (DMS)
        
        if len(l.split(' ')) > 1:  # just a typo (like '3514 S')
            pos = l.split(' ')[-1]
            lat = float(l[:2] + '.' + l[2:].split(' ')[0])
            
            if pos == 's':
                return -1 * lat
            else:
                return lat
            
        elif '-' in l: 
            d = float(l[1:3])               # degrees
            m = float(l[3:5])               # minutes
            s = float(l[5:].split(' ')[0])  # seconds
            
            pos = l[5:].split(' ')[-1]  # North or South
            
            lat = d + (m/60) + (s/3600)
            
            return -1 * lat

        else:
            d = float(l[0:2])              # degrees
            m = float(l[2:4])              # minutes
            s = float(l[4:].split(' ')[0]) # seconds

            pos = l[4:].split(' ')[-1]  # North or South

            lat = d + (m/60) + (s/3600)
            
            if pos == 's':
                return -1 * lat
            else:
                return lat
    elif 's' in l:   # degrees south need to multiply by -1
        return float('-' + l.split(' ')[0])
    elif 'n' in l:
        return float(l.split(' ')[0])
    else:
        return l
        
def correct_long(l):
    l = str(l).lower().replace(',','.').strip().replace('\n','')
    
    if l == 'nan':
        return np.NAN
#     elif '.' not in l:  # assuming its in DMS format
#         d = int(l[:2])  # degrees
#         m = int(l[2:4]) # minutes
#         s = int(l[4:].split(' ')[0])
        
#         pos = l[4:].split(' ')[-1]  # East or West
        
#         long = d + (m/60) + (s/3600)
#         if pos == 'w':
#             return -1 * long
#         else:
#             return long
    elif np.abs(float(l.split(' ')[0])) > 180: # abnormally large values indicate a different format (DMS)
        
        if len(l.split(' ')) > 1:  # just a typo (like '3514 S')
            pos = l.split(' ')[-1]
            lat = float(l[:2] + '.' + l[2:].split(' ')[0])
            
            if pos == 'w':
                return -1 * lat
            else:
                return lat
        
        elif '-' in l:
            d = float(l[1:3])  # degrees
            m = float(l[3:5]) # minutes
            s = float(l[5:].split(' ')[0])

            pos = l[5:].split(' ')[-1]  # East or West

            long = d + (m/60) + (s/3600)
            
            return -1 * long
        else:
            d = float(l[0:2])  # degrees
            m = float(l[2:4]) # minutes
            s = float(l[4:].split(' ')[0])

            pos = l[4:].split(' ')[-1]  # East or West

            long = d + (m/60) + (s/3600)
            
            if pos == 'w':
                return -1 * long
            else:
                return long

    elif 'w' in l:   # degrees west need to multiply by -1
        return float('-' + l.split(' ')[0])
    elif 'e' in l:
        return float(l.split(' ')[0])

    else:
        return l