# Kirjoita ohjelma, joka kysyy nimesi ja sen jälkeen tervehtii sinua omalla nimelläsi.
def greet_user():
    name = input("Kuka olet? : ")
    if name:
        print(f"Terve, {name}!")

greet_user()