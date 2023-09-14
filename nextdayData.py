import requests
from googletrans import Translator

r = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q=aktobe&appid=9fc9557dd4062bcaf7e732e10ee2e879&units=metric")

dataNextDay = r.json()


dttime = dataNextDay['list'][8]['dt_txt']

windDirectionNextDay = ''
windSpeedDescriptionNextDay = ''
windSpeedNextDay = dataNextDay['list'][8]['wind']['speed']
windDirectionDescriptionNexDay = dataNextDay['list'][8]['wind']['deg']

tempNextDay = dataNextDay['list'][8]['main']['temp']
temp_likeNextDay = dataNextDay['list'][8]['main']['feels_like']
humidityNextDay = dataNextDay['list'][8]['main']['humidity']
descriptionNextDay = dataNextDay['list'][8]['weather'][0]['description']

if windSpeedNextDay <= 0.2:
    windSpeedDescriptionNextDay = 'Штиль'
elif windSpeedNextDay <= 1.5:
    windSpeedDescriptionNextDay = 'Тихий'
elif windSpeedNextDay <= 3.3:
    windSpeedDescriptionNextDay = 'Легкий'
elif windSpeedNextDay <= 5.4:
    windSpeedDescriptionNextDay = 'Слабый'
elif windSpeedNextDay <= 7.9:
    windSpeedDescriptionNextDay = 'Умеренный'
elif windSpeedNextDay <= 10.7:
    windSpeedDescriptionNextDay = 'Умеренный+'
elif windSpeedNextDay <= 13.8:
    windSpeedDescriptionNextDay = 'Сильный'
elif windSpeedNextDay <= 17.1:
    windSpeedDescriptionNextDay = 'Сильный+'
elif windSpeedNextDay <= 20.7:
    windSpeedDescriptionNextDay = 'Очень сильный, ушып кетесин'
else:
    windSpeedDescriptionNextDay = 'Шторм!'

if windDirectionDescriptionNexDay <= 22:
    windDirectionNextDay = 'Север'
elif windDirectionDescriptionNexDay <= 67:
    windDirectionNextDay = 'Северо-Восток'
elif windDirectionDescriptionNexDay <= 112:
    windDirectionNextDay = 'Восток'
elif windDirectionDescriptionNexDay <= 157:
    windDirectionNextDay = 'Юго-Восток'
elif windDirectionDescriptionNexDay <= 202:
    windDirectionNextDay = 'Юг'
elif windDirectionDescriptionNexDay <= 247:
    windDirectionNextDay = 'Юго-Запад'
elif windDirectionDescriptionNexDay <= 292:
    windDirectionNextDay = 'Запад'
elif windDirectionDescriptionNexDay <= 337:
    windDirectionNextDay = 'Северо-Запад'
elif windDirectionDescriptionNexDay <= 360:
    windDirectionNextDay = 'Север'

translator = Translator()
translationNextDay = translator.translate(descriptionNextDay, src='en', dest='ru')
