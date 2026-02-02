# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), 
# metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.


import time
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")


class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin if alin <= ylin else ylin
        self.ylin = ylin if alin <= ylin else alin
        self.kerros = self.alin

    def nayta(self):
        clear()
        for k in range(self.ylin, self.alin - 1, -1):
            if k == self.kerros:
                print(f"| [ HISSI ] | kerros {k}")
            else:
                print(f"|           | kerros {k}")
        time.sleep(0.4)

    def kerros_ylös(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            self.nayta()

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            self.nayta()

    def siirry_kerrokseen(self, tavoite):
        if tavoite < self.alin:
            tavoite = self.alin
        elif tavoite > self.ylin:
            tavoite = self.ylin
        while self.kerros < tavoite:
            self.kerros_ylös()
        while self.kerros > tavoite:
            self.kerros_alas()

def main():
    lowest_floor = int(input("Anna alin kerros: "))
    highest_floor = int(input("Anna ylin kerros: "))
    hissi = Hissi(lowest_floor, highest_floor)
    hissi.nayta()
    kohde = int(input("Mihin kerrokseen haluat mennä ({}, {})? ".format(lowest_floor, highest_floor)))
    hissi.siirry_kerrokseen(kohde)
    input("Paina Enter palataksesi alimpaan kerrokseen...")
    hissi.siirry_kerrokseen(hissi.alin)
    input("Paina Enter lopettaaksesi...")
    return

if __name__ == "__main__":
    main()
