# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 18:23:50 2021

@author: Rebecca
"""

import geopandas

grid_file = 'or_grid2mi.gpkg'
blockgroup_file = 'final-bg-territory.gpkg'

grid= geopandas.read_file(grid_file)

block_groups = geopandas.read_file(blockgroup_file)

bg_grid = geopandas.sjoin(grid,
                          block_groups,
                          how="left",
                          op='intersects')

bg_grid = bg_grid.drop(columns=['index_right','left','right','top','bottom'])

bg_grid.to_csv('blockgroup_grid2.csv')

bg_grid.to_file('blockgroup_grid2.gpkg',layer='grid',driver='GPKG')