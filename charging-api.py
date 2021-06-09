# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 15:07:31 2021

@author: Rebecca
"""

import requests
import pandas as pd

# Do I need any of the variable file etc?
#var_file = 'NEED NAME HERE'
#out_file = 'data-'+var_file

#var_info = pd.read_csv(var_file)

#var_name = var_info['variable']]
#var_list = ['NAME']+var_name
#var_string = ','.join(var_list)

api = "https://developer.nrel.gov/api/alt-fuel-stations/v1.json"

#for_clause = 'county:*'
#in_clause = 'state:41'

key_value = "eaGZjo5y1ooxlzIpc1guONFfVQ6hkjlYWNWBAduh"
# limit to charging stations and state in payload, can keep status
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
# throw this into a csv and cut out everything else after 

