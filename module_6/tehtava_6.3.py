# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

def gallons_to_liters(gallons):
    liters = gallons * 3.785
    return liters

def main():
    while True:
        gallons = input("Anna bensiinin määrä gallonoina (negatiivinen luku lopettaa): ")
        try:
            gallons = float(gallons)
        except ValueError:
            print("Virhe: Syötä kelvollinen luku.")
            continue
        if gallons < 0:
            print("Negatiivinen luku syötetty, ohjelma lopetetaan.")
            break
        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallonaa on {liters:.3f} litraa.")
    return

if __name__ == "__main__":
    main()