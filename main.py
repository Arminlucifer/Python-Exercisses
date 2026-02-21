# -----------------------THIS IS A TUTORIAL FROM BRO CODE-------------------------
# import math
# print("Hello World")
# print("Its's Really Good")
# --------------------------------------------------------------------------------
# Variable = A container for a value (string, integer, float, booleaan)
# --------------------------------------------------------------------------------
# Strings
# first_name = "Armin"
# food = "pizza"

# print(first_name)
#
# print(f"Hello {first_name}")
# print(f"you like {food}")
# ---------------------------------------------------------------------------------
# Integers

# age = 21
# num_of_students = 30
# print(f"You are {age} years old")
# print(f"Your class has {num_of_students} of students")
# ----------------------------------------------------------------------------------
# Float

# price = 10.99
# distance = 5.5
# print(f"The price is ${price}")
# print(f"You ran {distance}km")
# --------------------------------------------------------------------------------
## Boolean#

## is_student = False#

# print(f"Are you a student? {is_student}")

# if is_student:
# print("You are a student")
# else:
# print("You are NOT a student")
# --------------------------------------------------------------------------------
# Typecasting = The process of converting a variable from one data type to another
#                            str(), int(), float(), bool()

# name = "Armin Jahangiri"
# age = 21
# gpa = 3.2
# is_student = True

# print(type(age))

# gpa = int(gpa)

# print(gpa)
# -----------------------------------------------------------------------------------
# input() = A function that prompts the user to enter data
#                   Returns the enterted data as a string

# name = input("What is your name? :")

# print(f"hello {name}!")

# age = int(input("How old are you? :"))
# age = int(age)
# age = age + 1
# print("HAPPY BIRTHDAY")
# print(f"You are {age} years old")

# ------------------Exercise 1 Rectangle Area Calc-------------------------------

# length = float(input("Enter Length"))
# width = float(input("Enter Width"))
# Area = length*width
# print(f"Area is {Area}!")


# ------------------Exercise 2 Shopping cart program-----------------------------

# item = input("What Item Would You Like To Buy?: ")
# price = float(input("What Is the price?: "))
# quantity = int(input("How many would you like to buy?: "))

# Total = price * quantity

# print(f"You are gonna buy {quantity} {item} and the total price is {Total}Toman ")


# -------------------------------------math shit--------------------------------

# friends = 5

# friends += 1
# friends -= 1
# friends *= 3
# friends /= 2
# friends **= 2
# remainder = friends % 2
# print(remainder)
# print(friends)

# x = 3.14
# y = -4
# z = 5

# result = round(x)
# result = abs(y)
# result = pow(y, z)
# result = max(y, z, x)

# result = min(y, z, x)

# print(result)


# print(math.pi)
# print(math.e)
# x = 9.5
# result = math.sqrt(x)
# result = math.ceil(x)   # round the num to up
# result = math.floor(x)   # round the num to down

# print(result)


# -----------------------------Excersice 4-----------------------------------


# radius = float(input("enter the radius:  "))
# print(f"result= {round(math.pi * 2 * radius, 2)}cm")


# -------------------Excersice 5 AREA OF A CIRCLE---------------------------------


# radius = float(input("Input the radius of the circle: "))
# print(f"The Area Of Circle Is {round(pow(radius,  2) * math.pi, 2)}")

# ------------------------Excersice 6 وتر-------------------------------------


# a = float(input("Enter A: "))
# b = float(input("Enter B: "))
# print(f"The Vatar is {round(math.sqrt(pow(a, 2) + pow(b, 2)), 2)}")


# ---------------IF STATEMENT = do sm code only IF some condition is True---------
#               Else Do smth else

# age = int(input("Enter Your Age: "))
# if age >= 100:
#    print("YOU OLD ASS")
# elif age >= 18:
#    print("You are eligible")
# elif age <= 0:
#    print("You haven't been born yet")
# else:
#    print("You are NOT eligible")

# response = input("would u ike some food? (Y/N): ")
# if response == "Y":
#    print("have some food")
# else:
#    print("IDGAF")


# ----------------------------Python Calculator----------------------------------

# = float(input(("Enter The First Number: ")))
# = float(input(("Enter The Second number: ")))
# = input("What You Wanna Do With Them? (+ - / *): ")
# f c == "+":
#   print(a+b)
# lif c == "-":
#   print(a-b)
# lif c == "*":
#   print(a * b)
# lif c == "/":
#   print(round((a/b), 2))

# --------------------------Python weight converter-----------------------------

