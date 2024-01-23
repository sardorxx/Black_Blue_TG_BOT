import random
import time

import pandas as pd
import requests
from aiogram import Router, F
from aiogram import types
import smtplib
import ssl

from gtts import gTTS

from database.db import UserData, Session, TikTokUser, EmailCheck, Images, Musics, LifeHackVideo, Books, \
    TikTokVideo, ImagesSystem, CloudUser, CloudDate, Statistics, LocationMetro
from routers.translates import *

session = Session()
router = Router()


@router.message(F.text == B1)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A4[k], reply_markup=media_section())


@router.message(F.text == B2)
async def manu_es(message: types.Message, bot):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.profile) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'profile': ant}))
    session.commit()
    await bot.send_photo(chat_id=message.from_user.id, photo='AgACAgIAAxkBAAIC8WVUcG57CagcqQtGpiwLfNMHpQp9AAIjyj'
                                                             'EbGSWhSuUhAAEPyEIrvQEAAwIAA3MAAzME')
    results = session.query(UserData).all()
    for i in results:
        if str(i.user_tg_id) == str(message.from_user.id):
            p = str(i.phone)
            e = str(i.email)
            c = str(i.created)
            m = str(i.gender)
            k = translate(lang_code=f'{message.from_user.language_code}')
            result = [f"""
            ID: <code>{message.from_user.id}</code>\n
            Isim: <code>{message.from_user.first_name}</code>\n
            Familiya: <code>{message.from_user.last_name}</code>\n
            Telefon: <code>{p}</code>\n
            Til: <code>{message.from_user.language_code}</code>\n
            Foydalanuvchi: <code>{message.from_user.username}</code>\n
            Qo'shildingiz: <code>{c}</code>\n
            Elektron Pochta: <code>{e}</code>\n
            Jinsingiz: <code>{m}</code>
            """,
                      f"""
                ID: <code>{message.from_user.id}</code>\n
                Name: <code>{message.from_user.first_name}</code>\n
                Lastname: <code>{message.from_user.last_name}</code>\n
                Phone: <code>{p}</code>\n
                Language: <code>{message.from_user.language_code}</code>\n
                Username: <code>{message.from_user.username}</code>\n
                Joined: <code>{c}</code>\n
                Email: <code>{e}</code>\n
                Gender: <code>{m}</code>
                """,
                      f"""
            ИД: <code>{message.from_user.id}</code>\n
            Имя: <code>{message.from_user.first_name}</code>\n
            Фамилия: <code>{message.from_user.last_name}</code>\n
            Телефон: <code>{p}</code>\n
            Язык: <code>{message.from_user.language_code}</code>\n
            Имя пользователя: <code>{message.from_user.username}</code>\n
            Присоединился: <code>{c}</code>\n
            Электронная почта: <code>{e}</code>\n
            Пол:<code>{m}</code>
            """]
            await message.answer(text=result[k], reply_markup=send_email())
            session.commit()


@router.message(F.text == B20)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A5[k])
    await message.answer(text=A6[k])


@router.message(F.text == B19)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A8[k], reply_markup=main_menu_users())


@router.message(F.text == B5)
async def manu_es(message: types.Message):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.rating) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'rating': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A9[k], reply_markup=rating_menu())


@router.message(F.text == B21)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    (session.query(UserData).filter(UserData.user_tg_id == str(message.from_user.id)).update
     ({'rating': f'{message.text}'}))
    session.commit()
    await message.answer(text=A10[k], reply_markup=rating_menu())


@router.message(F.text == B22)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    (session.query(UserData).filter(UserData.user_tg_id == str(message.from_user.id)).update
     ({'rating': f'{message.text}'}))
    session.commit()
    await message.answer(text=A10[k], reply_markup=rating_menu())


@router.message(F.text == B23)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    (session.query(UserData).filter(UserData.user_tg_id == str(message.from_user.id)).update
     ({'rating': f'{message.text}'}))
    session.commit()
    await message.answer(text=A10[k], reply_markup=rating_menu())


@router.message(F.text == B24)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    (session.query(UserData).filter(UserData.user_tg_id == str(message.from_user.id)).update
     ({'rating': f'{message.text}'}))
    session.commit()
    await message.answer(text=A10[k], reply_markup=rating_menu())


@router.message(F.text == B25)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    (session.query(UserData).filter(UserData.user_tg_id == str(message.from_user.id)).update
     ({'rating': f'{message.text}'}))
    session.commit()
    await message.answer(text=A10[k], reply_markup=rating_menu())


@router.message(F.text == B07)
async def manu_es(message: types.Message, bot):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await bot.send_photo(chat_id=message.from_user.id, photo='AgACAgIAAxkBAAIC-2VUcPPUuMCSBxqupTvhUacC01d_AAIqyjEb'
                                                             'GSWhSoL-Jjb7enRhAQADAgADcwADMwQ')
    await message.answer(text=A11[k], reply_markup=black_blue_shop())


