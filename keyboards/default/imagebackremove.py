from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

imagremove = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="imgremove")
        ],
    ],
    resize_keyboard=True
)



menuz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='admin'),
            KeyboardButton(text="tilni o'zgartirish")
        ],
    ],
    resize_keyboard=True
)

meneng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='admin'),
            KeyboardButton(text="change the language")
        ],
    ],
    resize_keyboard=True
)

menru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='admin'),
            KeyboardButton(text="изменить язык")
        ],
    ],
    resize_keyboard=True
)