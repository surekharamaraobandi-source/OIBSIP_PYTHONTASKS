import random
import string

print("===== RANDOM PASSWORD GENERATOR =====")

# User input
length = int(input("Enter password length: "))

print("\nChoose character types:")
print("1. Letters")
print("2. Numbers")
print("3. Symbols")

use_letters = input("Include letters? (y/n): ").lower()
use_numbers = input("Include numbers? (y/n): ").lower()
use_symbols = input("Include symbols? (y/n): ").lower()

characters = ""

# Add character sets
if use_letters == 'y':
    characters += string.ascii_letters

if use_numbers == 'y':
    characters += string.digits

if use_symbols == 'y':
    characters += string.punctuation

# Validation
if len(characters) == 0:
    print("Please select at least one character type.")
else:
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:")
    print(password)