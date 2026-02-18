def withdraw(balance):
    amount = float(input("How much money would you like to withdraw: $"))
    if amount > balance:
        print("Amount Cannot be greater than your balance")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount
