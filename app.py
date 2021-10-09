import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from flask import render_template, request, redirect, url_for, flash

#################################################
# Database Setup
#################################################
connection_string = "postgres:postgres@localhost:5432/aircraft_project"
#matt_connection_string = "postgresql://postgres:Thatstraightline84!@localhost:5432/aircraft_project"
<<<<<<< HEAD
engine = create_engine(f'postgresql://{connection_string}')
# engine = create_engine(
    # "postgresql://postgres:postgres@localhost:5432/aircraft_project")
=======
#engine = create_engine(f'postgresql://{matt_connection_string}')
engine = create_engine("postgresql://postgres:postgres@localhost:5432/aircraft_project")
>>>>>>> jack

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
aircraft_metadata = Base.classes.aircraft_metadata
flight_summary = Base.classes.flight_summary
flight_trajectory = Base.classes.flight_trajectory

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def test_two_data():
    session = Session(engine)

    # Query all passengers
    results1 = session.query(flight_trajectory.timestamp, flight_trajectory.altitude,flight_trajectory.callsign, flight_trajectory.flight_id, flight_trajectory.groundspeed, flight_trajectory.icao24, flight_trajectory.latitude, flight_trajectory.longitude, flight_trajectory.squawk, flight_trajectory.track, flight_trajectory.vertical_rate).filter(flight_trajectory.icao24 == 'e06442').order_by(flight_trajectory.timestamp.desc())
    results2 = session.query(flight_summary.flight_id, flight_summary.callsign, flight_summary.number, flight_summary.icao24,flight_summary.registration, flight_summary.typecode, flight_summary.origin, flight_summary.landing, flight_summary.destination, flight_summary.diverted,flight_summary.tweet_problem, flight_summary.tweet_result, flight_summary.tweet_fueldump, flight_summary.avh_id, flight_summary.avh_problem, flight_summary.avh_result, flight_summary.avh_fueldump)
    results3 = session.query(aircraft_metadata.icao24, aircraft_metadata.registration, aircraft_metadata.manufacturericao, aircraft_metadata.manufacturername, aircraft_metadata.model, aircraft_metadata.typecode, aircraft_metadata.serialnumber, aircraft_metadata.linenumber, aircraft_metadata.icaoaircrafttype, aircraft_metadata.operator, aircraft_metadata.built, aircraft_metadata.firstflightdate, aircraft_metadata.engines, aircraft_metadata.notes, aircraft_metadata.categorydescription).filter(aircraft_metadata.icao24 == 'e06442')
  	
    session.close()

    timestamp= [result[0] for result in results1]
    altitude= [int(result[1]) for result in results1]
    callsign = [result[2] for result in results1]
    flight_id= [result[3] for result in results1]
    groundspeed= [int(result[4]) for result in results1]
    icao24 = [result[5] for result in results1]
    latitude= [int(result[6]) for result in results1]
    longitude= [int(result[7]) for result in results1]
    squawk = [int(result[8]) for result in results1]
    track= [int(result[9]) for result in results1]
    vertical_rate= [int(result[10]) for result in results1]
    
    trajectory_table = [{
        "Timestamp": timestamp,
        "Altitude": altitude,
        "Callsign": callsign,
        "Flight ID": flight_id,
        "Groundspeed": groundspeed,
        "ICAO24": icao24,
        "Latitude": latitude,
        "Longitude": longitude,
        "Squawk": squawk,
        "Track": track,
        "Vertical Rate":vertical_rate
    }]  

    flight_id2= [result[0] for result in results2]
    callsign = [result[1] for result in results2]
    number= [result[2] for result in results2]
    icao24 = [result[3] for result in results2]
    registration = [result[4] for result in results2]
    typecode= [result[5] for result in results2]
    origin = [result[6] for result in results2]
    landing= [result[7] for result in results2]
    destination = [result[8] for result in results2]
    diverted= [result[9] for result in results2]
    tweet_problem = [result[10] for result in results2]
    tweet_result= [result[11] for result in results2]
    tweet_fueldump = [result[12] for result in results2]
    avh_id = [result[13] for result in results2]
    avh_problem= [result[14] for result in results2]
    avh_result = [result[15] for result in results2]
    avh_fueldump = [result[16] for result in results2]
    
    flight_summary_table = [{
        "Flight ID": flight_id2,
        "Callsign": callsign,
        "Number": number,
        "ICAO24": icao24,
        "Registration":registration,
        "Typecode": typecode,
        "Origin": origin,
        "Landing": landing,
        "Destination": destination,
        "Diverted": diverted,
        "Tweet Problem": tweet_problem,
        "Tweet Result": tweet_result,
        "Tweet Fueldump": tweet_fueldump,
        "AVH ID": avh_id,
        "AVH Problem": avh_problem,
        "AVH Result": avh_result,
        "AVH Fueldump": avh_fueldump
    }] 

    icao24= [result[0] for result in results3]
    registration = [result[1] for result in results3]
    manufacturericao= [result[2] for result in results3]
    manufacturername = [result[3] for result in results3]
    model = [result[4] for result in results3]
    typecode= [result[5] for result in results3]
    serialnumber = [result[6] for result in results3]
    linenumber= [result[7] for result in results3]
    icaoaircrafttype = [result[8] for result in results3]
    operator= [result[9] for result in results3]
    built= [result[10] for result in results3]
    firstflightdate = [result[11] for result in results3]
    engines= [result[12] for result in results3]
    notes = [result[13] for result in results3]
    categorydescription = [result[14] for result in results3]

    aircraft_info_table  = [{
        "ICAO24": icao24,
        "Registration": registration,
        "Manufacturer ICAO": manufacturericao,
        "Manufacturer Name": manufacturername,
        "Model":model,
        "Typecode": typecode,
        "Serialnumber": serialnumber,
        "Line number": linenumber,
        "ICAO Aircraft Type": icaoaircrafttype,
        "Operator": operator,
        "Built": built,
        "First Flight Date": firstflightdate,
        "Engines": engines,
        "Notes": notes,
        "Category Description": categorydescription
    }]

    table_list=[trajectory_table, flight_summary_table, aircraft_info_table]
    return render_template('index.html', data = table_list)


