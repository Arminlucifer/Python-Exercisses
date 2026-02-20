import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
# print(f"Chars: {chars}")
# print()
key = chars.copy()
random.shuffle(key)
# print(f"keys: {key}")

# ENCRYPT
message = input("Enter a message you want to Encrypt: ")
encrypted_message = ""

for letter in message:
    index = chars.index(letter)
    encrypted_message += key[index]

print(f"encrypted_message: {encrypted_message}")

# DECRYPT
message = input("Enter a message you want to Decrypt: ")

decrypted_message = ""

for letter in encrypted_message:
    index = key.index(letter)
    decrypted_message += chars[index]

print(f"Decrypted Message: {decrypted_message}")
