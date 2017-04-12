"""
    Implementation for navie bayes
"""

from form_data.pandas_functions         import read_pandas_raw_csv

from sklearn.naive_bayes                import MultinomialNB
from sklearn.feature_extraction.text    import CountVectorizer

import sys

def classify_NB(data_frame):
    count_vectorizer = CountVectorizer()
    counts = count_vectorizer.fit_transform(data_frame['processed_words'].values)
    
    classifier = MultinomialNB()
    targets = data_frame['sentiment'].values
    classifier.fit(counts, targets)

    return classifier

def check_all_from_same_data_frame(classifier, data_frame):
    count_vectorizer = CountVectorizer()
    example_counts = count_vectorizer.transform(data_frame['processed_words'].values)
    predictions = classifier.predict(example_counts)
    
    for i in range(len(predictions)):
        print 'Pridictions -> ', predictions[i], ' | Actual -> ', data_frame['sentiment'].values[i]


if __name__ == "__main__":
    try:
        data_file_name = sys.argv[1]
    except:
        print '[ERROR] in input'

    data_frame = read_pandas_raw_csv(data_file_name)
    c = classify_NB(data_frame)
    check_all_from_same_data_frame(c, data_frame)
