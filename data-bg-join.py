# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 20:13:23 2021

@author: Rebecca
"""

import pandas as pd

census_2 = 'data-census-variables-2.csv'

census = pd.read_csv(census_2,dtype=str)

hh_inc = census[['hhinc_<10', 'hhinc_10-15', 'hhinc_15-20', 'hhinc_20-25', 'hhinc_25-30', 'hhinc_30-35', 'hhinc_35-40', 'hhinc_40-45', 'hhinc_45-50', 'hhinc_50-60', 'hhinc_60-75','hhinc_med','GEOID']]

grid = 'blockgroup_grid.csv'

bg = pd.read_csv(grid,dtype=str)

bg = bg.drop(columns=['Unnamed: 0'])

merged = hh_inc.merge(bg,on='GEOID',how='inner',indicator=True)

merged = merged.drop(columns=['_merge'])

merged.to_csv('initial-merged-data.csv')

#%%
#hh_vars = [c for c in census.columns if c.startswith('hhinc_')]

#hh_inc = census[hh_vars,['GEOID']]

#pop = census[['tot_pop','GEOID']]

#race_vars = [c for c in census.columns if c.startswith('race_')]

#race_data

#sub = [c for c in d.columns if c.startswith('ed_')]


