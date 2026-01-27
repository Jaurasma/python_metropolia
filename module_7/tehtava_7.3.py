# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. 
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
# Löydät koodeja helposti selaimen avulla.)

AIRPORTS = {}

def populate_sample_data():
    sample_data = {
        "EFHK": "Helsinki-Vantaa Lentoasema",
        "KJFK": "John F. Kennedy International Airport",
        "EGLL": "London Heathrow Airport",
        "LFPG": "Charles de Gaulle Airport",
        "RJTT": "Tokyo Haneda Airport"
    }
    AIRPORTS.update(sample_data)

def add_airport():
    icao_code = input("Anna lentoaseman ICAO-koodi: ").upper()
    name = input("Anna lentoaseman nimi: ")
    AIRPORTS[icao_code] = name
    print(f"Lentoasema {name} lisätty koodilla {icao_code}.")

def search_airport():
    icao_code = input("Anna haettavan lentoaseman ICAO-koodi: ").upper()
    if icao_code in AIRPORTS:
        print(f"Lentoaseman nimi: {AIRPORTS[icao_code]}")
    else:
        print("Lentoasemaa ei löydy.")

def switch(choise):
    return {
        '1': add_airport,
        '2': search_airport,
        '3': exit
    }.get(choise, lambda: print("Virheellinen valinta, yritä uudelleen."))()

def main():
    # populate_sample_data()  # Ota kommentti pois testataksesi esimerkkitiedoilla
    while True:
        print("\nValitse toiminto:")
        print("1. Syötä uusi lentoasema")
        print("2. Hae lentoaseman tiedot")
        print("3. Lopeta")
        choice = input("Valintasi (1/2/3): ")
        switch(choice)

if __name__ == "__main__":
    main()