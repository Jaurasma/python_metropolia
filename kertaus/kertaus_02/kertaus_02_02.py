list = []
while True:
    number = int(input("Uusi arvo: "))
    if number == 0:
        print("Hei hei!")
        break
    list.append(number)
    print("Lista nyt:", list)
    print("Lista järjestyksessä:", sorted(list))
