# Read the coefficients of the linear equations
a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

# Flag to check if a solution is found
solution_found = False

# Iterate through every value of x from -10 to 10
for x in range(-10, 11):
    for y in range(-10, 11):
        # Check if the current x and y satisfy both equations
        if a1 * x + b1 * y == c1 and a2 * x + b2 * y == c2:
            # Output the solution and finish
            print(x, y)
            solution_found = True
            break  # Exit the inner loop
    if solution_found:
        break  # Exit the outer loop if a solution is found

# If no solution is found, output "No solution"
if not solution_found:
    print("No solution")
