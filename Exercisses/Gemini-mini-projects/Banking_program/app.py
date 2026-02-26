import time


class Account:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def show_balance(self):
        print(f"Your Balance: {self.__balance}$")

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Current Balance: {self.__balance}$")
        return self.__balance

    def withdraw(self, amount):
        if self.__balance < amount:
            print(f"You don't have {amount}$ in your bank account")
            return self.__balance
        else:
            self.__balance -= amount
            print(f"Current Balance: {self.__balance}$")
            return self.__balance


class SavingAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate
        self.last_interest_time = 0

    def apply_interest(self):
        current_time = time.time()
        if current_time - self.last_interest_time >= 60:
            interest = self.balance * self.interest_rate

            print(f"Adding interest: {interest}$")
            self.deposit(interest)
            self.last_interest_time = current_time
            print("Interest applied successfully!")
        else:
            remaining = 60 - (current_time - self.last_interest_time)
            print(f"Chill bro! You have to wait {remaining} more seconds")


running = True

my_account = SavingAccount(100, 0.05)

while running:
    print("********Welcome!********")
    print()
    print("What Would You Like To Do?")
    print()
    print("1.Check balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")
    print("Add interest")
    user = input(
        "Enter a number: (1/2/3/4/5) ")

    if user.isdigit():
        match user:
            case "1":
                my_account.show_balance
            case "2":
                deposit_running = True
                while deposit_running:
                    amount = input("Alright, HOW MUCH? (b)ack $").lower()
                    match amount:
                        case "b":
                            print("Bruh make your decission")
                            for i in range(3):
                                print("loading...")
                                time.sleep(1)
                            deposit_running = False
                            break
                        case a if a.isdigit():
                            amount = float(amount)
                            my_account.deposit(amount)
                            print("Done")
                            deposit_running = False
                            break
                        case _:
                            print(
                                f"Bro are you KIDDING? YOU Can't deposit '{amount}' in your shitty bank account")
                            continue

            case "3":
                withdraw_running = True
                while withdraw_running:
                    my_account.show_balance
                    amount = input("Alright, HOW MUCH? (b)ack $").lower()
                    match amount:
                        case "b":
                            print("Bruh make your decission")
                            for i in range(3):
                                print("loading...")
                                time.sleep(1)
                            withdraw_running = False
                            break
                        case a if a.isdigit():
                            amount = float(amount)
                            my_account.withdraw(amount)
                            print("Done")
                            withdraw_running = False
                            break
                        case _:
                            print(
                                f"Bro are you KIDDING? YOU Can't withdraw '{amount}' in your shitty bank account")
                            continue

            case "4":
                print("Thanks god you are finally leaving me alone")
                running = False
                break

            case "5":
                my_account.apply_interest()
    else:
        print("I SAID NUMBER IDIOT")
        for i in range(3):
            print("please wait...")
            time.sleep(1)
            continue

print("Have a shitty day < 3")
