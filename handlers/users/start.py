import sqlite3

import logging
from aiogram import types
from data.config import CHANNELS,ADMINS
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from loader import bot, dp, db
from utils.misc import subscription
from keyboards.default.imagebackremove import imagremove
from keyboards.default.adminKeyboards import admincommands
from keyboards.inline.InlineKeyboards import til



@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
    chat_id = message.from_user.id
    username = message.from_user.username
    fulname = message.from_user.first_name
    data_of_create = str(message.date)

    try:
        db.add_user(chat_id=chat_id,username=username,fullname=fulname,date_of_created=data_of_create)
        for admin in ADMINS:
            await bot.send_message(chat_id=admin,text=f" {message.from_user.first_name} bazaga qoshildi")
    except sqlite3.IntegrityError as err:
        for admin in ADMINS:
            await bot.send_message(chat_id=admin, text=err)

    for x in db.select_all_users():
        if x[1] == chat_id:
            test = x
            break
    if test[-1] == None:
        await message.reply(f"🇺🇿 Tilni tanlang\n🇺🇸 Select a language\n🇷🇺 Выберите язык", reply_markup=til)
    elif test[-1] == 'uzbek':
        user = message.from_user.id
        final_status = True
        btn = InlineKeyboardMarkup(row_width=1)
        for channel in CHANNELS:
            status = await subscription.check(user_id=user, channel=channel)
            final_status *= status
            chat = await bot.get_chat(channel)
            if status:
                invite_link = await chat.export_invite_link()
                btn.insert(InlineKeyboardButton(text=f"✅ {chat.title}", url=invite_link))
            if not status:
                invite_link = await chat.export_invite_link()
                btn.insert(InlineKeyboardButton(text=f"❌ {chat.title}", url=invite_link))
        btn.add(InlineKeyboardButton(text="♻️Obunani tekshirish", callback_data="check_subs"))
        if final_status:
            if message.from_user.id == 1363350178:
                await bot.send_message(chat_id=message.from_user.id,
                                       text=f"Assalomu alaykum {message.from_user.first_name} siz adminsiz",
                                       reply_markup=admincommands)
            else:
                await message.answer(f"Assalomu alaykum {message.from_user.full_name}!\n"
                                     f"Botdan foydalanish uchun kerakli bo'limni tanlang!", reply_markup=imagremove)
        if not final_status:
            await message.answer("Botdan to'liq foydalanish uchun quyidagi kanallarga obuna bo'ling!",
                                 disable_web_page_preview=True, reply_markup=btn)



    elif test[-1] == 'english':
        user = message.from_user.id
        final_status = True
        btn = InlineKeyboardMarkup(row_width=1)
        for channel in CHANNELS:
            status = await subscription.check(user_id=user, channel=channel)
            final_status *= status
            chat = await bot.get_chat(channel)
            if status:
                invite_link = await chat.export_invite_link()
                btn.insert(InlineKeyboardButton(text=f"✅ {chat.title}", url=invite_link))
            if not status:
                invite_link = await chat.export_invite_link()
                btn.insert(InlineKeyboardButton(text=f"❌ {chat.title}", url=invite_link))
        btn.add(InlineKeyboardButton(text="♻️Check subscription", callback_data="check_subs"))
        if final_status:
            if message.from_user.id == 1363350178:
                await bot.send_message(chat_id=message.from_user.id,
                                       text=f"Assalomu alaykum {message.from_user.first_name} siz adminsiz",
                                       reply_markup=admincommands)
            else:
                await message.answer(f"Hello {message.from_user.full_name}!\n"
                                          f"Select the desired section to use the bot!!", reply_markup=imagremove)
        if not final_status:
            await message.answer("Subscribe to the channels below to get the most out of the bot!",
                                      disable_web_page_preview=True, reply_markup=btn)




    elif test[-1] == 'rus':
        user = message.from_user.id
        final_status = True
        btn = InlineKeyboardMarkup(row_width=1)
        for channel in CHANNELS:
            status = await subscription.check(user_id=user, channel=channel)
            final_status *= status
            chat = await bot.get_chat(channel)
            if status:
                invite_link = await chat.export_invite_link()
                btn.insert(InlineKeyboardButton(text=f"✅ {chat.title}", url=invite_link))
            if not status:
                invite_link = await chat.export_invite_link()
                btn.insert(InlineKeyboardButton(text=f"❌ {chat.title}", url=invite_link))
        btn.add(InlineKeyboardButton(text="♻️Проверить подписку", callback_data="check_subs"))
        if final_status:
            if message.from_user.id == 1363350178:
                await bot.send_message(chat_id=message.from_user.id,
                                       text=f"Assalomu alaykum {message.from_user.first_name} siz adminsiz",
                                       reply_markup=admincommands)
            else:
                await message.answer(f"Привет {message.from_user.full_name}!\n"
                                          f"Выберите нужный раздел для использования бота!", reply_markup=imagremove)
        if not final_status:
            await message.answer("Подпишитесь на каналы ниже, чтобы получить максимальную отдачу от бота!",
                                      disable_web_page_preview=True, reply_markup=btn)

