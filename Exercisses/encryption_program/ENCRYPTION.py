import string
import random

characters = " " + string.ascii_letters + string.digits + string.punctuation
characters = list(characters)
keys = characters.copy()

random.shuffle(keys)
# Encrypt
message = input("Enter a message you want to Encrypy: ")
Encrypted = ""

for letter in message:
    index = characters.index(letter)
    Encrypted += keys[index]

print(f"Your Message = {message}")
print(f"Encrypted Message = {Encrypted}")

#  decrypt

Encrypted = input("Enter a message you want to decrypt: ")
Decryption = ""

for letter in Encrypted:
    index = keys.index(letter)
    Decryption += characters[index]

print(f"Your Message = {Decryption}")
