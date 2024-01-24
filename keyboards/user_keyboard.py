from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import KeyboardBuilder, KeyboardButton

from constants import *


def phone_num():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[

            KeyboardButton(text=f"{B0}", request_contact=True)
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def admin_menu():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=B51),
            KeyboardButton(text=B52),
            KeyboardButton(text=B53),
            KeyboardButton(text=B54),
            KeyboardButton(text=B55)
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def main_menu_users():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=B1),
            KeyboardButton(text=B2),
            KeyboardButton(text=B3),
            KeyboardButton(text=B4),
            KeyboardButton(text=B5),
            KeyboardButton(text=B7),
            KeyboardButton(text=B6),
            KeyboardButton(text=B07),
        ]
    )
    builder.adjust(3)
    return builder.as_markup(resize_keyboard=True)


def media_section():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=B8),
            KeyboardButton(text=B9),
            KeyboardButton(text=B10),
            KeyboardButton(text=B11),
            KeyboardButton(text=B12),
            KeyboardButton(text=B13),
            KeyboardButton(text=B14),
            KeyboardButton(text=B15),
            KeyboardButton(text=B16),
            KeyboardButton(text=B17),
            KeyboardButton(text=B18),
            KeyboardButton(text=B19),
        ]
    )
    builder.adjust(3)
    return builder.as_markup(resize_keyboard=True)


def send_email():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=B020),
            KeyboardButton(text=B0020),
            KeyboardButton(text=B20),
            KeyboardButton(text=B19),
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def rating_menu():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=B21),
            KeyboardButton(text=B22),
            KeyboardButton(text=B23),
            KeyboardButton(text=B24),
            KeyboardButton(text=B25),
            KeyboardButton(text=B19),
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def black_blue_shop():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=B26),
            KeyboardButton(text=B27),
            KeyboardButton(text=B19),
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def xsm_menu():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=B28),
            KeyboardButton(text=B29),
            KeyboardButton(text=B029),
            KeyboardButton(text=B19),
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def tik_menu():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=B30)
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def tik_account_menu():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=B30),
            KeyboardButton(text=B30)
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def account_tik_menu():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=B38),
            KeyboardButton(text=B39)
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def tok_menu():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=B31)
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def useful_menu():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=B32),
            KeyboardButton(text=B33),
            KeyboardButton(text=B34),
            KeyboardButton(text=B35),
            KeyboardButton(text=B19),
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def watch_life_hack():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=B36),
            KeyboardButton(text=B37),
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def medias_menu():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=B43),
            KeyboardButton(text=B44),
            KeyboardButton(text=B45),
            KeyboardButton(text=B0041),
            KeyboardButton(text=B19),
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def medias_music_menu():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=B40),
            KeyboardButton(text=B040),
            KeyboardButton(text=B042),
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def medias_image_menu():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=B41),
            KeyboardButton(text=B041),
            KeyboardButton(text=B042),
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def medias_movie_menu():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=B42),
            KeyboardButton(text=B0042),
            KeyboardButton(text=B042),
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def cloud_menu():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=B46),
            KeyboardButton(text=B47),
            KeyboardButton(text=B48),
            KeyboardButton(text=B37),
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def mass_media():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[

            KeyboardButton(text="🌐Google", web_app=WebAppInfo(url="https://www.google.com/")),
            KeyboardButton(text="📽️Youtube", web_app=WebAppInfo(url="https://www.youtube.com/")),
            KeyboardButton(text="📧Mail", web_app=WebAppInfo(url="https://www.google.com/intl/en/gmail/about/")),
            KeyboardButton(text="📰Wikipedia", web_app=WebAppInfo(url="https://www.wikipedia.org/")),
            KeyboardButton(text="🗺️Google Map", web_app=WebAppInfo(url="https://www.google.com/maps/")),
            KeyboardButton(text="💬Twitter(X)", web_app=WebAppInfo(url="https://twitter.com/")),
            KeyboardButton(text="🗨️Facebook", web_app=WebAppInfo(url="https://www.facebook.com/")),
            KeyboardButton(text="⬇️Installer app",
                           web_app=WebAppInfo(url="https://en.savefrom.net/1-youtube-video-downloader-533nN/")),
            KeyboardButton(text="📪Instagram", web_app=WebAppInfo(url="https://www.instagram.com/")),
            KeyboardButton(text="♟️Chess.com", web_app=WebAppInfo(url="https://www.chess.com/")),
            KeyboardButton(text="🔄️Translate", web_app=WebAppInfo(url="https://translate.google.com/")),
            KeyboardButton(text="💟Yahoo!!!", web_app=WebAppInfo(url='https://finance.yahoo.com/')),
            KeyboardButton(text="🔙Back to Medias"),
        ]
    )
    builder.adjust(4, 4, 4)
    return builder.as_markup(resize_keyboard=True)


