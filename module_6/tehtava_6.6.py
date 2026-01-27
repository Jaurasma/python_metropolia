# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

def pizza_unit_price(diameter_cm, price_eur):
    radius_m = (diameter_cm / 2) / 100  # Muutetaan säde metreiksi
    area_m2 = math.pi * (radius_m ** 2)  # Lasketaan pinta-ala neliömetreinä
    unit_price = price_eur / area_m2  # Lasketaan yksikköhinta euroina per neliömetri
    return unit_price

def main():
    unit_prices = []
    for i in range(2):
        print(f"Pizza {i+1}:")
        diameter = float(input("Anna pizzan halkaisija senttimetreinä: "))
        price = float(input("Anna pizzan hinta euroina: "))
        unit_price = pizza_unit_price(diameter, price)
        unit_prices.append(unit_price)
        print(f"Pizzan {i+1} yksikköhinta: {unit_prices[i]:.2f} €/m²\n")    

    if unit_prices[0] < unit_prices[1]:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif unit_prices[1] < unit_prices[0]:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Molemmilla pizzoilla on sama yksikköhinta.")

if __name__ == "__main__":
    main()