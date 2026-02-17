# Number Guessing game

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print(f"Guess the number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess > highest_num or guess < lowest_num:
            print("Out of range")
            print(f"Guess the number between {lowest_num} and {highest_num}")
        elif guess > answer:
            print("Too High! Try again")
        elif guess < answer:
            print("Too low! Try again")
        else:
            print("CORRECT!")
            print(f"The number of guesses = {guesses}")
            is_running = False
    else:
        print("The guess is not valid")
        print(f"Guess the number between {lowest_num} and {highest_num}")
