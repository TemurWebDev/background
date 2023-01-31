from loader import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ContentType, Message,InputFile
from pathlib import Path
from rembg import remove
from PIL import Image
from aiogram.dispatcher import FSMContext

from states.personalData import PersonalData

download_path = Path().joinpath("downloads")
download_path.mkdir(parents=True, exist_ok=True)


@dp.message_handler(text="imgremove", state=None)
async def enter_test(message: types.Message):
    await message.answer("Rasm yuboring")
    await PersonalData.img.set()



@dp.message_handler(content_types='photo',state=PersonalData.img)
async def imagebakcgroundremove(message: Message,state: FSMContext):
    print(await message.photo[-1].download(destination=download_path))
    file = str(await message.photo[-1].download(destination=download_path))[44:55]
    print(file)
    # await message.reply("Rasm qabul qilindi\n",f"file_id = {message.photo[-1].file_id}")

    input_path = "C:/Users/User/Desktop/test_1bot/downloads/photos/"+file
    output_path = "C:/Users/User/Desktop/test_1bot/downloads/photos/output.png"
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)

    photo_file = InputFile(path_or_bytesio="downloads/photos/output.png")
    await bot.send_document(chat_id=message.from_user.id,document=photo_file, caption="foto")

    await state.finish()



@dp.message_handler(content_types='photo',state=None)
async def test(message: Message):
    await message.answer("menyudan foydalaning")