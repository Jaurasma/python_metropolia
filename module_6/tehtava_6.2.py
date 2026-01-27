# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def roll_super_dice(dice_size):
     return(random.randint(1, dice_size))

def main():
    dice_size = int(input("Anna arpakuution sivujen lukumäärä (kokonaisluku, vähintään 1): "))
    while True:
        result = roll_super_dice(dice_size)
        print(f"Arvottu silmäluku: {result}")
        if result == dice_size:
            print(dice_size, "tuli! Ohjelma lopetetaan.")
            break
    return()  

if __name__ == "__main__":
    main()