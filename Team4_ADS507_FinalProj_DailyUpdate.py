# -*- coding: utf-8 -*-
"""
Title of Project: Daily Weather and Alerts for San Diego, Along with Historical Comparisons
Team Number: 4
Group Members: Shailja Somani, John Vincent Deniega, & Tara Dehdari
Class & Semester: ADS 507, Spring 2024

The goal of this py file is to create a simple file that will feed into a daily cron job 
to make daily API calls to two data sources regarding San Diego weather data (basic 
weather conditions and weather alerts). The data retreived from those daily API calls will 
then be stored locally on a MySQL database.
"""

# PART 1: SET-UP
# Package imports
from datetime import datetime, timedelta
from nwsapy import api_connector # For NWS API
import requests # For OpenWeather API
import pymysql # To connect to MySQL 

# Hide warnings for cleanliness
import warnings
warnings.filterwarnings('ignore')

# Set up connection into SQL 
userName = 'root'  
userPass = 'invincible4tw' # INSERT your password here
conn = pymysql.connect(host='localhost', port=int(3306), user=userName, passwd=userPass)
cursor = conn.cursor()
conn.select_db('WeatherDatabase')

# Check that working correctly - commented out for cron job
#print(pd.read_sql_query("""SHOW TABLES""", conn))

# PART 2: OpenWeatherAPI: Daily Temperature Data
# Make API call to OpenWeather for San Diego lat & long
latitude_SD = 32.715736
longitude_SD = -117.161087

url = f'https://api.openweathermap.org/data/3.0/onecall?lat={latitude_SD}&lon={longitude_SD}&appid=1024bc200ad2448da47e940dcfe0a5d9'
response = requests.get(url)

if response.status_code == 200:
  data = response.json()
else:
  print('Error:', response.status_code)
  
# Get data points to put into SQL
data_to_append = {k: data.get('daily')[0][k] for k in ['dt', 'sunrise', 'sunset', 'humidity', 'uvi', 'wind_speed']}
data_to_append['temp'] = data.get('daily')[0].get('temp').get('day')
data_to_append

# Format for SQL
# Separate date field into day, month, & year so it can be viewed together or just by month & day
date = datetime.utcfromtimestamp(data_to_append['dt'])
year = date.year
month = date.month
day = date.day
# Convert temp from K to C
temp_C = round(data_to_append['temp'] - 273.15, 4)
temp_C
# Convert sunrise to formatted time in PST, not GMT
sunrise_gmt = datetime.utcfromtimestamp(data_to_append['sunrise'])
sunrise_pst = (sunrise_gmt - timedelta(hours=8)).strftime("%H:%M:%S")
sunrise_pst
# Convert sunset to formatted time in PST, not GMT
sunset_gmt = datetime.utcfromtimestamp(data_to_append['sunset'])
sunset_pst = (sunset_gmt - timedelta(hours=8)).strftime("%H:%M:%S")
sunset_pst

# Define the INSERT statement.
insert_stmt = """
    INSERT INTO DailyWeatherConditions (day, month, year, sunrise, sunset, humidity, uvi, wind_speed, temp)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

# Data to be inserted; for example, for March 14th, 2024
data_sql = (day, month, year, sunrise_pst, sunset_pst, data_to_append['humidity'], 
            data_to_append['uvi'], data_to_append['wind_speed'], temp_C)
# Check correct statement - again, commented out for cron job
#print(data_sql)
    
# Execute the SQL command
try: 
    cursor.execute(insert_stmt, data_sql)
    print("OpenWeather API weather conditions put into SQL database.")
except: 
    print("Could not put OpenWeather API weather conditions into SQL database.")

# PART 3: NWS API: Daily Weather Alerts
# Connect to NWS API
api_connector.set_user_agent("Application Name", "youremail@domain.com")
server_ping = api_connector.ping_server()

# Always a good idea to check to make sure an error didn't occur.
# There are times when a 400 or 500 error will occur.
if server_ping.has_any_request_errors:
    raise ConnectionError(server_ping['detail'])
else:
    print(server_ping.status)  # will print OK
api_connector.set_user_agent("NWSAPy", "ssomani@sandiego.edu")

# CAZ050 is San Diego's code, but sometimes there might not be an active alert
CA_Alert = api_connector.get_alert_by_zone('CAZ050') # NWS Zone Code for San Diego (CAZ050)

# Check if any alerts for today
if len(CA_Alert.to_dict()) == 0:
    # If no alerts, insert None for everything but headline. Insert "No Alert Today" for headline
    data_sql_2 = (datetime.now().day, datetime.now().month, datetime.now().year, 
                  None, None, None, None, None, "No Alert Today", None)
else:
    # If an alert exists, grab it & parse it
    df = CA_Alert.to_dict()[1]
    
    # Parse API pull into Python variables in accordance with SQL table schema in beginning of Notebook
    year_2 = df["sent"].year
    month_2 = df["sent"].month
    day_2 = df["sent"].day
    affected_zones = str(df["affected_zones"])
    areaDesc = str(df["areaDesc"])
    description = str(df["description"])
    effective_utc = (df["effective_utc"] - timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
    ends_utc = (df["ends_utc"] - timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
    headline = str(df["headline"])
    severity = str(df["severity"])

    # Data to be inserted
    data_sql_2 = (day_2, month_2, year_2, affected_zones, areaDesc, description, effective_utc, ends_utc, headline, severity)
    
# Check correct statement - again, commented out for cron job
#print(data_sql_2)
    
# Define the INSERT statement.
insert_stmt_2 = """
        INSERT INTO DailyWeatherAlerts (day, month, year, affected_zones, areaDesc, description, effective_utc, ends_utc, headline, severity)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

# Execute insert statement
try: 
    cursor.execute(insert_stmt_2, data_sql_2)
    print("NWS API weather alerts put into SQL database.")
except: 
    print("Could not put NWS API weather alerts into SQL database.")
    
conn.commit()


