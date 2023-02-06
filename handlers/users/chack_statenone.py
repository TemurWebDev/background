import logging
from aiogram import types
from data.config import CHANNELS,ADMINS
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from loader import bot, dp, db
from utils.misc import subscription
from keyboards.default.imagebackremove import imagremove








@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    user = db.select_user(chat_id=call.from_user.id)
    if user[-1] == None:
        pass

    elif user[-1] == 'uzbek':
        #await call.answer()
        result = str()
        btn = InlineKeyboardMarkup()
        final_status = True
        for channel in CHANNELS:
            status = await subscription.check(user_id=call.from_user.id,
                                              channel=channel)
            final_status *= status
            channel = await bot.get_chat(channel)
            if not status:
                invite_link = await channel.export_invite_link()
                btn.add(InlineKeyboardButton(text=f"❌ {channel.title}", url=invite_link))

        btn.add(InlineKeyboardButton(text="♻️Obunani tekshirish", callback_data="check_subs"))
        if final_status:
            await call.message.answer("Assalomu alaykum! Kerakli bo'limni tanlang", reply_markup=imagremove)
            await call.message.delete()
        if not final_status:
            await call.answer('Kanalga obuna bolishingiz kerak!', cache_time=0.05, show_alert=True)



    elif user[-1] == 'english':
        #await call.answer()
        result = str()
        btn = InlineKeyboardMarkup()
        final_status = True
        for channel in CHANNELS:
            status = await subscription.check(user_id=call.from_user.id,
                                              channel=channel)
            final_status *= status
            channel = await bot.get_chat(channel)
            if not status:
                invite_link = await channel.export_invite_link()
                btn.add(InlineKeyboardButton(text=f"❌ {channel.title}", url=invite_link))

        btn.add(InlineKeyboardButton(text="♻️Check subscription", callback_data="check_subs"))
        if final_status:
            await call.message.answer("Hello there! Select the desired section", reply_markup=imagremove)
            await call.message.delete()
        if not final_status:
            await call.answer('You must subscribe to the channel!', cache_time=0.05, show_alert=True)



    elif user[-1] == 'rus':
        #await call.answer()
        result = str()
        btn = InlineKeyboardMarkup()
        final_status = True
        for channel in CHANNELS:
            status = await subscription.check(user_id=call.from_user.id,
                                              channel=channel)
            final_status *= status
            channel = await bot.get_chat(channel)
            if not status:
                invite_link = await channel.export_invite_link()
                btn.add(InlineKeyboardButton(text=f"❌ {channel.title}", url=invite_link))

        btn.add(InlineKeyboardButton(text="♻️Проверить подписку", callback_data="check_subs"))
        if final_status:
            await call.message.answer("Привет! Выберите нужный раздел", reply_markup=imagremove)
            await call.message.delete()
        if not final_status:
            await call.answer('Вы должны подписаться на канал!', cache_time=0.05, show_alert=True)



