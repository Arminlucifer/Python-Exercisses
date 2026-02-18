def deposit():
    amount = float(input("Enter the amount of money you want to withdraw: $"))
    if amount <= 0:
        print("The Minimum amount of withdraw is 1$")
        return 0
    else:
        return amount
