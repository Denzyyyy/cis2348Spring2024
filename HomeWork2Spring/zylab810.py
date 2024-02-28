# Read the input word or phrase
input_str = input()

# Remove spaces from the input string
input_str_no_space = input_str.replace(" ", "")

# Check if the input string without spaces is equal to its reverse
if input_str_no_space == input_str_no_space[::-1]:
    print(f"{input_str} is a palindrome")
else:
    print(f"{input_str} is not a palindrome")
