"""
    From the raw reviews form testing and training data
"""

from form_data.pandas_functions import read_pandas_raw_csv

import os, sys
import random
import numpy

from copy import deepcopy

def get_neg_pos_file_names(neg_pos_file_name, train_ratio, random_seed=49):
    neg_pos_filename_data_frame = read_pandas_raw_csv(neg_pos_file_name)
    train_size = len(neg_pos_filename_data_frame['neg']) + len(neg_pos_filename_data_frame['pos']) 
    train_size *= train_ratio
    
    neg_size = int(abs(train_size*0.5))
    pos_size = int(abs(train_size - neg_size))
    
    numpy.random.seed(random_seed)
    neg_files = numpy.random.choice(neg_pos_filename_data_frame['neg'], neg_size, replace=False)
    
    numpy.random.seed(random_seed)
    pos_files = numpy.random.choice(neg_pos_filename_data_frame['pos'], pos_size, replace=False)
    
    return list(neg_files) + list(pos_files)

def write_train_test_data(training_data, raw_review_file_name, train_file_name, test_file_name):
    """
        The raw data that we get, we put it in these files in different folders
        Later we use it for testing and training
        Train size is hard coded to 70%
    """
    data_frame = read_pandas_raw_csv(raw_review_file_name)

    test_data_frame = deepcopy(data_frame)
    train_data_frame = deepcopy(data_frame)
    indexes = data_frame.index

    for index in indexes:
        if index not in training_data:
            train_data_frame = train_data_frame.drop(index)

    for file_name in training_data:
        if file_name in test_data_frame.index:
            test_data_frame = test_data_frame.drop(file_name)

    #write test and train data frames
    train_data_frame.to_csv(train_file_name)
    test_data_frame.to_csv(test_file_name)

    return train_data_frame, test_data_frame

def main_test_train(neg_pos_file_name, random_seed, raw_review_file_name, train_file_name, test_file_name):
    train_ratio = 0.7
    training_data = get_neg_pos_file_names(neg_pos_file_name, train_ratio, random_seed)
    train_data_frame, test_data_frame = write_train_test_data(training_data, raw_review_file_name, train_file_name, test_file_name)

    return train_data_frame, test_data_frame

if __name__ == "__main__":
    try:
        raw_review = sys.argv[1]
        neg_pos_file = sys.argv[2]
        train_file = sys.argv[3]
        test_file = sys.argv[4]
        random_seed = int(sys.argv[5])
    except:
        print '[ERROR] in input'

    main_test_train(neg_pos_file, random_seed, raw_review, train_file, test_file)

