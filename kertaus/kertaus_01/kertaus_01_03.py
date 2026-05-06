from math import sqrt

def sqrt_loop():
    while True:
        num = int(input("Anna numero: "))
        if num == 0:
            print("Exiting...")
            break
        elif num < 0:
            print("Virheellinen luku")
        else:
            print(f"{sqrt(num):.1f}")

if __name__ == "__main__":
    sqrt_loop()