@app.route("/flight_dashboard_<icao>")
def change(icao):
    session = Session(engine)

    # Query all passengers
    results1 = session.query(flight_trajectory.timestamp, flight_trajectory.altitude,flight_trajectory.callsign, flight_trajectory.flight_id, flight_trajectory.groundspeed, flight_trajectory.icao24, flight_trajectory.latitude, flight_trajectory.longitude, flight_trajectory.squawk, flight_trajectory.track, flight_trajectory.vertical_rate).filter(flight_trajectory.icao24 == icao).order_by(flight_trajectory.timestamp.desc())
    results2 = session.query(flight_summary.flight_id, flight_summary.callsign, flight_summary.number, flight_summary.icao24,flight_summary.registration, flight_summary.typecode, flight_summary.origin, flight_summary.landing, flight_summary.destination, flight_summary.diverted,flight_summary.tweet_problem, flight_summary.tweet_result, flight_summary.tweet_fueldump, flight_summary.avh_id, flight_summary.avh_problem, flight_summary.avh_result, flight_summary.avh_fueldump)
    results3 = session.query(aircraft_metadata.icao24, aircraft_metadata.registration, aircraft_metadata.manufacturericao, aircraft_metadata.manufacturername, aircraft_metadata.model, aircraft_metadata.typecode, aircraft_metadata.serialnumber, aircraft_metadata.linenumber, aircraft_metadata.icaoaircrafttype, aircraft_metadata.operator, aircraft_metadata.built, aircraft_metadata.firstflightdate, aircraft_metadata.engines, aircraft_metadata.notes, aircraft_metadata.categorydescription).filter(aircraft_metadata.icao24 == icao)
  	
    session.close()

    timestamp= [result[0] for result in results1]
    altitude= [float(result[1]) for result in results1]
    callsign = [result[2] for result in results1]
    flight_id= [result[3] for result in results1]
    groundspeed= [float(result[4]) for result in results1]
    icao24 = [result[5] for result in results1]
    latitude= [float(result[6]) for result in results1]
    longitude= [float(result[7]) for result in results1]
    squawk = [int(result[8]) for result in results1]
    track= [float(result[9]) for result in results1]
    vertical_rate= [float(result[10]) for result in results1]
    
    trajectory_table = [{
        "Timestamp": timestamp,
        "Altitude": altitude,
        "Callsign": callsign,
        "Flight ID": flight_id,
        "Groundspeed": groundspeed,
        "ICAO24": icao24,
        "Latitude": latitude,
        "Longitude": longitude,
        "Squawk": squawk,
        "Track": track,
        "Vertical Rate":vertical_rate
    }]  

    flight_id2= [result[0] for result in results2]
    callsign = [result[1] for result in results2]
    number= [result[2] for result in results2]
    icao24 = [result[3] for result in results2]
    registration = [result[4] for result in results2]
    typecode= [result[5] for result in results2]
    origin = [result[6] for result in results2]
    landing= [result[7] for result in results2]
    destination = [result[8] for result in results2]
    diverted= [result[9] for result in results2]
    tweet_problem = [result[10] for result in results2]
    tweet_result= [result[11] for result in results2]
    tweet_fueldump = [result[12] for result in results2]
    avh_id = [result[13] for result in results2]
    avh_problem= [result[14] for result in results2]
    avh_result = [result[15] for result in results2]
    avh_fueldump = [result[16] for result in results2]
    
    flight_summary_table = [{
        "Flight ID": flight_id2,
        "Callsign": callsign,
        "Number": number,
        "ICAO24": icao24,
        "Registration":registration,
        "Typecode": typecode,
        "Origin": origin,
        "Landing": landing,
        "Destination": destination,
        "Diverted": diverted,
        "Tweet Problem": tweet_problem,
        "Tweet Result": tweet_result,
        "Tweet Fueldump": tweet_fueldump,
        "AVH ID": avh_id,
        "AVH Problem": avh_problem,
        "AVH Result": avh_result,
        "AVH Fueldump": avh_fueldump
    }] 

    icao24= [result[0] for result in results3]
    registration = [result[1] for result in results3]
    manufacturericao= [result[2] for result in results3]
    manufacturername = [result[3] for result in results3]
    model = [result[4] for result in results3]
    typecode= [result[5] for result in results3]
    serialnumber = [result[6] for result in results3]
    linenumber= [result[7] for result in results3]
    icaoaircrafttype = [result[8] for result in results3]
    operator= [result[9] for result in results3]
    built= [result[10] for result in results3]
    firstflightdate = [result[11] for result in results3]
    engines= [result[12] for result in results3]
    notes = [result[13] for result in results3]
    categorydescription = [result[14] for result in results3]

    aircraft_info_table  = [{
        "ICAO24": icao24,
        "Registration": registration,
        "Manufacturer ICAO": manufacturericao,
        "Manufacturer Name": manufacturername,
        "Model":model,
        "Typecode": typecode,
        "Serialnumber": serialnumber,
        "Line number": linenumber,
        "ICAO Aircraft Type": icaoaircrafttype,
        "Operator": operator,
        "Built": built,
        "First Flight Date": firstflightdate,
        "Engines": engines,
        "Notes": notes,
        "Category Description": categorydescription
    }]

    table_list=[trajectory_table, flight_summary_table, aircraft_info_table]
    return render_template('index.html', data = table_list)