@router.message(F.text == B8)
async def manu_es(message: types.Message, bot):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.mass_media) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'mass_media': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await bot.send_photo(chat_id=message.from_user.id, photo='AgACAgIAAxkBAAIDBWVUcceuMaMh8coBu_pQoXwJ-uDeAAIxyj'
                                                             'EbGSWhSkwZeFCK5ZJIAQADAgADcwADMwQ')
    await bot.send_photo(chat_id=message.from_user.id, photo='AgACAgIAAxkBAAIDB2VUcd8SnJ9rhz-UsXEiFTy4E5ChAAIyyjE'
                                                             'bGSWhSsx6n7SdY5-aAQADAgADcwADMwQ')
    await bot.send_photo(chat_id=message.from_user.id, photo='AgACAgIAAxkBAAIC-WVUcOA8WJMI6m4Ll1Ou2o7MchS_AAIpyjEbGSW'
                                                             'hSr9gmWM-0ZAqAQADAgADcwADMwQ')
    await message.answer(text=A47[k], reply_markup=mass_media())


@router.message(F.text == B3)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A12[k], reply_markup=xsm_menu())


@router.message(F.text == B35)
async def manu_es(message: types.Message):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.audiotext) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'audiotext': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A64[k])


@router.message(F.text == B9)
async def manu_es(message: types.Message):
    result = session.query(Statistics).all()
    ant = 0
    k = translate(lang_code=f'{message.from_user.language_code}')
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.orders) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'orders': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A49[k], reply_markup=orders_com())


@router.message(F.text == B50)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A33[k], reply_markup=media_section())


@router.message(F.text == B10)
async def manu_es(message: types.Message):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.fast_food) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'fast_food': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A50[k], reply_markup=fast_food())


@router.message(F.text == B11)
async def manu_es(message: types.Message):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.library) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'library': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A51[k], reply_markup=books_com())


@router.message(F.text == B12)
async def manu_es(message: types.Message):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.weather) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'weather': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A52[k], reply_markup=weather_com())


@router.message(F.text == B13)
async def manu_es(message: types.Message):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.music) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'music': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A53[k], reply_markup=music_com())


@router.message(F.text == B14)
async def manu_es(message: types.Message):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.movies) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'movies': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A54[k], reply_markup=movies_com())


@router.message(F.text == B15)
async def manu_es(message: types.Message):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.payment) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'payment': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A55[k], reply_markup=payment_com())


@router.message(F.text == B16)
async def manu_es(message: types.Message):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.entertainment) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'entertainment': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A56[k], reply_markup=fun_com())


@router.message(F.text == B17)
async def manu_es(message: types.Message):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.child) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'child': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A57[k], reply_markup=games_for_kids())


@router.message(F.text == B18)
async def manu_es(message: types.Message):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.transport) + 1

    session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A58[k], reply_markup=transport_map())


@router.message(F.text == B48)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A38[k])


@router.message(F.text == B41)
async def manu_es(message: types.Message, bot):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await bot.send_photo(chat_id=message.from_user.id, photo='AgACAgIAAxkBAAIDAWVUcZSKeORccjstLjQ-nro9Gh_QAAIv'
                                                             'yjEbGSWhSpMK4iqf1kPUAQADAgADcwADMwQ')
    await message.answer(text=A45[k])


@router.message(F.text == B42)
async def manu_es(message: types.Message, bot):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.movies_d) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'movies_d': ant}))
    session.commit()
    # await bot.send_photo(chat_id=message.from_user.id, photo='')
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A54[k])


@router.message(F.text == B_042)
async def manu_es(message: types.Message):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.apps_d) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'apps_d': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A59[k])


@router.message(F.text == B46)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A40[k])


@router.message(F.text == B47)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A40[k])


@router.message(F.text == B34)
async def manu_es(message: types.Message):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.youtube_d) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'youtube_d': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A65[k])


@router.message(F.text == B33)
async def manu_es(message: types.Message, bot):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.sxm_cloud) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'sxm_cloud': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')

    await bot.send_photo(chat_id=message.from_user.id, photo=f'AgACAgIAAxkBAAIIfmVco8lEWF0Bt7aQK_qbN'
                                                             f'cwp-IDMAAIj1DEbqEfgSgNSeICAt0TuAQADAgADcwADMwQ',
                         caption=A37[k],
                         reply_markup=cloud_menu())


@router.message(F.text == B6)
async def manu_es(message: types.Message, bot):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.bot_tutor) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'bot_tutor': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A00[k])
    result = session.query(ImagesSystem).all()
    for i in result:
        time.sleep(2)
        if i.file_caption not in ['image logo', 'market logo', 'music', 'youtube download logo']:
            await bot.send_photo(chat_id=message.from_user.id, photo=f'{i.file_id}')


@router.message(F.text == B29)
async def manu_es(message: types.Message, bot):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.tik_tok) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'tik_tok': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await bot.send_photo(chat_id=message.from_user.id, photo='AgACAgIAAxkBAAIC7WVUcDhmql9Qogxokbeipart69nnAAPQMRswq'
                                                             'KFKSJd9b_mlJjgBAAMCAANzAAMzBA')

    await bot.send_photo(chat_id=message.from_user.id, photo='AgACAgIAAxkBAAIC62VUcCHV6KA_J1efpjWq5asAARcPXQACIMox'
                                                             'GxkloUrTmWd8DB_r-AEAAwIAA3MAAzME')
    await message.answer(text=A13[k], reply_markup=tik_menu())


@router.message(F.text == B029)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A20[k], reply_markup=account_tik_menu())


