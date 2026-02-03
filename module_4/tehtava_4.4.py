# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    #print(f"Debug: Arvottu luku on {number_to_guess}")  # Debug-print, remove the comment to see the number
    while True:
        try:
            guess = int(input("Arvaa luku (1-10): "))
            if guess < 1 or guess > 10:
                print("Luku ei ole välillä 1-10. Yritä uudelleen.")
                continue
            if guess < number_to_guess:
                print("Liian pieni arvaus.")
            elif guess > number_to_guess:
                print("Liian suuri arvaus.")
            else:
                print("Oikein!")
                break
        except ValueError:
            print("Virheellinen syöte. Anna kokonaisluku.")

def main():
    guess_the_number()

if __name__ == "__main__":
    main()