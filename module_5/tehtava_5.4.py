# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen. Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

def city_names():
    cities = []

    for i in range(5):
        city = input(f"Anna kaupungin {i + 1} nimi: ")
        cities.append(city)

    print("Syötetyt kaupungit:")
    for city in cities:
        print(city)

def main():
    city_names()

if __name__ == "__main__":
    main()