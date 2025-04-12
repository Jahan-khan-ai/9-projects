import random
import string

# Define the characters to use in the password
letters = string.ascii_letters  # a-z and A-Z
digits = string.digits          # 0-9
special_chars = string.punctuation  # !@#$%^&* etc.

# Combine all possible characters
all_chars = letters + digits + special_chars

# Ask user for the password length
length = int(input("Enter the desired password length: "))

# Generate the password
password = ''.join(random.choice(all_chars) for _ in range(length))

# Print the generated password
print("Your generated password is:", password)