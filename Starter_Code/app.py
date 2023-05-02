# Import the dependencies.
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,func
from flask import Flask, Request, jsonify



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()


# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def main():
    return(
        f"Climate changes in Hawaii<br />"
        f"Available Routes<br />"
        f"Rainfall from last year: /api/v1.0/Precipitation<br />"
        f"/api/v1.0/stations<br />"
        f"/api/v1.0/tobs<br />"
        f"/api/v1.0/yyyy-mm-dd<br/>"
        f"/api/v1.0/yyyy-mm-dd/yyyy-mm-dd"
    )

@app.route("/api/v1.0/Precipitation")
def prcp():
          last_date = dt.date(2017, 8, 23) - dt.timedelta(days= 365)
          result= session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>= last_date).all()
          session.close()
          Precipitation= {date: prcp for date, prcp in result}
          return jsonify (Precipitation)

@app.route("/api/v1.0/stations")
def stations():
    outcome= session.query(Station.station).all()
    session.close()
    station_name= list(np.ravel(outcome))
    return jsonify (station_name)

@app.route("/api/v1.0/tobs")
def tobs():
    outcome1= session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281', Measurement.date >= '2016-08-23').all()
    session.close()
    tobs = list(np.ravel(outcome1))
    return jsonify (tobs)

@app.route("/api/v1.0/<start>")
def start(start):
    outcome2= session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start).all()
    session.close()
    #Create an empty list to hold values
    temp_stats = []
    for min, avg, max in outcome2:
        tobs_dict = {}
        tobs_dict["Min"] = min
        tobs_dict["Max"] = max
        tobs_dict["Average"] = avg
        temp_stats.append(tobs_dict)
    return jsonify(temp_stats)

@app.route('/api/v1.0/<start>/<end>')
def start_end(start,end):
    outcome3= session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()
    #Create an empty list to hold values
    all_stats = []
    for min, avg, max in outcome3:
        tobs_dict1 = {}
        tobs_dict1["Min"] = min
        tobs_dict1["Max"] = max
        tobs_dict1["Average"] = avg
        all_stats.append(tobs_dict1)
    return jsonify(all_stats)


    
if __name__ == "__main__":
    app.run(debug=True)


