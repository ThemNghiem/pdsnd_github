import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    global city,month,day
    month = "all"
    day = "all"
   
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data of Chicago, New York, or Washington ? ').lower()
        if city.lower() not in ('chicago', 'new york', 'washington'):
            print("Invalid Input.")
        else:
            break
            
    while True:
        mode = input('Would you like to filter the data by month, day, both or not at all ? Type \"none\" for no filter ').lower()
        if mode not in ('month', 'day', 'both', 'none'):
            print("Invalid Input.")
        else:
            break
                    
    
    # TO DO: get user input for month (all, january, february, ... , june)
    if mode == 'both' or mode == 'month':
        while True:
            month = input('Which month? January, February, March, April, May or June or all ? ').lower()
            if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
                print("Invalid Input.")
            else:
                break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if mode == 'both' or mode == 'day':
        while True:
            day = input('Which day or all ? ').lower()
            if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
                print("Invalid Input.")
            else:
                break

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
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
    print('Most common month : ')
    print(df['month'].value_counts().idxmax())
    print('Count: ')
    print(df['month'].value_counts().max())


    # TO DO: display the most common day of week
    print('Most common day of week : ')
    print(df['day_of_week'].value_counts().idxmax())
    print('Count: ')
    print(df['day_of_week'].value_counts().max())

    # TO DO: display the most common start hour
    print('Most common hour : ')
    print(df['Start Time'].dt.hour.value_counts().idxmax())
    print('Count: ')
    print(df['Start Time'].dt.hour.value_counts().max())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most common start station : ')
    print(df['Start Station'].value_counts().idxmax())
    print('Count: ')
    print(df['Start Station'].value_counts().max())


    # TO DO: display most commonly used end station
    print('Most common end station : ')
    print(df['End Station'].value_counts().idxmax())
    print('Count: ')
    print(df['End Station'].value_counts().max())


    # TO DO: display most frequent combination of start station and end station trip
    df['Start - End'] = df[["Start Station", "End Station"]].apply(" - ".join, axis=1)
    print('Most common frequent combination of start station and end station trip : ')
    print(df['Start - End'].value_counts().idxmax())
    print('Count: ')
    print(df['Start - End'].value_counts().max())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: ')
    print(df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Average travel time: ')
    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    global city
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types: ')
    for i, v in df['User Type'].value_counts().items():
        print( i, ' ', v)
        
    if city == 'chicago' or city == 'new york':
        # TO DO: Display counts of gender
        print('Counts of gender : ')
        for i, v in df['Gender'].value_counts().items():
            print( i, ' ', v)

        # TO DO: Display earliest, most recent, and most common year of birth
        print('The most earliest year of birth: ')
        print(df['Birth Year'].min())

        print('The most recent year of birth: ')
        print(df['Birth Year'].max())

        print('The most common year of birth: ')
        print(df['Birth Year'].value_counts().idxmax())
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def get_individuals(df):

   start = 0
   column_name_list = list(df)
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
   while True:
        more_data = input('Would you like to view individual trip data ? ').lower()
        if more_data.lower() not in ('yes', 'no'):
            print("Invalid Input.")        
        else:
            if more_data.lower() == 'yes' :
                end = start + 5
                if end >= len(df):
                    print ('This is the end of the data, showing the last 5 rows')
                    end = len(df)
                    start = end -5
                for i in range(start,end):
                    for k in column_name_list:
                        print(k+':',df.iloc[i, column_name_list.index(k)] , '\n'
                             )
                        start+=5
            if more_data.lower() == 'no' :
                break
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        df.rename(columns={ df.columns[0]: "''" }, inplace = True)
        df = df.iloc[:,:-3]
        
        get_individuals(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

            
if __name__ == "__main__":
	main()
