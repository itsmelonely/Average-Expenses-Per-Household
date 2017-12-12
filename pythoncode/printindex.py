"""print index"""

import pandas as pd
import numpy

def test():
    """read csv and print index and data list"""
    data_frame = pd.read_csv('expenditure.csv')
    data = (numpy.array(data_frame)).tolist()

    #take the ","s out
    data_ready = [[i.replace(',', '') if i.count(',') >= 1 else i for i in lst] for lst in data]

    for i in range(len(data_ready)):
        print(i, data[i][0])

test()
