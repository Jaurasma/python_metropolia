name = input("Kerro nimesi: ")
if name != "Matti":
    keitto = input("Montako keittoannosta? ")
    hinta = int(keitto) * 5.90
    print(f"Kokonaishinta on {hinta:.2f}")
print("Seuraava, kiitos!")