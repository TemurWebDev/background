from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp,db
from states.personalData import PersonalData

@dp.message_handler(CommandHelp(),state=PersonalData.img)
async def bot_help(message: types.Message):
        text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/lang - Tilni o'zgartirish")
    
        await message.answer("\n".join(text))


@dp.message_handler(commands='tugatish',state=PersonalData.img)
async def state_finish(message: types.Message):
    await message.reply('tugatildi')
