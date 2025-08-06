# !/usr/bin/env python3

# This is a practice file for functions in Python.
# Functions are repeatable actions that can be called 
# multiple times without needing to rewrite the code.

# Functions must first be defined using the keyword 'def'.
# Functions can take parameters, which are values passed to the function.
# Functions can also return values, which are the results of the function's actions.
# Functions may return 'None', which means they do not return a value.

# Function to test years for leap year
def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
    else:
        return False

# A predefined list of years and their expected results are passed to the function
# If the function returns the expected result, it is considered "OK".
# If the function does not return the expected result, it is considered "Failed".
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end=" ")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

# Expanding this function to check for number of days in a given month
def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
    else:
        return False
    
def days_in_month(year, month):
    months_30 = [4, 6, 9, 11]
    months_31 = [1, 3, 5, 7, 8, 10, 12]
    days = 0
    feb = is_year_leap(year)
    if feb == True and month == 2:
        days = 29
    elif feb == False and month == 2:
        days = 28
    elif month in months_30:
        days = 30
    elif month in months_31:
        days = 31
    else:
        return None
            
    return days
        
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end=" ")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

# Further expanding function to tell what day of the year a passed date is

def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
    else:
        return False
    
def days_in_month(year, month):
    months_30 = [4, 6, 9, 11]
    months_31 = [1, 3, 5, 7, 8, 10, 12]
    days = 0
    feb = is_year_leap(year)
    if feb == True and month == 2:
        days = 29
    elif feb == False and month == 2:
        days = 28
    elif month in months_30:
        days = 30
    elif month in months_31:
        days = 31
    else:
        return None
            
    return days
    
def day_of_year(year, month, day):
    value = 0
    month_passed = 1
    if month == 0 or month > 12 or day > 31:
        return None
    elif month == 1:
        return day
    else:
        for n in range(month - 1):
            prev_month = days_in_month(year, month_passed)
            value += prev_month
            month_passed += 1
            
        value += day
        return value
        
query_year = int(input("Enter a year: "))
query_month = int(input("Enter a month: "))
query_day = int(input("Enter a day: "))
result = day_of_year(query_year, query_month, query_day)
print(f"The date {query_year}-{query_month:02d}-{query_day:02d} is the {result} day of the year.")

# Prime Number Checker Function
def is_prime(num):
    if num == 0 or num == 1:
        return
    elif num == 2:
        return num
    else:
        check = True
        for x in range(2, num + 1):
            if (num % x) == 0 and x != num:
                check = False
                break
        if check == True:
            return num

limit = int(input('Please enter a number to see all previous prime numbers: '))        
for i in range(1, limit):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()

# Fibonacci Sequence Function
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):  # testing
    print(n, "->", fib(n))
