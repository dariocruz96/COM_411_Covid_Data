"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries

 
"""

# TODO: Your code here
import tui


def total_records(covid_records):
    total = tui.total_records(covid_records)
    return total


def loaded_record(covid_records):
    record = tui.display_record(covid_records[tui.serial_number() - 1])
    return record


def records_by_observation_date(covid_records):
    observation_dates = tui.observation_dates()
    for date in observation_dates:
        count = 0
        while True:
            if count >= len(covid_records):
                break
            elif date == covid_records[count][1]:
                print(covid_records[count])
                count += 1
            else:
                count += 1