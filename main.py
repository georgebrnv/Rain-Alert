import requests
import smtplib

OWM_Endopoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "{YOUR API from OPENWEATHERMAP.ORG}"

EMAIL = "example.email.com"
PASSWORD = "password123"

connection = smtplib.SMTP("smtp.example.com")
connection.starttls()
connection.login(user=EMAIL, password=PASSWORD)

# Type in your longitude and latitude
parameters = {
    "lon": -96.994171,
    "lat": 33.046341,
    "appid": api_key,
}

response = requests.get(url=OWM_Endopoint, params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]


def bring_an_umbrella(data):
    for weather_cond in data[:4]:
        print(weather_cond["weather"])
        condition_code = weather_cond["weather"][0]["id"]
        if int(condition_code) < 700:
            return True


if bring_an_umbrella(weather_data):
    print("Bring an umbrella!")
    connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject: Rain Alert!\n\nDon't forget your umbrella today!")
else:
    print("It's clear, don't worry about your umbrella!")
    connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject: It's clear today!\n\nDon't worry about your umbrella today!")

