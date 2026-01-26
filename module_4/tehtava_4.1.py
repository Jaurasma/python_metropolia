# Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.
def print_multiples_of_three():
    number = 3
    count = 0
    while number <= 1000:
        count += 1
        line_end = "\n" if count % 10 == 0 else ""
        print(f"{number:4d}", end=line_end)
        number += 3
    if count % 10 != 0:
        print()

print_multiples_of_three()
