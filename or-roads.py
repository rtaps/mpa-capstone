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

co_ids = ['009','067','051','071','005','047','053']

n = 0
for c in co_ids:
    filename = f"zip://tl_2019_41{c}_roads.zip"
    co_roads = geopandas.read_file(filename)
    if n == 0: 
        or_roads = co_roads
    else:
        or_roads = or_roads.append(co_roads)
    n = n+1

or_roads = or_roads.to_crs(epsg=2913)

#%%    
or_roads.to_file('roads.gpkg',layer='roads_all',driver='GPKG')


# Clip to the service territory
# Don't want any new attributes

terr = 'service_territory.gpkg'

territory = geopandas.read_file(terr)

#roads = geopandas.clip(or_roads, territory)

roads = geopandas.clip(or_roads, territory['geometry'])

#roads.to_file('clipped-roads.gpkg',layer='territory',driver='GPKG')
# reload the real territory and do a dissolve on it to get one polygon
# then do the clip this way if it doesn't take that long
# If it takes too long, go through QGIS 
# Then save the clip version