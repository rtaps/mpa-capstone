# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 22:57:47 2021

@author: Rebecca
"""

import pandas as pd
import geopandas

var_file = 'data-census-variables-1.csv'
out_file = 'merge-'+var_file

census = pd.read_csv(var_file,dtype=str)

columns = [c for c in census.columns if c.startswith('tot')]
columns = columns + [c for c in census.columns if c.startswith('race')]
columns = columns + [c for c in census.columns if c.startswith('tenu')]
columns = columns + [c for c in census.columns if c.startswith('edu')]
columns = columns + [c for c in census.columns if c.startswith('comp')]

#census_floats = census[columns].astype(float)

for c in columns:
    census[c] = census[c].astype(float)
    
terr = 'final-bg-territory.gpkg'

bg = geopandas.read_file(terr)

merged = bg.merge(census,on='GEOID',how='left',indicator=True)

merged = merged.drop(columns=['_merge'])

merged.to_csv(out_file)

merged.to_file('merge-census-1.gpkg',layer='bg',driver='GPKG')

#%%



#columns = [c for c in census.columns if c.startswith('earn')]
#columns = columns + [c for c in census.columns if c.startswith('pass')]
#columns = columns + [c for c in census.columns if c.startswith('hhinc')]
#columns = columns + [c for c in census.columns if c.startswith('occ')]
#columns = columns + [c for c in census.columns if c.startswith('mort')]
#columns = columns + [c for c in census.columns if c.startswith('emp')]

#columns = [c for c in census.columns if c.startswith('hhlang')]
#columns = columns + [c for c in census.columns if c.startswith('grent')]

#columns = [c for c in census.columns if c.startswith('crent')]

#columns = [c for c in census.columns if c.startswith('tran')]
