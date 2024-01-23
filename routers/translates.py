from keyboards.user_keyboard import *


def translate(lang_code):
    uz, en, ru = 0, 1, 2
    lang = lang_code
    if str(lang) == 'uz':
        return uz
    elif str(lang) == 'en':
        return en
    elif str(lang) == 'ru':
        return ru
    else:
        return en


translate(lang_code='en')


def check_username(username_tiktok):
    for i in str(username_tiktok):
        if i.islower():
            pass
        elif i.isdigit():
            pass
        elif i == '_':
            pass
        else:
            return A22
    return True


check_username(username_tiktok='sardor_555_unique')


def check_email(check_mail):
    c = str(check_mail)[-10:]
    if c == '@gmail.com':
        return True
    else:
        return A23


check_email(check_mail='@gmail.com')


def code_generator():
    for k in range(1):
        import random
        a = """qwZ1XCV2er3QWER7ty8BN0MuiopHJ4K5Lasd6fT9YUIdfgdggERG"""
        c = "1234567890"
        n, d, m = 1, '', ''
        for j in range(35):
            s = random.randrange(51)
            d += str(a[s])
            if len(d) == 35:
                for i in range(10):
                    n = random.randrange(9)
                    m += str(c[n])
                    if len(m) == 10:
                        x = f"{m}"
                        return str(x)


code_generator()


def cloud_token():
    for k in range(1):
        import random
        a = """qwZ1XCV2er3QWER7ty8BN0MuiopHJ4K5Lasd6fT9YUIdfgdggERG"""
        c = "1234567890"
        n, d, m = 1, '', ''
        for j in range(10):
            s = random.randrange(51)
            d += str(a[s])
            if len(d) == 10:
                for i in range(5):
                    n = random.randrange(9)
                    m += str(c[n])
                    if len(m) == 5:
                        x = f"{m}_{d}"
                        return str(x)


code_generator()


def date_con(n, m):
    m = str(m)[:-6]
    df1 = str(n)[:13]
    fd1 = str(m)[:13]

    return df1, fd1


date_con(n='2023-11-14 20:09:35', m='2023-11-15 05:14:56+00:00')




