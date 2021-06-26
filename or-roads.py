# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 15:03:38 2021

@author: Rebecca
"""

import geopandas

# Identify the counties in the service territory and their ID numbers
# Counties: Columbia, Washington, Multnomah, Yamhill, Clackamas, Marion, Polk

co_ids = [ '009', '067', '051', '071', '005', '047', '053' ]

n = 0
for c in co_ids:
    filename = f"zip://tl_2019_41{c}_roads.zip"
    co_roads = geopandas.read_file( filename )
    if n == 0: 
        or_roads = co_roads
    else:
        or_roads = or_roads.append( co_roads )
    n = n + 1

or_roads = or_roads.to_crs( epsg=2913 )

or_roads.to_file( 'roads.gpkg', layer='roads_all', driver='GPKG' )

# Use QGIS or another GIS software to clip the roads to the service territory