# Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.
def calculate_numbers():
    num1 = int(input("Anna ensimmäinen kokonaisluku: "))
    num2 = int(input("Anna toinen kokonaisluku: "))
    num3 = int(input("Anna kolmas kokonaisluku: "))

    summa = num1 + num2 + num3
    tulo = num1 * num2 * num3
    keskiarvo = summa / 3

    print(f"Lukujen summa on: {summa}")
    print(f"Lukujen tulo on: {tulo}")
    print(f"Lukujen keskiarvo on: {keskiarvo}")

calculate_numbers()
