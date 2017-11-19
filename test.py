"""test module"""

import pandas as pd

def read():
    """read csv"""
    data_frame = pd.read_csv('expenditure.csv')
    print(data_frame)

read()
