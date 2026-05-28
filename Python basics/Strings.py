# 1. Creation and Basic Formatting
text = "Python Programming"
name = "Alex"

# Using f-strings (available in Python 3.6+) to insert variables
greeting = f"Hello, {name}! Welcome to {text}."
print(greeting)

# 2. Case Manipulation
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")

# 3. Concatenation and Repetition
new_string = text + " is Fun!" # Joining strings with '+'
echo = "Python! " * 3         # Repeating strings with '*'
print(new_string)
print(echo)

# 4. Slicing and Indexing
# Slicing uses [start:stop:step]
first_word = text[0:6]        # Gets 'Python' (index 0 to 5)
last_char = text[-1]          # Gets 'g' using negative indexing
reversed_text = text[::-1]    # Reverses the string
print(f"First word: {first_word}, Last char: {last_char}")
print(f"Reversed: {reversed_text}")

# 5. Searching and Checking
sentence = "Learning Python is very easy."
print(f"Starts with 'Learning': {sentence.startswith('Learning')}")
print(f"Does it contain 'Python'?: {'Python' in sentence}")
print(f"Position of 'easy': {sentence.find('easy')}")

# 6. Cleaning and Replacing
messy_string = "   Too many spaces   "
clean_string = messy_string.strip()  # Removes leading/trailing whitespace
updated_text = text.replace("Python", "Java") # Swaps substrings
print(f"Cleaned: '{clean_string}'")
print(f"Replaced: {updated_text}")

# 7. Counting and Measuring
print(f"Length of '{text}': {len(text)}")
print(f"Count of 'n' in '{text}': {text.count('n')}")
