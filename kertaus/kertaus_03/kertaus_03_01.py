sanakirja = {
    "John": ["John", 30, "Engineer"],
    "Emily": ["Emily", 25, "Artist"],
    "Anna": ["Anna", 22, "Student"]
}

print(f"Johnin nimi: {sanakirja['John'][0]}, ikä: {sanakirja['John'][1]}")
print(f"Emilyn ammatti: {sanakirja['Emily'][2]}")
sanakirja["Anna"][2] = "Teacher"
sanakirja["James"] = ["James", 28, "Writer"]
sanakirja["Sophia"] = ["Sophia", 35, "Doctor"]
del sanakirja["Emily"]
print(sanakirja)