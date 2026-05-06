#Kirjoita ohjelma, joka kysyy tuntipalkan, tehdyt tunnit ja viikonpäivän. Ohjelma tulostaa
#päiväpalkan, joka on tuntipalkka kerrottuna tehdyillä tunneilla, paitsi sunnuntaina,
#jolloin tuntipalkka on kaksinkertainen.
#Esimerkkituloste:
#Tuntipalkka: 8.5
#Tehdyt tunnit: 3
#Viikonpäivä: maanantai
#Päiväpalkka: 25.5 euroa

tuntipalkka = float(input("Tuntipalkka: "))
tehdyt_tunnit = float(input("Tehdyt tunnit: "))
viikonpaiva_wild = str(input("Viikonpäivä: "))
viikonpaiva = viikonpaiva_wild.lower()
kerroin = 1

if viikonpaiva == "sunnuntai":
    kerroin = 2

paivapalkka = (tuntipalkka * tehdyt_tunnit) * kerroin
print (f"Päiväpalkka: {paivapalkka:.2f} euroa")