# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

def five_largest_numbers():
    numbers = []

    while True:
        user_input = input("Syötä luku (tai paina Enter lopettaaksesi): ")
        if user_input == "":
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Virhe: Syötä kelvollinen luku.")

    numbers.sort(reverse=True)
    largest_five = numbers[:5]

    print("Viisi suurinta lukua suurimmasta alkaen:")
    for num in largest_five:
        print(num)

def main():
    five_largest_numbers()

if __name__ == "__main__":
    main()