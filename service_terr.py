# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 23:25:24 2021

@author: Rebecca
"""
# Read the service territory shapefile and Census block group shapefile
# Do a spatial join and write to gpkg to display block groups in the territory

import geopandas

# Census Block Groups
    
or_bg_counties = 'zip://tl_2020_41_bg.zip'

block_groups = geopandas.read_file(or_bg_counties)

# Service territory

service_shp = 'zip://PGE_ServiceTerritory.zip'

service_territory = geopandas.read_file(service_shp)

service_territory.to_file('initial_serviceterritory.gpkg',
                          layer='service_territory',
                          driver='GPKG')

# Set the projection of the block groups to that off the service territory

block_groups = block_groups.to_crs(epsg=2913)

# Join the block groups onto the service territory

service_blockgrps_o = geopandas.sjoin(block_groups,
                                    service_territory,
                                    how="inner",
                                    op='overlaps')

service_blockgrps_w = geopandas.sjoin(block_groups,
                                    service_territory,
                                    how="inner",
                                    op='within')

service_blockgrps = service_blockgrps_o.append(service_blockgrps_w)

service_blockgrps = service_blockgrps.drop(columns=['index_right'])

service_blockgrps.to_csv('service_territory_blockgroups.csv')

service_blockgrps.to_file('service_blockgroups.gpkg',
                          layer='service_territory',
                          driver='GPKG')
