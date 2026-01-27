# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

def print_season():
    seasons = ("talvi", "kevät", "kesä", "syksy")
    
    month = int(input("Anna kuukauden numero (1-12): "))
    
    if 1 <= month <= 12:
        season = seasons[month % 12 // 3]
        print(f"Kuukausi {month} kuuluu vuodenaikaan: {season}.")
    else:
        print("Virhe: Anna kuukausi numerona välillä 1-12.")

def main():
    print_season() 
    return

if __name__ == "__main__":
    main()