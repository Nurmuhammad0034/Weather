import requests
from bs4 import BeautifulSoup

weather_url = "https://www.gismeteo.ru/weather-tashkent-5331/10-days/"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

full_page = requests.get(weather_url, headers=headers)


soup = BeautifulSoup(full_page.content, 'html.parser')


natija = soup.findAll('span', {'class': "unit unit_temperature_c" })

bugun = natija[1].text
ertaga = natija[3].text
indinga = natija[5].text

print(f"Bugungi ob havo {bugun}C, ertaga {ertaga}C, indinga {indinga}C,")
