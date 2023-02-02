import logging
from aiogram.types import CallbackQuery,InlineKeyboardButton,InlineKeyboardMarkup
from data.config import CHANNELS,ADMINS
from utils.misc import subscription
from loader import bot, dp, db
from aiogram import types

from keyboards.default.imagebackremove import imagremove
from keyboards.default.adminKeyboards import admincommands
from keyboards.inline.InlineKeyboards import til




@dp.callback_query_handler(text="uzbek")
async def til_uz(call: CallbackQuery):
    print(call.data)
    lang = call.data
    db.update_user_email(lang=lang, chat_id=call.from_user.id)
    user = db.select_user(chat_id=call.from_user.id)
    await bot.send_message(chat_id=1363350178,text=f"{user} ning tili {lang} bolib saqlandi")

    await call.message.delete()

    user = call.from_user.id
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
        if call.from_user.id == 1363350178:
            await bot.send_message(chat_id=call.from_user.id,
                                   text=f"Assalomu alaykum {call.from_user.first_name} siz adminsiz",
                                   reply_markup=admincommands)
        else:
            await call.message.answer(f"Assalomu alaykum {call.from_user.full_name}!\n"
                                 f"Botdan foydalanish uchun kerakli bo'limni tanlang!", reply_markup=imagremove)
    if not final_status:
        await call.message.answer("Botdan to'liq foydalanish uchun quyidagi kanallarga obuna bo'ling!",disable_web_page_preview=True, reply_markup=btn)

    await call.answer(cache_time=60)



@dp.callback_query_handler(text="english")
async def til_eng(call: CallbackQuery):
    print(call.data)
    lang = call.data
    db.update_user_email(lang=lang, chat_id=call.from_user.id)
    user = db.select_user(chat_id=call.from_user.id)
    await bot.send_message(chat_id=1363350178, text=f"{user} ning tili {lang} bolib saqlandi")

    await call.message.delete()

    user = call.from_user.id
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
        if call.from_user.id == 1363350178:
            await bot.send_message(chat_id=call.from_user.id,
                                   text=f"Assalomu alaykum {call.from_user.first_name} siz adminsiz",
                                   reply_markup=admincommands)
        else:
            await call.message.answer(f"Hello {call.from_user.full_name}!\n"
                                 f"Select the desired section to use the bot!!", reply_markup=imagremove)
    if not final_status:
        await call.message.answer("Subscribe to the channels below to get the most out of the bot!",disable_web_page_preview=True, reply_markup=btn)

    await call.answer(cache_time=60)




@dp.callback_query_handler(text="rus")
async def til_ru(call: CallbackQuery):
    print(call.data)
    lang = call.data
    db.update_user_email(lang=lang, chat_id=call.from_user.id)
    user = db.select_user(chat_id=call.from_user.id)
    await bot.send_message(chat_id=1363350178, text=f"{user} ning tili {lang} bolib saqlandi")

    await call.message.delete()

    user = call.from_user.id
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
        if call.from_user.id == 1363350178:
            await bot.send_message(chat_id=call.from_user.id,
                                   text=f"Assalomu alaykum {call.from_user.first_name} siz adminsiz",
                                   reply_markup=admincommands)
        else:
            await call.message.answer(f"Привет {call.from_user.full_name}!\n"
                                 f"Выберите нужный раздел для использования бота!", reply_markup=imagremove)
    if not final_status:
        await call.message.answer("Подпишитесь на каналы ниже, чтобы получить максимальную отдачу от бота!",disable_web_page_preview=True, reply_markup=btn)
    await call.answer(cache_time=60)



@dp.message_handler(commands='lang')
async def lang_update(message:types.Message):
    await message.reply(f"🇺🇿 Tilni tanlang\n🇺🇸 Select a language\n🇷🇺 Выберите язык", reply_markup=til)