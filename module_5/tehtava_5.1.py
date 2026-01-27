# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random

def roll_dice():
    num_dice = int(input("Anna arpakuutioiden lukumäärä (kokonaisluku): "))
    total_sum = 0
    i = 0

    for i in range(num_dice):
        roll = random.randint(1, 6)
        print (f"Arpakuution {i + 1} silmäluku: {roll}")
        i += 1
        total_sum += roll

    print(f"Arpakuutioiden silmälukujen summa on: {total_sum}")

roll_dice()