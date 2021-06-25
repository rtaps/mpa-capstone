# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:18:52 2021

@author: Rebecca
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the EV data file
ev_data = '2020-07-EV-Dashboard-Data.xlsx'

ev = pd.read_excel(ev_data,dtype={'GEOID10':str})

# Limit to cars that are registered in-state; dropping vehicles registered out of state
ev = ev[ev['US_CNTY_CD'] != 'Out of state']

x = ev[ ev['GEOID10'].isna() ]

ev = ev.drop(columns=['GEOID'])

ev['GEOID'] = ev['GEOID10']

ev['make_mod'] = ev['make1'] + ' ' + ev['model1']

# Keeping EV model years to 2011 and above
is_recent = ev['model_yr'] > 2010

ev = ev[is_recent]

make = ev.groupby(['model_yr','make1']).size()

make.to_csv('vehicles.csv')

#%%
# Dropping non-car or SUV EVs
typ = ev.set_index('VEH_TYPE')
typ = typ.drop(['Motorcycle','Low-Speed Car','Moped'],axis=0)

typ = typ.groupby(['VEH_TYPE']).size()

# set the year as the index
# separate column for each kind of car
# seaborn - for each record it'd be the year model and number of them 
# x as year and hue = model
# y is count

mod = ev.groupby(['model_yr','make1']).size()


#test = typ.groupby(['model_yr','make1']).size()

#uns = mod.unstack('make1')
#uns = uns.fillna(0)
#uns.plot.bar(stacked=True)
#uns.save_file('draft-chart.png',dpi=300)


fig, ax1 = plt.subplots()
plt.hist(ev['model_yr'],color=['teal'])
fig.tight_layout()


#%%
x1 = ev['make_mod'].astype(str)
x2 = ev['model_yr'].astype(str)

fig, ax1 = plt.subplots()
plt.hist( x1, x2)
fig.suptitle("Title")
ax1.set_title(None)
ax1.set_ylabel("Total")
ax1.set_xlabel("Model year")

fig.tight_layout()
