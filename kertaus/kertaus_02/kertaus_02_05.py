def suurin_arvo(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

if __name__ == "__main__":
    luku1 = float(input("Anna ensimmäinen luku: "))
    luku2 = float(input("Anna toinen luku: "))
    luku3 = float(input("Anna kolmas luku: "))
    print(f"Suurin arvo on: {suurin_arvo(luku1, luku2, luku3)}")