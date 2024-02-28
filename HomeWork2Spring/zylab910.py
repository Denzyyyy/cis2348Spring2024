import csv

# Read the name of the input file from the user
filename = input()

# Initialize a dictionary to store word frequencies
word_freq = {}

# Open the input file using csv.reader()
with open(filename, 'r') as file:
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Iterate over each word in the row
        for word in row:
            # Convert the word to lowercase to handle case-insensitive comparison
            word = word.lower()

            # Update the word frequency in the dictionary
            word_freq[word] = word_freq.get(word, 0) + 1

# Output the words and their frequencies
for word, freq in word_freq.items():
    print(f'{word} {freq}')


