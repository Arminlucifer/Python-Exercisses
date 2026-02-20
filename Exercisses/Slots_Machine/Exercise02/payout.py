
def payout(row, bet):
    match (row):
        case r if r[0] == r[1] == r[2]:
            match (row, bet):
                case (r, _) if r[0] == "🍒":
                    bet = bet * 5
                case (r, _) if r[0] == "🍉":
                    bet = bet * 7
                case (r, _) if r[0] == "🔔":
                    bet = bet * 10
                case (r, _) if r[0] == "🌟":
                    bet = bet * 20
            print(f"YOU WON! ${bet}")
            return bet

        case _:
            print("You've lost the round")
            return 0
