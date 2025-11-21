# Import the datetime module.
# Define a function get_day_of_week that takes a date string in YYYY-MM-DD format.
# Use datetime.strptime() to convert the date string into a datetime object and then use strftime('%A') to get the day of the week.
# Test the function with various dates.

import datetime as dt

def get_day_of_week(date_str):
    try:
        date_obj = dt.datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime('%A')
    except ValueError:
        return "Invalid date"

print('-'*40)
a = get_day_of_week("2023-04-15")  # Invalid date
print(a)
print('-'*40)
b = get_day_of_week("2032-12-02")  # Valid date
print(b)
print('-'*40)

