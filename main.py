# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
# Output:       Valid date is printed or user is alerted that an invalid date was entered.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31
LEAP_YEAR = MIN_YEAR % 4 == 0 and (MIN_YEAR % 100 == 0 or MIN_YEAR % 400 == 0) 
year = None
month = None 
day = None

# Get the year, then the month, then the day
# housekeeping()

month = int(input("Enter a month: "))
day = int(input("Enter a day: "))
year = int(input("Enter a year: "))

# Check to be sure date is valid
validDate = True

if int(year) <= MIN_YEAR:
    validDate = False
elif int(month) < MIN_MONTH:
    validDate = False
elif int(month) > MAX_MONTH:
    validDate = False
elif int(day) < MIN_DAY:
    validDate = False
elif int(day) > MAX_DAY:
    validDate = False
elif month == 2 and day > 28 and year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
    validDate = False
elif month == 4 or month == 6 or month == 9 or month == 11 and day > 30:
    validDate = False    
# invalid day for April, June, September, November, February for a non leap year

# Test to see if date is valid and output date and whether it is valid or not
# endOfJob()
if validDate == True: print(str(month) + "/" + str(day) + "/" + str(year) + " is a valid date") 
    # Output statement
else: print(str(month) + "/" + str(day) + "/" + str(year) + " is an invalid date") 
    # Output statement
