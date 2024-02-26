# San Diego Weather Data Analysis
### ADS 507 Spring 2024 Team 4 Final Project

## Overview
This project aims to report out data regarding daily weather information. We use insights into daily weather conditions in San Diego, including historical comparisons and daily alerts to achieve thtis. The analysis involves integrating data from multiple sources, including the National Weather Service (NWS) API, OpenWeather API, and a historical weather dataset containing San Diego Weather Averages from 1939-2019. The data we output will also be compared to historical data to observe any trends or similarities. By integrating these datasets, we aim to offer a holistic view of daily weather trends with alerts in San Diego, enabling us to compare current weather patterns with historical averages.

## Team Members
- Shailja Somani
- John Vincent Deniega
- Tara Dehdari

## Dependencies
- Python 3.9 or higher
- MySQL
- Ability to run cron jobs: Access to Mac Terminal or Windows PowerShell
- Required Python libraries:
  - pandas
  - numpy
  - matplotlib
  - requests
  - nwsapy
  - pymysql

## User Guide
1. Install all required Python libraries using pip.
2. Clone this repository to your local machine.
3. Run the notebook titled: Team4_ADS507_FinalProject.ipynb
* This notebook contains the initial setup of the SQL database, which is called WeatherDatabase.
* It will create 3 tables: DailyWeatherAlerts, DailyWeatherConditions, & HistoricalWeatherData within the WeatherDatabase. It will also create a view called DailyWeatherView summarizing daily weather data with comparisions to data 5 years and 10 year ago.
* Make sure to replace sensitive information such as MySQL database credentials and API keys with your own credentials.
* The notebook will insert all historical weather data into the HistoricalWeatherData table, assuming you have data.csv from this repo in the same folder where you're running the notebook.
* The notebook will also insert today's data from both APIs into their respective tables.
4. In order to automate daily calls to both APIs and insert that data into WeatherDatabase, create a cron job using Terminal if you're on a Mac or PowerShell if you're on a PC. Have the cron job run the py file in this repo (Team4_ADS507_FinalProj_DailyUpdate.py) daily. 
* Guides for both are as follows: [Mac Cron Jobs](https://phoenixnap.com/kb/cron-job-mac); [PC Cron Jobs](https://phoenixnap.com/kb/cron-job-windows#)
* Example syntax is as follows: 0 10 * * * /Users/shailjasomani/opt/anaconda3/bin/python3 /Users/shailjasomani/Documents/USD_MS_ADS/ADS_507/Final_Project/Team4_ADS507_FinalProj_DailyUpdate.py
* This syntax assumes you want to run the job at 10am daily. Replace the first path with where Python 3 is stored on your computer and the second with where you have stored this file from this repo: Team4_ADS507_FinalProj_DailyUpdate.py
5. If you wish to connect your MySQL server to Tableau, do the following:
* Download and install an [ODBC driver from here.](https://www.iodbc.org/dataspace/doc/iodbc/wiki/iodbcWiki/Downloads#Mac%20OS%20X)
* Download and install the [MySQL ODBC Connector from here.](https://dev.mysql.com/downloads/connector/odbc/)
* Restart Tableau and follow the instructions here to connect to a [MySQL server.](https://help.tableau.com/current/pro/desktop/en-us/examples_mysql.htm?_gl=1*16tubdr*_ga*NTE0MzEyNTMyLjE3MDgzOTEyOTc.*_ga_8YLN0SNXVS*MTcwODM5MTI5Ni4xLjEuMTcwODM5MTMzOS4wLjAuMA) You will be prompted to enter information regarding your local MySQL server and user credentials (the same as you inserted in Team4_ADS507_FinalProject.ipynb for the initial database creation).  

## Notes
- Ensure proper internet connectivity to fetch data from external APIs.
- If you are running this all locally, make sure your laptop is turned on/awake at the time the cron job is being triggered.
- Ensure data.csv is in the same folder as Team4_ADS507_FinalProject.ipynb when you run it. 
- Handle exceptions gracefully, especially when dealing with API responses and database operations.
- The analysis can be further extended by incorporating additional weather parameters and conducting deeper statistical analysis.
- Future state will involve connecting to a cloud SQL server which multiple users can access simultaneously.

## Initial Configuration Notebook Contents
The initial configuration of the SQL database is done via the following notebook: Team4_ADS507_FinalProject.ipynb. Here's a breakdown of the notebook contents:

1. **Notebook Setup**: Importing necessary libraries and setting up connections to MySQL server.
2. **Connect into MySQL & Define Database**: Build out WeatherDatabase with 3 tables and 1 view.
3. **San Diego Weather Historical Daily Averages Dataset Analysis**:
- Exploratory Data Analysis (EDA) and preprocessing of historical weather data.
- Visualization of data distributions and removal of outliers.
- Insertion of cleaned historical weather data into the MySQL database.
3. **OpenWeather API: Daily Weather Data**:
- Making API calls to OpenWeather to retrieve daily temperature data for San Diego.
- Parsing API response and inserting today's weather metrics data into the MySQL database.
4. **National Weather Service API - Daily Alerts**:
- Connecting to the NWS API to retrieve daily weather alerts for San Diego.
- Parsing API response and inserting today's alert data into the MySQL database.

## Contributors
Contributions to this project are welcome. Feel free to fork the repository and submit pull requests for improvements or bug fixes.
