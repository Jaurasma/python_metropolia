#Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

# Save your API key in a .env file as OPEN_WEATHER_API_KEY=your_api_key / Tallenna API-avain .env-tiedostoon muodossa OPEN_WEATHER_API_KEY=your_api_key
import os
import requests
from dotenv import load_dotenv 
load_dotenv()

def fetch_weather_data(city):
    api_key = os.getenv("OPEN_WEATHER_API_KEY")
    if not api_key:
        print("API-avain puuttuu. Tarkista .env-tiedosto.")
        return

    location_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    response = requests.get(location_url)
    if response.status_code == 200:
        data = response.json()
        if not data:
            print("Paikkakuntaa ei löytynyt.")
            return
        lat = data[0]["lat"]
        lon = data[0]["lon"]
    else:
        print("Paikkakunnan sijaintitietojen hakeminen epäonnistui.")
        return
    
    
    better_weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=fi"
    response = requests.get(better_weather_url)
    if response.status_code == 200:
        data = response.json()
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]

        print(f"Säätila: {description}")
        print(f"Lämpötila: {temperature:.1f} °C")
    else:
        print("Säätietojen hakeminen epäonnistui.")
        print("Tarkista paikkakunnan nimi ja API-avain.")


if __name__ == "__main__":
    city = input("Anna paikkakunnan nimi: ")
    fetch_weather_data(city)
