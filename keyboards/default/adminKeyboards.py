from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

admincommands = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="admin panel")
        ],
        [
            KeyboardButton(text="imgremove")
        ],
    ],
    resize_keyboard=True
)

adminusers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="users"),
        ],
        [
            KeyboardButton(text="back")
        ],
    ],
    resize_keyboard=True
)