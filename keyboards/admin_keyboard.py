from aiogram.utils.keyboard import KeyboardBuilder, KeyboardButton
from constants import *

def admins_menu():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=B51),
            KeyboardButton(text=B52),
            KeyboardButton(text=B53),
            KeyboardButton(text=B54),
            KeyboardButton(text=B55),
            KeyboardButton(text=B56),
            KeyboardButton(text=B57),
            KeyboardButton(text=B58),
            KeyboardButton(text=B59),
            KeyboardButton(text=B60),
            KeyboardButton(text=B61),
            KeyboardButton(text=B62),
            KeyboardButton(text=B63),
            KeyboardButton(text=B64),
            KeyboardButton(text=B65),
            KeyboardButton(text=B66),
        ]
    )
    builder.adjust(3)
    return builder.as_markup(resize_keyboard=True)

