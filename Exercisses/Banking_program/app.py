import deposit
import check_balance
import withdraw


def main():
    balance = 0
    running = True

    while running:
        print("=====BANKING PROGRAM======")
        print()
        print("What Would You Like To Do?")
        print()
        print("1.Check balance")
        print("2.Withdraw Money")
        print("3.Deposit Money")
        print("4.Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        match choice:
            case "1":
                check_balance.check_balance(balance)
            case "2":
                balance -= withdraw.withdraw(balance)
            case "3":
                balance + deposit.deposit(balance)
            case "4":
                running = False
            case _:
                print("That is not a valid input")
    print("That you! Have a nice day")


if __name__ == "__main__":
    main()
