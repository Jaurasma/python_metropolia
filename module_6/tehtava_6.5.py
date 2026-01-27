# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def remove_odd_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

def main():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_list = remove_odd_numbers(test_list)
    print(f"Alkuperäinen lista: {test_list}")
    print(f"Karsittu lista (vain parilliset luvut): {filtered_list}")
    return

if __name__ == "__main__":
    main()