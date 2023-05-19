# Old way to slice main DB

# slicing main database (repteis)
Table = repteis[['NumeroDeCatalogo','DataDeEntrada','DataDaDeterminacao','DataColetaInicial','Class','Kingdom', 
                    'Genero_ent', 'Genero_atual', 'Especie_ent', 'Especie_atual','Subespecie_atual','Type Status 1',
                    'DeterminatorFirstName1', 'DeterminatorLastName1', 'genero_e_especie_ent',
                    'genero_e_especie_atual','MinAltitude','MaxAltitude',
                    'Ordem', 'Familia', 'Phylum', 'Qualificador_atual', 'NotasTaxonomicas']].copy()

# OBS: Determined Date1 has many missing values... CHECK THAT
d = []
counter=0
for row in Table['DataColetaInicial']:
    if not str(row).find('/')==-1:
        dates_values = str(row).split("/")
        year = int(dates_values[-1])
        month = int(dates_values[1])
#        if (month>1) and (month<12):
            #store the year and month in a datetime datatype for later sorting
#            dateRecord = datetime.datetime(year,month,1) 
    else:
        year = Table.loc[counter, 'DataColetaInicial']
        month = Table.loc[counter, 'DataColetaInicial']
    
    # mais um condicional para tratar anos vazios ' '
    if year == ' ':
        year = np.NAN
        month = np.NAN
        
    d.append({'year_collected':year,
              'month_collected':month,
              'catalog_number':Table.loc[counter,'NumeroDeCatalogo'],
              'class':Table.loc[counter,'Class'],
              'kingdom':Table.loc[counter,'Kingdom'], 'genus_old':Table.loc[counter,'Genero_ent'],
              'genus':Table.loc[counter,'Genero_atual'],
              'species_old':Table.loc[counter,'Especie_ent'],
              'species':Table.loc[counter,'Especie_atual'],
              'subspecies':Table.loc[counter, 'Subespecie_atual'],
              'genero_e_especie_ent': Table.loc[counter,'genero_e_especie_ent'],
              'genero_e_especie_atual': Table.loc[counter,'genero_e_especie_atual'],
              'type_status':Table.loc[counter,'Type Status 1'], 
              'determinator_first_name':Table.loc[counter,'DeterminatorFirstName1'],
              'determinator_last_name':Table.loc[counter,'DeterminatorLastName1'],
              'altitude':Table.loc[counter,'MinAltitude'],
              'max_altitude':Table.loc[counter,'MaxAltitude'],
              'order':Table.loc[counter,'Ordem'],
              'family':Table.loc[counter,'Familia'],
              'phylum': Table.loc[counter,'Phylum'],
              'tipo': Table.loc[counter,'NotasTaxonomicas'],
              'qualifier': Table.loc[counter,'Qualificador_atual']
              })
    counter = counter+1

    
NewTable = pd.DataFrame(d)


### collecting determined year (p.s.: being careful to keep NaNs as they show up)
NewTable['ano_determinacao'] = np.nan

d1 = []
counter=0
for row in Table['DataDaDeterminacao']:
    try:  # if Determined Date1 is empty, keep it so 
        if np.isnan(row):
            year= np.NAN
    
    except:
        if not str(row).find('/')==-1:
            dates_values = str(row).split("/")
            year = int(dates_values[-1])
            month = int(dates_values[1])
#            if (month>1) and (month<12):
                #store the year and month in a datetime datatype for later sorting
#                dateRecord = datetime.datetime(year,month,1)    
    
    NewTable.loc[counter, 'ano_determinacao'] = year
    counter = counter+1

    
### collecting start year (p.s.: being careful to keep NaNs as they show up)  
NewTable['year_cataloged'] = np.nan
d1 = []
counter=0
for row in Table['DataDeEntrada']:
    try:  # if Start Date is empty, keep it so 
        if np.isnan(row):
            year= np.NAN
    
    except:
        if not str(row).find('/')==-1:
            dates_values = str(row).split("/")
            year = int(dates_values[-1])
            month = int(dates_values[1])
#            if (month>1) and (month<12):
                #store the year and month in a datetime datatype for later sorting
#                dateRecord = datetime.datetime(year,month,1)    

    NewTable.loc[counter, 'year_cataloged'] = year
    counter = counter+1

# NewTable['determined_year'] = pd.Series(year, index=NewTable.index)
NewTable.head(2)