@app.route("/summary_stats")
def summary_stats():
     session = Session(engine)
     # Queries for summary statistics
<<<<<<< HEAD
     results1 = engine.execute('select distinct substr(am.manufacturername,1,6), count(distinct fs.flight_id) from flight_summary fs, flight_trajectory ft, aircraft_metadata am where fs.flight_id = ft.flight_id and am.icao24 = ft.icao24 group by substr(am.manufacturername,1,6) order by count(distinct fs.flight_id) DESC').fetchall()
     results2 = engine.execute('select distinct fs.origin, count(distinct fs.flight_id) from flight_summary fs, flight_trajectory ft, aircraft_metadata am where fs.flight_id = ft.flight_id and am.icao24 = ft.icao24 group by fs.origin order by count(distinct fs.flight_id) DESC').fetchall()
     results3 = engine.execute('select distinct fs.destination, count(distinct fs.flight_id) from flight_summary fs, flight_trajectory ft, aircraft_metadata am where fs.flight_id = ft.flight_id and am.icao24 = ft.icao24 group by fs.destination order by count(distinct fs.flight_id) DESC').fetchall()
     results4 = engine.execute('select distinct am.icaoaircrafttype, count(distinct fs.flight_id) from flight_summary fs, flight_trajectory ft, aircraft_metadata am where fs.flight_id = ft.flight_id and am.icao24 = ft.icao24 group by am.icaoaircrafttype order by count(distinct fs.flight_id) DESC').fetchall()
     results5 = engine.execute('select distinct fs.avh_problem, count(distinct fs.flight_id) from flight_summary fs, flight_trajectory ft, aircraft_metadata am where fs.flight_id = ft.flight_id and am.icao24 = ft.icao24 group by fs.avh_problem').fetchall()
     results6 = engine.execute('select distinct fs.avh_result, count(distinct fs.flight_id) from flight_summary fs, flight_trajectory ft, aircraft_metadata am where fs.flight_id = ft.flight_id and am.icao24 = ft.icao24 group by fs.avh_result').fetchall()
