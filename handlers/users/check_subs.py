import logging
from aiogram import types
from data.config import CHANNELS,ADMINS
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from loader import bot, dp, db
from utils.misc import subscription
from keyboards.default.imagebackremove import imagremove
from keyboards.default.adminKeyboards import admincommands
from keyboards.inline.InlineKeyboards import til






@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    for x in db.select_all_users():
        if x[1] == call.from_user.id:
            test = x
            break
    if test[-1] == None:
        pass
        #await call.message.answer('Hali til tanlanmagan')
        # await message.reply(f"🇺🇿 Tilni tanlang\n🇺🇸 Select a language\n🇷🇺 Выберите язык", reply_markup=til)
    elif test[-1] == 'uzbek':
        await call.answer()
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
            await call.answer(cache_time=60)
            await call.message.answer(
                "Siz quyidagi kanal(lar)ga obuna bo'lmagansiz!\nIltimos obuna bo'lib tekshirish tugmasini bosing ",
                reply_markup=btn)
            await call.message.delete()


    elif test[-1] == 'english':
        await call.answer()
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
            await call.answer(cache_time=60)
            await call.message.answer(
                "You are not subscribed to the channel(s) below!\nPlease subscribe and then click the verify button ",
                reply_markup=btn)
            await call.message.delete()


    elif test[-1] == 'rus':
        await call.answer()
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
            await call.answer(cache_time=60)
            await call.message.answer(
                "Вы не подписаны на канал(ы) ниже!\nПожалуйста, подпишитесь, а затем нажмите подтвердить ",
                reply_markup=btn)
            await call.message.delete()