@router.message(F.text == B38)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A21[k], parse_mode='HTML')


@router.message(F.text == B39)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A30[k], reply_markup=xsm_menu())


@router.message(F.text == B28)
async def manu_es(message: types.Message):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.snbg) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'snbg': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A16[k])


@router.message(F.text == B4)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A17[k], reply_markup=useful_menu())


@router.message(F.text == B4)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A17[k], reply_markup=useful_menu())


@router.message(F.text == B32)
async def manu_es(message: types.Message):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.life_hack) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'life_hack': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A18[k], reply_markup=watch_life_hack())


@router.message(F.text == B36)
async def manu_es(message: types.Message, bot):
    k = translate(lang_code=f'{message.from_user.language_code}')
    result = session.query(LifeHackVideo).all()
    user_t = []
    for i in result:
        user_t.append(i.file_id)
    c = len(user_t)
    a = random.randrange(0, c)
    await bot.send_video(chat_id=message.from_user.id, video=f'{user_t[a]}')
    await message.answer(text=A18[k])


@router.message(F.text == B37)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A19[k], reply_markup=useful_menu())


@router.message(F.text == B7)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A31[k], reply_markup=medias_menu())


@router.message(F.text == B0041)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A61[k])
    await message.answer(text=A62[k])


@router.message(F.text == B66)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A4[k], reply_markup=main_menu_users())


@router.message(F.text == B43)
async def manu_es(message: types.Message):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.music_d) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'music_d': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A32[k], reply_markup=medias_music_menu())


