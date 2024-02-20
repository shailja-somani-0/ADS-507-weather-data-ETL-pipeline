# San Diego Weather Data Analysis
### ADS 507 Spring 2024 Team 4 Final Project

## Overview
This project aims to report out data regarding daily weather information. We use insights into daily weather conditions in San Diego, including historical comparisons and daily alerts to achieve thtis. The analysis involves integrating data from multiple sources, including the National Weather Service (NWS) API, OpenWeather API, and a historical weather dataset containing San Diego Weather Averages from 1939-2019. The data we output will also be compared to historical data to observe any trends or similarities. 

## Team Members
- Shailja Somani
- John Vincent Deniega
- Tara Dehdari

## Dependencies
- Python 3.9 or higher
- Required Python libraries:
  - pandas
  - numpy
  - matplotlib
  - requests
  - nwsapy
  - pymysql

## Setup
1. Install the required Python libraries using pip:
   pip install nwsapy pandas numpy matplotlib requests pymysql
2. Clone this repository to your local machine.

## Notebook Contents
The analysis is conducted using a Jupyter Notebook. Here's a breakdown of the notebook contents:

1. **Notebook Setup**: Importing necessary libraries and setting up connections to MySQL database.
2. **San Diego Weather Historical Daily Averages Dataset Analysis**:
- Exploratory Data Analysis (EDA) and preprocessing of historical weather data.
- Visualization of data distributions and removal of outliers.
- Insertion of cleaned historical weather data into the MySQL database.
3. **OpenWeather API: Daily Temperature Data**:
- Making API calls to OpenWeather to retrieve daily temperature data for San Diego.
- Parsing API response and inserting data into the MySQL database.
4. **National Weather Service API - Daily Alerts**:
- Connecting to the NWS API to retrieve daily weather alerts for San Diego.
- Parsing API response and inserting alert data into the MySQL database.

## Usage
1. Run the notebook cell by cell to execute the analysis steps.
2. Make sure to replace sensitive information such as MySQL database credentials and API keys with your own.

## Notes
- Ensure proper internet connectivity to fetch data from external APIs.
- Handle exceptions gracefully, especially when dealing with API responses and database operations.
- The analysis can be further extended by incorporating additional weather parameters and conducting deeper statistical analysis.

## Contributors
Contributions to this project are welcome. Feel free to fork the repository and submit pull requests for improvements or bug fixes.