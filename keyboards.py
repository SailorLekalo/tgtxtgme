from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

f_kb = [
    [KeyboardButton(text='Атака 👋'),KeyboardButton(text='Способность'),KeyboardButton(text='Смена оружия')],
    [KeyboardButton(text='Использование предмета'),KeyboardButton(text='Сбежать'),KeyboardButton(text='Блокировать'),KeyboardButton(text='Увернуться')]
]

fight_kb = ReplyKeyboardMarkup(keyboard=f_kb, keyresize_keyboard=True)


b_kb = [
    [KeyboardButton(text='Эта кнопка ничего не делает')],
]

base_kb = ReplyKeyboardMarkup(keyboard=b_kb, keyresize_keyboard=True)