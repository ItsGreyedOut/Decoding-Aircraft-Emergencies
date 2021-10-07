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
jack_connection_string = "postgres:postgres@localhost:5432/aircraft_project"
#matt_connection_string = "postgresql://postgres:Thatstraightline84!@localhost:5432/aircraft_project"
engine = create_engine(f'postgresql://{jack_connection_string}')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
aircraft_metadata= Base.classes.aircraft_metadata
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
def dashboard():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    """List all available api routes."""
    #return render_template('index.html', dashboard=results)
    combined_query=text("select * "
                        "from flight_summary fs, flight_trajectory ft, aircraft_metadata am "
                        "where fs.flight_id = ft.flight_id "
                        "and am.icao24 = ft.icao24 "
                        "and ft.flight_id in "
                        "(select distinct ft.flight_id from flight_trajectory ft where ft.flight_id = :x)")
    combined_flight_data = engine.execute(combined_query, {"x":"ARG1511_20180101"}).fetchall()
    combined_df = pd.DataFrame(combined_flight_data)
    return render_template('index.html', dashboard=combined_df.to_json())

#TRAJECTORY DEFAULT
@app.route("/trajectory_default")
def trajectory_initial():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    """List all available api routes."""
    #return render_template('index.html', dashboard=results)
    default_trajectory_query = text("select * "
                        "from flight_trajectory ft "
                        "where ft.flight_id in "
                        "(select distinct ft.flight_id from flight_trajectory ft where ft.flight_id = :x)") 
    initial_aircraft_trajectory = engine.execute(default_trajectory_query, { "x":"ARG1511_20180101"}).fetchall()
    trajectory_df = pd.DataFrame(initial_aircraft_trajectory)
    return render_template('index.html', first_view_trajectory=trajectory_df.to_json())

#TRAJECTORY FILTERED
@app.route("/trajectory_filtered")
def trajectory_dynamic():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    """List all available api routes."""
    #return render_template('index.html', dashboard=results)
    user_selected_aircraft_trajectory = text("select * "
                        "from flight_trajectory ft "
                        "where ft.flight_id in "
                        "(select distinct ft.flight_id from flight_trajectory ft where ft.flight_id = :x)") 
    filtered_aircraft_trajectory = engine.execute(user_selected_aircraft_trajectory, {"x":"ARG1511_20180101"}).fetchall()
    filtered_trajectory_df = pd.DataFrame(filtered_aircraft_trajectory)
    return render_template('index.html', filtered_view_trajectory=filtered_trajectory_df.to_json())


@app.route("/test")
def test():
    session = Session(engine)

    # Query all passengers
    results = engine.execute('select distinct substr(am.manufacturername,1,6), count(distinct fs.flight_id) from flight_summary fs, flight_trajectory ft, aircraft_metadata am where fs.flight_id = ft.flight_id and am.icao24 = ft.icao24 and ft.flight_id in (select distinct ft.flight_id from flight_trajectory ft where ft.squawk = 7700) group by substr(am.manufacturername,1,6) order by count(distinct fs.flight_id) DESC').fetchall()

    session.close()
    #return render_template('index.html', squawk7700=results)
    data = {'result': [dict(row) for row in results]}
    return render_template('index.html', dataFromFlask=data)



@app.route("/api/v1.0/squawk7700")
def squawk7700():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all passengers
    results = engine.execute('select distinct substr(am.manufacturername,1,6), count(distinct fs.flight_id) from flight_summary fs, flight_trajectory ft, aircraft_metadata am where fs.flight_id = ft.flight_id and am.icao24 = ft.icao24 and ft.flight_id in (select distinct ft.flight_id from flight_trajectory ft where ft.squawk = 7700) group by substr(am.manufacturername,1,6) order by count(distinct fs.flight_id) DESC').fetchall()

    session.close()
    return render_template('index.html', squawk7700=results)


@app.route("/api/v1.0/about")
def about():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all passengers
    results = session.query(Pharma_spending.country_code, Pharma_spending.percent_pharmaceutical_spending).all()

    session.close()
    return render_template('index2.html', about=results)

if __name__ == '__main__':
    app.run(debug=True)



# # import necessary libraries
# from models import create_classes
# import os
# from flask import (
#     Flask,
#     render_template,
#     jsonify,
#     request,
#     redirect)

# #################################################
# # Flask Setup
# #################################################
# app = Flask(__name__)

# #################################################
# # Database Setup
# #################################################

# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# Pet = create_classes(db)

# # create route that renders index.html template
# @app.route("/")
# def home():
#     return render_template("index.html")


# # Query the database and send the jsonified results
# @app.route("/send", methods=["GET", "POST"])
# def send():
#     if request.method == "POST":
#         name = request.form["petName"]
#         lat = request.form["petLat"]
#         lon = request.form["petLon"]

#         pet = Pet(name=name, lat=lat, lon=lon)
#         db.session.add(pet)
#         db.session.commit()
#         return redirect("/", code=302)

#     return render_template("form.html")


# @app.route("/api/pals")
# def pals():
#     results = db.session.query(Pet.name, Pet.lat, Pet.lon).all()

#     hover_text = [result[0] for result in results]
#     lat = [result[1] for result in results]
#     lon = [result[2] for result in results]

#     pet_data = [{
#         "type": "scattergeo",
#         "locationmode": "USA-states",
#         "lat": lat,
#         "lon": lon,
#         "text": hover_text,
#         "hoverinfo": "text",
#         "marker": {
#             "size": 50,
#             "line": {
#                 "color": "rgb(8,8,8)",
#                 "width": 1
#             },
#         }
#     }]

#     return jsonify(pet_data)


# if __name__ == "__main__":
#     app.run()