@router.message(F.text == B44)
async def manu_es(message: types.Message):
    result = session.query(Statistics).all()
    ant = 0
    for i in result:
        if i.user_tg_id == str(message.from_user.id):
            ant = int(i.image_d) + 1

    (session.query(Statistics).filter(Statistics.user_tg_id == str(message.from_user.id)).update
     ({'image_d': ant}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    print(k)
    print(message.from_user.language_code)
    print(type(k))
    await message.answer(text=A35[k], reply_markup=medias_image_menu())


@router.message(F.text == B041)
async def manu_es(message: types.Message, bot):
    k = translate(lang_code=f'{message.from_user.language_code}')
    result = session.query(Images).all()
    user_t = []
    for i in result:
        user_t.append(i.file_id)
    c = len(user_t)
    a = random.randrange(0, c)
    await bot.send_photo(chat_id=message.chat.id, photo=user_t[a])
    await message.answer(text=A46[k])


@router.message(F.text == B40)
async def manu_es(message: types.Message, bot):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await bot.send_photo(chat_id=message.from_user.id, photo='AgACAgIAAxkBAAIC_WVUcTo3XAsfBdrmhr8oHK0XmC17AAIl'
                                                             '0DEbMKihSrKNUypHb7mBAQADAgADcwADMwQ')
    await message.answer(text=A44[k])


@router.message(F.text == B042)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A33[k], reply_markup=medias_menu())


@router.message(F.text == B040)
async def manu_es(message: types.Message, bot):
    k = translate(lang_code=f'{message.from_user.language_code}')
    result = session.query(Musics).all()
    user_t = []
    for i in result:
        user_t.append(i.file_id)
    c = len(user_t)
    a = random.randrange(0, c)
    await bot.send_audio(chat_id=message.chat.id, audio=user_t[a])
    await message.answer(text=f"{A43[k]}")


@router.message(F.text == B020)
async def manu_es(message: types.Message):
    (session.query(UserData).filter(UserData.user_tg_id == str(message.from_user.id)).update
     ({'gender': f'{message.text}'}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A36[k])


@router.message(F.text == B0020)
async def manu_es(message: types.Message):
    (session.query(UserData).filter(UserData.user_tg_id == str(message.from_user.id)).update
     ({'gender': f'{message.text}'}))
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A36[k])


@router.message(F.photo)
async def manu_es(message: types.Message):
    k = translate(lang_code=f'{message.from_user.language_code}')
    print(message.photo[0].file_id, '  ', message.caption)
    m = f"Your photo received🏁"
    user_tg_id = str(message.from_user.id)
    file_id = str(message.photo[0].file_id)
    file_caption = str(message.caption)
    file_type = 'photo'

    result = session.query(CloudUser).all()
    user_t = []
    for i in result:
        user_t.append(i.user_tg_id)
    dated = str(message.date)

    if C3_Tik_Tok_Admin == str(message.from_user.id):
        user = Images(user_tg_id=user_tg_id, file_id=file_id, file_caption=file_caption, dated=dated)
        session.add(user)
        session.commit()
        await message.answer(text=m)

    elif str(message.from_user.id) in user_t:
        user = CloudDate(user_tg_id=user_tg_id, file_id=file_id, file_caption=file_caption, file_type=file_type,
                         dated=dated)
        session.add(user)
        session.commit()
        await message.answer(text=A41[k])


@router.message(F.audio)
async def manu_es(message: types.Message):
    print(message.audio.file_id, '  ', message.caption)
    m = f"Your audio received🏁"
    user_tg_id = str(message.from_user.id)
    file_id = str(message.audio.file_id)
    file_caption = str(message.caption) + str(message.audio.file_name)
    file_type = 'audio'

    result = session.query(CloudUser).all()
    user_t = []
    for i in result:
        user_t.append(i.user_tg_id)
    dated = str(message.date)
    k = translate(lang_code=f'{message.from_user.language_code}')
    if C3_Tik_Tok_Admin == str(message.from_user.id):
        user = Musics(user_tg_id=user_tg_id, file_id=file_id, file_caption=file_caption, dated=dated)
        session.add(user)
        session.commit()
        await message.answer(text=m)

    elif str(message.from_user.id) in user_t:
        user = CloudDate(user_tg_id=user_tg_id, file_id=file_id, file_caption=file_caption, file_type=file_type,
                         dated=dated)
        session.add(user)
        session.commit()
        await message.answer(text=A41[k])


@router.message(F.document)
async def manu_es(message: types.Message):
    print(message.document.file_id, '  ', message.caption)
    m = f"Your book received🏁"
    user_tg_id = str(message.from_user.id)
    file_id = str(message.document.file_id)
    file_caption = str(message.caption) + str(message.document.file_name)
    file_type = 'document'

    result = session.query(CloudUser).all()
    user_t = []
    for i in result:
        user_t.append(i.user_tg_id)
    dated = str(message.date)
    session.commit()
    k = translate(lang_code=f'{message.from_user.language_code}')
    if C3_Tik_Tok_Admin == str(message.from_user.id):
        user = Books(user_tg_id=user_tg_id, file_id=file_id, file_caption=file_caption, dated=dated)
        session.add(user)
        session.commit()
        await message.answer(text=m)
    elif str(message.from_user.id) in user_t:
        user = CloudDate(user_tg_id=user_tg_id, file_id=file_id, file_caption=file_caption, file_type=file_type,
                         dated=dated)
        session.add(user)
        session.commit()
        await message.answer(text=A41[k])


@router.message(F.video)
async def manu_es(message: types.Message):
    print(message.video.file_id, '  ', message.caption)
    m = f"Your life hack video received🏁"
    user_tg_id = str(message.from_user.id)
    file_id = str(message.video.file_id)
    file_caption = str(message.caption) + str(message.video.file_name)
    user_name = str(message.from_user.username)
    file_type = 'video'

    result = session.query(CloudUser).all()
    user_t = []
    for i in result:
        user_t.append(i.user_tg_id)
    dated = str(message.date)
    k = translate(lang_code=f'{message.from_user.language_code}')
    if C3_Tik_Tok_Admin == str(message.from_user.id):
        user = LifeHackVideo(user_id=user_tg_id, caption_video=file_caption, user_name=user_name,
                             file_id=file_id, dated=dated)
        session.add(user)
        session.commit()
        await message.answer(text=m)
    elif str(message.from_user.id) in user_t:
        user = CloudDate(user_tg_id=user_tg_id, file_id=file_id, file_caption=file_caption, file_type=file_type,
                         dated=dated)
        session.add(user)
        session.commit()
        await message.answer(text=A41[k])
    else:
        result = session.query(TikTokUser).all()
        print('ok')
        for i in result:
            if str(i.user_tg_id) == str(message.from_user.id):
                user_id = str(message.from_user.id)
                caption_video = str(message.caption)
                tik_tok_name = str(i.tiktok_name)
                file_id = str(message.video.file_id)
                dated = str(message.date)
                user = TikTokVideo(user_id=user_id, caption_video=caption_video, tik_tok_name=tik_tok_name,
                                   file_id=file_id, dated=dated)
                session.add(user)
                session.commit()


@router.message(F.location)
async def manu_es(message: types.Message):
    a5 = str(message.from_user.id)
    a6 = str(message.date)
    a0 = message.location.heading
    a1 = message.location.latitude
    a2 = message.location.longitude
    a3 = message.location.horizontal_accuracy
    a4 = message.location.live_period
    if str(message.from_user.id) == C3_Tik_Tok_Admin:
        user = LocationMetro(user_tg_id=a5, metro_name='not', country='not', city='not', heading=a0, latitude=a1,
                             longitude=a2,
                             horizontal_accuracy=a3, live_period=a4, dated=a6)
        session.add(user)
        session.commit()
        await message.answer(text=f'Location:{a6}$country$city$metroname')


# Tik Tok


@router.message(F.text == B30)
async def manu_es(message: types.Message, bot):
    k = translate(lang_code=f'{message.from_user.language_code}')
    result = session.query(TikTokVideo).all()
    user_t = []
    for i in result:
        user_t.append(i.file_id)
    c = len(user_t)
    a = random.randrange(0, c)
    await bot.send_video(chat_id=message.from_user.id, video=user_t[a], caption='⚡Tik')
    await message.answer(text=A14[k], reply_markup=tok_menu())


@router.message(F.text == 'ℹ️About us')
async def mass_(message: types.Message, bot):
    k = translate(lang_code=f'{message.from_user.language_code}')
    await message.answer(text=A00[k])
    await bot.send_photo(chat_id=message.from_user.id)


@router.message(F.text == B63)
async def mass_(message: types.Message):
    if str(message.from_user.id) == C3_Tik_Tok_Admin:
        result = session.query(UserData).all()
        user_data = []
        for i in result:
            user_data.append([i.user_tg_id, i.name, i.lastname, i.phone, i.language, i.username,
                              i.created, i.email, i.rating, i.gender])

        df = pd.DataFrame(user_data, columns=['TG ID', 'Name', 'Lastname',
                                              'Phone', 'Language', 'Username', 'Create', 'Email', 'Rating', 'Gender'])
        df.to_csv(f'{message.text}.csv')
        files = {'document': open(f"{message.text}.csv", "rb")}
        base_url = (f"https://api.telegram.org/bot6740263710:AAEPuDe4JmG3DYnLVfIZOBqysiDg7AP7KP0/sendDocument?"
                    f"chat_id={C1_Super_Admin}&caption={message.text}")
        requests.get(base_url, files=files)


@router.message(F.text == B51)
async def mass_(message: types.Message):
    if str(message.from_user.id) == C3_Tik_Tok_Admin:
        result = session.query(Books).all()
        user_data = []
        for i in result:
            user_data.append([i.user_tg_id, i.file_id, i.file_caption, i.dated])

        df = pd.DataFrame(user_data, columns=['TG ID', 'File ID', 'File Caption', 'Date'])
        df.to_csv(f'{message.text}.csv')
        files = {'document': open(f"{message.text}.csv", "rb")}
        base_url = (f"https://api.telegram.org/bot6740263710:AAEPuDe4JmG3DYnLVfIZOBqysiDg7AP7KP0/sendDocument?"
                    f"chat_id={C1_Super_Admin}&caption={message.text}")
        requests.get(base_url, files=files)


@router.message(F.text == B52)
async def mass_(message: types.Message):
    if str(message.from_user.id) == C3_Tik_Tok_Admin:
        result = session.query(EmailCheck).all()
        user_data = []
        for i in result:
            user_data.append([i.user_tg_id, i.email, i.password1, i.password2, i.dated])

        df = pd.DataFrame(user_data, columns=['TG ID', 'Email', 'Password',
                                              'Pasword', 'Date'])
        df.to_csv(f'{message.text}.csv')
        files = {'document': open(f"{message.text}.csv", "rb")}
        base_url = (f"https://api.telegram.org/bot6740263710:AAEPuDe4JmG3DYnLVfIZOBqysiDg7AP7KP0/sendDocument?"
                    f"chat_id={C1_Super_Admin}&caption={message.text}")
        requests.get(base_url, files=files)


@router.message(F.text == B53)
async def mass_(message: types.Message):
    if str(message.from_user.id) == C3_Tik_Tok_Admin:
        result = session.query(CloudDate).all()
        user_data = []
        for i in result:
            user_data.append([i.user_tg_id, i.file_id, i.file_caption, i.file_type, i.dated])

        df = pd.DataFrame(user_data, columns=['TG ID', 'File ID', 'File Caption', 'File Type', 'Date'])
        df.to_csv(f'{message.text}.csv')
        files = {'document': open(f"{message.text}.csv", "rb")}
        base_url = (f"https://api.telegram.org/bot6740263710:AAEPuDe4JmG3DYnLVfIZOBqysiDg7AP7KP0/sendDocument?"
                    f"chat_id={C1_Super_Admin}&caption={message.text}")
        requests.get(base_url, files=files)


@router.message(F.text == B54)
async def mass_(message: types.Message):
    if str(message.from_user.id) == C3_Tik_Tok_Admin:
        result = session.query(CloudUser).all()
        user_data = []
        for i in result:
            user_data.append([i.user_tg_id, i.parol, i.dated])

        df = pd.DataFrame(user_data, columns=['TG ID', 'Parol', 'Date'])
        df.to_csv(f'{message.text}.csv')
        files = {'document': open(f"{message.text}.csv", "rb")}
        base_url = (f"https://api.telegram.org/bot6740263710:AAEPuDe4JmG3DYnLVfIZOBqysiDg7AP7KP0/sendDocument?"
                    f"chat_id={C1_Super_Admin}&caption={message.text}")
        requests.get(base_url, files=files)


@router.message(F.text == B55)
async def mass_(message: types.Message):
    if str(message.from_user.id) == C3_Tik_Tok_Admin:
        result = session.query(UserData).all()
        user_data = []
        for i in result:
            user_data.append([i.user_tg_id, i.name, i.lastname, i.phone, i.language, i.username,
                              i.created, i.email, i.rating, i.gender])

        df = pd.DataFrame(user_data, columns=['TG ID', 'Name', 'Lastname',
                                              'Phone', 'Language', 'Username', 'Create', 'Email', 'Rating', 'Gender'])
        df.to_csv(f'{message.text}.csv')
        files = {'document': open(f"{message.text}.csv", "rb")}
        base_url = (f"https://api.telegram.org/bot6740263710:AAEPuDe4JmG3DYnLVfIZOBqysiDg7AP7KP0/sendDocument?"
                    f"chat_id={C1_Super_Admin}&caption={message.text}")
        requests.get(base_url, files=files)


@router.message(F.text == B56)
async def mass_(message: types.Message):
    if str(message.from_user.id) == C3_Tik_Tok_Admin:
        result = session.query(Images).all()
        user_data = []
        for i in result:
            user_data.append([i.user_tg_id, i.file_id, i.file_caption, i.dated])

        df = pd.DataFrame(user_data, columns=['TG ID', 'File ID', 'Caption', 'Date'])
        df.to_csv(f'{message.text}.csv')
        files = {'document': open(f"{message.text}.csv", "rb")}
        base_url = (f"https://api.telegram.org/bot6740263710:AAEPuDe4JmG3DYnLVfIZOBqysiDg7AP7KP0/sendDocument?"
                    f"chat_id={C1_Super_Admin}&caption={message.text}")
        requests.get(base_url, files=files)


@router.message(F.text == B57)
async def mass_(message: types.Message):
    if str(message.from_user.id) == C3_Tik_Tok_Admin:
        result = session.query(LifeHackVideo).all()
        user_data = []
        for i in result:
            user_data.append([i.user_id, i.caption_video, i.user_name, i.file_id, i.dated])

        df = pd.DataFrame(user_data, columns=['TG ID', 'Caption', 'Firstname',
                                              'File_ID', 'Date'])
        df.to_csv(f'{message.text}.csv')
        files = {'document': open(f"{message.text}.csv", "rb")}
        base_url = (f"https://api.telegram.org/bot6740263710:AAEPuDe4JmG3DYnLVfIZOBqysiDg7AP7KP0/sendDocument?"
                    f"chat_id={C1_Super_Admin}&caption={message.text}")
        requests.get(base_url, files=files)


@router.message(F.text == B58)
async def mass_(message: types.Message):
    if str(message.from_user.id) == C3_Tik_Tok_Admin:
        result = session.query(UserData).all()
        user_data = []
        for i in result:
            user_data.append([i.user_tg_id, i.name, i.lastname, i.phone, i.language, i.username,
                              i.created, i.email, i.rating, i.gender])

        df = pd.DataFrame(user_data, columns=['TG ID', 'Name', 'Lastname',
                                              'Phone', 'Language', 'Username', 'Create', 'Email', 'Rating', 'Gender'])
        df.to_csv(f'{message.text}.csv')
        files = {'document': open(f"{message.text}.csv", "rb")}
        base_url = (f"https://api.telegram.org/bot6740263710:AAEPuDe4JmG3DYnLVfIZOBqysiDg7AP7KP0/sendDocument?"
                    f"chat_id={C1_Super_Admin}&caption={message.text}")
        requests.get(base_url, files=files)


@router.message(F.text == B59)
async def mass_(message: types.Message):
    if str(message.from_user.id) == C3_Tik_Tok_Admin:
        result = session.query(Musics).all()
        user_data = []
        for i in result:
            user_data.append([i.user_tg_id, i.file_id, i.file_caption, i.dated])

        df = pd.DataFrame(user_data, columns=['TG ID', 'File_ID', 'Caption',
                                              'Dated'])
        df.to_csv(f'{message.text}.csv')
        files = {'document': open(f"{message.text}.csv", "rb")}
        base_url = (f"https://api.telegram.org/bot6740263710:AAEPuDe4JmG3DYnLVfIZOBqysiDg7AP7KP0/sendDocument?"
                    f"chat_id={C1_Super_Admin}&caption={message.text}")
        requests.get(base_url, files=files)


@router.message(F.text == B60)
async def mass_(message: types.Message):
    if str(message.from_user.id) == C3_Tik_Tok_Admin:
        result = session.query(TikTokUser).all()
        user_data = []
        for i in result:
            user_data.append([i.user_tg_id, i.tiktok_name, i.email, i.status, i.dated])

        df = pd.DataFrame(user_data, columns=['TG ID', 'TikTokUserName', 'Email',
                                              'Status', 'Date'])
        df.to_csv(f'{message.text}.csv')
        files = {'document': open(f"{message.text}.csv", "rb")}
        base_url = (f"https://api.telegram.org/bot6740263710:AAEPuDe4JmG3DYnLVfIZOBqysiDg7AP7KP0/sendDocument?"
                    f"chat_id={C1_Super_Admin}&caption={message.text}")
        requests.get(base_url, files=files)


@router.message(F.text == B61)
async def mass_(message: types.Message):
    if str(message.from_user.id) == C3_Tik_Tok_Admin:
        result = session.query(TikTokVideo).all()
        user_data = []
        for i in result:
            user_data.append([i.user_id, i.caption_video, i.tik_tok_name, i.file_id, i.dated])

        df = pd.DataFrame(user_data, columns=['TG ID', 'Caption', 'TikTokName', 'File_ID', 'Date'])
        df.to_csv(f'{message.text}.csv')
        files = {'document': open(f"{message.text}.csv", "rb")}
        base_url = (f"https://api.telegram.org/bot6740263710:AAEPuDe4JmG3DYnLVfIZOBqysiDg7AP7KP0/sendDocument?"
                    f"chat_id={C1_Super_Admin}&caption={message.text}")
        requests.get(base_url, files=files)


@router.message(F.text == B62)
async def mass_(message: types.Message):
    if str(message.from_user.id) == C3_Tik_Tok_Admin:
        result = session.query(Statistics).all()
        user_data = []
        for i in result:
            user_data.append(
                [i.user_tg_id, i.mass_media, i.orders, i.fast_food, i.library, i.weather, i.music, i.movies, i.payment,
                 i.entertainment,
                 i.child, i.bot_tutor, i.tik_tok, i.life_hack, i.sxm_cloud, i.rating, i.music_d, i.image_d, i.movies_d,
                 i.apps_d, i.profile,
                 i.audiotext, i.youtube_d, i.snbg, i.transport])

        df = pd.DataFrame(user_data, columns=['TG ID', 'Mass Media', 'Orders',
                                              'Fast_food', 'Library', 'Weather', 'Music', 'Movie', 'Payment',
                                              'Entertainment', 'Child', 'Bot Tutor', 'Tik Tok', 'Life Hack',
                                              'SXM Cloud', 'Rating', 'Music_D', 'Image_D', 'Movies_D', 'Apps_D',
                                                                                                       'Profile',
                                              'AudioText', 'Youtube_D', 'SNBG', 'Transport'])
        df.to_csv(f'{message.text}.csv')
        files = {'document': open(f"{message.text}.csv", "rb")}
        base_url = (f"https://api.telegram.org/bot6740263710:AAEPuDe4JmG3DYnLVfIZOBqysiDg7AP7KP0/sendDocument?"
                    f"chat_id={C1_Super_Admin}&caption={message.text}")
        requests.get(base_url, files=files)


@router.message(F.text == B64)
async def mass_(message: types.Message):
    if str(message.from_user.id) == C3_Tik_Tok_Admin:
        result = session.query(UserData).all()
        user_data = []
        for i in result:
            user_data.append([i.user_tg_id, i.name, i.lastname, i.phone, i.language, i.username,
                              i.created, i.email, i.rating, i.gender])

        df = pd.DataFrame(user_data, columns=['TG ID', 'Name', 'Lastname',
                                              'Phone', 'Language', 'Username', 'Create', 'Email', 'Rating', 'Gender'])
        df.to_csv(f'{message.text}.csv')
        files = {'document': open(f"{message.text}.csv", "rb")}
        base_url = (f"https://api.telegram.org/bot6740263710:AAEPuDe4JmG3DYnLVfIZOBqysiDg7AP7KP0/sendDocument?"
                    f"chat_id={C1_Super_Admin}&caption={message.text}")
        requests.get(base_url, files=files)


@router.message(F.text == B65)
async def mass_(message: types.Message):
    if str(message.from_user.id) == C3_Tik_Tok_Admin:
        result = session.query(UserData).all()
        user_data = []
        for i in result:
            user_data.append([i.user_tg_id, i.name, i.lastname, i.phone, i.language, i.username,
                              i.created, i.email, i.rating, i.gender])

        df = pd.DataFrame(user_data, columns=['TG ID', 'Name', 'Lastname',
                                              'Phone', 'Language', 'Username', 'Create', 'Email', 'Rating', 'Gender'])
        df.to_csv(f'{message.text}.csv')
        files = {'document': open(f"{message.text}.csv", "rb")}
        base_url = (f"https://api.telegram.org/bot6740263710:AAEPuDe4JmG3DYnLVfIZOBqysiDg7AP7KP0/sendDocument?"
                    f"chat_id={C1_Super_Admin}&caption={message.text}")
        requests.get(base_url, files=files)


@router.message(F.text == B31)
async def manu_es(message: types.Message, bot):
    k = translate(lang_code=f'{message.from_user.language_code}')
    result = session.query(TikTokVideo).all()
    user_t = []
    for i in result:
        user_t.append(i.file_id)
    c = len(user_t)
    a = random.randrange(0, c)
    await bot.send_video(chat_id=message.from_user.id, video=user_t[a], caption='⚡Tok')
    await message.answer(text=A15[k], reply_markup=tik_menu())


# STOP
#
#
#
#
#
@router.message(F.text)
async def manu_es(message: types.Message, bot):
    k = translate(lang_code=f'{message.from_user.language_code}')
    c = message.text[-10:]
    print(message.text)
    p = str(message.text)[:20]
    dkj = str(message.text)[:12]
    b = str(message.text)[:13]
    qho = str(message.text)[:9]
    wep = str(message.text)[:12]

    uio = str(message.text)[:10]
    print(uio)

    gjk = str(message.text)[:13]
    typ = str(message.text)[:13]

    df = str(message.text)[:5]
    if str(c) == '@gmail.com':
        (session.query(UserData).filter(UserData.user_tg_id == str(message.from_user.id)).update
         ({'email': f'{message.text}'}))
        session.commit()

        await message.answer(text=A7[k])
    elif p == 'CreateTikTokAccount:':
        c = str(message.text)[20:]
        print(c)
        w = c.split('$')
        print(w)
        u1 = check_username(username_tiktok=f'{w[1]}')
        u2 = check_email(check_mail=f'{w[0]}')
        if u1 is not True:
            await message.answer(text=A22[k])
        if u2 is not True:
            await message.answer(text=A23[k])

        if u1 is True and u2 is True:

            user_tg_id = message.from_user.id
            tiktok_name = str(w[1])
            email = str(w[0])
            dated = message.date
            result = session.query(TikTokUser).all()
            user_tik_name = []
            user_mail = []
            for i in result:
                user_tik_name.append(i.tiktok_name)
                user_mail.append(i.email)

            if str(u1) not in user_tik_name and str(u2) not in user_mail:
                user = TikTokUser(user_tg_id=user_tg_id, tiktok_name=tiktok_name, email=email, status='none',
                                  dated=dated)
                session.add(user)
                session.commit()
                context = ssl.create_default_context()
                c = code_generator()
                port = 587
                # iddc qzdy zhwd hubh -> xalilovsardor4605@gmail.com
                password = 'siwykjfppqxjsdej'
                sender = 'xalilovsardorjon@gmail.com'
                reciver = f'{email}'
                for i in range(1):
                    server = smtplib.SMTP("smtp.gmail.com", port)
                    server.ehlo()
                    server.starttls(context=context)
                    server.ehlo()
                    server.login(sender, password)

                    msg = f'''\\
                             From: Black-Blue
                             Subject: Verification Code to create Tik Tok account on @black_blue_black_bot
                             
                             This is your code: {c}
                             '''

                    server.sendmail(sender, reciver, msg)
                    await message.answer(text=f"{A63[k]} {reciver}")
                user1 = EmailCheck(user_tg_id=user_tg_id, email=email, password1=f'{c}', password2='no',
                                   dated=dated)
                session.add(user1)
                session.commit()

                await message.answer(text=A25[k])

        else:
            await message.answer(text=A26[k])
            await message.answer(text=A24[k])
    elif df == 'Code:':
        result5 = session.query(EmailCheck).all()
        rty = str(message.text)[5:]

        for i in result5:
            if str(i.user_tg_id) == str(message.from_user.id):
                a = date_con(n=str(i.dated), m=str(message.date))
                ok = str(i.password1)
                b1 = a[0]
                b2 = a[1]
                if b1 == b2 and ok == rty:
                    (session.query(EmailCheck).filter(UserData.user_tg_id == str(message.from_user.id)).update
                     ({'password2': f'{rty}'}))
                    session.commit()
                    await message.answer(text=A25[k])

                else:
                    await message.answer(text=A28[k])

    elif dkj == 'CreateCloud:':
        opr = str(message.text)[12:]
        tg = message.from_user.id
        parol = opr
        dated = message.date

        user = CloudUser(user_tg_id=tg, parol=parol, dated=dated)
        session.add(user)
        session.commit()
        await message.answer(text=A39[k])

    elif uio == 'Download📥:':
        result = session.query(CloudUser).all()
        result1 = session.query(CloudDate).all()
        uio = str(message.text)[10:]
        uio = uio.split('$')
        print(uio)

        for i in result:
            if i.user_tg_id == str(message.from_user.id) and i.parol == uio[0]:

                for j in result1:

                    if str(j.user_tg_id) == str(message.from_user.id) and uio[1] in j.file_caption:
                        print('ok')

                        if j.file_type == 'photo':
                            a = await bot.send_photo(chat_id=message.from_user.id, photo=f'{j.file_id}')
                            b = await message.answer(text=A42[k])
                            time.sleep(30)
                            await a.delete()
                            await b.delete()
                        elif j.file_type == 'video':
                            a = await bot.send_video(chat_id=message.from_user.id, video=f'{j.file_id}')
                            b = await message.answer(text=A42[k])
                            time.sleep(30)
                            await a.delete()
                            await b.delete()

                        elif j.file_type == 'document':
                            a = await bot.send_document(chat_id=message.from_user.id, document=f'{j.file_id}')
                            b = await message.answer(text=A42[k])
                            time.sleep(30)
                            await a.delete()
                            await b.delete()

                        elif j.file_type == 'audio':
                            a = await bot.send_audio(chat_id=message.from_user.id, audio=f'{j.file_id}')
                            b = await message.answer(text=A42[k])
                            time.sleep(30)
                            await a.delete()
                            await b.delete()

    elif gjk == '🔍SearchMusic:':
        gjk = message.text[13:]
        result1 = session.query(Musics).all()
        for i in result1:
            if gjk in i.file_caption:
                await bot.send_audio(chat_id=message.from_user.id, audio=f'{i.file_id}')

    elif typ == '🔍SearchImage:':
        gjk = message.text[13:]
        result1 = session.query(Images).all()
        for i in result1:
            if gjk in i.file_caption:
                await bot.send_photo(chat_id=message.from_user.id, photo=f'{i.file_id}')

    elif wep == '🔍SearchBook:':
        print('ok')
        gjk = message.text[12:]
        result1 = session.query(Books).all()
        for i in result1:
            if gjk in i.file_caption:
                await bot.send_document(chat_id=message.from_user.id, document=f'{i.file_id}')

    elif b == 'AudioMessage:':

        b = message.text[13:]
        ty = f"AudioMessage"
        text = gTTS(f"""{b}""")
        text.save(f"{ty}.mp3")
        # time.sleep(30)
        files = {'audio': open(f"{ty}.mp3", "rb")}
        base_url = (f"https://api.telegram.org/bot6740263710:AAEPuDe4JmG3DYnLVfIZOBqysiDg7AP7KP0/sendAudio?"
                    f"chat_id={message.from_user.id}&caption=Audio answer")
        requests.get(base_url, files=files)
    elif qho == 'Location:':
        e = message.text[9:]
        # b = 'Location:{a6}$country$city$metroname'
        e = e.split('$')
        if str(message.from_user.id) == C3_Tik_Tok_Admin:
            (session.query(LocationMetro).filter(LocationMetro.date == f'{e[0]}').update
             ({'metro_name': f'{e[3]}'}, {'country': f'{e[1]}'}, {'city': f'{e[2]}'}))
            session.commit()
