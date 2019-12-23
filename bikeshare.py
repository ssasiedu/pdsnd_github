import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new_york': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # A while loop to take in the correct input for the city name.
    while True:
        #(str) city - variable for taking in user input for the name of the city.
        city = input("\nEnter in the name of the city you would like to analyze: [chicago], [new_york] or [washington]?").lower()
        if city in CITY_DATA:
            print("\nGreat you would like to analyze data for: ",city)
            break #breaking the loop after a correct city name has been entered.
        else:
            #Nofitifying the user about a wrong input
            print("\nSorry you entered a wrong city name.\n")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    # a while loop to take in the correct input for the month you perfer to filter the data by
    while True:
        #(str) month - variable for taking in the user input for the month you would like to filter the data by
        month = input("\nEnter in name of the month you would like to filter by: [all],[january],[february],[march],[april],[may],[june]?").lower()
        if month in ['all','january', 'february', 'march', 'april', 'may', 'june']:
            print("\nGreat you would like to filter on :",month)
            break #breaking the loop after a correct month has been entered
        else:
            # notifying the user about a wrong input
            print("\nSorry you entered a wrong month for the filter parameter.")
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # a while loop to take in the correct input for the day you perfer to filter the data by
    while True:
        #(str) day - variable for taking in the user input for the day you would like to filter the data by
        day = input("\nEnter in name of the week you would like to filter by: [all],[mon],[tue],[wed],[thu],[fri],[sat],[sun]?").lower()
        if day in ['all','mon','tue','wed','thu','fri','sat','sun']:
            print("\nGreat you would like to filter on :",day)
            print("\n\nWell Done!")
            break #breaking the loop after a correct input has been made
        else:
            # notifying the user about a wrong input
            print("\nSorry you entered a wrong day for the filter parameter.")
           

    print('-'*40)
    return city, month, day

    

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time 
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    #common_month - variable for keeping the value of the most common month
    common_month = df['month'].mode()[0]
    print("The most common month: {}".format(common_month))

    # TO DO: display the most common day of week
    #common_dow - variable for keeping the most common day of the week
    common_dow = df['day_of_week'].mode()[0]
    print("The most common day of the week: ",common_dow)

    # TO DO: display the most common start hour
    #converting start time to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #extract hour from the start time column
    df['hour'] = df['Start Time'].dt.hour
    
    #displaying the most common start hour
    print("The most common start hour: ",df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

  
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #common_start_station - variable to hold the most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("Commonly used Start Station : ",common_start_station)

    # TO DO: display most commonly used end station
    #common_stop_station - variable to hold the most commonly used end station
    common_stop_station = df['End Station'].mode()[0]
    print("Commonly used End Station: ",common_stop_station)

    # TO DO: display most frequent combination of start station and end station trip
    #start_end_station - variable for holding the most frequent combination of start station and end station trip
    start_end_station = df.groupby(['Start Station','End Station']).size().idxmax()
    print("The most frequent combination of start and end station trip: ",start_end_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #printing the total summation of the trip duration
    print("Total Travel Time : ",df['Trip Duration'].sum())

    # TO DO: display mean travel time
    #printing the mean of the trip duration
    print("Total Travel Time (Mean) : ",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    #Printing the total counts of user types
    print("Total Counts of User Types: \n",df['User Type'].value_counts())

    # TO DO: Display counts of gender
    #printing the total counts of gender
    print("\nTotal counts of gender: \n",df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print("\nThe earliest year of birth: \n",df['Birth Year'].min())
    print("\nThe most recent year of birth: \n",df['Birth Year'].max())
    print("\nThe most common year of birth: \n",df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
       
def main():
    """
    This system is designed to explore the Bikeshare Project based on three cities namely:
    Chicago,Washington DC and New York.
    The system starts by asking the user whether he/she would like to view some raw data in 5 rows.
    After the user has opted out of the raw data, the system calculates the statistical reports.
    These includes: time statistics,station statistics,trip duration and user statistics.
    """
    end_point = 5  #end point for data viewing 
    start_point = 0  #start point for data viewing
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)  
        while True:
            #(str) user_input - variable for taking in user input whether to view raw data or not
            user_input = input("\nWould you like to view the raw data? Enter [yes] or [no]:").lower()
            if user_input in ['yes','no']:
                if user_input == 'yes':
                    while True:
                        print("\nPrinting raw data...........from row {} to {}".format(start_point,end_point - 1))
                        print(df.iloc[start_point:end_point]) #printing the raw data
                        end_point += 5 #increamenting by 5
                        start_point += 5 #increamenting by 5
                        print('-'*40)
                        print("\nIf you want to see more data. Enter [yes] again:\n")
                        break # breaking from the loop after printing the first 5 rows of raw data   
                else:
                    print('-'*40)
                    print("System will now print statistical description of the data.")
                    break
            else:
                #prompting the user, when a wrong input has been entered
                print("You entered the wrong input")
                
        #Decribing the data before running statitical reports
        print("\nDescribing the data.")
        print('-'*40)
        print(df.describe())
        print('-'*40)
        
        #running the time statistics
        try:
            time_stats(df)
        #incase of an exception the system will handle it smoothly      
        except:
            print("There is no avaiable data to analyze")
            
        #running the statition statistical reports
        try:
            station_stats(df)
        #incase of an exception the system will handle it smoothly      
        except:
            print("There is no avaiable data to analyze")
            
         #running the trip duration statistics     
        try:
            trip_duration_stats(df)
        #incase of an exception the system will handle it smoothly  
        except:
            print("There is no avaiable data to analyze")
            
        #running the user statistical report    
        try:
            user_stats(df)
        #incase of an exception the system will handle it smoothly    
        except: 
            print("There is no avaiable data to analyze")
            
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
