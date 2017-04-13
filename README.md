# Movie_review
## Problem Statement
I have solved the Problem Statement B

## Installing Libraries
The following python were used. In order to install just type `sudo pip install <library>`
+ pandas
* matplotlib
* numpy
* sklearn
* nltk

Other inbuilt python libraries are also used such as `sys`, `copy`, `random` etc.

One can run the below command to install all the dependencies
```
    sudo pip install pandas matplotlib numpy sklearn nltk
```

## Raw Data
The raw data with is in `movie_data/` (basically unziped version of the given zipped movie review).<br>
In this folder there are 2 more folders `neg/` and `pos/`. Each contain 1000 `.txt` files with negative and positive reviews respectively.
This data is from taken from [here](http://www.cs.cornell.edu/people/pabo/movie-review-data/)<br>

## Pandas DataFrame
The module `form_data` contains all the codes that deal with the pandas library. Now I will explaining about each script in this module

### init_data.py
This file contains functions that are used for converting the raw data in `movie_data/` into pandas dataframe.<br>
The function `main_form_data_frame` reads through the `movie_data/` then goes to `neg/` and `pos/` folders and read all the text files. This data is then converted into pandas data frame of the following format
```
    index(file_name) | raw_string | sentiment 
```
Where file_name of the `.txt` file is used as the index. There are 2 columns, first being the string form of the value of in the txt file i.e. all lines of the file concatinated into a single string. <br>
The `sentiment` column consists of the sentiment of the review i.e. basically which folder the txt file comes from `neg` for negative `pos` for positive<br>

Example of the raw data frame:
```
                                                                raw_string sentiment
    cv394_5137.txt   defending your life is an imaginative vision o...     pos
    cv460_10842.txt  deep rising is one of " those " movies . \nthe...     pos
    cv316_6370.txt   if he doesn=92t watch out , mel gibson is in d...     pos
    ....
```

When we run this module inorder to initialy form the `raw_data_frame` we run the following command
```
    python -m form_data.init_data <folder_name> <name_of_csv_file_for_storing_dataframe>
```
where `<folder_name>` is the location where the unziped data is kept. For our case it is `movie_data/`<br>
The second parameter `<name_of_csv_file_for_storing_dataframe>` is the location where one wants to store the data frame in csv format. We store all the `csv` file in folder `form_data/dataframe/`. This is file that will be formed<br>

For obtaining `raw_review.csv` we run the following command
```
    python -m form_data.init_data movie_data/ form_data/dataframe/raw_review.csv
    
    #NOTE
    Time taken ~ 8 secs for the complete data set
```

### pandas_functions.py
This file contains functions that are used to form a `sentiment_data_frame` data frame. This data set contains 2 columns. The value in the columns are the file names for either `neg` or `pos` column.<br>
The dataframe is something like
```
                     neg              pos
    0    cv077_23172.txt   cv394_5137.txt
    1    cv981_16679.txt  cv460_10842.txt
    2    cv619_13677.txt   cv316_6370.txt
    ....

    #Note there is no index for this data frame
```
The use of the dataframe is so that we can get all the filenames correspoding to a sentiment. This is used furted down the line inorder to extract some more information<br>
This module also has a function `read_pandas_raw_csv` which is used extensively through out the code. This basically converts csv file to pandas dataframe with appopriate headers and labels<br>

The command that is run is
```
    python -m form_data.pandas_functions form_data/dataframe/raw_review.csv form_data/dataframe/sentiment_filenames.csv
```

Another funtion in this module is `form_processed_word_frequency_data_frame`. This function is used to form a dataframe from a given dict of the form
```
    {'neg' : {word : frequency,..}, 'pos' : {word:frequency,..}}
```
<br>
Both the above stated functions `read_pandas_raw_csv` and `form_processed_word_frequency_data_frame` are not used in this particular file but these are imported by other modules<br>

### form_train_test.py
This is the code that is run inorder to form the training and the testing set from the `raw_reviews.csv` file or data frame<br>
Let us say we want a training 70% testing 30% of the data.(code is hard coded for this %). Let the total size be N.<br> 
First the `sentiment_filnames.csv` is read and converted to a dataframe. From here we choose randomly with seed.

