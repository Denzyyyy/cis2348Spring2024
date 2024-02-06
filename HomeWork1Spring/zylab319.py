# Hugues Izah psid = 2310365
import math

height = float(input("Enter wall height (feet):\n"))
width = float(input("Enter wall width (feet):\n"))

area = int(height * width)
print(f"Wall area: {area} square feet")

paint_needed = area / 350.0
print(f"Paint needed: {paint_needed:.2f} gallons")

cans_needed = math.ceil(paint_needed)
print(f"Cans needed: {cans_needed} can(s)")

paint_colors = {'red': 35, 'blue': 25, 'green': 23}

color_choice = input("\nChoose a color to paint the wall:\n").lower()

if color_choice in paint_colors:
    cost_per_gallon = paint_colors[color_choice]
    total_cost = cost_per_gallon * cans_needed
    print(f"Cost of purchasing {color_choice} paint: ${total_cost}")
else:
    print("Invalid color choice.")
