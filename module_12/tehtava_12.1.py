# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle. Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti.

import requests as requests

def hae_chuck_norris_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    
    if response.status_code == 200:
        vitsi_data = response.json()
        vitsi = vitsi_data.get("value", "Vitsiä ei löytynyt.")
        print(vitsi)
    else:
        print("Vitsin hakeminen epäonnistui.")

def main():
    hae_chuck_norris_vitsi()

if __name__ == "__main__":
    main()