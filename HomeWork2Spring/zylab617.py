# Define the key for character replacements
key = {
    'i': '!',
    'a': '@',
    'm': 'M',
    'B': '8',
    'o': '.'
}

# Read the input simple password
simple_password = input()

# Initialize the stronger password as an empty string
stronger_password = ""

# Iterate through each character in the input simple password
for char in simple_password:
    # Check if the character is in the key, if yes, replace it with the corresponding value
    if char.lower() in key:
        stronger_password += key[char.lower()]  # Append the replacement character
    else:
        stronger_password += char  # Keep the character unchanged if not in the key

# Append "q*s" to the end of the stronger password
stronger_password += "q*s"

# Output the stronger password
print(stronger_password)
