import csv
import math

# PART 1: Read and clean data
# The code for reading the contents of the spotify file comes from the Bob Ross excercise we did in class
def load_data(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8-sig') as csvfile: #This line specifically comes exactly from the Bob Ross excercise. This line serves to open the csv file, and we use 'r' because all we want to do with the csv file is access it in a readable mode. I am not fully aware f what the encoding = 'utf-8-sig' does in regards to this code however, I was able to do some research and find out that it "identified the encoding format rather than the byte order of the document" - https://learn.microsoft.com/en-us/globalization/encoding/byte-order-mark
            hostReader = csv.DictReader(csvfile)#In this line, we use 'csv.DictReader' to actually read the information found in the CSV file. This function is incredibly helpful as it interprets each row of the CSV as a dictionary. In this dictionary, the keys are the column names. 
            spotifyCsvData = [row for row in hostReader if "" not in row.values()] #We are using list comprehension to clean the hostReader dictionary. This comprehension filters out any rows where there are empty strings. We do not want to deal with rows that have missing data.
    except IOError: #When running previous iterations of this code, I kept getting this error. I did some research into this to learn more, and I discovered that IOErrors are Input/Output errors. This arises when we attempt to oppen a file that may not exist - https://www.educba.com/python-ioerror/.         
        print("Make sure you're using a file that actually exists on your computer. Also make sure that you are spelling the name of the file used correctly and exactly how it was saved on the computer")
    except Exception as e: 
        print("Error found in code:", e) #This second 'except' exists to present to the user if any other sort of error is present in the code. The print statement will actually print out the exact issue found in the code, saving the specific error as variable 'e', and printing it so that the user can easily fix said error
        
    trackNameList = [] #This  list will be used to keep track of the unique track names so that we can avoid having duplicates in the list
    cleanedData=[] #This list's purpose is to store the list post-cleaning. This list stores all of the complete and unique data from the CSV

    for row in spotifyCsvData: #This loop iterates through all of the rows stores in spotifyCsvData to check for duplicates

        if row['track_name'] not in trackNameList: #This conditional serves to make sure that the track_name value of the row being checked is not already a part of the trackNameList. By checking this, we are able to make sure we are only dealing with unique data. 

            trackNameList.append(row['track_name']) #We do this to keep track of the data we have already seen in the list

            cleanedData.append(row)  #This list adds the whole row to this list knowing that the appended data is unique and not already in the list

    return cleanedData 

    
# PART 2: Audio analysis function, sort function, table_print function
# By default, print the 'top 20'




# PART 2A: Creation of Sort Function
# This code I used comes directly from the ZyBooks, specifically chapter 16.6
# I chose to use selection sort because it was easier for me to grasp this concept in comparison to insertion sort
def selection_sort(nested_list, pos):
    for i in range(len(nested_list)-1): #Outer loop is designed to iterate through the "nested_list" and it stops at the penulitmate element. The reason why I made the loop stop at the penultimate element is because the subsequent loop will compare each element with the element that comes after it, and the final element will have nothing after it. 
        indexMin = i #I created this variable so that I can save the index of the smallest value found during the iterations of the inner loop. 

        for j in range(i + 1, len(nested_list)):    
            if nested_list[j][pos] < nested_list[indexMin][pos]: #This conditional is designed to check if the element found at index 'j' is smaller than the elment currently being stored in indexMin. If the value of j is indeed smaller than the current value of indexMin, then the new value of indexMin will become 'j'.
                indexMin = j  

        #These three lines work to swap the element at the current outer loop index 'i' with the element stored at 'indexMin'. Doing this will put the actual smallest value at the right place. 
        temp = nested_list[i] 

        nested_list[i] = nested_list[indexMin]

        nested_list[indexMin] = temp
        
    return nested_list

#PART 2B: Creation of the Table Print Function
# The code I will be using is a slight variation of the code used in the lesson 18.3 excercise
def table_print(headers, data, width = 40): 
    
    output="{:<{}} {:<{}} {:<{}}" #In this line, I am defining 3 placeholders

    print(output.format(headers[0],width,headers[1],width,headers[2],width)) #This line is designed to format the header elements into the placeholders using the format function. 
    print("-" * (width) * 3) #This line prints dashes to seperate the header from the data. The length of the dashes is equal to three times the specified width


    for (col0,col1,col2) in data: #This loop runs through 'data', which contains all the rows of data. It will print each row by formatting the elements into their respective placeholders using the format function, similar to the code in line 61.
        print(output.format(col0,width,col1,width,col2,width))

    print()

#PART 2C: Creation of the Track Analysis Function
def track_analysis(track_list, feature, cutoff = 20):

    try:

        trackFeatures = ['track_popularity','track_acousticness','track_danceability','track_duration_ms', 'track_energy','track_instrumentalness', 'track_loudness','track_tempo', 'track_tempo','track_valence'] #This list defines all the potential parameters related to track analysis. This list contains all the potential features the user can get information on

        if feature in trackFeatures: #This conditional exists to verify that the feature the user inputs exists and information can be gathered regarding that,

           trackInfo =[[row['track_name'],row['artist_name'], float(row[feature])] for row in track_list] #This newly created list is designed to contain the information regarding track name, the arist(s) who made the track, and the specified feature. The information is saved in the form of a float because a) many of the features are conveyed as decimals and b) when the data is stored in any other form, the incorrect data is presented 

           trackInfo = selection_sort(trackInfo,2) #Calls the sorting function to sort all of the information from least to greatest

           trackInfo.reverse() #reversing the sort so that the highest values are seen at the top

           table_print(['track_name','artist_name', feature],trackInfo[0:cutoff])  #Calling the table_print function to ensure that the information is conveyed in a tabular form

        else:

            raise Exception('We do not have information on that feature, please make sure your spelling is correct or try another feature') #Error handling in the event that the user inputs an invalid feature or spells it wrong

    except Exception as e:  

        print("Error:", e)    #Error handling in the event that any other errors arise in the code





# PART 4: BONUS - Artist info function

def remove_duplicates(artist_fact):
    unique_elements = list(set(artist_fact))
    dataShow = " ".join([str(unique_elements)])
    return dataShow

def artist_info(track_list, artist_name):
    track_names = []
    followers = []
    popularity_score = []
    genres = []
   

    for data in track_list:
        if data['artist_name'] == artist_name:
            track_names.append(data['track_name'])
            followers.append(int(data['artist_followers']))  # Convert to int
            popularity_score.append(int(data['artist_popularity']))  # Convert to int
            genres.append(data['artist_genres'])
             

    followers2 = remove_duplicates(followers)
    genres2 = remove_duplicates(genres)
   

 
    
    print(f"\n# Followers: {followers2}")
    print(f"Popularity score: {popularity_score[0]}")
    print(f"Genres: {genres2}\n")  
    print(f"Tracks released: \n\t{"\n""\t".join(track_names)}\n")
    
   





# Test code for the Module

if __name__ == "__main__":

    # TEST PART 1

    spotify_data_test = load_data('spotify_data_2022.csv')

    print(len(spotify_data_test), "rows loaded successfully!")

    print()



        

    # TEST PART 2A

    instruments = [("Trumpet", "Brass", 35), ("Saxophone", "Woodwind", 12),

                   ("Snare Drum", "Percussion", 22), ("Cymbal", "Percussion", 40)]

    sorted_instruments = selection_sort(instruments, 2)

    print(sorted_instruments)

    print()



    # TEST PART 2B

    table_print(["Instrument", "Type", "Amount"], sorted_instruments, 15)

    print()



    # TEST PART 2C

    track_analysis(spotify_data_test, "track_popularity", 10)

    print()
