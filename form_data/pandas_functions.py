"""
    Consists of all the functions for pandas
"""

import sys
import pandas

def read_pandas_raw_csv(file_name):
    """
        Returns pandas dataframe for the csv
    """
    data_frame = pandas.read_csv(file_name, header=0, index_col=0)

    return data_frame

def form_sentiment_vs_file_name_data_frame(data_frame, write_to_file):
    """
        Given the raw data frame as the input form another data frame with index as the sentiment and column as the file_name
        For getting all files with pos sentiment use `sentiment_data_frame.pos`
    """
    temp_dict = {'neg' : [], 'pos' : []}

    for file_name in data_frame.index:
        sentiment = data_frame.get_value(index=file_name, col='sentiment')
        temp_dict[str(sentiment)].append(file_name)

    sentiment_data_frame = pandas.DataFrame(temp_dict)

    if write_to_file:
        sentiment_data_frame.to_csv(write_to_file)

if __name__ == "__main__":
    try:
        raw_file_name = sys.argv[1]
        sentiment_file_name = sys.argv[2]
    except:
        print '[ERROR] in input file'

    data_frame = read_pandas_raw_csv(raw_file_name)
    form_sentiment_vs_file_name_data_frame(data_frame, sentiment_file_name)
