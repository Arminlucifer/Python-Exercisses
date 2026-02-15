#    ----- EXERCISE-----
# CREATE A TWO DIMENSIONAL KEY PAD (PHONE)

key_pad = (("1", "2", "3"),
           ("4", "5", "6"),
           ("7", "8", "9"),
           ("*", "0", "#"))
for collection in key_pad:
    for item in collection:
        print(item, end=" ")
    print()
