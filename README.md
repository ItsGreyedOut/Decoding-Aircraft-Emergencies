# 🧐 Decoding Aircraft Emergencies

![alt text](http://github.com/itsgreyedout/project-3/blob/master/images/airplane.jpg?raw=true)

## About this project:
As frequent flyers, our team was interested in exploring in-flight emergency air situations using squawk 7700 codes. We created an interactive web dashboard using Heroku to explore over 4.2 million rows of data from OpenSky which we loaded into PostgreSQL. 

Data is derived from the OpenSky dataset in order to illustrate in-flight emergency situations triggering the 7700 transponder code. Data spans flights seen by the network's more than 2500 members between 1 January 2018 and 29 January 2020.

Multiple charts update from data that is stored in PostgreSQL. The project is powered by a Python Flask API and Heroku. 

## Business implications:
Airlines can use this data to highlight safety issues they need to address and compare aircraft performance. This data can help governing entities and aerospace companies like the FAA, etc. determine where issues most commonly arise. Customers can use this data to learn about frequent flight emergencies and select airlines or aircraft types with fewer emergencies. 

## Technologies: :hammer:	
- Python
- SQLAlchemy
- PostgreSQL
- Javascript
- D3
- Chart.js
- Leaflet
- HTML/Bootstrap/CSS
- Flask
- Heroku

## Architectural Diagram:
![ETL](https://i.pinimg.com/originals/b1/79/90/b17990f25c4ac34d41b1e759e472a980.jpg)

## Approach
1. Identify data sources and dependencies
2. Collect and clean aircraft, emergency and flight trajectory data
3. Join 3 datasets on flight_id & icao
4. Load data in PostgreSQL using SQLAlchemy
5. Create Flask App and connect routes to PostgreSQL
6. Create charts and map using Javascript libraries
7. Customize html and css for final application
8. Visualize dashboard locally or in Heroku

## Transformations
- Create SQL schemas
- Lowercase column names so that they can be loaded into postgresql
- Convert data types
- Remove NaN values and rows
- Query and filter using SQLAlchemy
- Jsonify data to power javascript visualizations

## Limitations, Assumptions & Challenges
- Limited time of project
- Flight data is from Jan 2018 to Feb 2020
- Only 813 flights of squawk code 7700 data, however each flight has many rows of data
- Assume data is correct since the dataset was manually filled with research from various sources on the Internet to fill missing info from OpenSky
- One of the biggest challenges in this project was trying to deploy our website on Heroku. Our database had around 4.2 million rows of data. It wasn't until we completed the project that we learned the free version of Heroku has a limitation of 10k records. Since each row is a lat/long point on our flight path visualization, we could not reduce our dataset without rebuilding our final application. We were unable to do this to time constraints. Deploying an application to Heroku for the first time, we learned many new things like importing correct libraries, modifying flask, connecting to Heroku's database, and ensuring that your data is under 10k records.

## Run Flask
To Deploy our Flask App, please follow the below steps :

- Step 1: Git clone our repository 
- Step 2: Confirm that jupyter notebook is up and running with the env where you have the python libraries mentioned in the notebook installed
- Step 3: Confirm that you have postgress app up and running in your machine
- Step 4: Confirm that your postgress username and password is added to the config.py
- Step 5: Create a database in postgres called 'aircraft_project'
- Step 6: Use the aircraft_schema file to run the create table commands
- Step 7: Run aircraft_traffic.ipynb jupyter notebook to connect to PostgreSQL and upload data into SQL database
- Step 8: Confirm that your app.py file has the correct password for PostgreSQL for engine.config
- Step 10: Execute command python app.py and launch the server using URL: http://127.0.0.1:5000/

## Data Sources:
Data is derived from the OpenSky dataset. Data spans flights seen by the network's more than 2500 members between 1 January 2018 and 29 January 2020.

- [Aircraft Metadata zip](https://opensky-network.org/datasets/metadata/)
- [Aircraft Flight parquet.gz](https://zenodo.org/record/3937483#.YVYFBUbMIdV)
- [Flight Summary 7700.csv](https://zenodo.org/record/3937483#.YVYFBUbMIdV) 

## Schema (ERD): 
Our schema consists of 3 tables, linked via flight_id and icao24 ids. Tables consist of 4.2 million rows of data.
![ERD](https://i.pinimg.com/originals/86/17/5b/86175b976971235e668c1d22cc378ef3.jpg)

## Visualizations & Analysis
We created several interactive visualizations for our website using JavaScript libraries like Leaflet, Plotly and D3. A walkthrough of our application is below: 

 <img src="http://github.com/itsgreyedout/project-3/blob/master/images/application_walkthrough.gif" alt="application_walkthrough_gif" title="application_walkthrough_gif" width = 300 />

#### Emergency Aircraft Dashboard
- Select a flight date, origin or problem from one of the dropdowns
![Flight data1](https://i.pinimg.com/originals/50/12/07/501207287434926a415418c0dd752f75.jpg)
- Select a flight from the table
![Flight data2](https://i.pinimg.com/originals/1b/84/e5/1b84e5007ac8a09ada8156fdce3f9757.jpg)
- Aircraft and Flight info data and visualization dynamically update for selected flight
![Flight data3](hhttps://i.pinimg.com/originals/f7/21/46/f7214693871d62ff9cf85ce1dc3a24bd.jpg)
- Flight Telemetry data and visualization dynamically update for selected flight
![Flight data4](https://i.pinimg.com/originals/26/79/a9/2679a9416896d95791d1a1b48ee85469.jpg)
- Flight Map data and visualization dynamically update to show flight path of selected flight
![Flight data5](https://i.pinimg.com/originals/77/1e/d6/771ed657a1c828d41790a7f8ff2045c0.jpg)

#### Squawk 7700 Statistics 
- Select flight manufacturer, origin, aircraft type, avh problem, avh result from the dropdown
- Data and visualization title dynamically update
![Flight data3](https://i.pinimg.com/originals/44/ed/6f/44ed6fd40fc286faeb1b753c6fe08de7.jpg)

## Website Design
This application includes 3 responsive webpages with dynamic navigation built using HTML, CSS, and Bootstrap.

![ERD](https://i.pinimg.com/originals/80/32/c0/8032c0441c2fd4d277184c3ac5e4363c.jpg)

## Contributors:

Lauren To -  https://github.com/laurenemilyto

Jack Cohen -  https://github.com/jackatopolis

Matthew Bishop - https://github.com/mabishop84

Grey Hardy -  https://github.com/ItsGreyedOut
