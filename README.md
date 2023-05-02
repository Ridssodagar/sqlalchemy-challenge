# sqlalchemy-challenge

Instructions
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

Part 1: Analyze and Explore the Climate Data

In this section, I have use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, I have  use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:

using the provided files under Resources (climate_starter.ipynb and hawaii.sqlite) to complete climate analysis and data exploration.

I have use the SQLAlchemy create_engine() function to connect to SQLite database.

Use the SQLAlchemy automap_base() function to reflect tables into classes, and then save references to the classes named station and measurement.

Linked Python to the database by creating a SQLAlchemy session.

Precipitation Analysis
Find the most recent date in the dataset.

Using that date, got the previous 12 months of precipitation data by querying the previous 12 months of data.
Select only the "date" and "prcp" values.

Load the query results into a Pandas DataFrame. Explicitly set the column names.

Sort the DataFrame values by "date".

Plot the results by using the DataFrame plot method, as the following image shows:

image.png

Use Pandas to print the summary statistics for the precipitation data.

Station Analysis

I have use the hawaii_stations.csv to analyse the data.

Design a query to calculate the total number of stations in the dataset.

Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:

List the stations and observation counts in descending order.

Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.

Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:

Filter by the station that has the greatest number of observations.

Query the previous 12 months of TOBS data for that station.

Plot the results as a histogram with bins=12, as the following image shows:

Close the session.

Part 2: Design Your Climate App
After completing my initial analysis, I have design a Flask API based on the queries that just developed. To do so, use Flask to created routes as follows:
Start at the homepage.
Listed all the available routes.
Converted the query results from precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
Return the JSON representation of dictionary.
Return a JSON list of stations from the dataset.
Query the dates and temperature observations of the most-active station for the previous year of data.
Return a JSON list of temperature observations for the previous year.
Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

All the images of the graph is attached under graphs folder.
I have utilized ASK BCS for somehelp with Route 
Also I had hurdle with my classmates to complete the assignment.


