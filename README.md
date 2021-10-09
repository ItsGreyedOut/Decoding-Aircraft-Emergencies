# Project-3

# 🧐 Decoding Aircraft Emergencies

![alt text](http://github.com/itsgreyedout/project-3/blob/master/images/airplane.jpg?raw=true)

## About this project:
As frequent flyers, our team was interested in exploring in-flight emergency air situations using squawk 7700 codes. We created an interactive web dashboard using Heroku to explore over 4.2 million rows of data from OpenSky which we loaded into PostgreSQL. 

Data is derived from the OpenSky dataset in order to illustrate in-flight emergency situations triggering the 7700 transponder code. Data spans flights seen by the network's more than 2500 members between 1 January 2018 and 29 January 2020.

Multiple charts update from data that is stored in PostgreSQL. The project is powered by a Python Flask API and Heroku. 

Airlines can use this data to highlight safety issues they need to address and compare aircraft performance. Customers can use this data to learn about frequent flight emergencies and select airlines or aircraft types with fewer emergencies. 

Dashboard Link: [Link](https://gtdsproject3aircraftdata.herokuapp.com/)

## Technologies: :hammer:	
- Python
- SQLAlchemy
- SQL
- PostgreSQL
- Javascript
- D3
- Chart.js
- Leaflet
- HTML/Bootstrap/CSS
- Flask
- Heroku


## Architectural Diagram:
![ETL](https://github.com/ItsGreyedOut/Project-3/blob/master/images/airplane_etl_diagram.png)

## Approach
1. Identify data sources and dependencies
2. Collect and clean aircraft, emergency and flight trajectory data
3. Join 3 datasets on flight_id & icao
4. Load data in PostgreSQL using SQLAlchemy
5. Create Flask App and connect routes to PostgreSQL
6. Create charts and map using Javascript libraries
7. Customize html and css for final application
8. Visualize dashboard in Heroku

## Limitations & Assumptions
- Limited time of project
- Flight data is from before Feb 2020
- Only 813 rows of squawk code 7700 data
- Assume data is correct via OpenSky


## Data Sources:
Data is derived from the OpenSky dataset. Data spans flights seen by the network's more than 2500 members between 1 January 2018 and 29 January 2020.

- [Aircraft Metadata zip](https://opensky-network.org/datasets/metadata/)
- [Aircraft Flight parquet.gz](https://zenodo.org/record/3937483#.YVYFBUbMIdV)
- [Flight Summary 7700.csv](https://zenodo.org/record/3937483#.YVYFBUbMIdV) 

## Schema (ERD): 
![ERD](https://github.com/ItsGreyedOut/Project-3/blob/master/images/ERD.png)

## Dashboard: 


## Contributors:

Lauren To -  https://github.com/laurenemilyto

Jack Cohen -  https://github.com/jackatopolis

Matthew Bishop - https://github.com/mabishop84

Grey Hardy -  https://github.com/ItsGreyedOut
