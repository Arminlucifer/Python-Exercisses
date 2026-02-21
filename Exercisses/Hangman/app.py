import random

words = ("apple", "banana", "grape", "orange", "strawberry")


hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\ ",
                   "   "),

               5: (" o ",
                   "/|\\ ",
                   "/  "),

               6: (" o ",
                   "/|\\ ",
                   "/ \\ ")}


def display_art(wrong_guesses):
    print('__________________')
    for i in hangman_art[wrong_guesses]:
        print(i)
    print('__________________')


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    pass


def main():
    runnig = True
    answer = random.choice(words)
    wrong_guesses = 0
    guessed_letters = set()
    hint = ["_"] * len(answer)
    while runnig:
        display_art(wrong_guesses)
        print()
        display_hint(hint)
        print()
        guess = input("Enter a letter: ").lower()
        


if __name__ == "__main__":
    main()
