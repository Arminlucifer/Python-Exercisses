# concession stand program

# dictionary {key:value}

menu = {"pizza": 9.99,
        "popcorn": 3.99,
        "soda": 0.99,
        "chips": 1.99}

cart = []
total = 0

print("------ MENU ------")

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("___________________________")
print("___________________________")
print()


while True:
    order = input("What would you like?(q to quit) ").lower()
    if order == "q":
        break
    elif menu.get(order) is not None:
        cart.append(order)
print("----------YOU ORDER----------")
for order in cart:
    total += menu.get(order)
    print(order, end="-")
print()

print(f"Your total is ${total:.2f}")
