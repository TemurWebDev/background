from loader import dp, bot,db
import os
from aiogram import types
from aiogram.types import ContentType, Message, InputFile
from rembg import remove
from PIL import Image
from aiogram.dispatcher import FSMContext

from states.personalData import PersonalData

download_path = "files"


@dp.message_handler(text="imgremove", state=None)
async def enter_test(message: types.Message):
    for x in db.select_all_users():
        if x[1] == message.from_user.id:
            test = x
            break
    if test[-1] == 'uzbek':
        await message.reply("Rasm yuboring")
    if test[-1] == 'english':
        await message.reply("Send a picture")
    if test[-1] == 'rus':
        await message.reply("Отправить картинку")
    await PersonalData.img.set()


@dp.message_handler(content_types='photo', state=PersonalData.img)
async def imagebakcgroundremove(message: Message, state: FSMContext):
    for x in db.select_all_users():
        if x[1] == message.from_user.id:
            test = x
            break
    if test[-1] == 'uzbek':
        m = await message.reply("Biroz kuting...")
    if test[-1] == 'english':
        m = await message.reply("Wait a little...")
    if test[-1] == 'rus':
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


@dp.message_handler(content_types='photo', state=None)
async def test(message: Message):
    for x in db.select_all_users():
        if x[1] == message.from_user.id:
            test = x
            break
    if test[-1] == None:
        pass
    if test[-1] == 'uzbek':
        await message.answer("menyudan foydalaning")
    if test[-1] == 'english':
        await message.answer("use the menu")
    if test[-1] == 'rus':
        await message.answer("использовать меню")

