import tui
import csv
import visual
import process

covid_records = []

def run():

    tui.welcome()

    tui.progress("Data loading", 0)
    while True:
        try:
            with open("data\covid_19_data.csv") as file:
                csv_reader = csv.reader(file)
                next(csv_reader)
                for values in csv_reader:
                    covid_records.append(values)
                break
        except FileNotFoundError:
            tui.error("The file cannot be found or loaded")
            break
    tui.total_records(len(covid_records))
    tui.progress(f'Data loading', 100)
    while True:
        try:
            variant = tui.menu()

            if variant == 1:
                tui.progress("Data processing", 0)
                tui.progress("Data processing", 100)
                variant = tui.menu(variant)
                if variant == 1:
                    tui.progress("Record retrieval", 0)
                    process.loaded_record(covid_records)
                    tui.progress("Record retrieval", 100)
                elif variant == 2:
                    tui.progress("Records retrieval", 0)
                    process.records_by_observation_date(covid_records)
                    tui.progress("Records retrieval", 100)
                elif variant == 3:
                    tui.progress("Grouping process", 0)
                    group_by_country_region = process.group_by_country_region(covid_records)
                    tui.display_records(group_by_country_region)
                    tui.progress("Grouping process", 100)
                elif variant == 4:
                    tui.progress("Summary process", 0)
                    summary = process.summary_of_records(covid_records)
                    tui.display_records(summary)
                    tui.progress("Summary process", 100)

            if variant == 2:
                tui.progress("Data visualisation operation", 0)
                variant = tui.menu(variant)
                if variant == 1:
                    visual.pie_chart(covid_records)

                elif variant == 2:
                    visual.bar_chart(covid_records)
                elif variant == 3:
                    visual.summary_of_records(covid_records)
                    visual.run()
        # Task 25: Check if the user selected the option for exporting data.  If so, then do the following:
        # - Use the appropriate function in the module 'tui' to retrieve the type of data to be exported.
        # - Check what option has been selected
        #
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has started.
        # - Export the data (see below)
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has completed.
        #
        # To export the data, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create suitable classes with appropriate methods.
        # You should use these to write the records (either all or only those for a specific country/region) to a JSON file.
        # TODO: Your code here

        # Task 26: Check if the user selected the option for exiting the program.
        # If so, then break out of the loop
        # TODO: Your code here

        # Task 27: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message
        # TODO: Your code here

        except ValueError:
            tui.error("--Invalid input--!\n")


if __name__ == "__main__":
    run()
