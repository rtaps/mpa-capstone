# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 15:16:03 2021

@author: Rebecca
"""

import geopandas

# Pull the data from the FTP server as indicated in the README file
transm_data = 'Electric_Transmission_Lines2020.gdb'

transmission = geopandas.read_file( transm_data, driver='OpenFileGDB' )

transmission.to_file( 'or-transmission-lines.gpkg', layer='transmission', driver='GPKG' )

subst_data = 'Electric_Substations2020.gdb'

substations = geopandas.read_file( subst_data, driver='OpenFileGDB' )

substations.to_file( 'or_substations.gpkg', layer='substations', driver='GPKG' )

# Use QGIS or another GIS software to clip the transmission lines and substations to the service territory