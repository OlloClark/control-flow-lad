# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input("Enter the month of the year (Jan - Dec):").upper()

if month in ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]:
    print(f"You entered {month}")
    day = input("Enter the day of the month (1-31):")
    if int(day) in range(1, 32):
        print(f"you entered {month} {day}")
    else:
        print("not a valid day; use 1-31")
    if month in ["JAN", "FEB"]:
        if month == "FEB" and int(day) in range(29,32):
            print("FEB only has 28 days")
        else:
            print(f"{month} {day} is in Winter")
    elif month == "MAR":
        if int(day) < 20:
            print(f"{month} {day} is in Winter")
        else:
            print(f"{month} {day} is in Spring")
    elif month in ["APR", "MAY"]:
        if month == "APR" and int(day) == 31:
            print(f"{month} only has 30 days")
        else:
            print(f"{month} {day} is in Spring")
    elif month == "JUN":
        if int(day) == 31:
            print(f"{month} only has 30 days")
        elif int(day) < 21:
            print(f"{month} {day} is in Spring")
        else:
            print(f"{month} {day} is in Summer")
    elif month in ["JUL", "AUG"]:
        print(f"{month} {day} is in Summer")
    elif month == "SEP":
        if int(day) == 31:
            print(f"{month} only has 30 days")
        elif int(day) < 22:
            print(f"{month} {day} is in Summer")
        else:
            print(f"{month} {day} is in Autumn")
    elif month in ["OCT", "NOV"]:
        if month == "NOV" and int(day) == 31:
            print(f"{month} only has 30 days")
        else:
            print(f"{month} {day} is in Autumn")
    elif month == "DEC":
        if int(day) < 21:
            print(f"{month} {day} is in Autumn")
        else:
            print(f"{month} {day} is in Winter")
else:
    print("not a valid entry; use 3 letter month code")

