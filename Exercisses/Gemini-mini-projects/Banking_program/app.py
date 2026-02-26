import time


class Account:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def show_balance(self):
        print(f"Your Balance: {self.__balance}$")

    def deposit(self, amount):
        self.__balance + amount
        print(f"Current Balance: {self.__balance}$")
        return self.__balance

    def withdraw(self, amount):
        if self.__balance < amount:
            print(f"You don't have {amount}$ in your bank account")
        else:
            self.__balance - amount
            print(f"Current Balance: {self.__balance}$")
            return self.__balance


running = True

my_account = Account(100)

while running:
    print("********Welcome!********")
    print()
    print("What Would You Like To Do?")
    print()
    print("1.Check balance")
    print("2.Deposit Money")
    print("3. Withdraw Money")
    print("4.Exit")
    user = input(
        "Enter a number: (1/2/3/4) ")

    try:
        match user:
            case "1":
                my_account.show_balance
           # case 2:
                # amount = input("Alright, HOW MUCH? ")
          #  case 3:
          #      pass
          #  case 4:
          #      pass
    except ValueError:
        print("I SAID NUMBER IDIOT")
        for i in range(3):
            print("please wait...")
            time.sleep(1)
            continue

    except Exception:
        print("Something Went Wrong")
        for i in range(3):
            print("please wait...")
            time.sleep(1)
            continue


print("Have a nice day!")
