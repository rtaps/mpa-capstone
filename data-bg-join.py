# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 20:13:23 2021

@author: Rebecca
"""

import pandas as pd
import geopandas

#census_2 = 'data-census-variables-2.csv'

census_inc = 'income-data.csv'

census = pd.read_csv(census_inc,dtype=str)

grid = 'blockgroup_grid2.gpkg'

bg = geopandas.read_file(grid)

#bg = bg.drop(columns=['Unnamed: 0'])

merged = bg.merge(census,on='GEOID',how='left',indicator=True)

merged = merged.drop(columns=['_merge'])

merged = merged.fillna(0)

trim = merged['hhinc_low'].to_frame()

trim['x'] = merged['geometry'].apply(lambda pt:pt[0].x)
trim['y'] = merged['geometry'].apply(lambda pt:pt[0].y)

trim.index.name = 'grid_point'

trim.to_csv('income-merged-data.csv')

#%%
#hh_vars = [c for c in census.columns if c.startswith('hhinc_')]

#hh_inc = census[hh_vars,['GEOID']]

#pop = census[['tot_pop','GEOID']]

#race_vars = [c for c in census.columns if c.startswith('race_')]

#race_data

#sub = [c for c in d.columns if c.startswith('ed_')]

#data = data.astype(float)
