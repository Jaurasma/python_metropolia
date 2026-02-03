# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

def inches_to_cm():
    while True:
        inches = float(input("Anna pituus tuumina (liukuluku) (negatiivinen lopettaa): "))
        if inches < 0:
            print("Ohjelma lopetettu.")
            break
        cm = inches * 2.54
        print(f"{inches} tuumaa on {cm:.2f} senttimetriä.")
def main():
    inches_to_cm()

if __name__ == "__main__":
    main()