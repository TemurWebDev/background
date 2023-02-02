from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp,db


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
        text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/lang - Tilni o'zgartirish")
    
        await message.answer("\n".join(text))