# imports 
import numpy as np
import pandas as pd
from collections import defaultdict


# function to treat Persons Names
def treat_names(name, pos='first'):
    '''
    Treat names keeping NaN as such.
    
    Arguments: 
        - name (str): name to be treated. 
        - pos (str): name position. One of ['first', 'last']
    '''
    if type(name) == str and pos == 'first':     # first name
        
        if len(name.split(' ')) > 1:             # treats composite names (+ 1 name)
            return str(name).strip().split(' ')[0].capitalize()
        else:
            return str(name).strip().capitalize()
    
    elif type(name) == str and pos == 'last':    # last name
        
        if len(name.split(' ')) > 1:             # treats composite last name (+ 1 surname)
            return str(name).strip().split(' ')[-1].capitalize()
        else:
            return str(name).strip().capitalize()   
    else:
        return name
    

# function to treat taxonomy columns
def treat_taxon_columns(df:pd.DataFrame, columns, inplace=True):
    temp = df[columns].copy()
    
    if inplace:
        for col in columns:
            print(f'Adjusting column {col}')
            
            if 'especie' in col.lower():
                df[col] = df[col].apply(lambda x:str(x).lower().strip())
            else:
                df[col] = df[col].apply(lambda x:str(x).lower().strip().capitalize())
                
        return None
    else:
        for col in columns:
            print(f'Adjusting column {col}')
            
            if 'especie' in col.lower():
                temp[col] = temp[col].apply(lambda x:str(x).lower().strip())
            else:
                temp[col] = temp[col].apply(lambda x:str(x).lower().strip().capitalize())
                
        return temp    
    
    
def str_with_nan2int(string):
    try:
        if not np.isnan(string):
            return int(string)
        else:
            return np.NAN
    except:
        if str(string).lower() == 'nan':
            return np.NaN
        else:
            return int
            

def getMonthAndYear(date):
    '''
    Tries to catch month and year from a string date in dd/mm/YYYY format. 
    
    This function treats for some anomalies found on National Museum Databases, such as: 
        dd/mm/YY/ 
        and 
        ' '
    
    Inputs: 
        date: a string date in dd/mm/YYYY format
        
    Outputs:
        (month, year) tuple.
        
    p.s.: if the function is not able to infer month and year from the string date, it returns np.NAN for both.
    '''
    
    month = np.NAN 
    year = np.NAN
    # tests if it's empty or NAN
    if str(date).lower() == 'nan' or str(date) == ' ' or date == None:
        return (month, year)
    
    elif not str(date).find('/')==-1:
        dates_values = str(date).split("/")
        year = int(dates_values[-1])
        month = int(dates_values[1])
        
        return (month, year)
    ## se a data tem duas / (dd/mm/aaaa)
    elif str(date).count('/') == 2:
        split_date = str(date).split('/')
        year = int(split_date[-1])
        month = int(split_date[1])
        
        return (month, year)
    
    else:
        print(f"Couldn't figure out (month, year) for : {date}")
        return (month, year)


# corrects reptiles order Squama e Squamta
def correct_squamata(string):
    if str(string).lower() == 'squama' or str(string).lower() == 'squamta':
        return 'Squamata'
    else:
        return str(string)
    
# substitutes #n/d form 'Nan'
def correct_nd(string):
    if str(string) == "#n/d":
        return np.NAN
    elif str(string).lower() == 'nan':
        return np.NAN
    else:
        return string


def convert2float(n):
    '''
    This function tries to convert the input to float. If not successful, returns NAN.
    '''
    try:
        return float(n)
    except:
        return np.NAN


def correct_type(type):
    '''
    Function to correct some typos in Type information keeping NAN as such.

    input:
        type: string of that animal's type

    output:
        corrected type (string)
    '''
    # detected_typos = {}
    corrected_type = type.lower().strip().capitalize()
    return corrected_type


def brazilian_region(state):
    '''
    Given a state, this function returns the brazilian region for that state.
    '''

    state = str(state)
    regions = {
    'Rio de Janeiro':'SE',
    'São Paulo':'SE',
    'Espírito Santo': 'SE',
    'Pernambuco':'NE',
    'Santa Catarina':'S',
    'Amazonas':'N',
    'Goiás':'CO',
    'Roraima':'N',
    'Pará':'N',
    'Mato Grosso':'CO',
    'Acre': 'N',
    'Bahia': 'NE',
    'Minas Gerais': 'SE',
    'Mato Grosso do Sul': 'CO',
    'Paraná': 'S',
    'Rondônia': 'N',
    'Ceará': 'NE',
    'Maranhão': 'NE',
    'Rio Grande do Sul': 'S',
    'Paraíba': 'NE',
    'Distrito Federal': 'CO',
    'Alagoas': 'NE',
    'Amapá':'N',
    'Piauí': 'NE',
    'Brasília': 'CO',
    'Tocantins': 'N',
    'Rio Grande do Norte': 'NE',
    'Sergipe': 'NE',
    'Minas Gerais/Goiás/Distrito Federal': 'CO',
    'Santa Catarina-Rio Grande do Sul': 'S'
    }

    if state not in regions.keys():
        return np.NAN
    else:
        return regions[state]