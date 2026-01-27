# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

def name_collection():
    names = set()

    while True:
        name = input("Syötä nimi (tai paina Enter lopettaaksesi): ")
        if name == "":
            break
        if name in names:
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
            names.add(name)

    print("Syötetyt nimet:")
    for name in names:
        print(name)

def main():
    name_collection()
    return 

if __name__ == "__main__":
    main()
