# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 18:23:50 2021

@author: Rebecca
"""

import geopandas

grid_file = 'or_grid_2mi.gpkg'
blockgroup_file = 'final-bg-territory.gpkg'

grid= geopandas.read_file(grid_file)

block_groups = geopandas.read_file(blockgroup_file)

bg_grid = geopandas.sjoin(grid,
                          block_groups,
                          how="left",
                          op='intersects')

bg_grid = bg_grid.drop(columns=['index_right'])

bg_grid.to_csv('blockgroup_grid.csv')

bg_grid.to_file('blockgroup_grid.gpkg',layer='grid',driver='GPKG')