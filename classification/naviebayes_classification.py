"""
    Implementation for navie bayes
"""

from form_data.pandas_functions         import read_pandas_raw_csv

from sklearn.naive_bayes                import MultinomialNB
from sklearn.feature_extraction.text    import CountVectorizer

import sys
import pandas

count_vectorizer = CountVectorizer()

def classify_NB(train_data_frame):
    counts = count_vectorizer.fit_transform(train_data_frame['processed_words'].values)    
    classifier = MultinomialNB()
    targets = train_data_frame['sentiment'].values
    classifier.fit(counts, targets)

    return classifier

def append_prediction_to_data_frame(classifier, test_data_frame):
    """
        Get predictions from MultinomialNB and append to the processed data frame
    """
    example_counts = count_vectorizer.transform(test_data_frame['processed_words'].values)
    predictions = classifier.predict(example_counts)
    test_data_frame['prediction'] = map(unicode, predictions)

    return test_data_frame

def main_classification(train_data_file_name, test_data_file_name, write_back_test_data):
    train_data_frame = read_pandas_raw_csv(train_data_file_name)
    test_data_frame = read_pandas_raw_csv(test_data_file_name)

    classifier = classify_NB(train_data_frame)

    test_data_frame = append_prediction_to_data_frame(classifier, test_data_frame)

    if write_back_test_data == "True":
        test_data_frame.to_csv(test_data_file_name)

    return test_data_frame

if __name__ == "__main__":
    try:
        train_data_file_name = sys.argv[1]
        test_data_file_name = sys.argv[2]
        write_back_test_data = sys.argv[3]
    except:
        print '[ERROR] in input'

    t = main_classification(train_data_file_name, test_data_file_name, write_back_test_data)
    print 'Test Data Frame ->\n', t
