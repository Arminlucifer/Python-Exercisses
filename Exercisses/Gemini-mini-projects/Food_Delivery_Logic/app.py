import time


def add_loading(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            print("Loading...")
            time.sleep(1)
        return func(*args, **kwargs)
    return wrapper


@add_loading
def show_menu(menu):
    print("****Menu****")
    for key, value in menu.items():
        print(f"{key:10} {value:.2f}$")


menu = {
    "Pizza": 19.99,
    "Burger": 10.99,
    "Fries": 5.99,
    "Coke": 2.99
}


class Account:
    def __init__(self, customer_name, customer_address, customer_rate):
        self._customer_name = customer_name
        self._customer_address = customer_address
        self._customer_rate = customer_rate

    def ShowMyAccount(self):
        print("------Your Account Details-------")
        print(f"Your name: {self._customer_name}")
        print(f"Your Address: {self._customer_address}")
        print(f"Your Rate: {self._customer_rate}/10")


class Order(Account):
    def __init__(self, customer_name, customer_address, customer_rate, order_name):
        super().__init__(customer_name, customer_address, customer_rate)
        self._order_name = order_name
        self.cart = []

    def add_order(self, order_name):
        self.cart.append(order_name)
        print(f"{order_name} has been added to your cart")
        print(f"{menu[order_name]}$")

    def show_bill(self):
        print("------YOUR ORDER-----")
        total = 0
        if not self.cart:
            print("Your Cart is empty")
        else:
            for item in self.cart:
                print(f"-{item:10}: {menu[item]}")
                total += menu[item]
            print("-" * 20)
            print(f"Your total: {total:.2f}$")


current_user = Order("Armin", "4th Keyhan", 6, "")

# account1.ShowMyAccount()

running = True

while running:
    print(f"------{current_user._customer_name}, Welcome To Our Resturant------")
    print("1: Order Food")
    print("2: Show My Bill")
    print("3: Check My Account Details")

    user = input("What Would You Like to do?(1/2/3/4) ")
    try:

        match user:
            case "1":
                show_menu(menu)
                order_running = True
                while order_running:
                    order_name = input(
                        "What Would You Like to order?/(Q)uit: ").capitalize()
                    match order_name:
                        case "Q":
                            break
                        case  o if o in menu:
                            current_user.add_order(order_name)
                        case _:
                            print(f"{order_name} is not in menu")
            case "2":
                current_user.show_bill()
                break
            case "3":
                current_user.ShowMyAccount()
    except ValueError:
        print("Your Input was NOT valid")
        continue


print("Have a Great (Shitty) Day")
