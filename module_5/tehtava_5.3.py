# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

def is_prime():
    number = int(input("Anna kokonaisluku: "))
    
    if number <= 1:
        print(f"Luku {number} ei ole alkuluku.")
        return

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print(f"Luku {number} ei ole alkuluku.")
            return

    print(f"Luku {number} on alkuluku.")

is_prime()