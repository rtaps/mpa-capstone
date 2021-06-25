# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 23:07:12 2021

@author: Rebecca
"""

import pandas as pd
import matplotlib.pyplot as plt
import geopandas

filename = 'data-census-variables-1.csv'

use_type = {'GEOID':str}

file = pd.read_csv(filename,dtype=use_type)

# This is the proportion of renters
file['tenu_p-rent'] = file['tenu_rent']/file['tenu_tot']

# This is the proportion of non-white people
file['race_nonw'] = file['race_tot'] - file['race_white']

file['race_prop'] = file['race_nonw']/file['race_tot']

to_file = file[['GEOID','race_prop','race_nonw','tenu_p-rent','tenu_rent','tenu_tot']]

to_file.to_csv('race-tenure-data.csv')

terr = 'final-bg-territory.gpkg'

bg = geopandas.read_file(terr)

merged1 = bg.merge(to_file,on='GEOID',how='left',indicator=True)

merged1 = merged1.drop(columns=['_merge'])

merged1['race_quint'] = pd.qcut(merged1['race_prop'], 5, labels=False)

merged1['tenu_quint'] = pd.qcut(merged1['tenu_p-rent'], 5, labels=False)

merged1.to_file('race-tenure.gpkg',layer='bg',driver='GPKG')

#race = file['race_prop']
#rent = file['tenu_p-rent']
#county = file['county']
#geo = file['GEOID']

#fig, ax1 = plt.subplots()

#plt.bar(county,rent)
#fig.suptitle("Title")
#ax1.set_title(None)
#ax1.set_ylabel("Percent renters")
#ax1.set_xlabel("County")
#fig.tight_layout()

#%%

import pandas as pd
import matplotlib.pyplot as plt
import geopandas 
import numpy as np

filename = 'data-census-variables-2.csv'

use_type = {'GEOID':str}

file2 = pd.read_csv(filename,dtype=use_type)

# Proportion of low income people ie 60 percent of the 2019 median income in oregon
high_inc = file2['hhinc_40-45'] + file2['hhinc_45-50'] + file2['hhinc_50-60'] + file2['hhinc_60-75'] + file2['hhinc_75-100'] + file2['hhinc_100-125'] + file2['hhinc_125-150'] + file2['hhinc_150-200'] + file2['hhinc_>200']
file2['hhinc_low'] = file2['hhinc_tot'] - high_inc
file2['hhinc_prop'] = file2['hhinc_low']/file2['hhinc_tot']

# Proportion of people who have received public assistance
file2['passist_prop'] = file2['passist_with']/file2['passist_tot']

#to_write = file2[['GEOID','hhinc_low']]
to_file = file2[['GEOID','hhinc_low','hhinc_prop','passist_prop']]

to_file.to_csv('hhinc-passist-data.csv')

terr = 'final-bg-territory.gpkg'

bg = geopandas.read_file(terr)

merged2 = bg.merge(to_file,on='GEOID',how='left',indicator=True)

merged2 = merged2.drop(columns=['_merge'])

merged2['inc_quint'] = pd.qcut(merged2['hhinc_prop'], 5, labels=False)

merged2['assist_quint'] = pd.qcut(merged2['passist_prop'], 5, labels=False)

merged2.to_file('hhinc-passist.gpkg',layer='bg',driver='GPKG')

#%%

import pandas as pd
import matplotlib.pyplot as plt

filename = 'data-census-variables-3.csv'

use_type = {'GEOID':str}

file3 = pd.read_csv(filename,dtype=use_type)

# Houses that speak other than English
file3['hhlang_not-e'] = file3['hhlang_tot'] - file3['hhlang_eng']
file3['hhlang_prop'] = file3['hhlang_not-e']/file3['hhlang_tot']

# Houses with limited english speaking
file3['hhlang_lim'] = file3['hhlang_slim'] + file3['hhlang_inlim'] + file3['hhlang_asli'] + file3['hhlang_limo']
file3['hhlang_lipro'] = file3['hhlang_lim']/file3['hhlang_tot']

to_file = file3[['GEOID','hhlang_prop','hhlang_not-e','hhlang_lipro','hhlang_lim']]

to_file.to_csv('hhlang-data.csv')

terr = 'final-bg-territory.gpkg'

bg = geopandas.read_file(terr)

merged3 = bg.merge(to_file,on='GEOID',how='left',indicator=True)

merged3 = merged3.drop(columns=['_merge'])

merged3['hhlang_quint'] = pd.qcut(merged3['hhlang_prop'], 5, labels=False)

merged3.to_file('hhlang.gpkg',layer='bg',driver='GPKG')

#%%

# Making the index!!

race = merged1[['race_quint','GEOID']]

tenure = merged1['tenu_quint']

inc = merged2['inc_quint'] 

assist = merged2['assist_quint']

lang = merged3['hhlang_quint']

quints = [race, tenure, inc, assist, lang]

index = pd.DataFrame()
index = index.join(quints)    

