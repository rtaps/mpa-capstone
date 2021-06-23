# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 15:16:03 2021

@author: Rebecca
"""

import geopandas
import pandas as pd

transm_data = 'Electric_Transmission_Lines2020.gdb'

transmission = geopandas.read_file(transm_data,driver='OpenFileGDB')

transmission.to_file('or-transmission-lines.gpkg',layer='transmission',driver='GPKG')

subst_data = 'Electric_Substations2020.gdb'

substations = geopandas.read_file(subst_data,driver='OpenFileGDB')

substations.to_file('or_substations.gpkg',layer='substations',driver='GPKG')

terr = 'service_territory.gpkg'

territory = geopandas.read_file(terr)

subst_clip = geopandas.clip(substations,territory['geometry'])
subst_clip.to_file('substations.gpkg',layer='territory',driver='GPKG')

#%%
transm_clip = geopandas.clip(transmission,territory['geometry'])
transm_clip.to_file('transmission.gpkg',layer='territory',driver='GPKG')