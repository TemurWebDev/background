from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

til = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🇺🇿 uz',callback_data='uzbek'),
            InlineKeyboardButton(text='🇺🇸 eng',callback_data='english'),
            InlineKeyboardButton(text='🇷🇺 ru',callback_data='rus')
        ],
    ]
)

