# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def main():
    test_list = [3, 5, 7, 2, 8]
    result = sum_of_list(test_list)
    print(f"Listan {test_list} lukujen summa on: {result}")
    return

if __name__ == "__main__":
    main()

