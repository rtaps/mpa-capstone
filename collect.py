#! /bin/python3
#  Spring 2020 (PJW)
#
#  Use the Census API to collect information about educational
#  attainment by county for New York State.
#

import requests
import pandas as pd

#
#  Read the auxiliary file containing the list of variables and 
#  the groups they should be aggregated into.
#

var_info = pd.read_csv('census-variables.csv')

#
#  Get the names of the variables and build a string of 
#  variable names that can be passed to the Census API.
#

var_name = var_info['variable'].to_list()
var_list = ['NAME']+var_name
var_string = ','.join(var_list)

#
#  Set up the components of the API call. This omits my Census
#  API key since the code will be posted on the web.
#

api = "https://api.census.gov/data/2018/acs/acs5"

for_clause = 'county:*'
in_clause = 'state:36'

payload = {'get':var_string,'for':for_clause,'in':in_clause}

#
#  Make the API call and check whether an error code was 
#  returned.
#

response = requests.get(api,payload)

if response.status_code == 200 :
    print('Request successful')
else:
    print('Returned status:',response.status_code)
    print('Returned text:',response.text)
    assert False 

#
#  The results are in JSON. Parse the JSON into a Python object. 
# It will be a list of rows, each of which is itself a list.
#

row_list = response.json()

#
#  The first row is the column names and the remaining rows are the data.
#

colnames = row_list[0]
datarows = row_list[1:]

#
#  Build a Pandas dataframe and set the index to the NAME column.
#

attain = pd.DataFrame(columns=colnames,data=datarows)
attain.set_index('NAME',inplace=True)

#
#  Write out the results.
#

attain.to_csv('census-data.csv')
