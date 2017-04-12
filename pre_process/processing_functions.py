"""
    Functions that will pre process the txt
"""

from form_data.pandas_functions import read_pandas_raw_csv, form_processed_word_frequency_data_frame

import sys
import pandas

from nltk.stem.snowball import EnglishStemmer

stem = EnglishStemmer().stem

def get_stop_words(stop_word_file_name='pre_process/list_of_stop_words.txt'):
    """
        Return a list of stop words from the file name
        We also stem the stop words so that we can compare directily with the stemmed words
    """
    with open(stop_word_file_name) as stop_file:
        stop_words = stop_file.readline()

    stop_words = map(stem, stop_words[:-1].split(','))

    return stop_words

def get_stemmed_tokenized_lower(raw_string, stop_words=[]):
    """
        By default we do not have stop words. We can have them or remove them and see the performance
    """
    stemmed_words = []

    cleaner_string = raw_string.lower()
    cleaner_string = ''.join([i for i in raw_string if i.isalpha() or i==u' ' or i==u'\n'])
    
    for line in cleaner_string.split(u'\n'):
        for word in line.split(u' '):
            stemmed_word = stem(word)
            
            if stemmed_word != u'' and stemmed_word not in stop_words and len(stemmed_word) > 1:
                stemmed_words.append(stemmed_word)

    return stemmed_words

def add_processed_words_to_raw_data_frame(data_frame):
    """
        Goes to each file_name and pre process the raw string and addes a column to it
        Return the modified data frame with processed_words columns as well as processed_words vs frequency data frame
    """
    processed_words_frequency_dict = {'neg':{}, 'pos':{}}

    stop_words = get_stop_words()

    data_frame['processed_words'] = pandas.DataFrame(columns=['processed_words'], dtype=list)

    for file_name in data_frame.index:
        print 'file_name ->', file_name 
        temp_process_words = data_frame.get_value(index=file_name, col='raw_string')
        sentiment = data_frame.get_value(index=file_name, col='sentiment')
        temp_process_words = get_stemmed_tokenized_lower(temp_process_words, stop_words)
        
        for word in temp_process_words:
            if word not in processed_words_frequency_dict[sentiment].keys():
                processed_words_frequency_dict[sentiment][word] = 1
            else:
                processed_words_frequency_dict[sentiment][word] += 1

        data_frame.set_value(value=temp_process_words, index=file_name, col='processed_words')

    frequency_data_frame = form_processed_word_frequency_data_frame(processed_words_frequency_dict)

    return data_frame, frequency_data_frame

def main_add_processed_words(raw_file_name):
    data_frame = read_pandas_raw_csv(raw_file_name)
    data_frame, frequency_data_frame = add_processed_words_to_raw_data_frame(data_frame)

    return data_frame, frequency_data_frame

if __name__ == "__main__":
    """ Testing for stemming function.
    with open('pre_process/test_string.txt') as temp_file:
        test_string=temp_file.readline()
    stop_words = get_stop_words()
    stem_words = get_stemmed_tokenized_lower(test_string, stop_words)
    """
    try:
        raw_file_name = sys.argv[1]
    except:
        print '[ERROR] in input'
    d,f = main_add_processed_words(raw_file_name)
    print 'Data frame ->', d
    print 'Frequency -> ', f
