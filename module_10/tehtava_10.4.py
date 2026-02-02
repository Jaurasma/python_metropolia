#Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

#tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
#tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
#kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
#Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi. Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.


import random

class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        otsikko = f"{'Sija':>4}  {'Rekisteri':<10}  {'Matka (km)':>12}  {'Nopeus':>8}  {'Huippu':>8}"
        viiva = "-" * len(otsikko)
        rivit = [otsikko, viiva]
        tulokset = sorted(self.autot, key=lambda a: a.kuljettu_matka, reverse=True)
        for sija, auto in enumerate(tulokset, start=1):
            rivit.append(
                f"{sija:>4}  {auto.rekisteritunnus:<10}  "
                f"{auto.kuljettu_matka:>12.1f}  {auto.tämänhetkinen_nopeus:>8.0f}  "
                f"{auto.huippunopeus:>8.0f}"
            )
        print("\n".join(rivit))

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_km:
                return True
        return False

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

    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    tunnit = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunnit += 1
        if tunnit % 10 == 0:
            print(f"\nTilanne {tunnit} tunnin jälkeen:")
            kilpailu.tulosta_tilanne()

    print(f"\nKilpailu on ohi {tunnit} tunnin jälkeen! Lopullinen tilanne:")
    kilpailu.tulosta_tilanne()

if __name__ == "__main__":
    main()