# weight = float(input("Enter Your Weight: "))
# unit = input("K or L?: ")
#
# if unit == "K":
#    print(f"Your weight is {weight * 2.205}Lbs.")
# elif unit == "L":
#    print(f"Your weight is {weight / 2.205}Kgs.")
# else:
#    print(f"{unit} is not a valid unit")


# -----------------------temperature conversion program--------------------------

# unit = input("Is this temperature in Celsius or Farenheit (C/F): ")
# temperature = float(input("Please enter the temperature: "))
#
# if unit == "C":
#    print(f"The temperature is {round((temperature * 9) / 5 + 32, 1)}F")
# elif unit == "F":
#    print(f"The temperature is {round((temperature - 32) * 5 / 9, 1)}C")
# else:
#    print(f"{Unit} was not valid")

# --------------------------------------------------------------------------------
# Logical operators = evaluate multipie conditions (or, and, not)
#                   or= at least one condition must be True
#                   and= both condition must be True
#                   not=  inverts the condition (not False, not True)


# temp = 20
# is_sunny = False

# if temp >= 28 and is_sunny:
#    print("It is HOT outside 🔥")
#    print("It is SUNNY ☀️")
# elif temp > 0 and is_sunny:
#    print("It is COLD outside 🥶")
#    print("It is SUNNY ☀️")
# elif 28 > temp > 0 and is_sunny:
#    print("It is WARM outside 😊")
#    print("It is SUNNY 🌞")
# elif temp >= 28 and not is_sunny:
#    print("It is HOT outside 🔥")
#    print("It is CLOUDY ☁️")
# elif temp > 0 and not is_sunny:
#    print("It is COLD outside 🥶")
#    print("It is CLOUDY ☁️")
# elif 28 > t and not is_sunny:
#    print("It is WARM outside 😊")
#    print("It is CLOUDY ☁️")

# ---------------------------------------------------------------------------------
# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                   print or assign of two values based on a conditoin
#                   X if condition else Y

# user_role = "geust"

# print("Full Acccess" if user_role == "admin" else "Limited Access")

# ---------------------------------------------------------------------------------
# name = input("Enter your full name: ")
# phone_number = input("Enter Your Phone number: ")
# result = len(name)
# result = name.find("J")
# result = name.rfind("i")
# result = name.rfind("q")
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
# result = phone_number.replace("-", " ")
# print(result)

# print(help(str))

# ------------------------Validate user input exercise-------------------------
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must contain digits

# user_name = input("Enter your username: ")
#
# un = user_name.find(" ")
# un2 = len(user_name)
# un3 = user_name.isalpha()
#
# if un == -1 and un2 <= 12 and un3:
#    print("Username is valid")
# else:
#    print("Username is NOT valid ")


# -----indexing = accessing elements of a sequence using [] (indexing operator)----
#               [Start : end: step]

# credit_number = "1234-5678-9012-3456"

# print(credit_number[0])
# print(credit_number[0:])
# print(credit_number[:4])
# print(credit_number[-1])
# print(credit_number[:-1])
# print(credit_number[3:7])
# print(credit_number[::3])


# ----Excersice : Create a program that returns last 4 digits of a credit number----

# cn = "1234-5678-8745-3647"
# print(cn[-4:])

# Excersice : Create a program that reverse the credit number

# cn = "1234-5678-8745-3647"

# print(cn[::-1])


# ---------format specifiers = {value:flags} format a value based on what---------
#                   flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03= allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign leftmost position
# :  = insert a space before positive numbers
# :, = comma seprator

# price1 = 3000.14159
# price2 = -9870.65
# price3 = 1200.34

# print(f"price 1 is {price1:.1f}")
# print(f"price 2 is {price2:.1f}")
# print(f"price 3 is {price3:.1f}")

# print(f"price 1 is {price1:10}")
# print(f"price 2 is {price2:10}")
# print(f"price 3 is {price3:10}")

# print(f"price 1 is {price1:010}")
# print(f"price 2 is {price2:010}")
# print(f"price 3 is {price3:010}")

# print(f"price 1 is {price1:<10}")
# print(f"price 2 is {price2:<10}")
# print(f"price 3 is {price3:<10}")

# print(f"price 1 is {price1:>10}")
# print(f"price 2 is {price2:>10}")
# print(f"price 3 is {price3:>10}")


# print(f"price 1 is {price1:^10}")
# print(f"price 2 is {price2:^10}")
# print(f"price 3 is {price3:^10}")

# print(f"price 2 is {price2:+10}")
# print(f"price 3 is {price3:+10}")
# print(f"price 1 is {price1:+10}")

