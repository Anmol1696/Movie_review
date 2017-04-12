"""
    Script for reading the movie reviews as well as code for forming pandas dataframes
"""
import sys
import os

import pandas

def get_reviews_and_form_data_frame(folder_name, data_frame_columns=['raw_string', 'sentiment']):
    """
        Given that the stucture of the data is of the form that the 'movie_data/' has 2 folders 'pos' and 'neg' with positive and negative reviews each
        We go to each folder and read all the files and store it in the pandas file
        In the folder $folder_name we will have 2 folders 'neg' and 'pos'. This functions goes in boht and gets the value
    """
    data_frame = pandas.DataFrame(columns=data_frame_columns)
    
    for sentiment in ['pos', 'neg']:
        file_names = os.listdir(folder_name + sentiment + '/')
        
        for file_name in file_names:
            with open(folder_name + sentiment + '/' + file_name) as input_file:
                # Single string as problem states single line is filled in dataframe
                file_data = ''.join(input_file.readlines())
            
            temp_data_frame = pandas.DataFrame([[file_data, sentiment]], index=[file_name], columns=data_frame_columns)
            data_frame = data_frame.append(temp_data_frame)

    return data_frame

def main_form_data_frame(folder_name, data_frame_folder):
    """
        This function forms the csv file for data frame
    """
    data_frame = get_reviews_and_form_data_frame(folder_name)
    data_frame.to_csv(data_frame_folder)

def free_ram():
    """
        Tries to free using a basic equation as the above functions might use alot of buffer
    """
    try:
        os.system('echo 1 > /proc/sys/vm/drop_caches')
    except:
        print '[WARRNING]: Not able to free ram'

if __name__ == "__main__":
    try:
        folder_name = sys.argv[1]
        data_frame_folder = sys.argv[2]
    except:
        print '[ERROR] Input folders name incorrect'

    print 'Forming data frame'
    main_form_data_frame(folder_name, data_frame_folder)
    print 'Done\nFreeing Memory'
    free_ram()
