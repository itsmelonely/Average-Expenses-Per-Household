"""Western of Central Region Graph"""

import pandas as pd
import numpy
import pygal


def read():
    """read csv"""
    data_frame = pd.read_csv('expenditure.csv')
    data = (numpy.array(data_frame)).tolist()

    #take the ","s out
    data_ready = [[i.replace(',', '') if i.count(
        ',') >= 1 else i for i in lst] for lst in data]

    chart(data_ready)


def chart(data):
    """render chart"""
    line_chart = pygal.Line(
        title='Central Region Average Expenditure per Household (Baht/Year)',
        x_title='Year',
        y_title='Baht')
    line_chart.x_labels = map(str, range(2549, 2559))

#adding data
    country_group = {
        'Western':[22, 27, 28, 21, 25, 26, 24],
        'Northern':[23, 7, 8, 9, 10, 11, 19],
        'Eastern':[12, 13, 14, 15, 16, 17, 18, 20]
    }
    for i in country_group['Western']:
        line_chart.add(data[i][0], [int(j) for j in data[i][1:]])
    line_chart.render_to_file('AvgCentralW.svg')

read()
