#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).

def login_system():
    correct_username = "python"
    correct_password = "rules"
    attempts = 0
    max_attempts = 5
    while attempts < max_attempts:
        username = input("Anna käyttäjätunnus: ")
        password = input("Anna salasana: ")
        if username == correct_username and password == correct_password:
            print("Tervetuloa!")
            return
        else:
            attempts += 1
            print(f"Väärä käyttäjätunnus tai salasana. Yritä uudelleen. ({max_attempts - attempts} yritystä jäljellä)")
    print("Pääsy evätty.")

login_system()