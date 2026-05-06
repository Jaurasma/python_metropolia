def sanalaskin(lista):
    long_words = 0
    for i in range(len(lista)):
        if len(lista[i]) > 5:
            long_words += 1
    return long_words

if __name__ == "__main__":
    lista = ["kissa", "koira", "hevonen", "lintu", "krokotiili"]
    print(f"Listassa on {sanalaskin(lista)} sanaa, jotka ovat pidempiä kuin 5 kirjainta.")