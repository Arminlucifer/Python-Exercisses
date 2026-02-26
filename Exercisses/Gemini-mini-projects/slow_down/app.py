import time


def slow_down(func):
    def wrapper(*args, **kwargs):
        print("Please wait while we are making your donut...")
        time.sleep(2)
        return func(*args, **kwargs)
    return wrapper


@slow_down
def donut(flavor):
    print(f"Your {flavor} Donut is ready!")


donut("Chocolate")
