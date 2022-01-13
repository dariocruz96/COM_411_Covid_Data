"""
This module is responsible for visualising the data using Matplotlib.
"""

"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display the number of confirmed cases per country/region using a pie chart
- Display the top 5 countries for deaths using a bar chart
- Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
time. This could focus on a specific country or countries.

Each function should visualise the data using Matplotlib.
"""

# TODO: Your code here
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import process


def pie_chart(covid_records):
    summary = process.summary_of_records(covid_records)
    labels = []
    sizes = []

    for item in summary:
        labels.append(item[0])
        sizes.append(item[1]['Cases'])

    plt.pie(sizes, labels=labels)
    plt.show()


def bar_chart(covid_records):
    summary = process.summary_of_records(covid_records)
    summary.sort(key=lambda x: x[1]['Deaths'])
    x = []
    y = []
    for i in range(5):
        x.append(summary[i - 1][0])
        y.append(summary[i - 1][1]['Deaths'])

    plt.xlabel("Countries")
    plt.ylabel("Number of deaths by Covid-19 in January 2020")

    plt.bar(x, y)
    plt.show()