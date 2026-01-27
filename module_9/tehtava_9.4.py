# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne.
# Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

import random

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
    autot = []
    for i in range(1, 11):
        huippunopeus = random.randint(100, 200)
        rekisteritunnus = f"ABC-{i}"
        auto = Auto(rekisteritunnus, huippunopeus)
        autot.append(auto)

    racing = True
    while racing:
        for auto in autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)
            if auto.kuljettu_matka >= 10000:
                racing = False

    tulokset = sorted(autot, key=lambda a: a.kuljettu_matka, reverse=True)

    otsikko = f"{'Sija':>4}  {'Rekisteri':<10}  {'Matka (km)':>12}  {'Nopeus':>8}  {'Huippu':>8}"
    viiva = "-" * len(otsikko)
    rivit = [otsikko, viiva]
    for sija, auto in enumerate(tulokset, start=1):
        rivit.append(
            f"{sija:>4}  {auto.rekisteritunnus:<10}  "
            f"{auto.kuljettu_matka:>12.1f}  {auto.tämänhetkinen_nopeus:>8.0f}  "
            f"{auto.huippunopeus:>8.0f}"
        )
    print("\n".join(rivit))

if __name__ == "__main__":
    main()
