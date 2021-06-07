# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 14:19:06 2021

@author: Rebecca
"""

import requests
import pandas as pd

var_file = 'census-variables-1.csv'
out_file = 'data-'+var_file

var_info = pd.read_csv(var_file)

var_name = [n+"E" for n in var_info['variable']]
var_list = ['NAME']+var_name
var_string = ','.join(var_list)

api = "https://api.census.gov/data/2019/acs/acs5"

for_clause = 'block group:*'
in_clause = 'county:* state:41'

key_value = "3f1a4a5d44c6fc9c1f538e64cbb1d7bd64ec3d4c"

payload = {'get':var_string,'for':for_clause,'in':in_clause,'key':key_value}

response = requests.get(api,payload)

if response.status_code == 200 :
    print('Request successful')
else:
    print('Returned status:',response.status_code)
    print('Returned text:',response.text)
    assert False 

row_list = response.json()

colnames = row_list[0]
datarows = row_list[1:]

attain = pd.DataFrame(columns=colnames,data=datarows)
attain.set_index('NAME',inplace=True)

# Concatenate the state county etc
# GEOID

attain.to_csv(out_file)
