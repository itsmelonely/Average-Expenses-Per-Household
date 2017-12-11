"""test module"""

import pandas as pd
import numpy
import pygal

def read():
    """read csv"""
    data_frame = pd.read_csv('expenditure.csv')
    data = (numpy.array(data_frame)).tolist()

    #take the ","s out
    data_ready = [[i.replace(',', '') if i.count(',') >= 1 else i for i in lst] for lst in data]


    #create charts
    line_chart = pygal.Line()
    line_chart.title = 'Bungkan'
    line_chart.x_title = 'Years'
    line_chart.y_title = 'Baht'
    line_chart.x_labels = map(str, range(2006, 2016))
    line_chart.add(data_ready[56][0], [int(i) for i in data_ready[56][1:]])
    line_chart.render_to_file('test.svg')


read()
