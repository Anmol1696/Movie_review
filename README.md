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
###init_data.py
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
```
