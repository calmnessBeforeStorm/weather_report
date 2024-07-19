from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnSwitchMode = KeyboardButton(text='Поменять режим')

# мод
btnAdvancedMode = KeyboardButton(text='Расширенный режим')
btnSimplifiedeMode = KeyboardButton(text='Упрощенный режим')
modsMenu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[btnAdvancedMode, btnSimplifiedeMode]])

# расширенный режим
currentWeather = KeyboardButton(text='Текущая погода')
nextDayWeather = KeyboardButton(text='Завтрашняя погода')
presentWeather = KeyboardButton(text='Сегодняшняя погода')
btnPeriodic = KeyboardButton(text='Периодическая отправка погоды')
advanceMenu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[currentWeather, nextDayWeather], [btnSwitchMode, presentWeather], [btnPeriodic]])

#simpleMode
'''cделаю какданибуд'''
