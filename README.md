# i210_Mastery_Project2
In this project, we will use real Spotify data collected with the Spotify API. The dataset you will be using contains a report of nearly 1000 tracks released in 2022, including track details, artist info, and audio data for each track.

# 1. Load Data: Create a function load_data to read data from spotify_data_2022.csv and clean it up

A) In my_mod.py, write a function load_data() that takes the name of a csv file as
input, reads the contents of that csv file with a DictReader (use exception
handling), uses a list comprehension to filter out any rows with incomplete data,
and then removes any duplicate tracks (use the first one with a given
track_name) before returning the cleaned-up data. We’ll use this data in Parts 2 - 4.
(hint: see lesson 19 – yours will be very similar)

In my_mod.py, run the test code at the bottom and make sure you get the correct
number of rows. If you get more rows, you may not have removed the duplicate
tracks!

# 2. Top Track Analysis: Create functions to analyze, sort, and display top tracks by an audio feature

Write 3 functions to analyze, sort, and display track data by an audio feature, using the
cleaned data from Part 1.

A) In my_mod.py, write a function (selection_sort() or insertion_sort() ) that takes
as input a nested list and an index position, and uses either selection sort or
insertion sort to sort the nested list by the value at the given index position in
ascending order (small to large). This function will be called in track_analysis()
to sort tracks by feature.

(hint: see lesson 16 – your version needs to the given index position)
In my_mod.py, run the test code at the bottom and make sure you get the correct
sorting order for the instruments (least (12) to most (40) in the last column)!

B) In my_mod.py, write a function table_print() that takes a list of column headers,
a nested list of data (where each element of the list is a tuple with three elements
– one for the track name column, one for the artist name column, and one for the
column of the feature being analyzed), and an optional column width (choose a
reasonable default) as input, and prints out the data in a tabular format. It
won’t return anything, since its only job is to print out formatted data.
(hint: see lesson 18 – your version just needs to handle 1 more column!)
In my_mod.py, run the test code and make sure you get the correct output.

C) In my_mod.py, write a function track_analysis(), that takes in the cleaned data, a
track feature to sort by (e.g., track_danceability, track_loudness, etc.), and a
number of tracks as input, and displays a table of the top tracks with the highest
values for the given feature in descending order, showing the track names, their
artist names, and their values for the feature. If the feature doesn’t exist, print an
error message. Otherwise, the number of tracks requested should be displayed.
This function won’t return anything but should call the other 2 functions you
wrote in Part 2.

In my_mod.py, run the test code at the bottom and make sure you get the correct
output for track_analysis(spotify_data_test, "track_popularity", 10)

# 3. Write a Main section that runs our ‘Menu’ for the user
Our main section will allow the user to perform a top track analysis using our function
from Part 2. Don’t forget to import your my_mod.py file into your MP2_solution.py file.
A) In MP2_solution.py, allow the user to decide to perform a top track analysis. Ask the
user to enter a track feature to sort by and how many tracks to display, then call
the track_analysis() function. Remember, they should only be able to choose track
features (see last page of instructions for descriptions of columns). Here’s an
example:

B) In MP2_solution.py, allow our program to run as long as the user wants to keep
exploring the data. When we’ve printed out the information the user asks for, we’ll
present the menu options again. Allow the user to quit the program with a
specific input (accept any version without regard to upper or lower case).

C) In MP2_solution.py, make sure to use error handling if the user enters an invalid
menu option, and allow them to choose again.


