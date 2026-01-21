# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

def check_hemoglobin():
    while True:
        gender = input("Anna biologinen sukupuolesi (mies/nainen): ").strip().lower()
        if gender in ("mies", "nainen"):
            break
        print("Virheellinen syöte. Yritä uudelleen.")
    while True:
        try:
            hemoglobin = float(input("Anna hemoglobiiniarvosi (g/l) (liukuluku):"))
        except ValueError:
            print("Virheellinen hemoglobiiniarvo. Yritä uudelleen.")
            continue
        if hemoglobin < 0:
            print("Virheellinen hemoglobiiniarvo. Yritä uudelleen.")
            continue
        break
    if gender ==  "nainen":
        if hemoglobin < 117:
            print("Hemoglobiiniarvosi on alhainen.")
        elif 117 <= hemoglobin <= 175:
            print("Hemoglobiiniarvosi on normaali.")
        else:
            print("Hemoglobiiniarvosi on korkea.")
    elif gender == "mies":
        if hemoglobin < 134:
            print("Hemoglobiiniarvosi on alhainen.")
        elif 134 <= hemoglobin <= 195:
            print("Hemoglobiiniarvosi on normaali.")
        else:
            print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Virheellinen syöte. Yritä uudelleen.")

check_hemoglobin()
