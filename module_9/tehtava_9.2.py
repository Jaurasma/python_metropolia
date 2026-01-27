# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0
        
    def kiihdytä(self, nopeuden_muutos):
        self.tämänhetkinen_nopeus += nopeuden_muutos
        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        if self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

def main():
    auto = Auto("ABC-123", 142)
    print(f"Rekisteritunnus: {auto.rekisteritunnus}")
    print(f"Huippunopeus: {auto.huippunopeus} km/h")
    print(f"Tämänhetkinen nopeus: {auto.tämänhetkinen_nopeus} km/h")
    print(f"Kuljettu matka: {auto.kuljettu_matka} km\n")
    auto.kiihdytä(30)
    auto.kiihdytä(70)
    auto.kiihdytä(50)
    print(f"Nopeus kiihdytysten jälkeen: {auto.tämänhetkinen_nopeus} km/h")
    auto.kiihdytä(-200)
    print(f"Nopeus hätäjarrutuksen jälkeen: {auto.tämänhetkinen_nopeus} km/h")
    return

if __name__ == "__main__":
    main()