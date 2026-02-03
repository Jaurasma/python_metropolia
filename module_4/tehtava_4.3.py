# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

def find_min_max():
    numbers = []
    while True:
        user_input = input("Anna luku (tyhjä lopettaa): ")
        if user_input == "":
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Virheellinen syöte. Yritä uudelleen.")
    if numbers:
        print(f"Pienin luku: {min(numbers)}")
        print(f"Suurin luku: {max(numbers)}")
    else:
        print("Ei syötettyjä lukuja.")

def main():
    find_min_max()

if __name__ == "__main__":
    main()