=======
     results1 = engine.execute('select distinct am.manufacturername, count(distinct fs.flight_id) from flight_summary fs, flight_trajectory ft, aircraft_metadata am where fs.flight_id = ft.flight_id and am.icao24 = ft.icao24 group by am.manufacturername having length(am.manufacturername)>3 order by count(distinct fs.flight_id) DESC limit(10)').fetchall()
     results2 = engine.execute('select distinct fs.origin, count(distinct fs.flight_id) from flight_summary fs, flight_trajectory ft, aircraft_metadata am where fs.flight_id = ft.flight_id and am.icao24 = ft.icao24 group by fs.origin having length(fs.origin)>3 order by count(distinct fs.flight_id) DESC limit(10)').fetchall()
     results3 = engine.execute('select distinct fs.destination, count(distinct fs.flight_id) from flight_summary fs, flight_trajectory ft, aircraft_metadata am where fs.flight_id = ft.flight_id and am.icao24 = ft.icao24 group by fs.destination having length(fs.destination)>3 order by count(distinct fs.flight_id) DESC limit(10)').fetchall()
     results4 = engine.execute('select distinct am.icaoaircrafttype, count(distinct fs.flight_id) from flight_summary fs, flight_trajectory ft, aircraft_metadata am where fs.flight_id = ft.flight_id and am.icao24 = ft.icao24 group by am.icaoaircrafttype having length(am.icaoaircrafttype)>1 order by count(distinct fs.flight_id) DESC limit(10)').fetchall()
     results5 = engine.execute('select distinct fs.avh_problem, count(distinct fs.flight_id) from flight_summary fs, flight_trajectory ft, aircraft_metadata am where fs.flight_id = ft.flight_id and am.icao24 = ft.icao24 group by fs.avh_problem having length(fs.avh_problem)>3 order by count(distinct fs.flight_id) DESC limit(10)').fetchall()
     results6 = engine.execute('select distinct fs.avh_result, count(distinct fs.flight_id) from flight_summary fs, flight_trajectory ft, aircraft_metadata am where fs.flight_id = ft.flight_id and am.icao24 = ft.icao24 group by fs.avh_result having length(fs.avh_result)>3 order by count(distinct fs.flight_id) DESC limit(10)').fetchall()
>>>>>>> jack
     session.close()
     #Manufacturer Table
     manufacturer= [result[0] for result in results1]
     numberofflights = [int(result[1]) for result in results1]
    
     manufacturer_table  = [{
        "Flight Manufacturer": manufacturer,
        "Number of Flights with 7700 Squawk Code": numberofflights
     }]
     #Origins with most Squawk Codes
     origin= [result[0] for result in results2]
     numberofflights2 = [int(result[1]) for result in results2]
    
     origin_table  = [{
        "Origin": origin,
        "Number of Flights with 7700 Squawk Code": numberofflights2
     }]
     #Destinations with most Squawk Codes
     destination= [result[0] for result in results3]
     numberofflights3 = [int(result[1]) for result in results3]
    
     destination_table  = [{
        "Destination": destination,
        "Number of Flights with 7700 Squawk Code": numberofflights3
     }]
     #Aircraft Type with most Squawk Codes
     aircraft_type= [result[0] for result in results4]
     numberofflights4 = [int(result[1]) for result in results4]
    
     aircraft_type_table  = [{
        "Aircraft Type": aircraft_type,
        "Number of Flights with 7700 Squawk Code": numberofflights4
     }]
     #Problem Frequency
     avh_problem= [result[0] for result in results5]
     numberofflights5 = [int(result[1]) for result in results5]
    
     problem_frequency_table  = [{
        "AVH Problem": avh_problem,
        "Number of Flights with 7700 Squawk Code": numberofflights5
     }]
     
     #Result Frequency
     avh_result= [result[0] for result in results6]
     numberofflights6 = [int(result[1]) for result in results6]
    
     result_frequency_table  = [{
        "AVH Result": avh_result,
        "Number of Flights with 7700 Squawk Code": numberofflights6
     }]
     table_list1=[manufacturer_table, origin_table, destination_table, aircraft_type_table, problem_frequency_table, result_frequency_table]
     
