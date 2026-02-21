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
    print("".join(hint))


def display_answer(answer):
    print("".join(answer))


def main():
    running = True
    answer = random.choice(words)
    wrong_guesses = 0
    guessed_letters = set()
    hint = ["_"] * len(answer)
    while running:
        display_art(wrong_guesses)
        print()
        display_hint(hint)
        print()
        guess = input("Enter a letter: ").lower()
        if guess == answer:
            print("YOU WON!")
            running = False
        else:
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid input")
                continue
            if guess in answer:
                for i in range(len(answer)):
                    if answer[i] == guess:
                        hint[i] = guess
            else:
                wrong_guesses += 1
        if not "_" in hint:
            display_answer(answer)
            print("YOU WON!")
            running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            print("You've LOST")
            print("The answer was: ", end=" ")
            display_answer(answer)
            running = False


if __name__ == "__main__":
    main()
