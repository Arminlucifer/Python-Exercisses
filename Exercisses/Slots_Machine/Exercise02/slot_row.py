import random
symbols = ["🍒", "🍉", "🔔", "🌟"]


def roww():
    return [random.choice(symbols) for _ in range(3)]