<<<<<<< HEAD
     return render_template('index1.html', data = jsonify(table_list))

@app.route("/about")
def readme():
    print ('this is a very impressive project')

if __name__ == '__main__':
    app.run(debug=True)

# data = {'result': [dict(row) for row in results1]}
# return render_template('index.html', test_two_data= data)

# ADDI's solution
# results = db.session.query(Pet.name, Pet.lat, Pet.lon).all()

#     hover_text = [result[0] for result in results]
#     lat = [result[1] for result in results]
#     lon = [result[2] for result in results]'

# return jsonify(pet_data)
=======
     return render_template('index1.html', data = table_list1)
>>>>>>> jack


@app.route("/about")
def about():
    return render_template('index2.html')


<<<<<<< HEAD



# @app.route("/flight_summary")
# def flight_summary_data():
#     session = Session(engine)

#     # Query all passengers
#     results2 = session.query(flight_summary.flight_id, flight_summary.callsign, flight_summary.number, flight_summary.icao24,flight_summary.registration, flight_summary.typecode, flight_summary.origin, flight_summary.landing, flight_summary.destination, flight_summary.diverted,flight_summary.tweet_problem, flight_summary.tweet_result, flight_summary.tweet_fueldump, flight_summary.avh_id, flight_summary.avh_problem, flight_summary.avh_result, flight_summary.avh_fueldump).filter(flight_summary.flight_id == 'ARG1511_20180101')
  	
#     session.close()
#     flightid= [result[0] for result in results2]
#     callsign = [result[1] for result in results2]
#     number= [result[2] for result in results2]
#     icao24 = [result[3] for result in results2]
#     registration = [result[4] for result in results2]
#     typecode= [result[5] for result in results2]
#     origin = [result[6] for result in results2]
#     landing= [result[7] for result in results2]
#     destination = [result[8] for result in results2]
#     diverted= [result[9] for result in results2]
#     tweet_problem = [result[10] for result in results2]
#     tweet_result= [result[11] for result in results2]
#     tweet_fueldump = [result[12] for result in results2]
#     avh_id = [result[13] for result in results2]
#     avh_problem= [result[14] for result in results2]
#     avh_result = [result[15] for result in results2]
#     avh_fueldump = [result[16] for result in results2]
    
#     flight_summary_table = [{
        
#         "Flight ID": flightid,
#         "callsign": callsign,
#         "number": number,
#         "icao24": icao24,
#         "Registration":registration,
#         "typecode": typecode,
#         "origin": origin,
#         "landing": landing,
#         "destination": destination,
#         "diverted": diverted,
#         "tweet problem": tweet_problem,
#         "tweet result": tweet_result,
#         "tweet fueldump": tweet_fueldump,
#         "AVH ID": avh_id,
#         "AVH Problem": avh_problem,
#         "AVH Result": avh_result,
#         "AVH Fueldump": avh_fueldump
#     }] 
    
   
#     return render_template('index.html', flight_summary_data = jsonify(flight_summary_table))






# @app.route("/aircraft_info")
# def aircraft_info():
#     session = Session(engine)

#     # Query all passengers
#     results3 = session.query(aircraft_metadata.icao24, aircraft_metadata.registration, aircraft_metadata.manufacturericao, aircraft_metadata.manufacturername, aircraft_metadata.model, aircraft_metadata.typecode, aircraft_metadata.serialnumber, aircraft_metadata.linenumber, aircraft_metadata.icaoaircrafttype, aircraft_metadata.operator, aircraft_metadata.status, aircraft_metadata.built, aircraft_metadata.firstflightdate, aircraft_metadata.seatconfiguration, aircraft_metadata.engines, aircraft_metadata.modes, aircraft_metadata.adsb, aircraft_metadata.acars, aircraft_metadata.notes, aircraft_metadata.categorydescription).filter(aircraft_metadata.icao24 == 'aa3487')
  	

    
#     session.close()

