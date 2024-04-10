from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnSwitchMode = KeyboardButton('Поменять режим')

#mods
btnAdvancedMode = KeyboardButton('Расширенный режим')
btnSimplifiedeMode = KeyboardButton('Упрощенный режим')
modsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnAdvancedMode, btnSimplifiedeMode)

#advancemode
currentWeather = KeyboardButton('Текущая погода')
nextDayWeather = KeyboardButton('Завтрашняя погода')
btnpPeriodic = KeyboardButton('Периодическая отправка погоды')
advanceMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(currentWeather, nextDayWeather, btnSwitchMode, btnpPeriodic)

#simpleMode
'''cделаю какданибуд'''
