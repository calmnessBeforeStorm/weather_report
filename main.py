import asyncio,markups
import logging
from aiogram import Bot, Dispatcher, types
from weatherDesc import Weather
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('bot.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_handler)

weather = Weather(
    'https://api.openweathermap.org/data/2.5/weather?q=aktobe&appid=ID&units=metric',
    'http://api.openweathermap.org/data/2.5/forecast?q=aktobe&appid=ID&units=metric'
)

TOKEN = ''
botaio = Bot(token=TOKEN)
dp = Dispatcher()

registered_users = set()

async def scheduled(time):
    q = 1
    while True:
        print(q)
        q += 1
        await send_current_message_aktobe()
        await asyncio.sleep(time)

async def send_current_message_aktobe():
    data = weather.get_current_data()
    ids = [764445437, 766773855, 994006554, 5304318111]
    for i in ids:
        await botaio.send_message(chat_id=i,
                                  text=f"<b>Погода в текущее время!(periodic)\n\nОбщее описание погоды: {data['description']}\nТемпература воздуха: {round(data['temp'], 1)}°C\nОщущается как: {round(data['temp_like'], 1)}°C\nВлажность воздуха: {round(data['humidity'], 1)}%\nСостояние ветра: {data['windspeedDescription']}({data['windspeed']} м/с)</b>",
                                  parse_mode='HTML')

@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    if user_id not in registered_users:
        registered_users.add(user_id)

    await botaio.send_message(user_id, 'Выберите режим', reply_markup=markups.modsMenu)

@dp.message()
async def messages(message: types.Message):
    if message.text == 'Расширенный режим':
        await botaio.send_message(message.from_user.id, 'Выберите время', reply_markup=markups.advanceMenu)

    elif message.text == 'Упрощенный режим':
        await botaio.send_message(message.from_user.id, 'Режим находится в стадии разработки')

    elif message.text == 'Текущая погода':
        data = weather.get_current_data()
        await botaio.send_message(message.from_user.id,
                                  f"<b>Погода в текущее время!\n\nОбщее описание погоды: {data['description']}\nТемпература воздуха: {round(data['temp'], 1)}°C\nОщущается как: {round(data['temp_like'], 1)}°C\nВлажность воздуха: {round(data['humidity'], 1)}%\nСостояние ветра: {data['windspeedDescription']}({data['windspeed']} м/с)</b>",
                                  parse_mode='HTML', reply_markup=markups.advanceMenu)

    elif message.text == 'Завтрашняя погода':
        data = weather.get_nextDay_data()
        await botaio.send_message(message.from_user.id,
                                  f"<b>Завтрашний день\n\n9:00\nОбщее описание: {data['descriptionMorning']}\nТемпература воздуха: {round(data['tempMorning'], 1)}°C\nОщущается как: {round(data['tempLikeMorning'], 1)}°C\nВлажность воздуха: {round(data['humidityMorning'], 1)}%\nСостояние ветра: {data['windspeedDescriptionMorning']}({data['windspeedMoring']} м/с)\n\n12:00\nОбщее описание: {data['descriptionAfternoon']}\nТемпература воздуха: {round(data['tempAfternoon'], 1)}°C\nОщущается как: {round(data['tempLikeAfternoon'], 1)}°C\nВлажность воздуха: {round(data['humidityAfternoon'], 1)}%\nСостояние ветра: {data['windspeedDescriptionAfternoon']}({data['windspeedAfternoon']} м/с)\n\n21:00\nОбщее описание: {data['descriptionEvening']}\nТемпература воздуха: {round(data['tempEvening'], 1)}°C\nОщущается как: {round(data['tempLikeEvening'], 1)}°C\nВлажность воздуха: {round(data['humidityEvening'], 1)}%\nСостояние ветра: {data['windspeedDescriptionEvening']}({data['windspeedEvening']} м/с)</b>",
                                  parse_mode="HTML", reply_markup=markups.advanceMenu)

    elif message.text == 'Периодическая отправка погоды':
        await botaio.send_message(message.from_user.id, 'В разработке')

    elif message.text == 'Поменять режим':
        await botaio.send_message(message.from_user.id, 'Выберите режим', reply_markup=markups.modsMenu)

    elif message.text == 'Сегодняшняя погода':
        data = weather.get_presentDay_data()
        await botaio.send_message(message.from_user.id,
                                  f"<b>Сегодняшний день\n\n9:00\nОбщее описание: {data['descriptionMorning']}\nТемпература воздуха: {round(data['tempMorning'], 1)}°C\nОщущается как: {round(data['tempLikeMorning'], 1)}°C\nВлажность воздуха: {round(data['humidityMorning'], 1)}%\nСостояние ветра: {data['windspeedDescriptionMorning']}({data['windspeedMoring']} м/с)\n\n12:00\nОбщее описание: {data['descriptionAfternoon']}\nТемпература воздуха: {round(data['tempAfternoon'], 1)}°C\nОщущается как: {round(data['tempLikeAfternoon'], 1)}°C\nВлажность воздуха: {round(data['humidityAfternoon'], 1)}%\nСостояние ветра: {data['windspeedDescriptionAfternoon']}({data['windspeedAfternoon']} м/с)\n\n21:00\nОбщее описание: {data['descriptionEvening']}\nТемпература воздуха: {round(data['tempEvening'], 1)}°C\nОщущается как: {round(data['tempLikeEvening'], 1)}°C\nВлажность воздуха: {round(data['humidityEvening'], 1)}%\nСостояние ветра: {data['windspeedDescriptionEvening']}({data['windspeedEvening']} м/с)</b>",
                                  parse_mode="HTML", reply_markup=markups.advanceMenu)

async def main():
    await botaio.delete_webhook(drop_pending_updates=True)
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(7000))
    await dp.start_polling(botaio)

if __name__ == '__main__':
    asyncio.run(main())
