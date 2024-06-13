# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0):
        return (year % 100 == 0) and (year % 400 == 0) or year % 100 != 0
    else:
        return False

# Input from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
