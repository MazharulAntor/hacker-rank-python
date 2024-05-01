import calendar

month, day, year = map(int, input().split())
weekday_index = calendar.weekday(year, month, day)
day_name = ""

if weekday_index == 0:
    day_name = "Monday"
elif weekday_index == 1:
    day_name = "Tuesday"
elif weekday_index == 2:
    day_name = "Wednesday"
elif weekday_index == 3:
    day_name = "Thursday"
elif weekday_index == 4:
    day_name = "Friday"
elif weekday_index == 5:
    day_name = "Saturday"
elif weekday_index == 6:
    day_name = "Sunday"

print(day_name.upper())
