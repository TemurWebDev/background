from aiogram import types

from loader import dp,db

from states.personalData import PersonalData

@dp.message_handler(state=PersonalData.img)
async def bot_echo(message: types.Message):
  user = db.select_user(chat_id=message.from_user.id)
  if user[-1] == 'uzbek':
    await message.answer("Rasm yuboring! Yoki /cancel buyrug'i bilan holatni tugating!")
  if user[-1] == 'english':
    await message.answer("Send a picture! Or stop the situation with the /cancel command!")
  if user[-1] == 'rus':
    await message.answer("Отправить картинку! Или завершить статус командой /cancel!")




