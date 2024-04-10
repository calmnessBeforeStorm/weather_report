import requests, datetime

weather_descriptions = {

    'clear sky': 'без-дождиковое небо☀️',

    'few clouds': 'мини облачки🌤️',



    'scattered clouds': 'разочарованные облачка☁️',

    'broken clouds': 'разочарованные облачка☁️',

    'overcast clouds': 'грустные облачка🌥️',



    'light rain': 'вспотели облачка🌧️',

    'moderate rain': 'всплакнули облачка🌧️',

    'heavy intensity rain': 'нервный срыв облачков🌧️',

    'very heavy rain': 'двойной нервный срыв облачков🌧️',

    'extreme rain': 'нервный срыв с апатией облачков🌧️',

    'freezing rain': 'нервный срыв облачков в антарктиде❄️🌧️',

    'light intensity shower rain': 'плачь со смехом🌦️',

    'shower rain': 'депрешн облачки🌦️',

    'heavy intensity shower rain': 'плачь капризного ребенка🌧️🌧️',

    'ragged shower rain': 'кросс 15 метров и резкий стоп🌦️',



    'light intensity drizzle': 'моросящий дождь малой интенсивности🌧️',

    'drizzle': 'сопли вытекают наружу🌧️',

    'heavy intensity drizzle': 'моросящий дождь сильной интенсивности🌧️',

    'light intensity drizzle rain': 'моросящий дождь небольшой интенсивности🌧️',

    'drizzle rain': 'моросящий дождь🌧️',

    'heavy intensity drizzle rain': 'сильный моросящий дождь🌧️',

    'shower rain and drizzle': 'проливной дождь и морось🌧️',

    'heavy shower rain and drizzle': 'сильный ливень и морось🌧️',

    'shower drizzle': 'ливень моросящий дождь🌧️',



    'thunderstorm': 'гроза🌩',

    'thunderstorm with light rain': 'гроза с небольшим дождем⛈',

    'thunderstorm with rain': 'гроза с дождем⛈',

    'thunderstorm with heavy rain': 'гроза с проливным дождем⛈',

    'light thunderstorm': 'легкая гроза🌩',

    'heavy thunderstorm': 'сильная гроза🌩',

    'ragged thunderstorm': 'рваная гроза🌩',

    'thunderstorm with light drizzle': 'гроза с легким моросящим дождем⛈',

    'thunderstorm with drizzle': 'гроза с моросящим дождем⛈',

    'thunderstorm with heavy drizzle': 'гроза с сильным моросящим дождем⛈',



    'fog': 'облаака парят🌫',

    'mist': 'облака курят🌫',

    'smog': 'токсик облачка курят',

    'haze': 'мгла',

    'sand': 'высокая пыль',

    'dust whirls': 'вихри пыли',

    'dust whirls': 'вулканический пепел',

    'squalls': 'шквальный ветер',

    'tornado': 'торнадо',



    'light snow': 'мороженки падают❄️',

    'snow': 'мороженное❄️',

    'heavy snow': 'ульта мороженных❄️',

    'sleet': 'мороженное на бали❄️',

    'light shower sleet': 'курящие облака на бали с мороженным❄️🌧️',

    'shower sleet': 'ливень с мокрым снегом❄️🌧️',

    'light rain and snow': 'небольшой дождь и снег❄️🌧️',

    'rain and snow': 'дождь и снег❄️🌧️',

    'light shower snow': 'легкий дождь со снегом❄️🌧️',

    'shower sleet': 'интенсивный дождь❄️',

    'heavy shower snow': 'сильный интенсивный дождь❄️🌧'

}

