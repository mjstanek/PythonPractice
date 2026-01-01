# Practicing with the datetime module 

import datetime
import pytz

# Naive Dates:
# not a complete date/time - missing things like Time Zone or
# DST

# Aware Dates:
# Have enough information to determine Time Zone and DST

# ========== Dates ==========

# Create a date using the .date() method
# Pass a Year, Month, and Day to the method
# There is no need for a leading zero on single-digit month/days
d = datetime.date(2024, 8, 8)
print(d)

# Adding .today() will get the current date 
today = datetime.date.today()
print(today)
# This method can be enhanced by using dot notation to pull
# out the year, the month or the day
print(f"The current year is: {today.year}")
print(f"The current month is: {today.month}")
print(f"The current day is: {today.day}")

# We can pull the day of the week by either using the methods .weekday or .isoweekday
print(f"Weekday: {today.weekday()}")
print(f"ISO Weekday: {today.isoweekday()}")
# The difference is counting. Weekday goes Monday to Sunday as a 0 index, so 
# Monday = 0, Tuesday = 1 ... Sunday = 6
# ISO Weekday is the same scale, but starts at 1.
# Monday = 1, Tuesday = 2 ... Sunday = 7

# Time Delta
# Difference between two dates/times
# This is showcasing adding and subtracting a Time Delta to an existing/known date
timeDelta = datetime.timedelta(days=7)
print(today + timeDelta)
print(today - timeDelta)

# Time Deltas can also be used to determine the difference between two dates
nextBirthday = datetime.date(2026, 7, 8)
lastBirthday = datetime.date(2025, 7, 8)

untilNextBirthday = nextBirthday - today
fromLastBirthday = today - lastBirthday

print(f"It has been {fromLastBirthday.days} days since my last birthday and is " + 
      "{untilNextBirthday.days} days until my next brithday.")
print(f"{untilNextBirthday.days} days is also {untilNextBirthday.total_seconds()} seconds.")

# ========== Times ==========

# Time works with Hours, Minutes, Seconds, and Microseconds
# By default, does not contain Time Zone information
time = datetime.time(12, 31)
print(time)
print(f"Hour: {time.hour}")
print(f"Minute: {time.minute}")

# ========== Date/Time ==========

fullDate = datetime.datetime(2024, 8, 8, 12, 31)
print(fullDate)
# Every attribute is identifiable just as above
# Additionally, we can grab just the date using the .date() method
# or the time using the .time() method

print(fullDate + timeDelta)
hourDelta = datetime.timedelta(hours=461168)
print(fullDate + hourDelta)

# Current Times:
todayDateTime = datetime.datetime.today()
nowDateTime = datetime.datetime.now()
# NOTE .utcnow is deprecated
# utcNowDateTime = datetime.datetime.utcnow()
# Here is the new way of retrieving UTC Now
utcNowDateTime = datetime.datetime.now(datetime.UTC)
# The difference between the today and now method is shown above - the now
# method allows us to pass a Time Zone, whereas the today method pull the
# Time Zone of none and retrieves the local time 

print(f"Date/Time Today: {todayDateTime}")
print(f"Date/Time Now: {nowDateTime}")
print(f"Date/Time UTC Now: {utcNowDateTime}")

# ========== Time Zone ==========

# Python documentation recommends using the pytz module to work with Time Zones
# A best practice is to always use UTC when working with date/times

awareDate = datetime.datetime(2024, 8, 8, 12, 31, tzinfo=pytz.UTC)
print(awareDate)

awareDateEastern = awareDate.astimezone(pytz.timezone('US/Eastern'))
print(awareDateEastern)

# Converting naive dates to aware dates
# First we have to localize the datetime to make it Time Zone Aware
fullDate = pytz.timezone('US/Eastern').localize(fullDate)
fullDatePacific = fullDate.astimezone(pytz.timezone('US/Pacific'))

print(fullDate)
print(fullDatePacific)
# strftime --> F is for Format, so it helps format the time into a readable string output
print(fullDate.strftime('%B %d, %Y'))
# Recommended to just use the documentation to figure out what codes to pass

# strptime --> P is for Parse , so it helps to take a string input and force it into a datetime object
# Pass the date to convert, then the codes
stringDate = "August 08, 2024"
convertedStringDate = datetime.datetime.strptime(stringDate, '%B %d, %Y')
print(convertedStringDate)

# Once we have DateTime Objects, we can then do comparisons on them
print(nextBirthday > lastBirthday)
print(awareDate == awareDateEastern) # Note that the Time Zone Information reconciles here and these dates are the same
