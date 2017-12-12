"""Central of Northeastern Region Graph"""

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
        title='Northeastern Region Average Expenditure(Baht/Year)',
        x_title='Year',
        y_title='Baht')
    line_chart.x_labels = map(str, range(2549, 2559))
    line_chart.y_labels = [i*1000 for i in range(6, 19)]

    #adding data
    country_group = {
        'Northern': [56, 57, 59, 60, 61, 65, 66],
        'Central': [53, 54, 58, 62, 63, 64, 67],
        'Southern': [48, 49, 50, 51, 52, 55]
    }
    for i in country_group['Central']:
        line_chart.add(data[i][0], [int(j) for j in data[i][1:]])
    line_chart.render_to_file('AvgNortheastC.svg')


read()
