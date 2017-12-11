"""this module will render whole kingdom graph"""

import pandas as pd
import numpy
import pygal

def read():
    """read csv"""
    data_frame = pd.read_csv('expenditure.csv')
    data = (numpy.array(data_frame)).tolist()

    #take the ","s out
    data_ready = [[i.replace(',', '') if i.count(',') >= 1 else i for i in lst] for lst in data]
    chart(data_ready)


def chart(data):
    """render svg chart"""
    line_chart = pygal.StackedLine(
        title='Whole Kingdom Average Expenditure(Baht/Year)',
        x_title='Year',
        y_title='Baht',
        fill=True)
    line_chart.x_labels = map(str, range(2549, 2559))
    line_chart.add(data[0][0], [int(i) for i in data[0][1:]])
    line_chart.render_to_file('AvgKingdom.svg')

read()
