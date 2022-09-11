# Task: Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.
import calendar

user_year = int(input("Please enter a Year: "))
user_month = int(input("Please enter a Month (ex: 6 for June): "))

print(calendar.month(user_year, user_month))
