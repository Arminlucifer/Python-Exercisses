store = {
    "laptop": 10,
    "mouse": 3,
    "monitor": 7
}


def buy(item):
    if item in store:
        store[item] -= 1
        print(f"One {item} sold. Remaining: {store[item]}")

        if store[item] < 5:
            print(f"Warning! {item} is low on stock")

    else:
        print(f"{item} was not found")


buy("laptop")
buy("mouse")
buy("monitor")
buy("pizza")
