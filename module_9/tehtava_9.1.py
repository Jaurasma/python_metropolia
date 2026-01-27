# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
# Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0
        
def main():
    auto = Auto("ABC-123", 142)
    print(f"Rekisteritunnus: {auto.rekisteritunnus}")
    print(f"Huippunopeus: {auto.huippunopeus} km/h")
    print(f"Tämänhetkinen nopeus: {auto.tämänhetkinen_nopeus} km/h")
    print(f"Kuljettu matka: {auto.kuljettu_matka} km")
    return

if __name__ == "__main__":
    main()