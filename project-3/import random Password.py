import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ""
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        return "Error: No character set selected!"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# --- Main Program ---
print("🔐 Random Password Generator")
length = int(input("Enter password length: "))

use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

result = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)

print("\nGenerated Password:", result)
