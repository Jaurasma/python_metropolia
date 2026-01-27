# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def dice_roll():
    return(random.randint(1, 6))

def main():
    while True:
        result = dice_roll()
        print(f"Arvottu silmäluku: {result}")
        if result == 6:
            print("Kuusi tuli! Ohjelma lopetetaan.")
            break
    return()  
        
if __name__ == "__main__":
    main()
