import time

import requests
from aiogram import Router, types, F
from aiogram.filters import CommandStart

from database.db import UserData, Session, Statistics
from keyboards.admin_keyboard import admins_menu
from routers.translates import *

session = Session()

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message, bot):

    k = translate(lang_code=message.from_user.language_code)
    c = message.from_user.id
    result = session.query(UserData).all()
    user = []
    for i in result:
        user.append(i.user_tg_id)
    if str(c) in user:
        if C3_Tik_Tok_Admin == str(message.from_user.id):
            print('Ok')

            await message.answer(text=f'{A0[k]} {message.from_user.full_name}!!!', reply_markup=admins_menu())
        else:
            await message.answer(text=f'{A0[k]} {message.from_user.full_name}!!!', reply_markup=main_menu_users())

        session.commit()
    else:
        await bot.send_video(chat_id=message.from_user.id, video=V0[k])
        time.sleep(2)
        await message.answer(text=f'{A1[k]}📞', reply_markup=phone_num())
        session.commit()


@router.message(F.contact)
async def start_handler(message: types.Message, bot):
    await bot.send_photo(chat_id=message.from_user.id, photo='AgACAgIAAxkBAAIC6WVUbywPVtd6GL6YJkYajdKPNWdzAAIbyjE'
                                                             'bGSWhSoAJTGSpcYcbAQADAgADcwADMwQ')
    k = translate(lang_code=f'{message.from_user.language_code}')
    user_tg_id = message.from_user.id
    first_name = message.from_user.first_name
    lastname = message.from_user.last_name
    phone = message.contact.phone_number
    language = message.from_user.language_code
    username = message.from_user.username
    created = message.date

    if message.contact.user_id == message.from_user.id:
        user = UserData(user_id=user_tg_id, user_tg_id=user_tg_id, name=first_name, lastname=lastname, phone=phone,
                        language=language,
                        username=username, created=created, email='No', rating='No', gender='No')
        session.add(user)
        session.commit()
        await message.answer(text=f'{A2[k]}!!!')
        await message.answer(text=f'{A3[k]}!!!')
        uio = Statistics(user_tg_id=user_tg_id, mass_media=0, orders=0, fast_food=0, library=0,
                         weather=0, music=0, payment=0, entertainment=0, child=0, bot_tutor=0,
                         tik_tok=0, life_hack=0, sxm_cloud=0, rating=0, music_d=0, image_d=0,
                         movies_d=0, apps_d=0, profile=0, audiotext=0, youtube_d=0, snbg=0, movies=0, transport=0)
        session.add(uio)
        session.commit()
