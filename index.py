# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 23:07:12 2021

@author: Rebecca
"""

import pandas as pd
import geopandas

# Each block can be used for a different set of variables as the Census limits each call to 50 per CSV

# Load the first file
filename = 'data-census-variables-1.csv'

use_type = { 'GEOID':str }

file = pd.read_csv( filename, dtype=use_type )

# Compute the proportion of renters in each block group
file['tenu_p-rent'] = file['tenu_rent'] / file['tenu_tot']

# Compute the proportion of non-white people in each block group
file['race_nonw'] = file['race_tot'] - file['race_white']

file['race_prop'] = file['race_nonw'] / file['race_tot']

to_file = file[ [ 'GEOID', 'race_prop', 'race_nonw', 'tenu_p-rent', 'tenu_rent', 'tenu_tot' ] ]

to_file.to_csv( 'race-tenure-data.csv' )

# Load the GPKG file of the block groups in the service territory
terr = 'final-bg-territory.gpkg'

bg = geopandas.read_file( terr )

# Merge the variables with the block groups
merged1 = bg.merge( to_file, on='GEOID', how='left', indicator=True )

merged1 = merged1.drop( columns=['_merge'] )

# Compute the quintiles for each variable
merged1['race_quint'] = pd.qcut( merged1['race_prop'], 5, labels=False )

merged1['tenu_quint'] = pd.qcut( merged1['tenu_p-rent'], 5, labels=False )

merged1.to_file( 'race-tenure.gpkg', layer='bg', driver='GPKG' )

#%%

# Load the second variable CSV file
filename = 'data-census-variables-2.csv'

use_type = { 'GEOID':str }

file2 = pd.read_csv( filename, dtype=use_type )

# Compute the proportion of low income people - 60% of the 2019 median income in oregon
high_inc = file2['hhinc_40-45'] + file2['hhinc_45-50'] + file2['hhinc_50-60'] + file2['hhinc_60-75'] + file2['hhinc_75-100'] + file2['hhinc_100-125'] + file2['hhinc_125-150'] + file2['hhinc_150-200'] + file2['hhinc_>200']
file2['hhinc_low'] = file2['hhinc_tot'] - high_inc
file2['hhinc_prop'] = file2['hhinc_low'] / file2['hhinc_tot']

# Compute the proportion of people who have received public assistance
file2['passist_prop'] = file2['passist_with'] / file2['passist_tot']

to_file = file2[ [ 'GEOID', 'hhinc_low', 'hhinc_prop', 'passist_prop' ] ]

to_file.to_csv( 'hhinc-passist-data.csv' )

# Load the GPKG file of the block groups in the service territory
terr = 'final-bg-territory.gpkg'

bg = geopandas.read_file( terr )

# Merge the variables with the block groups
merged2 = bg.merge( to_file, on='GEOID', how='left', indicator=True )

merged2 = merged2.drop( columns=['_merge'] )

# Compute the quintiles for each variable
merged2['inc_quint'] = pd.qcut( merged2['hhinc_prop'], 5, labels=False )

merged2['assist_quint'] = pd.qcut( merged2['passist_prop'], 5, labels=False )

merged2.to_file( 'hhinc-passist.gpkg', layer='bg', driver='GPKG' )


#%%

filename = 'data-census-variables-3.csv'

use_type = { 'GEOID':str }

file3 = pd.read_csv( filename, dtype=use_type )

# Compute the proportion of households that speak a language other than English
file3['hhlang_not-e'] = file3['hhlang_tot'] - file3['hhlang_eng']
file3['hhlang_prop'] = file3['hhlang_not-e'] / file3['hhlang_tot']

# Compute the proportion of households with limited english speaking
file3['hhlang_lim'] = file3['hhlang_slim'] + file3['hhlang_inlim'] + file3['hhlang_asli'] + file3['hhlang_limo']
file3['hhlang_lipro'] = file3['hhlang_lim'] / file3['hhlang_tot']

to_file = file3[ [ 'GEOID', 'hhlang_prop', 'hhlang_not-e', 'hhlang_lipro', 'hhlang_lim' ] ]

to_file.to_csv( 'hhlang-data.csv' )

# Load the GPKG file of the block groups in the service territory
terr = 'final-bg-territory.gpkg'

bg = geopandas.read_file( terr )

# Merge the variables with the block groups
merged3 = bg.merge( to_file, on='GEOID', how='left', indicator=True )

merged3 = merged3.drop( columns=['_merge'] )

# Compute the quintiles for each variable
merged3['hhlang_quint'] = pd.qcut( merged3['hhlang_prop'], 5, labels=False )

merged3.to_file( 'hhlang.gpkg', layer='bg', driver='GPKG' )
#%%

# Establish the index

def get_quint( df, name ): 
    cur = df[ [ 'GEOID', name ] ]
    cur = cur.set_index( 'GEOID' )
    return cur 

race = get_quint( merged1, 'race_quint' )
tenure = get_quint( merged1, 'tenu_quint' )
inc = get_quint( merged2, 'inc_quint' ) 
assist = get_quint( merged2, 'assist_quint' )
lang = get_quint( merged3, 'hhlang_quint' )

quints = race

quints = quints.rename( columns={ 'race_quint':'race' } )
quints['tenure'] = tenure
quints['inc'] = inc
quints['assist'] = assist
quints['lang'] = lang

quints['mean'] = quints.sum( axis='columns' ) / 5

terr = 'final-bg-territory.gpkg'

bg = geopandas.read_file( terr )

quintiles = bg.merge( quints, on='GEOID', how='left', indicator=True )

quintiles = quintiles.drop( columns=['_merge'] )

quintiles.to_file( 'quintiles.gpkg', layer='quintiles', driver='GPKG' )