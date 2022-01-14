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

summary_list = []


def summary_of_records(covid_records):
    summary = {}
    global summary_list
    for record in covid_records:
        country_region = covid_records[0][3]
        date = record[1]
        cases = record[-3]
        deaths = record[-2]
        recoveries = record[-1]
        if country_region == covid_records[0][3] and date in summary:
            summary[date]['Cases'] += int(cases)
            summary[date]['Deaths'] += int(deaths)
            summary[date]['Recoveries'] += int(recoveries)
        elif country_region == covid_records[0][3]:
            summary[date] = {'Cases': 0, 'Deaths': 0, 'Recoveries': 0}
            summary[date]['Cases'] += int(cases)
            summary[date]['Deaths'] += int(deaths)
            summary[date]['Recoveries'] += int(recoveries)

    for key, value in summary.items():
        summary_list.append((key, value))
    return summary_list


fig, (ax1, ax2, ax3) = plt.subplots(3, 1)


def animate(frame):
    global ax1, ax2, ax3, summary_list
    plt.suptitle('Mainland China ( January 2020)')
    ax1.set_xlabel('Days')
    ax1.set_ylabel('Confirmed Cases')
    ax2.set_xlabel('Days')
    ax2.set_ylabel('Deaths')
    ax3.set_xlabel('Days')
    ax3.set_ylabel('Recoveries')
    day = []
    x = []
    y = []
    y2 = []
    y3 = []
    for index in range(frame):
        day.append(summary_list[index][0].split("/"))
        x.append(day[index][1])
        y.append(summary_list[index][1]['Cases'])
        y2.append(summary_list[index][1]['Deaths'])
        y3.append(summary_list[index][1]['Recoveries'])
    ax1.plot(x, y)
    ax2.plot(x, y2)
    ax3.plot(x, y3)


def run():
    line_animation = animation.FuncAnimation(fig,
                                             animate,
                                             frames=11,
                                             interval=1000)

    plt.show()