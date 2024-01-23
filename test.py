# for i in range(200):
#     print(f"B{i} = ''")


import pandas as pd
import requests

from routers.translates import code_generator

from database.db import Session, UserData

user_data = []
session = Session()
result = session.query(UserData).all()

for i in result:
    user_data.append([i.user_tg_id, i.name, i.lastname, i.username, i.language, i.phone, i.created, i.email])
    print([i.user_tg_id, i.name, i.lastname, i.username, i.language, i.phone, i.created, i.email])

df = pd.DataFrame(user_data, columns=['TG ID', 'Name', 'Lastname', 'Username',
                                      'Language', 'Phone', 'Create', 'Email'])
df.to_csv('books.csv')

files = {'audio': open(f"books.csv", "rb")}
base_url = (f"https://api.telegram.org/bot6740263710:AAEPuDe4JmG3DYnLVfIZOBqysiDg7AP7KP0/sendDocument?"
            f"chat_id={2134194986}&caption=Audio answer")
data = requests.get(base_url, files=files)
print(data.status_code)



# c = """
# Sell❌
# Categorize:Car
# Descriptions✅:
# Condition:Good👍
# Year: 2020
# Color: Black-Blue
# Model: Bugatti Chirom
# Country: Uzbekistan
# Type:Sport Car
# Max Speed: 390 km/h
# Start: 100 km/s 2.4 second
# Automatic
# Contact📞:
# Phone:+998994442211
# Telegram:@john2233_io
#
#
#
# """
# print(c)


# s = code_generator(n=6)
# print(s)

# print(len('🔍SearchImage:'))
