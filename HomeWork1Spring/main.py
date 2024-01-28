# Hugues Izah, student ID: 2310365
print("Birthday Calculator")

current_month = int(input("Current Month: "))
current_day = int(input("Day: "))
current_year = int(input("Year: "))

print("Birthday")
birthday_month = int(input("Month: "))
birthday_day = int(input("Day: "))
birthday_year = int(input("Year: "))

age = current_year - birthday_year
if (current_month, current_day) < (birthday_month, birthday_day):
    age -= 1

print(f"\nYou are {age} years old.")

if current_month == birthday_month and current_day == birthday_day:
    print("Happy Birthday!")
