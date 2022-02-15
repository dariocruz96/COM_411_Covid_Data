# COM_411_Covid_Data

Introduction

The COVID-19 pandemic has wreaked havoc and led to the dramatic loss of life and livelihood. Its impact continues to affect the way in which we live and interact. In
this assessment, you will analyse data related to COVID-19 cases as recorded during January 2020 when COVID-19 was first reported. You will work with a sample data set that is provided to you in the form of a CSV file. The data file, covid_19_data.csv, contains the following data:

(Column Description Type)

Serial Number A unique serial number for the observation record. Integer
Observation Date
The date when the observation was made. String
Province/State The province or state in which the observation was made. String
Country/Region The country or region in which the observation was made. String
Last Updated The date and time the observation was last updated. String
Confirmed The number of confirmed cases that were observed. Integer
Deaths The number of deaths that were observed. Integer
Recovered The number of recoveries that were observed. Integer
Each row in the file represents a single observation record.
The file contains complete data for all columns except Province/State. This means that this column may have some missing values.
All the columns contain a single value. This means there is no columns with multiple (comma-separated) values.
It is recommended that you familiarise yourself with the content of the data file before attempting the remainder of this assessment.

Requirements

You have been tasked with creating a software application that can be used to
process and manage data related to the COVID-19 observations. The requirements
for the system are as follows:

a) The system will present the user with a text-based user interface through
which a user will select options to load the data, process the data, persist the
data and visualise the data.

b) The system will load the data from a CSV file into memory.

c) The system will allow the user to process the loaded data as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all the records grouped by the country/region.
- Retrieve a summary of all the records. This should include the following

information for each country/region:
 - the total number of confirmed cases
 - the total number of deaths
 - the total number of recoveries
 
d) The system will allow the user to visualise the data as follows:
- Display the number of confirmed cases per country/region using a pie chart
- Display the top 5 countries for deaths using a bar chart
- Display a suitable (animated) visualisation to show how the number of
confirmed cases, deaths, and recovery change over time. This could focus on
a specific country or countries.

e) The system will allow the user to export data in the form of JSON. The data may be
- All the data
- The data for a specific country/region

Environment

You are required to use the following tools:

- PyCharm as your integrated development environment
- Python 3.8+ (preferably 3.9) as the standard python library
- Additionally, the following libraries/modules may be imported and utilised:
    csv – to process csv files
    datetime – to format dates
    enum – to add enumerations
    json – to process JSON files
    matplotlib - to produce visualisations
    os – to retrieve or check file paths
    random – to generate random numbers
    typing – to add type hints
    math – for math functions
    unittest – to construct and run tests
    
- Git Tools and GitHub for version control
- No other python libraries or modules should be used
