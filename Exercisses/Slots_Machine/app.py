# Python Slot Machine Program
import spin_row
import print_row
import paycheck


def main():
    balance = 100
    symbols = ["🍒", "🍉", "🔔", "🌟"]
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
        spin_row.spin_row()


if __name__ == "__main__":
    main()
