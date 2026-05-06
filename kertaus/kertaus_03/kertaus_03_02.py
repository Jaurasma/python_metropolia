sanakirja = {
    "Petteri" : ["Petteri", 1, "Matematiikka"],
    "Sanna" : ["Sanna", 2, "Kuvaamataito"],
    "Mikko" : ["Mikko", 3, "Historia"]
}
#• Hae ja tulosta yhden oppilaan vuosiluokka sekä toisen oppilaan lempiaine.
print(f"Petterin vuosiluokka: {sanakirja['Petteri'][1]}, Sannan lempiaine: {sanakirja['Sanna'][2]}")
#• Muokkaa sanakirjaa vaihtamalla yhden oppilaan lempiaine.
sanakirja["Petteri"][2] = "Fysiikka"
#• Lisää uusi oppilas sanakirjaan.
sanakirja["Liisa"] = ["Liisa", 4, "Kemia"]
#• Poista yksi olemassa oleva oppilas sanakirjasta.
del sanakirja["Sanna"]
#• Tulosta päivitetty sanakirja.
print(sanakirja)