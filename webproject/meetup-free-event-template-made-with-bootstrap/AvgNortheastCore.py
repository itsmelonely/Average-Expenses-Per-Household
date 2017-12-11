"""Northeastern Core Graph"""

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

    #adding data
    for i in range(48, 68):
        line_chart.add(data[i][0], [int(j) for j in data[i][1:]])
    line_chart.render_to_file('AvgNortheastCore.svg')

read()
