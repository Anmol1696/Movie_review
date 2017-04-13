"""
    Implementation for navie bayes
"""

from form_data.pandas_functions         import read_pandas_raw_csv

from sklearn.naive_bayes                import MultinomialNB
from sklearn.feature_extraction.text    import CountVectorizer
from sklearn.metrics                    import confusion_matrix, roc_curve, auc

import matplotlib.pyplot as plt
import sys
import pandas
import numpy

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
    test_data_frame['prediction_nb'] = map(unicode, predictions)

    prediction_proba = classifier.predict_proba(example_counts)[:,1]

    return test_data_frame, prediction_proba

def main_classification(train_data_file_name, test_data_file_name, write_back_test_data):
    train_data_frame = read_pandas_raw_csv(train_data_file_name)
    test_data_frame = read_pandas_raw_csv(test_data_file_name)

    classifier = classify_NB(train_data_frame)

    test_data_frame, prediction_proba = append_prediction_to_data_frame(classifier, test_data_frame)

    if write_back_test_data == "True":
        test_data_frame.to_csv(test_data_file_name)

    confusion = get_confusion_matrix(test_data_frame)
    print 'Confusion Matrix ->\n', confusion
    get_roc_curve(test_data_frame, prediction_proba)

    return test_data_frame

def get_confusion_matrix(test_data_frame):
    """
        Once the test_data_frame is updated with the predicted results, we use this to form confusion matrix
    """
    confusion = confusion_matrix(test_data_frame['sentiment'], test_data_frame['prediction_nb'], labels=['pos', 'neg'])

    return confusion

def get_roc_curve(test_data_frame, prediction_proba):
    """
        Return the ROC curve
    """
    sentiment_list = test_data_frame['sentiment']
    fpr, tpr, thresholds = roc_curve(sentiment_list, prediction_proba, pos_label='pos')

    roc_auc = auc(fpr, tpr)
   
    plot_roc_curve(fpr, tpr, roc_auc)

    return fpr, tpr, thresholds, roc_auc

def plot_roc_curve(false_positive_rate, true_positive_rate, roc_auc):
    plt.title('Receiver Operating Characteristic')
    plt.plot(false_positive_rate, true_positive_rate, 'b',
            label='AUC = %0.2f'% roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0,1],[0,1],'r--')
    plt.xlim([-0.1,1.2])
    plt.ylim([-0.1,1.2])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()

if __name__ == "__main__":
    try:
        train_data_file_name = sys.argv[1]
        test_data_file_name = sys.argv[2]
        write_back_test_data = sys.argv[3]
    except:
        print '[ERROR] in input'

    t = main_classification(train_data_file_name, test_data_file_name, write_back_test_data)
    print 'Test Data Frame ->\n', t
