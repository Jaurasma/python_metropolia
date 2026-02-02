# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.hissit = []
        for _ in range(hissien_lkm):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissiä(self, hissi_numero, kohde_kerros):
        if 0 <= hissi_numero < len(self.hissit):
            self.hissit[hissi_numero].siirry_kerrokseen(kohde_kerros)
        else:
            print("Virhe: Hissin numero ei ole kelvollinen.")

    def palohälytys(self):
        print("Palohälytys! Kaikki hissit palaavat pohjakerrokseen.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(hissi.alin)

class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin if alin <= ylin else ylin
        self.ylin = ylin if alin <= ylin else alin
        self.kerros = self.alin

    def kerros_ylös(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            print(f"Hissi on nyt kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.kerros}")

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
    number_of_elevators = int(input("Anna hissien lukumäärä: "))
    talo = Talo(lowest_floor, highest_floor, number_of_elevators)

    while True:
        elevator_number = int(input(f"Valitse hissi (0 - {number_of_elevators - 1}, -1 lopettaa, -2 palohälytys): "))
        if elevator_number == -1:
            break
        if elevator_number == -2:
            talo.palohälytys()
            input("Paina Enter jatkaaksesi...")
            continue
        target_floor = int(input(f"Mihin kerrokseen haluat mennä ({lowest_floor} - {highest_floor})? "))
        talo.aja_hissiä(elevator_number, target_floor)
        input("Paina Enter jatkaaksesi...")
    return

if __name__ == "__main__":
    main()
