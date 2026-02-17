# Shipping address program

def shipping(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "num" in kwargs:
        print(f"{kwargs.get('street')}, PostCode:{kwargs.get('post_num')}")
        print(f"apartment number:{kwargs.get('apt')}, num:{kwargs.get('num')}")
    elif "post_num" in kwargs:
        print(f"{kwargs.get('street')}, PostCode:{kwargs.get('post_num')}")
        print(
            f"apartment number:{kwargs.get('apt')}, POBOX:{kwargs.get('pobox')}")

    else:

        print(f"apartment number:{kwargs.get('apt')}")


shipping("Mr.", "Armin", "Jahangiri",
         street="Keyhan",
         # post_num="456456",
         # num="6",
         apt="4",
         pobox="#AZA77"
         )