class Weather():
    def __init__(self, current, nextday):
        self.current = current
        self.nextday = nextday

    def get_current_data(self):
        #получаю инфу в текущем моменте
        current = requests.get(self.current)
        data = current.json()

        if data['wind']['speed'] <= 0.2:
            windSpeedDescription = 'Штиль'
        elif data['wind']['speed'] <= 1.5:
            windSpeedDescription = 'Тихий'
        elif data['wind']['speed'] <= 3.3:
            windSpeedDescription = 'Легкий'
        elif data['wind']['speed'] <= 5.4:
            windSpeedDescription = 'Слабый'
        elif data['wind']['speed'] <= 7.9:
            windSpeedDescription = 'Умеренный'
        elif data['wind']['speed'] <= 10.7:
            windSpeedDescription = 'Умеренный+'
        elif data['wind']['speed'] <= 13.8:
            windSpeedDescription = 'Сильный'
        elif data['wind']['speed'] <= 17.1:
            windSpeedDescription = 'Сильный+'
        elif data['wind']['speed'] <= 20.7:
            windSpeedDescription = 'Очень сильный, ушып кетесин'
        else:
            windSpeedDescription = 'Шторм!'

        return {
            'windspeed': data['wind']['speed'],
            'windspeedDescription': windSpeedDescription,
            'temp': data['main']['temp'],
            'temp_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'description': weather_descriptions.get(data['weather'][0]['description'], data['weather'][0]['description'])
        }

    def get_nextDay_data(self):
        nextday = requests.get(self.nextday)
        data = nextday.json()

        currentDateTime = datetime.date.today()

        nextDateTime = currentDateTime + datetime.timedelta(days=1)

        morningKey = None
        afternoonKey = None
        eveningKey = None

        for value in data["list"]:
            dt_text = value["dt_txt"]
            if f"{nextDateTime.strftime('%Y-%m-%d')} 09:00:00" in dt_text:
                morningKey = value
            if f"{nextDateTime.strftime('%Y-%m-%d')} 12:00:00" in dt_text:
                afternoonKey = value
            if f"{nextDateTime.strftime('%Y-%m-%d')} 21:00:00" in dt_text:
                eveningKey = value

        def get_windspeed_Description(speed):
          if speed <= 0.2:
              return 'Штиль'
          elif speed <= 1.5:
              return 'Тихий'
          elif speed <= 3.3:
              return 'Легкий'
          elif speed <= 5.4:
              return 'Слабый'
          elif speed <= 7.9:
              return 'Умеренный'
          elif speed <= 10.7:
              return 'Умеренный+'
          elif speed <= 13.8:
              return 'Сильный'
          elif speed <= 17.1:
              return 'Сильный+'
          elif speed <= 20.7:
              return 'Очень сильный, ушып кетесин'
          else:
              return 'Шторм!'

        wsdM = get_windspeed_Description(morningKey['wind']['speed'])
        wsdA = get_windspeed_Description(afternoonKey['wind']['speed'])
        wsdE = get_windspeed_Description(eveningKey['wind']['speed'])

        return {
            'windspeedMoring' : morningKey['wind']['speed'],
            'windspeedAfternoon' : afternoonKey['wind']['speed'],
            'windspeedEvening' : eveningKey['wind']['speed'],

            'windspeedDescriptionMorning': wsdM,
            'windspeedDescriptionAfternoon': wsdA,
            'windspeedDescriptionEvening': wsdE,

            'tempMorning': morningKey['main']['temp'],
            'tempAfternoon': afternoonKey['main']['temp'],
            'tempEvening': eveningKey['main']['temp'],

            'tempLikeMorning': morningKey['main']['feels_like'],
            'tempLikeAfternoon': afternoonKey['main']['feels_like'],
            'tempLikeEvening': eveningKey['main']['feels_like'],

            'humidityMorning': morningKey['main']['humidity'],
            'humidityAfternoon': afternoonKey['main']['humidity'],
            'humidityEvening': eveningKey['main']['humidity'],

            'descriptionMorning': weather_descriptions.get(morningKey['weather'][0]['description'], morningKey['weather'][0]['description']),
            'descriptionAfternoon': weather_descriptions.get(afternoonKey['weather'][0]['description'], afternoonKey['weather'][0]['description']),
            'descriptionEvening': weather_descriptions.get(eveningKey['weather'][0]['description'], eveningKey['weather'][0]['description']),
        }
