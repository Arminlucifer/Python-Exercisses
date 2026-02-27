def mian():
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
            self._cart = []

        def order(self):
            if self._order_name in menu:
                self._cart.append(self._order_name)
                print(f"{self._order_name} has been added to your cart")
                print(f"{menu[self._order_name]}$")

            else:
                print(f"{self._order_name} is not available in menu")

        def calculate_total(self):
            pass

    account1 = Account("Armin", "4th Keyhan, num 6", 6)


# account1.ShowMyAccount()


if __name__ == "__main__":
    main()
