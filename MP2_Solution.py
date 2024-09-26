import my_mod as mod #When using just import my_mod, I was running into errors and the functions were not being called. I discovered import as via stack overflow and implementing this change allowed for my code to function properly- https://stackoverflow.com/questions/46806699/use-case-for-import-as-in-python

    
# PART 4: Main

track_list = mod.load_data('spotify_data_2022.csv') #calls upon first created function in my_mod to gather the information neccessary for this project

while True:
    # Print the menu in accordance to the pictures shown in the instructions is using tabs and new lines.
    try:
        print("Welcome to Spotify Data Analysis!")
        print("\tType '1' for audio analysis\n")
        print("\tType '2' for artist info\n")
        print("\tType 'quit' for to exit the program\n")

        answer = input('What would you like to do? ').lower()  #Ask the user what they would like to do nbased off the options in the menu 
        if answer == '1':
            print('\nTrack features include things like track_danceability, track_loudness, etc.')
            input1= str(input('Which track feature would you like to sort by? '))  
            input2= int(input('How many top tracks would you like to display? '))
            print('')#Provide the user with the appropriate ammount of data
            mod.track_analysis(track_list,input1,input2)#Calls upon the functions created in my_mod
            
        elif answer == '2':
            user_artist = input('Which artist would you like to pull information on?')
            snapshot = (f'\n{user_artist}\'s 2022 Spotify Snapshot')
            print(snapshot)
            for  i in range (len(snapshot)):
                print('-', end='')
            
            mod.artist_info(track_list, user_artist)

            
        elif answer == 'quit':  #Gives the user the option to end program
            print("Thank you for using Spotify Data Analysis; have a great day!")
            break
        else:
            raise Exception('Sorry, that is not a option on the menu') #In the event that the user inputs inappropriate information
    except Exception as e:
        print("Error:", e)  #In the event that the user makes any other sort of error.
    
        

                                
