import datetime
from aiogram import Bot, Dispatcher, types
from currentData import *
from nextdayData import *

TOKEN = ''
botaio = Bot(token=TOKEN)
dp = Dispatcher(botaio)

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M")

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    buttonCurrent = types.KeyboardButton(text="🎷 ! JAZZ FUSION ! 🎶 CURRENT")
    buttonNextDay = types.KeyboardButton(text="🎷 ! JAZZ FUSION ! 🎶 NEXT DAY")
    keyboard.add(buttonCurrent)
    keyboard.add(buttonNextDay)
    await message.answer("JAZZ FUSION??", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "🎷 ! JAZZ FUSION ! 🎶 CURRENT")
async def juzz_fusion(message: types.Message):
    await message.reply(f'<b>Сегодняшний день\nОбщее описание: {translationCurrent.text}</b>\n\n<b>Температура воздуха:</b> {round(tempCurrent, 1)}°C\n<b>Ощущается как:</b> {round(temp_likeCurrent, 1)}°C\n<b>Влажность воздуха:</b> {round(humidityCurrent, 1)}%\n<b>Состояние ветра:</b> {windSpeedDescription}({windspeedCurrent} м/с)\n<b>Направление ветра:</b> {windDirection}', parse_mode="HTML")

@dp.message_handler(lambda message: message.text == "🎷 ! JAZZ FUSION ! 🎶 NEXT DAY")
async def juzz_fusion(message: types.Message):
    await message.reply(f'<b>{dttime}</b>\n<b>Завтрашний день\nОбщее описание: {translationNextDay.text}</b>\n\n<b>Температура воздуха:</b> {round(tempNextDay, 1)}°C\n<b>Ощущается как:</b> {round(temp_likeNextDay, 1)}°C\n<b>Влажность воздуха:</b> {round(humidityNextDay, 1)}%\n<b>Состояние ветра:</b> {windSpeedDescriptionNextDay}({windSpeedNextDay} м/с)\n<b>Направление ветра:</b> {windDirectionNextDay}', parse_mode="HTML")


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
