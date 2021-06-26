# mpa-capstone
 
# Index of Underserved Communities: Targeting Transportation Electrification in Portland General Electric’s Service Territory

# 

## Summary
------
Expanding access to electrified transportation in historically marginalized and underserved communities is a vital part of implementing environmental justice and equity initiatives across the country. Low-income communities, particularly those of color, often experience the brunt of air pollution and climate change-related events and should be the priority for actions that can mitigate these effects. 

In this repository we use geospatial data analysis to pinpoint specific areas of PGE’s service territory to address gaps in access to electrified transportation. To do so we examine a number of characteristics of area residents, including: household income, whether residents rent or own their homes, race, primary language at home, and proximity to existing charging infrastructure. 

The median household income in Oregon in 2019 was $62,818. Our income cutoff matches that of PGE’s qualitative market research, which focused on households that earn 60% of the household median – approximately  $37,690. We included additional demographic factors that have also been shown to have effects on EV adoption – in particular, renting rather than owning a home, and not having access to a garage where a private home charging station could be installed.  

This repository contains several scripts that aggregate and analyze data to create an index of underserved communities in the Portland General Electric service territory. This index measures the following proportions at the Census block group level: 

-Households earning less than 60% of the 2019 Oregon median income; 

-People of color; 

-Households that receive public assistance;  

-Renters; 

-People who primarily speak a language other than English.  

The goal of this script is to establish a uniform index that accounts for the actual demography of the service area when measuring how they intersect. By doing so, PGE can use the index to inform where infrastructure and policy actions should be targeted in communities that do not already have access to resources.  

## Input Data 
------
Seven scripts, five CSV files, two GDB files, and 13 ZIP files as follows:

Request two API keys, from the following sources:
1. [NREL Developer Network](https://developer.nrel.gov/signup/)

2. [U.S. Census]( https://api.census.gov/data/key_signup.html)

### Shapefiles
------
1. Download the PGE Service Territory shapefile – provided by the utility

2. a) Census TIGER/Line County Block Group Shapefiles
    
    Follow the Web Interface Link at the [Census site](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html);
    
    Select the Year 2019 and the Block Group layer type,
    
    After hitting submit, select Oregon in the 2019 dropdown menu and download the file.

2. b) Census TIGER/Line Road Shapefiles

    Follow the Web Interface Link at the [Census site](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html);

    Select the Year 2019 and the Roads layer type, 

    After hitting submit, select Oregon in the 2019 dropdown menu and the county – for multiple counties, you will have to download multiple ZIP files.    

3. [Oregon Metro TriMet Shapefiles]( http://rlisdiscovery.oregonmetro.gov/?resourceId=99&searchTerm=transit);

    Select “Add to Queue” for the TriMet Bus System routes and stops, as well as the Light Rail lines and stations,

    After adding the files, choose “Download Selected” from “My Download Queue” to the left and follow any dialogues that pop up. 

4. [American Community Survey 2019 Data Tables]( https://www.census.gov/data/developers/data-sets/acs-5year.html);

    Select relevant variables from the ACS 5-Year survey and load into one or more CSV files with short descriptive names and longer, detailed names. 

    The Census limits variable calls to 50 variables per CSV, so multiple files are likely to be needed. 

5. [Oregon Spatial Data – Transmission Lines and Substations]( https://spatialdata.oregonexplorer.info/geoportal/)

    Initiate an FTP request for the transmission lines and substations and pull the GDB files from the ZIP that it generates. 


## Instructions
------
### Part 1: Downloading the Data and Generating Outputs 

1. Download the input data and API keys as detailed above.

2. Run the census-api script.

    i. The script will complete the API request to the Census and output one or multiple CSV files with the GEOID of each block group. 
    
3. Run the service-terr script. 

    i. The script will join the block groups and the service territory and output a geopackage displaying the result. 

4. Run the charging-api script.  
    
    i. The script will complete the API request to NREL and generate a CSV of all electric charging stations as well as a CSV of the Oregon electric charging stations. 

    ii. Load this CSV file into QGIS or another GIS software to convert the geometry of the prior CSV to a GPKG. 

    iii. After editing the name of that GPKG into the last part of the script, it will join the charging stations onto the service territory. 

5. Run the index script. 
    
    i. It will calculate the proportions of each variable in the block group, compute the quintiles, and generate GPKGs for each variable. 

    ii. It will also create a mean quintile for each variable to generate a single index score for the block groups, on a scale of 0-5, and join them to the service territory before writing that data to a GPKG. 

6. Run the or-roads script. 

    i. The script will run through the road ZIP files by county ID and generate a single GPKG of all the roads. 

7. Run the gdb-files script. 

    i. The script will generate two GPKGs, one for transmission lines and one for substations. 

8. Run the public-transit script. 

    i. The script will generate GPKGs for each file inputted – in this case, one each for bus lines, bus stops, light rail lines, and light rail stations. 

3. Confirm that the geopackages were created. 

### Part 2: Visualizing the Data 

1. Add new vector layers for each of the geopackages produced by the script. 

2. Filter and select the layers as desired to see the interactions between demographic data, electric charging stations (including location, charger type, price, and access), and existing infrastructure. 

3. The individual indices and overall index of the block groups should be clearly visible. 

4. Export your desired map layers as a png to save them. 

## Notes

1. Future examinations of data using this repository could include breaking out detailed demographic data, including race, to pinpoint who exactly needs access to expanded infrastructure. 

3. All gratitude goes to [Dr. Pete Wilcoxen](https://www.maxwell.syr.edu/wilcoxen/) for advising on this capstone project and supplying confidence when it was in short supply!
