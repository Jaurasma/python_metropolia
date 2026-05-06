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
                    print(f"Tulos: {num1 + num2}")
                elif laskuttoimitus == '-':
                    print(f"Tulos: {num1 - num2}")
                elif laskuttoimitus == '*':
                    print(f"Tulos: {num1 * num2}")
                elif laskuttoimitus == '/':
                    if num2 != 0:
                        print(f"Tulos: {num1 / num2}")
                    else:
                        print("Virhe: Nollalla ei voi jakaa.")
            except ValueError:
                print("Virhe: Syötä kelvolliset numerot.")
        else:
            print("Virhe: Valitse kelvollinen laskutoimitus.")

if __name__ == "__main__":
    laskin()