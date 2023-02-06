from loader import dp, bot,db
import os
import logging
from aiogram import types
from aiogram.types import ContentType, Message, InputFile
from rembg import remove
from PIL import Image
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from states.personalData import PersonalData

download_path = "files"


@dp.message_handler(text="imgremove", state=None)
async def enter_test(message: types.Message):
    user = db.select_user(chat_id=message.from_user.id)
    if user[-1] == 'uzbek':
        await message.reply("Rasm yuboring")
    if user[-1] == 'english':
        await message.reply("Send a picture")
    if user[-1] == 'rus':
        await message.reply("Отправить картинку")
    await PersonalData.img.set()



# # You can use state '*' if you need to handle all states
# @dp.message_handler(state=PersonalData.img, commands='cancel')
# @dp.message_handler(Text(equals='cancel', ignore_case=True), state=PersonalData.img)
# async def cancel_handler(message: types.Message, state: FSMContext):
#     """
#     Allow user to cancel any action
#     """
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#
#     logging.info('Cancelling state %r', current_state)
#     # Cancel state and inform user about it
#     user = db.select_user(chat_id=message.from_user.id)
#     if user[-1] == 'uzbek':
#         await message.reply('Holat tugatildi!')
#     if user[-1] == 'english':
#         await message.reply('Case closed!')
#     if user[-1] == 'rus':
#         await message.reply('Дело закрыто!')
#     await state.finish()


@dp.message_handler(content_types=ContentType.ANY, state=PersonalData.img)
async def imagebakcgroundremove(message: Message, state: FSMContext):
    if message.content_type==ContentType.PHOTO:
        user = db.select_user(chat_id=message.from_user.id)
        if user[-1] == 'uzbek':
            m = await message.reply("Biroz kuting...")
        if user[-1] == 'english':
            m = await message.reply("Wait a little...")
        if user[-1] == 'rus':
            m = await message.reply("Подождите немного...")
        le = len(str(await message.photo[-1].download(destination=download_path)))
        if le == 52:
            file = str(await message.photo[-1].download(destination=download_path))[40:50]
            input_path = "files/photos/" + file
            print(input_path)
            output_path = "files/photos/output.png"
            input = Image.open(input_path)
            output = remove(input)
            output.save(output_path)
            photo_file = InputFile(path_or_bytesio=output_path)
            await bot.send_document(chat_id=message.from_user.id, document=photo_file, caption="\n👉 @text_to_audiobot")
        elif le == 53:
            file = str(await message.photo[-1].download(destination=download_path))[40:51]
            print(file)
            input_path = "files/photos/" + file
            print(input_path)
            output_path = "files/photos/output.png"
            input = Image.open(input_path)
            output = remove(input)
            output.save(output_path)
            photo_file = InputFile(path_or_bytesio=output_path)
            await bot.send_document(chat_id=message.from_user.id, document=photo_file, caption="\n👉 @text_to_audiobot")
        elif le == 54:
            file = str(await message.photo[-1].download(destination=download_path))[40:52]
            input_path = "files/photos/" + file
            print(input_path)
            output_path = "files/photos/output.png"
            input = Image.open(input_path)
            output = remove(input)
            output.save(output_path)
            photo_file = InputFile(path_or_bytesio=output_path)
            await bot.send_document(chat_id=message.from_user.id, document=photo_file, caption="\n👉 @text_to_audiobot")

        await state.finish()

        await m.delete()

        path = 'files/photos/'
        for x in os.listdir(path):
            os.remove(path + x)
    else:
        await state.finish()
        await message.reply('Hato habar! imgremove tugmasini bosing va rasm yuboring.Bot sizga orqa fonni olib beradi')




@dp.message_handler(content_types='photo', state=None)
async def test(message: Message):
    user = db.select_user(chat_id=message.from_user.id)
    if user[-1] == None:
        pass
    if user[-1] == 'uzbek':
        await message.answer("menyudan foydalaning")
    if user[-1] == 'english':
        await message.answer("use the menu")
    if user[-1] == 'rus':
        await message.answer("использовать меню")

