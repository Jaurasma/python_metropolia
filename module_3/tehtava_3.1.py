# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

def check_fish_length():
    length = float(input("Anna kuhan pituus senttimetreinä: "))
    if length < 0:
        print("Pituus ei voi olla negatiivinen.")
    elif length < 37:
        print(f"Kuha on alamittainen. Laske kuha takaisin järveen. Puuttuu {37 - length} cm.")
    else:
        print("Hieno saalis!")
def main():
    check_fish_length()

if __name__ == "__main__":
    main()