class Vehicle:
    def __init__(self, brand, speed):
        self._brand = brand
        self._speed = speed

    def move(self):
        print(f"{self._brand} is moving")


class Car(Vehicle):

    def __init__(self, brand, speed, initial_fuel):
        super().__init__(brand, speed)
        self.fuel_level = initial_fuel

    def move(self):
        if self.fuel_level > 10:
            self.fuel_level -= 5
            print(f"{self._brand} is crusing! Fuel: {self.fuel_level}")
        else:
            print("Out of fuel! Refuel needed")


class Airplane(Vehicle):

    def __init__(self, brand, speed, max_height):
        super().__init__(brand, speed)
        self.max_height = max_height

    def fly(self):
        print(f"{self._brand} can fly up to {self.max_height}m")


my_garage = [Car("Benz", 200, 150),
             Airplane("Air-Buss", 700, 2000)]


for vehicle in my_garage:
    vehicle.move()
    if isinstance(vehicle, Airplane):
        vehicle.fly()