# print(f"price 1 is {price1:+,.2f}")
# print(f"price 2 is {price2:+,.2f}")
# print(f"price 3 is {price3:,.2f}")


# ---------while loop = execute some code WHILE some condition remains true--------

# name = input("Enter Your Name: ")
#
# while name == "":
#    print("You've not entered your name")
#    name = input("Enter Your Name: ")
# print(f"Hello {name}")

# age = int(input("Please Enter Your Age: "))
#
# while age < 0:
#    print("Age cannot be negative: ")
#    age = int(input("Please Enter Your Age: "))
# print(f"Your age is {age}")


# food = input("Enter a food you like (q to quit): ")
#
# while not food == "q":
#    print(f"You like {food}")
#    food = input("Enter another food you like (q to quit): ")
# print("bye")

# num = int(input("Enter a number between 1 and 10: "))

# while num < 1 or num > 10:
#    print(f"{num} was not in options")
#    num = int(input("Enter a number between 1 and 10: "))

# print(f"Your number is {num}")


# --------------- python compound interest calculator----------------------------

# principal = float(input("Enter your principal: "))
#
# while principal <= 0:
#    print("Principal cannot be less than or equal to 0")
#    principal = float(input("Enter your principal: "))
#
# rate = float(input("Enter your rate: "))
#
# while rate <= 0:
#    print("rate cannot be less than or equal to 0")
#    rate = float(input("Enter your rate: "))
#
#
# time = int(input("Enter time in years: "))
#
# while time <= 0:
#    print("Time cannot be less than or equal to 0")
#    time = int(input("Enter time in years: "))
#
# total = principal * pow((1+rate/100), time)
# print(f"The total is {total:,.2f}$")


# principal = float(input("Enter your principal: "))
#
# while principal < 0:
#    print("Principal cannot be less than  0")
#    principal = float(input("Enter your principal: "))
#
# rate = float(input("Enter your rate: "))
#
# while rate < 0:
#    print("rate cannot be 0")
#    rate = float(input("Enter your rate: "))
#
#
# time = int(input("Enter time in years: "))
#
# while time < 0:
#    print("Time cannot be less than 0")
#    time = int(input("Enter time in years: "))
#
# total = principal * pow((1+rate/100), time)
# print(f"The total is {total:,.2f}$")


# while True:
#    principal = float(input("Enter your principal: "))
#    if principal < 0:
#        print("Principal cannot be less than  0")
#    else:
#        break
#
#
# while True:
#    time = int(input("Enter your time in years: "))
#    if time < 0:
#        print("time cannot be less than  0")
#    else:
#        break
#
# while True:
#    rate = float(input("Enter the rate: "))
#    if rate < 0:
#        print("rate cannot be less than  0")
#    else:
#        break
#
# total = principal * pow((1+rate/100), time)
# print(f"The total is {total:,.2f}$")


# ----------for loops = execute a block of code a fixed number of times.----------
#      you can iterate over a range, string, sequence, etc.

# for x in range(10, 0, -1): # for x in reversed(range(1,11)):
#   print(x)

# credit_card = "2345-1234-7894-2589"
#
# for x in credit_card:
#    print(x)

# for x in range(1, 21):
#    if x == 13:
#        continue   #break = age break bezani faghat ta 12 mishmore
#    else:
#        print(x)


# ---------------EXERCISE : Count-down timer python program :--------------------
# import time
#
# my_time = int(input("Enter your time in seconds: "))
#
# for x in range(my_time, 0, -1):
#    seconds = x % 60
#    minutes = int(x/60) % 60
#    hours = int(x/3600)
#    print(f"{hours:02}:{minutes:02}:{seconds:02}")
#    time.sleep(1)
#
# print("WAKE UP")


# -----------nested loop = A loop whitin another loop (outer, inner)-------------
#               outer loop:
#                  inner loop:


# for i in range(0, 3):
#    for x in range(1, 10):
#        print(x, end="")
#    print()


# ------------------create a rectangle using nested loops based on input-----------
# rows = int(input("Enter the # of rows: "))
# columns = int(input("Enter the # of columns: "))
# symbol = input("Enter a symbol")
#
# for i in range(rows):
#    for x in range(columns):
#        print(symbol, end="")
#    print()

# ------------------------------------COLLECTIONS-----------------------------------------
# collection = single "variable" used to store multiple values
#   List = [] ordered and changable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. No Duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER


#   -----------List = [] ordered and changable. Duplicates OK--------------------

# fruits = ["apple", "orange", "banana", "cucumber"]
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

# print(fruits[1::2])
# for fruit in fruits:
#    print(fruit)

# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("banana")
# fruits.insert(0, "pineapple")
# fruits.sort()  # bar hasb alphabet
# fruits.reverse()  # bar hasb on chizi k khodemon nvshim (mishe ino ba sort mix kard)
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("banana"))
# print(fruits)


#   --------Set = {} unordered and immutable, but Add/Remove OK. Noo Duplicates------


# fruits = {"apple", "orange", "banana", "cucumber", "cucumber"}

# fruits.add("pineapple")
# fruits.remove("pineapple")
# fruits.pop()  # remove first element but its random

# print(fruits)


#   -------Tuple = () ordered and unchangeable. Duplicates OK. FASTER-------------

# fruits = ("apple", "orange", "banana", "cucumber", "cucumber", "apple", "orange")
#
# print(len(fruits))
# print("apple" in fruits)
# print(fruits.index("orange"))
# print(fruits.count("apple"))
# print(fruits)


# --------------------SHOPPING CART PROGRAM USING COLLECTIONS---------------------
# foods = []
# prices = []
# total = 0
#
# while True:
#    food = input("What foods would you like? (q to quit): ")
#    if food.lower() == "q":
#        break
#    else:
#        price = float(input("What is the price of the food? $"))
#        foods.append(food)
#        prices.append(price)
# print("------your cart-----")
# for food in foods:
#    print(food, end="-")
#
# for price in prices:
#    total += price
# print()
# print(f"Your total is ${total}")


# ----------------------------------- 2D LIST---------------------------------------

# fruits = ["apple", "orange", "banana", "coconut"]
# vegtables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "meat", "turkey"]

# groceries = [fruits, vegtables, meats]

# YOU CAN DO THIS INSTEAD (BELOW)
# groceries = (["apple", "orange", "banana", "coconut"],  # mishe az collection haye mokhtalef estefade kard
#             ["celery", "carrots", "potatoes"],
#            ["chicken", "meat", "turkey"])

# print(groceries[2][2])
# groceries[0].append("test")

# for collection in groceries:
#    for item in collection:
#        print(item, end=" ")
#    print()
# -------------------------------DICTIONARY-----------------------------------
# dictionary = a collection of {key:value} pairs
#          ordered and changeable. NO duplicates

# capitals = {"USA": "Washington D.C",
#            "Iran": "Tehran",
#            "Russia": "Moscow",
#            "India": "New Dehli"}

# print(capitals.get("USA"))

# if capitals.get("USA"):9
#    print("That capital exists")
# else:
#    print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.pop("Russia")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()

# print(keys)
# print(capitals)

# values = capitals.values()
# print(values)

# items = capitals.items()
# print(items)

# for key, value in capitals.items():
#    print(f"{key}, {value}")


# ---------------------------------------------------------------------------------------------
# random num

# import random

# help(random)

# print(random)


# low = 1
# high = 100
# number = random.randint(1, 6)
# number = random.randint(low, high)
# number = random.random()

# options = ("rock", "paper", "scissors")
# option = random.choice(options)
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# random.shuffle(cards)
# print(cards)
# print(option)
# print(number)


# -------------------- FUNCTION = A BLOCK OF REUSABLE CODE-------------
#         place () after the function name to invokke it

# def happy_bday(name, age):
#    print(f"HAPPY BIRTHDAY {name}")
#    print(f"You are now {age} years old!")
#
#
# happy_bday("Armin", 22)
# happy_bday("ali", 18)
# happy_bday("hossein", 40)

# ----------RETURN = STATEMENT USED TO END FUNCTION-----------------
#     and send a result back to caller

# def create_name(first, last):
#    first = first.capitalize()
#    last = last.capitalize()
#    return first + " " + last
#
#
# full_name = create_name("armin", "jahangiri")
#
# print(full_name)

# -------------------------------- Default arguments = A default value for certain parameters
# --------------------------------- default is used when that argument is omitted
#                                  make your functions more flexible, reduces # of arguments
#                                  1. positional, 2.DEFAULT, 3.keyword, 4.arbitrary

# 2.DEFAULT
# def net_price(list_price, discount=0, tax=0.05):
#    return list_price * (1-discount) * (1 + tax)
#
#
# print(net_price(500))
# print(net_price(500))
# print(net_price(500, .1, 0))
# -----------------------------------------------------------------------------
# 3.KEYWORD = an argument preceded by an identifier
#           helps with readability
#           order of arguments does't matter
#           1. positional, 2.DEFAULT, 3.keyword, 4.arbitrary

