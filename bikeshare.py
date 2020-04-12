import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
check=''
months=['january','february','march','april','may','june','july','august','september','october','november','december','all']
check_day=['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    inp=True
    while inp==True:
        city=input('Enter The Name of City You Want To Explore:\n').lower()
        global check
        check=city
        if(city=='chicago' or city=='new york city' or city=='washington' ):
            inp=False
        else:
            print('Enter A Valid City Name (chicago OR new york city OR washington)\n:')


    # get user input for month (all, january, february, ... , june)
    month_input=''
    while month_input not in months:
        month_input=input('Enter The Month You Would Like to Explore or All if you like to explore all Month\n').lower()
        if month_input=='all':
            month='all'
        else:
            month=month_input


    # get user input for day of week (all, monday, tuesday, ... sunday)
    days_input=''
    while days_input not in check_day:
        days_input=input('Enter The Day Of The week You Would Like TO Explore or All if you like to explore by all days\n').lower()
        if days_input=='all':
            day='all'
        else:
            day=days_input


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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['hour']=df['Start Time'].dt.hour
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    if month!='all':

        month=months.index(month)+1
        df=df[df['month']==month]
    if day!='all':
        df=df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("* Most Common Month-------->")
    print(' '*25,df['month'].mode()[0])

    # display the most common day of week
    print("* Most Common Day Of Week-->")
    #print(str(df['day_of_week']).mode()[0])
    print(' '*25,df['day_of_week'].value_counts().idxmax())

    # display the most common start hour
    print('* Most Common Start hour--->')
    print(' '*25,df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("* Most Common Start Station-->")
    print(' '*24,df['Start Station'].mode()[0])

    # display most commonly used end station
    print("* Most Common End Station---->")
    print(' '*24,df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    df['combo']=df['Start Station'] +' '+ ['End Station']
    print("* most frequent combination of start station and end station trip--")
    print(' '*51,df['combo'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("* total travel time------>")
    print(' '*20,df['Trip Duration'].sum())


    # display mean travel time
    print("* mean travel time------->")
    print(' '*20,df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count=df.groupby(['User Type'])['User Type'].count()
    print('counts of user type----->')
    print(user_type_count)


    if check=='chicago' or check=='new york city':
        # Display counts of gender
        gender_counts=df.groupby(['Gender'])['Gender'].count()
        print('counts of Gender type-----')
        print(gender_counts)

        # Display earliest, most recent, and most common year of birth
        temp=pd.DataFrame(df,columns=['Birth Year'])
        print('Most Recent Birth Year   -->',temp.max())
        print('Most Earliest Birth Year -->',temp.min())
        print('Most common Year Of Birth-->',temp['Birth Year'].mode()[0])



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        print_raw_input=input('Would you like to print raw data(YES/NO)',).lower()
        if print_raw_input == 'yes':
            print(df.loc[0:4])
        kk=int(df.shape[0])

        for i in range(5,kk,5):
            print_next=input('Would You like to print next five raw data(Yes/No)').lower()
            if print_next == 'yes':
                print(df.loc[i:i+4])
            else:
                break



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
