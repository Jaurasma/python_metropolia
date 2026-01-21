# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan. Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.
base = float(input("Anna suorakulmion kanta: "))
height = float(input("Anna suorakulmion korkeus: "))

perimeter = 2 * (base + height)
area = base * height

print(f"Suorakulmion piiri on: {perimeter}")
print(f"Suorakulmion pinta-ala on: {area}")