# def greet(greeting, title, first, last):
#    print(f"{greeting} {title}{first} {last}")
#
#
# greet("Hello", first="Armin", last="Jahangiri", title="Mr.")
# another example of keyword arguments
# print("1", "2", "3", "4", "5", sep=" XYZ ")
# -----------------------------------------------------------------------------
# 4 ARBITRARY:

# *args     = allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple keyword-arguments
#           *   unpacking operator

# def display_name(*args):
#    for arg in args:
#        print(arg, end=" ")
#
#
# display_name("MR", "Armin", "Jahangiri", "III")
# print()

# KWARGS:


# def get_address(**kwargs):
#    for key, value in kwargs.items():
#        print(f"{key}:{value}")
#
#
# get_address(street="Keyhan",
#            num="6",
#            city="Tehran",
#            zip="123")

# ------------------------------------------------------------------------------

# ITERABLES = an object / collection that can return its elements one at a time,
#               allowing it to be iterated over in a loop

# -------------------------------------------------------------------------------

# MEMBERSHIP OPERATORS = used to test whether a value or variable is found in a sequence
#           (string, list, tuple, set, dictionary)
#           1. in
#           2. not in

# grades = {"Sandy": "A",
#          "Spongebob": "C",
#          "Patrick": "F",
#          "squidward": "B"}
#
# student = input("Enter the name of a student: ")
#
# if student in grades:
#    print(f"{student}'s grade is {grades[student]}")  # = {gardes.get(student)}
# else:
#    print(f"{student} was not found")

# --------------------------------------------------------------------------------
# LIST COMPREHENSION = A concise way to create lists in Python
#           Compact and easier to read than tradiotional loops
#      FORMULA:[expression for value in iterable if condition]

# triples = [x * 3 for x in range(0, 11)]
# print(triples)
#
#
# fruits = ["apple", "banana", "cucumber", "coconut"]
# fruits_first = [char[0] for char in fruits]
# print(fruits_first)

# numbers = [1, 2, -4, 5, -7, -10]
# CONDITION:
# positive_numbers = [num for num in numbers if num > 0]
# print(positive_numbers)

# grades = {"Armin": 18,
#          "Ali": 8,
#          "Mamad": 12,
#          "Mona": 14,
#          "Reza": 2}
#
# passed_students = [grade for grade in grades if grades[grade] > 10 ]
# print(passed_students)

# Match-case statement(switch): An alternative to using mani=y "elif" statements
#           Excute some code if a value matches a 'case'
#           Benefits: cleaner and syntax is more readable

# ==========================================================================
# module = a file containing code you want to include in your program
#           use 'import' to include a module (built-in or your own)
#           useful to break up a large program reusable seprate files

# print(help("modules"))
# print(help("math"))

# import math = import math as m #behesh nickname midim
# print(m.pi)
# from math import pi #behtare az in ziad estfde nashe (name shit)
# print(pi)
# #==========================================================================

# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# ============================================================================
# if__name__ == __main__: (This script can be imported OR run standalone)
#                       Functions and classes in this module can be reused
#                       without the main block of code executing

# ex. library = Import library for funtionality
#       When running library directly, display a help page

# Good practice (code is modular,
#              helps readability,
#              leaves no global variables,
#              avoid unintended execution)
# ====================================================================================================================
# OBJECT ORIENTED:
# object = AA "Bundle" of relayed attributes (variables) and methods (functions)
#                   Ex phone, cup, book
#                   You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

# class car:
#    def __init__(self, model, year, color, maxspeed, price):
#        self.model = model
#        self.year = year
#        self.color = color
#        self.maxspeed = maxspeed
#        self.price = price
#
#    def drive(self):
#        print(f"You drive a {self.color} {self.model} ")
#
#    def describe(self):
#        print(f"It's a {self.color} {self.model}, which is for year {self.year} and the maximum speed of it is {self.maxspeed}KM/h and the price is currently ${self.price}")
#
#
# car1 = car("Supra", 2026, "Black", 356, 20000)
# car2 = car("Z4", 2018, "Red", 280, 17000)
#
# car1.describe()
# car2.describe()
#
# car1.drive()
# car2.drive()
# ============================================================================================================================

# Class variables = shared among all instances of a class
#           Defined outside the constructor
#           Allow you to share data among all objects created from that class

#class Student:
#    class_year = 2025
#    num_students = 0
#
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#        Student.num_students += 1
#
#
#student1 = Student("Armin", 21)
#student2 = Student("Erfan", 22)
#student3 = Student("Sponge-Bob", 28)
#student4 = Student("Patrick", 35)
#
#print(student1.name)
#print(student1.class_year)
#print(student2.name)
#print(student2.class_year)
