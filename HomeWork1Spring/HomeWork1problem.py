# Hugues Izah, student ID: 2310365
# Prompt the user to enter the current date
print("Birthday Calculator")

# Current day
current_month = int(input("Current day\nMonth: "))
current_day = int(input("Day: "))
current_year = int(input("Year: "))

# Prompt the user to enter their birthday
print("Birthday")
birthday_month = int(input("Month: "))
birthday_day = int(input("Day: "))
birthday_year = int(input("Year: "))

# Calculate age
age = current_year - birthday_year
if (current_month, current_day) < (birthday_month, birthday_day):
    age -= 1

# Output the age
print(f"\nYou are {age} years old.")

# Check if it's the user's birthday and output a message
if current_month == birthday_month and current_day == birthday_day:
    print("Happy Birthday!")