def orders_com():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[

            KeyboardButton(text="Uzum Market", web_app=WebAppInfo(url="https://uzum.uz/uz")),
            KeyboardButton(text="OLX_UZ", web_app=WebAppInfo(url="https://m.olx.uz/")),
            KeyboardButton(text="AliExpress",
                           web_app=WebAppInfo(
                               url="https://aliexpress.ru/?ysclid=lmgaclxuz3981726397&gatewayAdapt=glo2rus")),
            KeyboardButton(text="Amazon", web_app=WebAppInfo(url="https://www.amazon.com/")),
            KeyboardButton(text="🔙Back to Medias"),
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def fast_food():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[

            KeyboardButton(text="Oqtepa Lavash", web_app=WebAppInfo(url="https://oqtepalavash.uz/")),
            KeyboardButton(text="Bellissimo", web_app=WebAppInfo(url="https://bellissimo.uz")),
            KeyboardButton(text="Evos", web_app=WebAppInfo(url="https://evos.uz/en")),
            KeyboardButton(text="Yandex Eats",
                           web_app=WebAppInfo(url="https://eats.yandex.com/en-uz/tashkent?shippingType=delivery")),
            KeyboardButton(text="Uzum Tezkor", web_app=WebAppInfo(url="https://uzumtezkor.uz/")),
            KeyboardButton(text="🔙Back to Medias"),
        ]
    )
    builder.adjust(3, 2, 1)
    return builder.as_markup(resize_keyboard=True)


def books_com():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[

            KeyboardButton(text="PDF Driver", web_app=WebAppInfo(url="https://www.pdfdrive.com/")),
            KeyboardButton(text="E-Book", web_app=WebAppInfo(url="https://www.ebooks.com/en-us/")),
            KeyboardButton(text="Asaxiy", web_app=WebAppInfo(url="https://asaxiy.uz/product/knigi")),
            KeyboardButton(text="🔙Back to Medias"),
        ]
    )
    builder.adjust(3)
    return builder.as_markup(resize_keyboard=True)


def weather_com():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[

            KeyboardButton(text="Forecast", web_app=WebAppInfo(url="https://www.bbc.com/weather/1512569")),
            KeyboardButton(text="Weather", web_app=WebAppInfo(url="https://weather.com/?Goto=Redirected")),
            KeyboardButton(text="🔙Back to Medias"),
        ]
    )
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def music_com():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[

            KeyboardButton(text="Spotify", web_app=WebAppInfo(url="https://open.spotify.com/")),
            KeyboardButton(text="WorldStar", web_app=WebAppInfo(url="https://worldstarhiphop.com/videos/")),
            KeyboardButton(text="Dreeze", web_app=WebAppInfo(url="https://www.deezer.com/us/offers")),
            KeyboardButton(text="Songs 50.000+", web_app=WebAppInfo(url="https://pixabay.com/music/search/")),
            KeyboardButton(text="UzMusic", web_app=WebAppInfo(url="https://muznavo.net/2022_xit_qoshiqlari")),
            KeyboardButton(text="🔙Back to Medias"),
        ]
    )
    builder.adjust(3)
    return builder.as_markup(resize_keyboard=True)


def movies_com():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[

            KeyboardButton(text="Asilmedia", web_app=WebAppInfo(url="https://asilmedia.org/popular.html#")),
            KeyboardButton(text="Uzmovie", web_app=WebAppInfo(url="https://uzmovi.com/")),
            KeyboardButton(text="TopFilms", web_app=WebAppInfo(url="https://topfilms.me/")),
            KeyboardButton(text="🔙Back to Medias"),
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def payment_com():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[

            KeyboardButton(text="CLICK", web_app=WebAppInfo(url="https://my.click.uz/auth")),
            KeyboardButton(text="PAYME", web_app=WebAppInfo(url="https://payme.uz/home/main")),
            KeyboardButton(text="UZUM PAY", web_app=WebAppInfo(url="https://uzumbank.uz/")),
            KeyboardButton(text="🔙Back to Medias"),
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def fun_com():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[

            KeyboardButton(text="📸Virtual Travel", web_app=WebAppInfo(url="https://www.instantstreetview.com/")),
            KeyboardButton(text="ChatGPT", web_app=WebAppInfo(url="https://chat.openai.com/")),
            KeyboardButton(text="Yandex Browser", web_app=WebAppInfo(url='https://yandex.ru/search/?clid=2353835'
                                                                     '&text=&lr=194600')),
            KeyboardButton(text="🔙Back to Medias"),
        ]
    )
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def games_for_kids():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[

            KeyboardButton(text="🏆Creative", web_app=WebAppInfo(
                url="https://www.cartoonnetworkhq.com/games/category/creative")),
            KeyboardButton(text="🎮Adventure", web_app=WebAppInfo(
                url="https://www.cartoonnetworkhq.com/games/category/adventure")),
            KeyboardButton(text="🪄Fantasy", web_app=WebAppInfo(
                url="https://www.cartoonnetworkhq.com/games/category/fantasy")),
            KeyboardButton(text="🖌️Draw pictures", web_app=WebAppInfo(
                url="https://kidsdrawinghub.com/candy-coloring-pages-printable/")),
            KeyboardButton(text="🎶Music for sleep"),
            KeyboardButton(text="🎸Beethoven Simfoniya"),
            KeyboardButton(text="🎹Play Piano", web_app=WebAppInfo(url="https://pianoplays.com/")),
            KeyboardButton(text="🔙Back to Medias"),
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def transport_map():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text="🗺️Map", web_app=WebAppInfo(url='https://2gis.uz/tashkent')),
            KeyboardButton(text="🪪ATTO", web_app=WebAppInfo(url='https://web.atto.uz/uz')),
            KeyboardButton(text="🚌Bus Ticket", web_app=WebAppInfo(url='https://avtoticket.uz/')),
            KeyboardButton(text="🚕Yandex taxi", web_app=WebAppInfo(url="https://taxi.yandex.com/en_am/")),
            KeyboardButton(text="🔙Back to Medias")

        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)
