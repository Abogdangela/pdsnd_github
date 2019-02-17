import time
import datetime
import pandas as pd
import numpy as np

# python bikeshare.py - for convinience to fast launch the script

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - number of the month to filter by, or "all" (0) to apply no month filter
        (str) day - number of the day of week to filter by, or "all" (0) to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities=['chicago','new york city','washington']
    while True:
        try:
            city = input("Please, choose the city to analyze: Chicago, New York City or Washington.\n").lower()
        except Exception as e:
            print("Exception occurred: {}".format(e))
            continue
        if city not in cities:
            print("Sorry, I didn't get: {}. Please type the name of the city more properly.".format(city))
            continue
        if city in cities:
            print("{} - is a great choise, let's continue.".format(city))
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    months = {1:'January', 2: 'February', 3:'March', 4:'April', 5 :'May', 6: 'June', 0: 'all'}
    while True:
        try:
            month_int=int(input("Please choose the month from January to June (1-6) to filter by, or '0' to apply no month filter. \nPlease input int:\n"))
        except ValueError:
            print('Please input the number from 1 to 6')
            continue
        if month_int not in months:
            print("Try to type the month more properly.")
            continue
        if month_int in months:
            month=months[month_int]
            print("{}! Thank you for your choise!".format(month))
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = {1: 'Monday', 2: 'Tuesday', 3 : 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday', 0: 'all'}
    while True:
        try:
            day_int = int(input("Please input the day of week (1-7) to filter by, or '0' to apply no day filter. \nPlease input int:\n"))
        except ValueError:
            print('Please input the number from 1 to 7')
            continue
        if day_int not in days:
            print("Try to type the number of the day more properly.")
            continue
        if day_int in days:
            day=days[day_int]
            print("{}! Thank you for your choise!".format(day))
            break

    print('-'*40)

    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - number of the month to filter by, or "all" to apply no month filter
        (str) day - number of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    if month != 'all':

    #use the index of the months list to get the corresponding int
    #filter by month to create the new dataframe
    #filter by day of week if applicable
    #filter by day of week to create the new dataframe
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1
        df = df[df['month'] == month]

        if day != 'all':
            df = df[df['day_of_week'] == day.title()]
        else:
            return df
    else:
        return df

    print('\nRun some analysis of user statistics...\n')
    start_time = time.time()
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    try:
        # TO DO: display the most common month
        popular_month = df['month'].mode()[0]

        # TO DO: display the most common day of week
        popular_dow = df['day_of_week'].mode()[0]

        # TO DO: display the most common start hour
        popular_hour = df['hour'].mode()[0]

        print('Most Popular Month:  {}'.format(popular_month))
        print('Most Popular Day of week:  {}'.format(popular_dow))
        print('Most Popular Hour:  {}'.format(popular_hour))
    except IndexError:
        print('\nThe time statistic is out of range\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    try:
    # TO DO: display most commonly used start station
        common_start_station = df['Start Station'].value_counts().argmax()
    # TO DO: display most commonly used end station
        common_end_station = df['End Station'].value_counts().argmax()

    # TO DO: display most frequent combination of start station and end station trip
        most_common_start_end_station = df.groupby(['Start Station','End Station']).idxmax().index[-1]

        print('Most used start station:  {}'.format(common_start_station))
        print('Most used end station:  {}'.format(common_end_station))
        print('Most frequent combination of start station and end station trip:  {}'.format(most_common_start_end_station))
    except IndexError:
        print('\nThe statistic is out of range\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    try:
        # TO DO: display total travel time
        total_travel_time=(df['Trip Duration'].sum())/60

        # TO DO: display mean travel time
        mean_travel_time=(df['Trip Duration'].mean())/60

        print('Total travel time in minutes:  {}'.format(total_travel_time))
        print('Mean travel time in minutes:  {}'.format(mean_travel_time))
    except (IndexError, KeyError):
        print('\nOut of range\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    try:
    # TO DO: Display counts of user types
        user_types = df['User Type'].value_counts()[0:]

    # TO DO: Display counts of gender
        gender=df['Gender'].value_counts()[0:]

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest=int(df['Birth Year'].min())
        recent=int(df['Birth Year'].max())
        common=int(df['Birth Year'].value_counts().idxmax())

        print('Count of the user type:\n{}\n'.format(user_types))

        print('Count of gender:\n{}\n'.format(gender))

        print('Earliest year of birth:  {}\n'.format(earliest))
        print('Recent year of birth:  {}\n'.format(recent))
        print('Common year of birth:  {}\n'.format(common))

    except (KeyError, IndexError):
        print('\nUser Statistic is unavailable for this city\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    Irow = 0
    "Displays 5 lines of data based on user input. IF user wants more data, five more lines of data are displayed"

    more_info = input(str('\nDo you want to see raw data? Please type Yes or No!\n'))
    more_info = more_info.strip().lower()

    while True:
        if more_info == 'yes':
            new_df = df[Irow:Irow+5]
            print('\nThe raw data is presented below!\n')
            print(new_df)
            print('-'*80)
            Irow += 5
        more_info = input(str('\nDo you want to see more data? Please type Yes or No!\n'))
        if more_info != 'yes':
            break
    print('-'*80)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nThats\'s was great! Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
