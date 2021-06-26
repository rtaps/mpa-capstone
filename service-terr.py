# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 23:25:24 2021

@author: Rebecca
"""

import geopandas
import pandas as pd

# Download the service territory SHP and Census block group SHP as directed in the README file

# Load the Census Block Groups    
or_bg_counties = 'zip://tl_2019_41_bg.zip'

block_groups = geopandas.read_file( or_bg_counties )

# Load the service territory
service_shp = 'zip://PGE_ServiceTerritory.zip'

service_territory = geopandas.read_file( service_shp )

service_territory.to_file( 'initial_serviceterritory.gpkg',
                          layer='service_territory',
                          driver='GPKG' )

# Set the projection of the block groups to that off the service territory
block_groups = block_groups.to_crs( epsg=2913 )

# Join the service territory onto the block groups once on overlaps and once on within
service_blockgrps_o = geopandas.sjoin(block_groups,
                                    service_territory,
                                    how="inner",
                                    op='overlaps')

service_blockgrps_w = geopandas.sjoin(block_groups,
                                    service_territory,
                                    how="inner",
                                    op='within')


service_blockgrps = service_blockgrps_o.append( service_blockgrps_w )

service_blockgrps = service_blockgrps.drop( columns=['index_right'] )

service_blockgrps.to_csv( 'service_territory_blockgroups.csv' )

service_blockgrps.to_file( 'service_blockgroups.gpkg',
                          layer='service_territory',
                          driver='GPKG' )

# Identify by sight in QGIS/a GIS software the block groups that have no overlap
# Format them by GEOID in a CSV to drop from the final file

# Create a dataframe of the block groups to drop
drop = 'drop-block-groups.csv'
bg_todrop = pd.read_csv( drop, dtype=str )
bg_todrop = list( bg_todrop['GEOID'] )

# Keep only the block groups not on the drop list  
bg_tokeep = service_blockgrps['GEOID'].isin(bg_todrop) == False
bg_service = service_blockgrps[ bg_tokeep ]

bg_service.to_file( 'final-bg-territory.gpkg',
                   layer='service_territory',
                   driver='GPKG' )