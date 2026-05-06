def kuusi(size):
    print("Tämä on kuusi!")
    for i in range(size):
        print(" " * (size - i - 1) + "*" * (2 * i + 1))
    print(" " * (size - 1) + "*")

if __name__ == "__main__":
    koko = int(input("Anna kuusen koko: "))
    kuusi(koko)
