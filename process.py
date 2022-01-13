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


def group_by_country_region(covid_records):
    group = covid_records
    group.sort(key=lambda x: x[3])
    return group


def summary_of_records(covid_records):
    summary = {}
    summary_list = []
    for record in covid_records:
        country_region = record[3]
        cases = record[-3]
        deaths = record[-2]
        recoveries = record[-1]
        if country_region in summary:
            summary[country_region]['Cases'] += int(cases)
            summary[country_region]['Deaths'] += int(deaths)
            summary[country_region]['Recoveries'] += int(recoveries)
        else:
            summary[country_region] = {'Cases': 0, 'Deaths': 0, 'Recoveries': 0}
            summary[country_region]['Cases'] += int(cases)
            summary[country_region]['Deaths'] += int(deaths)
            summary[country_region]['Recoveries'] += int(recoveries)

    for key, value in summary.items():
        summary_list.append((key, value))

    return summary_list
