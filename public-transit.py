# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:27:51 2021

@author: Rebecca
"""

import geopandas

# Download the ZIP files as directed in the README file

# Load the ZIP files for both bus lines and stops
bus_lines = 'zip://buslines.zip'
bus_stops = 'zip://busstops.zip'

b_lines = geopandas.read_file( bus_lines )
b_stops = geopandas.read_file( bus_stops )

# Load the ZIP files for both light rail lines and stations
lrt_lines = 'zip://lrt_line.zip'
lrt_stops = 'zip://lrt_stop.zip'

l_lines = geopandas.read_file( lrt_lines )
l_stops = geopandas.read_file( lrt_stops )

bg_terr = 'final-bg-territory.gpkg'

territory = geopandas.read_file( bg_terr )
#%%

# Join the bus lines to the service territory
bline_terr = geopandas.sjoin(b_lines,
                             territory,
                             how="inner",
                             op='intersects')

bline_terr = bline_terr.drop( columns=['index_right'] )

bline_terr.to_file( 'bus-lines.gpkg', layer='b_lines', driver='GPKG' )
#%%

# Join the bus stops to the service territory
bstops_terr = geopandas.sjoin(b_stops,
                              territory,
                              how="inner",
                              op='intersects')

bstops_terr = bstops_terr.drop( columns=['index_right'] )

bstops_terr.to_file( 'bus-stops.gpkg', layer='b_lines', driver='GPKG' )
#%%

# Join the light rail lines to the service territory
llines_terr = geopandas.sjoin(l_lines,
                              territory,
                              how="inner",
                              op='intersects')

llines_terr = llines_terr.drop( columns=['index_right'] )

llines_terr.to_file( 'l-lines.gpkg', layer='l_lines', driver='GPKG' )
#%%

# Join the light rail stations to the service territory
lstops_terr = geopandas.sjoin(l_stops,
                              territory,
                              how="inner",
                              op='intersects')

lstops_terr = lstops_terr.drop( columns=['index_right'] )

lstops_terr.to_file( 'l-stops.gpkg', layer='l_stops', driver='GPKG' )