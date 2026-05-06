def sum(a, b):
    return a + b

def difference(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Virhe: Nollalla ei voi jakaa."


def laskin():
    while True:
        laskuttoimitus = input("Valitse laskutoimitus (+, -, *, /) tai 'loppu' lopettaa: ").lower()
        if laskuttoimitus == "loppu":
            print("Lopeetaan...")
            break
        elif laskuttoimitus in ['+', '-', '*', '/']:
            try:
                num1 = float(input("Anna ensimmäinen luku: "))
                num2 = float(input("Anna toinen luku: "))
                if laskuttoimitus == '+':
                    print(f"Tulos: {sum(num1, num2)}")
                elif laskuttoimitus == '-':
                    print(f"Tulos: {difference(num1, num2)}")
                elif laskuttoimitus == '*':
                    print(f"Tulos: {multiply(num1, num2)}")
                elif laskuttoimitus == '/':
                    print(f"Tulos: {divide(num1, num2)}")
            except ValueError:
                print("Virhe: Syötä kelvolliset numerot.")
        else:
            print("Virhe: Valitse kelvollinen laskutoimitus.")

if __name__ == "__main__":
    laskin()