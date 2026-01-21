# Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.
# LUX on parvekkeellinen hytti yläkannella.
# A on ikkunallinen hytti autokannen yläpuolella.
# B on ikkunaton hytti autokannen yläpuolella.
# C on ikkunaton hytti autokannen alapuolella.
# Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

def describe_cabin_class():
    cabin_class = input("Anna laivan hyttiluokka (LUX, A, B, C): ").upper()
    if cabin_class == "LUX":
        print("LUX on parvekkeellinen hytti yläkannella.")
    elif cabin_class == "A":
        print("A on ikkunallinen hytti autokannen yläpuolella.")
    elif cabin_class == "B":
        print("B on ikkunaton hytti autokannen yläpuolella.")
    elif cabin_class == "C":
        print("C on ikkunaton hytti autokannen alapuolella.")
    elif cabin_class == "EXIT":
        cabin_class = ""
        print("Ohjelma lopetettu.")
    else:
        print("Virheellinen hyttiluokka. yritä uudelleen.\nKirjoita EXIT lopettaaksesi.")
        describe_cabin_class()

    
describe_cabin_class()