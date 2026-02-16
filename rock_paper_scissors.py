# ROCK PAPER SCISSORS PROGRAM

import random

options = ("rock", "paper", "scissors")
computer_score = 0
player_score = 0
player = None
rounds = 1
its_running = True
tie_rounds = 0
print("ROCK/PAPER/SCISORS")

while its_running:
    game = random.choice(options)
    print(f"Its round {rounds}")

    player = input("Enter Your Choice(Rock-Paper-Scissors)/(Q)uit: ").lower()
    while player not in options:
        if player == "q":
            its_running = False
            break
        else:
            print("The input was not accurate")
        player = input(
            "Enter Your Choice(Rock-Paper-Scissors)/(Q)uit: ").lower()
    if its_running == False:
        break

    print(f"You :{player}")
    print(f"Computer :{game}")
    if player == game:
        print("Its a tie!")
        rounds += 1
        tie_rounds += 1
    elif player == "rock" and game == "paper":
        print("Computer won the round")
        rounds += 1
        computer_score += 1
    elif player == "paper" and game == "scissors":
        print("Computer won the round")
        rounds += 1
        computer_score += 1
    elif player == "scissors" and game == "rock":
        print("Computer won the round")
        rounds += 1
        computer_score += 1
    else:
        print("You WON the round!")
        rounds += 1
        player_score += 1


print("------STATS------")
print()
if player_score > computer_score:
    print("YOU WON THE GAME 😎")
    print(
        f"Your score: {player_score} computer_score: {computer_score} Tie Rounds: {tie_rounds}")
    print(f"Total rounds: {rounds - 1}")


elif player_score < computer_score:
    print("Computer won the game 😢")
    print(
        f"Your score: {player_score} computer score: {computer_score} Tie Rounds: {tie_rounds}")
    print(f"Tie rounds: {tie_rounds}")
    print(f"Total rounds: {rounds - 1}")


else:
    print("It was a tie! ☺️")
    print(
        f"Your score: {player_score} computer_score: {computer_score} Tie Rounds: {tie_rounds}")
    print(f"Total rounds: {rounds - 1}")
