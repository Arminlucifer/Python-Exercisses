weekdays = ["Saturday", "Sunday", "Monday",
            "Tuesday", "Wednesday", "Thursday", "Friday"]

day = input("Enter a day of a week: ").strip().capitalize()


def is_weeekend(day):
    match day:
        case "Friday" | "Thursday":
            return "It's Weekend!!"
        case _:
            return "It's NOT Weekend"


if day in weekdays:
    print(is_weeekend(day))
else:
    print("The input was not Valid!")
