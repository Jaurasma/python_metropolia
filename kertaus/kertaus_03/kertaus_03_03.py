kirjasto = {
    "Linnunradan käsikirja liftareille": {"kirjoittaja": "Douglas Adams","julkaisuvuosi": "1978", "genre": "scifi"},
    "Sinuhe egyptiläinen": {"kirjoittaja": "Mika Waltari", "julkaisuvuosi": "1945", "genre": "historiallinen romaani"},
    "Pieni prinssi": {"kirjoittaja": "Antoine de Saint-Exupéry", "julkaisuvuosi": "1943", "genre": "lastenkirja"},
}

#• Hae ja tulosta yhden kirjan kirjoittaja sekä toisen kirjan genre.
print(f"Linnunradan käsikirja liftareille kirjoittaja: {kirjasto['Linnunradan käsikirja liftareille']['kirjoittaja']}, Pieni prinssi genre: {kirjasto['Pieni prinssi']['genre']}")

#• Muokkaa: vaihda yhden kirjan genre.
kirjasto["Linnunradan käsikirja liftareille"]["genre"] = "komedia"

#• Lisää uusi kirja sanakirjaan.
kirjasto["Pikku toukka paksulainen"] = {"kirjoittaja": "Eric Carle", "julkaisuvuosi": "1969", "genre": "lastenkirja"}

#• Poista yksi olemassa oleva kirja sanakirjasta.
del kirjasto["Sinuhe egyptiläinen"]

#• Tulosta päivitetty sanakirja.
print(kirjasto)