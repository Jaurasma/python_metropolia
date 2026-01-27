

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

    def kulje(self, tunnit):
        self.kuljettu_matka += self.tämänhetkinen_nopeus * tunnit

    def tulosta_tiedot(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus} km/h")
        print(f"Tämänhetkinen nopeus: {self.tämänhetkinen_nopeus} km/h")
        print(f"Kuljettu matka: {self.kuljettu_matka} km")

def main():
    auto = Auto("ABC-123", 142)
    auto.kiihdytä(50)
    auto.kulje(2)
    auto.tulosta_tiedot()
    return

if __name__ == "__main__":
    main()