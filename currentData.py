import requests
from googletrans import Translator

r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Aqtobe&appid=9fc9557dd4062bcaf7e732e10ee2e879&units=metric")

dataCurrent = r.json()

windDirection = ''
windSpeedDescription = ''
windspeedCurrent = dataCurrent['wind']['speed']
windDirectionDescription = dataCurrent['wind']['deg']
tempCurrent = dataCurrent['main']['temp']
temp_likeCurrent = dataCurrent['main']['feels_like']
humidityCurrent = dataCurrent['main']['humidity']
description = dataCurrent['weather'][0]['description']


if windspeedCurrent <= 0.2:
    windSpeedDescription = 'Штиль'
elif windspeedCurrent <= 1.5:
    windSpeedDescription = 'Тихий'
elif windspeedCurrent <= 3.3:
    windSpeedDescription= 'Легкий'
elif windspeedCurrent <= 5.4:
    windSpeedDescription= 'Слабый'
elif windspeedCurrent <= 7.9:
    windSpeedDescription = 'Умеренный'
elif windspeedCurrent <= 10.7:
    windSpeedDescription= 'Умеренный+'
elif windspeedCurrent <= 13.8:
    windSpeedDescription = 'Сильный'
elif windspeedCurrent <= 17.1:
    windSpeedDescription = 'Сильный+'
elif windspeedCurrent <= 20.7:
    windSpeedDescription = 'Очень сильный, ушып кетесин'
else:
    windSpeedDescription = 'Шторм!'

if windDirectionDescription <= 22:
    windDirection = 'Север'
elif windDirectionDescription <= 67:
    windDirection = 'Северо-Восток'
elif windDirectionDescription <= 112:
    windDirection = 'Восток'
elif windDirectionDescription <= 157:
    windDirection = 'Юго-Восток'
elif windDirectionDescription <= 202:
    windDirection = 'Юг'
elif windDirectionDescription <= 247:
    windDirection = 'Юго-Запад'
elif windDirectionDescription <= 292:
    windDirection = 'Запад'
elif windDirectionDescription <= 337:
    windDirection = 'Северо-Запад'
elif windDirectionDescription <= 360:
    windDirection = 'Север'

translator = Translator()
translationCurrent = translator.translate(description, src='en', dest='ru')