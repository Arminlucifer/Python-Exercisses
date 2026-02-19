# Python Slot Machine Program
import spin_row
import print_row
import paycheck


def main():
    balance = 100
    print(" * * * * * * * *")
    print(" S  L  O  T  S")
    print(" M A C H I N E")
    print("🍒|🍉|🔔|🌟")

    while balance > 0:
        print(f"Your Total Balance ${balance}")
        bet = input("Enter your bet: $")
        match (bet, balance):
            case (b, _) if not b.isdigit():
                print("Enter a valid number!")
                continue

            case (b, bal) if int(b) > bal:
                print("Your Bet Cannot Be Greater Than Your Balance")

            case (b, _) if int(b) == 0:
                print("The minimum amount of bet is 1$")
                continue

        bet = int(bet)
        balance -= bet

        row = spin_row.spin_row()

        import time
        for _ in range(0, 3):
            print("Spinning...")
            time.sleep(1)

        print_row.print_row(row)

        payout = paycheck.paycheck(row, bet)
        if payout > 0:
            print(f"YOU WON ${payout}")

        else:
            print("You've Lost the round")

        if balance == 0:
            print("Sorry you've lost all of your money")
            break

        balance += payout
        print(f"Your Current balance is ${balance}")

        again = input("Do you want to play again? (Y/N): ").upper()
        if again == "Y":
            continue
        else:
            break


print("Hope to see you again!")

if __name__ == "__main__":
    main()
