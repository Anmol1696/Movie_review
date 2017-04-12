"""
    Functions that will pre process the txt
"""

from stemming.porter2 import stem

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
            
            if stemmed_word != u'' and stemmed_word not in stop_words:
                stemmed_words.append(stemmed_word)

    return stemmed_words

if __name__ == "__main__":
    with open('pre_process/test_string.txt') as temp_file:
        test_string=temp_file.readline()
    stop_words = get_stop_words()
    stem_words = get_stemmed_tokenized_lower(test_string, stop_words)
    print stem_words
