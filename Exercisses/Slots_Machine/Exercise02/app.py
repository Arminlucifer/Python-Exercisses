import slot_row
import show_row
import payout


def main():
    balance = 100
    print("S L O T S M A C H I N E")
    print("=======================")
    print("🍒|🍉|🔔|🌟")

    while balance > 0:
        print(f"Your current balance: ${balance}")
        bet = input("Please enter your bet: $")
        if bet.isdigit():
            match (balance, bet):
                case (bal, b) if bal < int(b):
                    print(
                        f"The BET Cannot be greater than your balance (${balance})")
                    continue
                case (_, b) if int(b) <= 0:
                    print("The minimum amount of bet is $1")
                    continue
        else:
            print("Please Enter a valid number")
            continue
        bet = int(bet)
        balance -= bet

        row = slot_row.roww()

        show_row.print_row(row)

        balance += payout.payout(row, bet)

        print(f"Your Balance: ${balance}")

        if balance == 0:
            print("Sorry, you,ve lost all of your money!")
            break

        again = input("Do You Want To Play-Again(Y/N)? ").upper()

        match again:
            case "Y":
                continue
            case "N":
                break

    print("Hope to see you again!!")


if __name__ == "__main__":
    main()
