# Program to take month and year as user input and print the calendar.
# Done By: Shivam Kislay 119220420
# Creation Date: 16-10-2019


# Function to determine if the entered year is a leap year.
# returns true if the year is leap else false
def is_leap(year):
    divby4 = year % 4 == 0
    divby100 = year % 100 == 0
    divby400 = year % 400 == 0
    return divby4 and (not divby100 or divby400)


# Function to return the number of days present in the month.
def num_days(month, year):
    # Assign number to their respective months
    Jan, March, May, July, Aug, Oct, Dec = 1, 3, 5, 7, 8, 10, 12
    April, June, Sept, Nov = 4, 6, 9, 11

    # Set variable thirty_days as true if month is equal to the below mentioned condition
    thirty_days = (month == Sept) or (month == April) or (month == June) or (month == Nov)

    # Set variable thirty_one_days as true if month is equal to the below mentioned condition
    thirty_one_days = (month == Jan) or (month == March) or (month == May) or (month == Aug) or (month == Oct) \
                      or (month == Dec) or (month == July)

    if thirty_days:
        return 30
    elif thirty_one_days:
        return 31
    elif is_leap(year):
        return 29
    else:
        return 28


# Function to Evaluate month and year and return the identifier for the start day of the month.
# e.g. 0 for Sunday, 1 for Monday, ......, 6 for Saturday
def start_day(month, year):
    total_days = 0
    year_counter = 2000
    month_counter = 1
    # logic to calculate total number of days between the mentioned month, year and 1, 1, 2000.
    for yy in range(year_counter, year + 1):
        for mm in range(month_counter, 13):
            if mm == month and yy == year:
                break
            days = num_days(mm, yy)
            total_days = total_days + days

    # We add 6 to the total number of days because 1/1/2000 was Saturday.
    # Positional Value of Saturday is 6
    return (total_days + 6) % 7


# Function to Print the Calendar in the Standard Calendar Format
def print_calendar(day, number_of_days):
    # loop to print calendar from the second row onwards
    while day <= number_of_days:
        # print("\n")
        print('')
        # loop to print the days with each day padded with 3 spaces each.
        for k in range(7):
            print("%3s" % day, end="")
            day = day + 1
            if day > number_of_days:
                break


# Parent function to evaluate the start position of the month and print the calendar..
# ..of the given month and year
def cal(month, year):
    # List to hold The week days. With [0] as Su and so on
    week = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
    # loop to print the Calendar Header
    for w in week:
        print("%3s" % w, end="")
    print("")
    # Function Call to return the starting position of each month.
    month_start_pos = start_day(month, year)
    date = 1
    # Loop to fill the first day till the month start day with blanks
    for i in range(month_start_pos):
        print("   ", end="")
    # loop to print the first row of the calendar
    for j in range(month_start_pos, 7):
        print("%3d" % date, end="")
        date = date + 1
    # Function call to print the calendar
    print_calendar(date, num_days(month, year))
