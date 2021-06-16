# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 15:07:31 2021

@author: Rebecca
"""

import requests
import pandas as pd


api = "https://developer.nrel.gov/api/alt-fuel-stations/v1.json"

key_value = "eaGZjo5y1ooxlzIpc1guONFfVQ6hkjlYWNWBAduh"

payload = {'api_key':key_value,'status':'all'}

response = requests.get(api,payload)

if response.status_code == 200 :
    print('Request successful')
else:
    print('Returned status:',response.status_code)
    print('Returned text:',response.text)
    assert False 

station_info = response.json()
station_list = station_info['fuel_stations']
stations = pd.DataFrame().from_records(station_list)

stations.to_csv('all-alt-stations.csv')

#%%
payload_2 = {'api_key':key_value,'status':'all','fuel_type':'ELEC','state':'OR'}

response = requests.get(api,payload_2)

if response.status_code == 200 :
    print('Request successful')
else:
    print('Returned status:',response.status_code)
    print('Returned text:',response.text)
    assert False 

station_info = response.json()
station_list = station_info['fuel_stations']
stations = pd.DataFrame().from_records(station_list)

stations.to_csv('or-ev-stations.csv')

#%%
terr = 'final-bg-territory.gpkg'
