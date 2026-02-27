import time


def add_loading(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            print("Please Wait...")
            time.sleep(1)
        return func(*args, **kwargs)
    return wrapper


class User:
    def __init__(self, username, email):
        self._username = username
        self._email = email

    def get_details(self):
        print(f"Username: {self._username}")
        print(f"Email Address: {self._email}")


class PremiumUser(User):
    def __init__(self, username, email, expiry_date):
        super().__init__(username, email)
        self._expiry_date = expiry_date
        self.active = True

    def get_details(self):
        super().get_details()
        if self._expiry_date > 0:
            print(f"Premium Days Remaining: {self._expiry_date}")
        else:
            print("Account Expired!")

    @add_loading
    def renew(self):
        self._expiry_date += 30
        print(f"Done! New Expiry: {self._expiry_date} days.")


user1 = PremiumUser("ArminLucifer", "awrminlucifer@gmail.com", 60)
user2 = User("Armin2nd", "arminlucifer@gmail.com")


user2.get_details()
print()
user1.get_details()
user1.renew()
