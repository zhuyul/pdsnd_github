import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_OR_DAY = {'1': 'month',
                '2': 'day',
                '3': 'all'}
MONTH_DATA = {'1': 'january',
              '2': 'february',
              '3': 'march',
              '4': 'april',
              '5': 'may',
              '6': 'june',
              '0': 'all'
             }
DAY_DATA = {'1': 'monday',
            '2': 'tuesday',
            '3': 'wednesday',
            '4': 'thursday',
            '5': 'friday',
            '6': 'saturday',
            '7': 'sunday',
            '0': 'all'}


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
    while True:
        try:  
            city = CITY_DATA[input('Would you like to see data for chicago, new york city, or washington?\n').lower()]
            break
        except KeyError:
            print('Wrong Value')

    while True:
        try:  
            #mord = input('Would you like to filter the data by month, day, or not at all?')
            mord = MONTH_OR_DAY[input('Would you like to filter the data by month, day, or not at all? 1 - month, 2 - day\n').lower()]
            break
        except KeyError:
            print('Wrong Value')
   
    month = 'all'
    day = 'all'
            
    # TO DO: get user input for month (all, january, february, ... , june)
    if mord == 'month':
        while True:
            try:  
                month = MONTH_DATA[input('Which month: 1 - January, 2 - February, 3 - March, 4 - April, 5 - May, or 6 - June?\n').lower()]
                break
            except KeyError:
                print('Wrong Value')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    elif mord == 'day':
        while True:
            try:  
                day = DAY_DATA[input('Which day: 1 - Monday, 2 - Tuesday, 3 - Wednesday, 4 - Thursday, 5 - Friday, 6 - Saturday, or 7 - Sunday?\n')]
                break
            except KeyError:
                print('Wrong Value')
    #print(city, month, day)
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    '''
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    '''        
    df = pd.read_csv(city)
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    #print(df['month'])
    df['day'] = df['Start Time'].dt.weekday
    #print(df['day'])
  
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month=months.index(month)+1
        df = df[df['month'] == month]
        
    elif day != 'all':
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day=days.index(day)+1
        df = df[df['day'] == day]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month    
    df['day'] = df['Start Time'].dt.weekday
    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:',popular_month)

    # TO DO: display the most common day of week
    #df['Start Time'] = pd.to_datetime(df['Start Time'])
    #df['day'] = df['Start Time'].dt.weekday_name
    popular_day = df['day'].mode()[0]
    print('Most Popular Day of Week:', popular_day)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')   

    # TO DO: display most commonly used start station
    start_station_counter = {}
    for start_station in df['Start Station']:
        if start_station not in start_station_counter:
            start_station_counter[start_station] = 1
        else:
            start_station_counter[start_station] +=1
    #print(start_station_counter)    
    start_station_count = df['Start Station'].value_counts()
    #max_start_station = start_station_count.max()
    start_max = max(start_station_counter, key=start_station_counter.get)
    print('Most Common Start Station:', start_max)
    
    # TO DO: display most commonly used end station
    end_station_counter = {}
    for end_station in df['End Station']:
        if end_station not in end_station_counter:
            end_station_counter[end_station] = 1
        else:
            end_station_counter[end_station] +=1
    #print(end_station_counter)    
    end_station_count = df['End Station'].value_counts()
    #max_end_station = end_station_count.max()
    #print(max_end_station)
    end_max = max(end_station_counter, key=end_station_counter.get)
    print('Most Common End Station:', end_max)
    

    # TO DO: display most frequent combination of start station and end station trip
    trip = df[['Start Station', 'End Station']].mode().loc[0]
    print('Most Common Combination: ', trip)
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('total travel time is %d' % total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('mean travel time is %s ' % mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(user_type)
    

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].fillna(0)
        gender_count = gender.value_counts()
        print('Gender Counts:', gender_count)
    except Exception:
        pass

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        df['birth'] = df['Birth Year']
        #df['birth'] = df['Birth Year'].fillna('NA')
        earlist = df['birth'].min(axis=0)
        most_recent = df['birth'].max(axis=0)
        common = df['birth'].mode()[0]
        print('Earlist Birth:', earlist)
        print('Most Recent Birth:', most_recent)
        print('Most Common Birth:', common)
    except Exception:
        pass
    print('-'*40)

def display_data(df):
    print_raw = input('Would you like to display raw data?').lower()
    if print_raw == 'yes':
        print(df.iloc[0:5])
    else:
        pass
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main()