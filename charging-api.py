# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 15:07:31 2021

@author: Rebecca
"""

import requests
import pandas as pd
import geopandas

api = "https://developer.nrel.gov/api/alt-fuel-stations/v1.json"

# Request an API key from NREL prior to running the script
key_value = "eaGZjo5y1ooxlzIpc1guONFfVQ6hkjlYWNWBAduh"

# This payload returns information for all the alternative fuel stations in the US
payload = { 'api_key':key_value, 'status':'all' }

response = requests.get( api, payload )

if response.status_code == 200 :
    print( 'Request successful' )
else:
    print( 'Returned status:', response.status_code )
    print( 'Returned text:', response.text )
    assert False 

station_info = response.json()
station_list = station_info[ 'fuel_stations' ]
stations = pd.DataFrame().from_records( station_list )

stations.to_csv( 'all-alt-stations.csv' )

#%%

# This payload returns information for the electric fuel stations in Oregon
payload_2 = { 'api_key':key_value, 'status':'all', 'fuel_type':'ELEC', 'state':'OR' }

response = requests.get( api, payload_2 )

if response.status_code == 200 :
    print( 'Request successful' )
else:
    print( 'Returned status:', response.status_code )
    print( 'Returned text:', response.text )
    assert False 

station_info = response.json()
station_list = station_info['fuel_stations']
stations = pd.DataFrame().from_records( station_list )

stations.to_csv( 'or-ev-stations.csv' )

# Use QGIS or another GIS software to convert the geometry of the prior CSV to a GPKG 
charging = 'or-ev-charging.gpkg'

charg_stat = geopandas.read_file( charging )

terr = 'service_territory.gpkg'

territory = geopandas.read_file( terr )

# Join the state charging stations onto the desired service territory file
stations_bg = geopandas.sjoin( charg_stat,
                              territory,
                              how='inner',
                              op="intersects" )

stations_bg = stations_bg.drop( columns=['index_right'] )

stations_bg.to_file( 'ev-stations.gpkg', layer='charg_stat', driver='GPKG' )

stations_bg.to_csv( 'ev-stations.csv' )
