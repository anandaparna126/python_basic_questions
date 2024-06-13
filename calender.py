import calendar

year = int(input("enter year: "))
month = int(input("enter month using 1-12: "))
calendar = calendar.month(year, month)
print(calendar)