# Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
def radius_area():
    radius = float(input("Anna ympyrän säde: "))
    area = 3.14159 * radius ** 2
    print(f"Ympyrän pinta-ala on: {area}")

radius_area()