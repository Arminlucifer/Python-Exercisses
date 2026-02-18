import random


OPTIONS = ("rock", "paper", "scissors")


WINS_AGAINST = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}


running = True
player_points = 0
computer_points = 0
tie_rounds = 0
total_rounds = 1


def calc_round(player, computer):

    match (player, computer):
        case (p, c) if p == c:
            return "Tie"
        case (p, c) if WINS_AGAINST[p] == c:
            return "Player"
        case _:
            return "Computer"


def final_winner(player_points, computer_points):

    match (player_points, computer_points):
        case (p, c) if p > c:
            return "Player"
        case (p, c) if c > p:
            return "Computer"
        case _:
            return "Tie"


while running:
    computer_choice = random.choice(OPTIONS)
    print(f"\n--- Round {total_rounds} ---")

    player_choice = input(
        "Enter your choice (rock / paper / scissors) or (q)uit: "
    ).strip().lower()

    while player_choice not in OPTIONS:
        if player_choice == "q":
            running = False
            break
        else:
            print("❌ Invalid input.")
            player_choice = input(
                "Enter your choice (rock / paper / scissors) or (q)uit: "
            ).strip().lower()

    if not running:
        break

    print(f"You chose     : {player_choice}")
    print(f"Computer chose: {computer_choice}")

    result = calc_round(player_choice, computer_choice)
    match result:
        case "Player":
            player_points += 1
            print("✅ You WON the round!")
        case "Computer":
            computer_points += 1
            print("💻 Computer won the round!")
        case "Tie":
            tie_rounds += 1
            print("🤝 It's a tie!")

    total_rounds += 1


print("\n===== FINAL STATS =====")

game_result = final_winner(player_points, computer_points)

match game_result:
    case "Player":
        print("🏆 You WON the game!!")
    case "Computer":
        print("💀 Computer won the game!")
    case "Tie":
        print("⚖️ The game ended in a tie!")

print(f"Your points     : {player_points}")
print(f"Computer points : {computer_points}")
print(f"Tie rounds      : {tie_rounds}")
print(f"Total rounds    : {total_rounds - 1}")
