# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 15:03:38 2021

@author: Rebecca
"""

import geopandas

# Counties: Columbia, Washington, Multnomah, Yamhill, Clackamas, Marion, Polk

#list with just county GEOIDs (009 etc)
# Loop through to read each census things once at a time and append
# append onto a blank geopackage before the loop - will add stuff as necessary
# Not a blank pandas dataframe
# good application of an f string

columbia_roads = 'zip://tl_2019_41009_roads.zip'
washington_roads = 'zip://tl_2019_41067_roads.zip'
multnomah_roads = 'zip://tl_2019_41051_roads.zip'
yamhill_roads = 'zip://tl_2019_41071_roads.zip'
clackamas_roads = 'zip://tl_2019_41005_roads.zip'
marion_roads = 'zip://tl_2019_41047_roads.zip'
polk_roads = 'zip://tl_2019_41053_roads.zip'

columb = geopandas.read_file(columbia_roads)
wash = geopandas.read_file(washington_roads)
mult = geopandas.read_file(multnomah_roads)
yam = geopandas.read_file(yamhill_roads)
clack = geopandas.read_file(clackamas_roads)
mar = geopandas.read_file(marion_roads)
polk = geopandas.read_file(polk_roads)