#     icao24= [result[0] for result in results3]
#     registration = [result[1] for result in results3]
#     manufacturericao= [result[2] for result in results3]
#     manufacturername = [result[3] for result in results3]
#     model = [result[4] for result in results3]
#     typecode= [result[5] for result in results3]
#     serialnumber = [result[6] for result in results3]
#     linenumber= [result[7] for result in results3]
#     icaoaircrafttype = [result[8] for result in results3]
#     operator= [result[9] for result in results3]
#     status = [result[10] for result in results3]
#     built= [result[11] for result in results3]
#     firstflightdate = [result[12] for result in results3]
#     seatconfiguration = [result[13] for result in results3]
#     engines= [result[14] for result in results3]
#     modes = [result[15] for result in results3]
#     adsb = [result[16] for result in results3]
#     acars= [result[17] for result in results3]
#     notes = [result[18] for result in results3]
#     categorydescription = [result[19] for result in results3]

#     aircraft_info_table  = [{

#         "ICAO24": icao24,
#         "registration": registration,
#         "anufacturericao": manufacturericao,
#         "manufacturername": manufacturername,
#         "Model":model,
#         "typecode": typecode,
#         "serialnumber": serialnumber,
#         "line number": linenumber,
#         "icaoaircrafttype": icaoaircrafttype,
#         "operator": operator,
#         "status": status,
#         "built": built,
#         "firstflightdate": firstflightdate,
#         "seatconfiguration": seatconfiguration,
#         "engines": engines,
#         "modes": modes,
#         "adsb": adsb,
#         "acars": acars,
#         "notes": notes,
#         "categorydescription": categorydescription
#     }]

#     return render_template('index.html', aircraft_info= aircraft_info_table)


# # # @app.route("/api/v1.0/squawk7700")
# # # def squawk7700():
# # #     # Create our session (link) from Python to the DB
# # #     session = Session(engine)

# # #     # Query all passengers
# # #     results = engine.execute('select distinct substr(am.manufacturername,1,6), count(distinct fs.flight_id) from flight_summary fs, flight_trajectory ft, aircraft_metadata am where fs.flight_id = ft.flight_id and am.icao24 = ft.icao24 and ft.flight_id in (select distinct ft.flight_id from flight_trajectory ft where ft.squawk = 7700) group by substr(am.manufacturername,1,6) order by count(distinct fs.flight_id) DESC').fetchall()

# # #     session.close()
# # #     return render_template('index.html', squawk7700=results)


# # # @app.route("/api/v1.0/about")
# # # def about():
# # #     # Create our session (link) from Python to the DB
# # #     session = Session(engine)

# # #     # Query all passengers
# # #     results = session.query(Pharma_spending.country_code, Pharma_spending.percent_pharmaceutical_spending).all()

# # #     session.close()
# #     return render_template('index2.html', about=results)




# # # import necessary libraries
# # from models import create_classes
# # import os
# # from flask import (
# #     Flask,
# #     render_template,
# #     jsonify,
# #     request,
# #     redirect)

# # #################################################
# # # Flask Setup
# # #################################################
# # app = Flask(__name__)

# # #################################################
# # # Database Setup
# # #################################################

# # from flask_sqlalchemy import SQLAlchemy
# # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# # # Remove tracking modifications
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # db = SQLAlchemy(app)

# # Pet = create_classes(db)

# # # create route that renders index.html template
# # @app.route("/")
# # def home():
# #     return render_template("index.html")


# # # Query the database and send the jsonified results
# # @app.route("/send", methods=["GET", "POST"])
# # def send():
# #     if request.method == "POST":
# #         name = request.form["petName"]
# #         lat = request.form["petLat"]
# #         lon = request.form["petLon"]

# #         pet = Pet(name=name, lat=lat, lon=lon)
# #         db.session.add(pet)
# #         db.session.commit()
# #         return redirect("/", code=302)

# #     return render_template("form.html")


# # @app.route("/api/pals")
# # def pals():
# #     results = db.session.query(Pet.name, Pet.lat, Pet.lon).all()

# #     hover_text = [result[0] for result in results]
# #     lat = [result[1] for result in results]
# #     lon = [result[2] for result in results]

# #     pet_data = [{
# #         "type": "scattergeo",
# #         "locationmode": "USA-states",
# #         "lat": lat,
# #         "lon": lon,
# #         "text": hover_text,
# #         "hoverinfo": "text",
# #         "marker": {
# #             "size": 50,
# #             "line": {
# #                 "color": "rgb(8,8,8)",
# #                 "width": 1
# #             },
# #         }
# #     }]

# #     return jsonify(pet_data)


# # if __name__ == "__main__":
# #     app.run()
=======
if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> jack
