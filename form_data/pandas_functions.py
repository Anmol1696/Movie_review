"""
    Consists of all the functions for pandas
"""

import pandas

def read_pandas_raw_csv(file_name):
    """
        Returns pandas dataframe for the csv
    """
    data_frame = pandas.read_csv(file_name, header=0, index_col=0)

    return data_frame

