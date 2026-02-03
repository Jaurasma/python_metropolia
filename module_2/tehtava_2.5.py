#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.

def convert_mass():
    leiviskat = float(input("Anna leiviskät: "))
    naulat = float(input("Anna naulat: "))
    luodit = float(input("Anna luodit: "))
    total_grams = (leiviskat * 20 * 32 * 13.3) + (naulat * 32 * 13.3) + (luodit * 13.3)
    kilograms = int(total_grams // 1000)
    grams = total_grams % 1000
    print(f"Massa nykymittojen mukaan: {kilograms} kilogrammaa ja {grams:.2f} grammaa.")

def main():
    convert_mass()

if __name__ == "__main__":
    main()