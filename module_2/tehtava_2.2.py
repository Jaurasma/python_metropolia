# Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
import math
def radius_area():
    radius = float(input("Anna ympyrän säde: "))
    area = math.pi * radius ** 2
    print(f"Ympyrän pinta-ala on: {area:.2f}")

def main():
    radius_area()

if __name__ == "__main__":
    main()