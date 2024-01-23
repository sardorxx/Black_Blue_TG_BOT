from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine('postgresql://postgres:Sar1571Xal2005@localhost/black_blue', echo=True)
engine = create_engine('sqlite:///black_blue.db', echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)


class UserData(Base):
    __tablename__ = 'users_data'
    user_id = Column(String, primary_key=True)
    user_tg_id = Column(String, unique=True)
    name = Column(String)
    lastname = Column(String)
    phone = Column(String)
    language = Column(String)
    username = Column(String)
    created = Column(DateTime)
    email = Column(String)
    rating = Column(String)
    gender = Column(String)

    def __init__(self, user_id, user_tg_id, name, lastname, phone, language, username, created, email, rating, gender):
        self.user_id = user_id
        self.user_tg_id = user_tg_id
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.language = language
        self.username = username
        self.created = created
        self.email = email
        self.rating = rating
        self.gender = gender

    def __repr__(self):
        return (f"{self.user_id} {self.user_tg_id} {self.name} {self.lastname}"
                f" {self.phone} {self.language} {self.username} {self.created} {self.email} {self.rating} {self.gender}")


class TikTokUser(Base):
    __tablename__ = 'tiktok_user'
    user_tg_id = Column(String)
    tiktok_name = Column(String, unique=True)
    email = Column(String, unique=True)
    status = Column(String)
    dated = Column(DateTime, primary_key=True)

    def __init__(self, user_tg_id, tiktok_name, email, status, dated):
        self.user_tg_id = user_tg_id
        self.tiktok_name = tiktok_name
        self.email = email
        self.status = status
        self.dated = dated

    def __repr__(self):
        return f"{self.user_id} {self.user_tg_id} {self.tiktok_name} {self.email} {self.status} {self.dated}"


class TikTokVideo(Base):
    __tablename__ = 'tiktok_video'
    user_id = Column(Integer)
    caption_video = Column(String)
    tik_tok_name = Column(String)
    file_id = Column(String, unique=True)
    dated = Column(String, primary_key=True)

    def __init__(self, user_id, caption_video, tik_tok_name, file_id, dated):
        self.user_id = user_id
        self.caption_video = caption_video
        self.tik_tok_name = tik_tok_name
        self.file_id = file_id
        self.dated = dated

    def __repr__(self):
        return f"{self.user_id} {self.caption_video} {self.tik_tok_name} {self.file_id} {self.dated}"


class Statistics(Base):
    __tablename__ = 'user_statistics'
    user_tg_id = Column(String, primary_key=True)
    mass_media = Column(Integer)
    orders = Column(Integer)
    fast_food = Column(Integer)
    library = Column(Integer)
    weather = Column(Integer)
    music = Column(Integer)
    movies = Column(Integer)
    payment = Column(Integer)
    entertainment = Column(Integer)
    child = Column(Integer)
    bot_tutor = Column(Integer)
    tik_tok = Column(Integer)
    life_hack = Column(Integer)
    sxm_cloud = Column(Integer)
    rating = Column(Integer)
    music_d = Column(Integer)
    image_d = Column(Integer)
    movies_d = Column(Integer)
    apps_d = Column(Integer)
    profile = Column(Integer)
    audiotext = Column(Integer)
    youtube_d = Column(Integer)
    snbg = Column(Integer)
    transport = Column(Integer)

    def __init__(self, user_tg_id, mass_media, orders, fast_food, library, weather, music, movies, payment,
                 entertainment,
                 child, bot_tutor, tik_tok, life_hack, sxm_cloud, rating, music_d, image_d, movies_d, apps_d, profile,
                 audiotext, youtube_d, snbg, transport):
        self.user_tg_id = user_tg_id
        self.mass_media = mass_media
        self.orders = orders
        self.fast_food = fast_food
        self.library = library
        self.weather = weather
        self.music = music
        self.movies = movies
        self.payment = payment
        self.entertainment = entertainment
        self.child = child
        self.transport = transport
        self.bot_tutor = bot_tutor
        self.tik_tok = tik_tok
        self.life_hack = life_hack
        self.sxm_cloud = sxm_cloud
        self.rating = rating
        self.music_d = music_d
        self.image_d = image_d
        self.movies_d = movies_d
        self.apps_d = apps_d
        self.profile = profile
        self.audiotext = audiotext
        self.youtube_d = youtube_d
        self.snbg = snbg

    def __repr__(self):
        return (f"{self.user_tg_id} {self.mass_media} {self.orders} {self.fast_food} {self.library} "
                f"{self.weather}"
                f"{self.weather} {self.music} {self.payment} {self.entertainment} {self.child} {self.bot_tutor}"
                f" {self.tik_tok} "
                f"{self.life_hack} {self.sxm_cloud} {self.rating} {self.music_d} {self.image_d} {self.movies_d}"
                f" {self.apps_d} {self.profile} {self.youtube_d} {self.audiotext} {self.snbg}")


class EmailCheck(Base):
    __tablename__ = 'check_user_email'
    user_tg_id = Column(String)
    email = Column(String, unique=True)
    password1 = Column(String)
    password2 = Column(String)
    dated = Column(DateTime, primary_key=True)

    def __init__(self, user_tg_id, email, password1, password2, dated):
        self.user_tg_id = user_tg_id
        self.email = email
        self.password1 = password1
        self.password2 = password2
        self.dated = dated

    def __repr__(self):
        return f"{self.user_tg_id} {self.email} {self.password1} {self.password2} {self.dated}"


class Images(Base):
    __tablename__ = 'images_table'
    user_tg_id = Column(String)
    file_id = Column(String, unique=True)
    file_caption = Column(String)
    dated = Column(String, primary_key=True)

    def __init__(self, user_tg_id, file_id, file_caption, dated):
        self.user_tg_id = user_tg_id
        self.file_id = file_id
        self.file_caption = file_caption
        self.dated = dated

    def __repr__(self):
        return f"{self.user_tg_id} {self.file_id} {self.file_caption} {self.dated}"


class Musics(Base):
    __tablename__ = 'musics_table'
    user_tg_id = Column(String)
    file_id = Column(String, unique=True)
    file_caption = Column(String)
    dated = Column(String, primary_key=True)

    def __init__(self, user_tg_id, file_id, file_caption, dated):
        self.user_tg_id = user_tg_id
        self.file_id = file_id
        self.file_caption = file_caption
        self.dated = dated

    def __repr__(self):
        return f"{self.user_tg_id} {self.file_id} {self.file_caption} {self.dated}"


class Books(Base):
    __tablename__ = 'books_table'
    user_tg_id = Column(String)
    file_id = Column(String, unique=True)
    file_caption = Column(String)
    dated = Column(String, primary_key=True)

    def __init__(self, user_tg_id, file_id, file_caption, dated):
        self.user_tg_id = user_tg_id
        self.file_id = file_id
        self.file_caption = file_caption
        self.dated = dated

    def __repr__(self):
        return f"{self.user_tg_id} {self.file_id} {self.file_caption} {self.dated}"


class LifeHackVideo(Base):
    __tablename__ = 'life_hack_video'
    user_id = Column(Integer)
    caption_video = Column(String)
    user_name = Column(String)
    file_id = Column(String, unique=True)
    dated = Column(String, primary_key=True)

    def __init__(self, user_id, caption_video, user_name, file_id, dated):
        self.user_id = user_id

        self.caption_video = caption_video
        self.user_name = user_name
        self.file_id = file_id
        self.dated = dated

    def __repr__(self):
        return f"{self.user_id} {self.caption_video} {self.user_name} {self.file_id} {self.dated}"


class ImagesSystem(Base):
    __tablename__ = 'images_system'
    user_tg_id = Column(String)
    file_id = Column(String, unique=True)
    file_caption = Column(String)
    dated = Column(String, primary_key=True)

    def __init__(self, user_tg_id, file_id, file_caption, dated):
        self.user_tg_id = user_tg_id
        self.file_id = file_id
        self.file_caption = file_caption
        self.dated = dated

    def __repr__(self):
        return f"{self.user_tg_id} {self.file_id} {self.file_caption} {self.dated}"


class CloudUser(Base):
    __tablename__ = 'cloud_user'
    user_tg_id = Column(String, primary_key=True)
    parol = Column(String)
    dated = Column(String)

    def __init__(self, user_tg_id, parol, dated):
        self.user_tg_id = user_tg_id
        self.parol = parol
        self.dated = dated

    def __repr__(self):
        return f"{self.user_tg_id} {self.parol} {self.dated}"


class CloudDate(Base):
    __tablename__ = 'cloud_data'
    user_tg_id = Column(String)
    file_id = Column(String, unique=True)
    file_caption = Column(String)
    file_type = Column(String)
    dated = Column(String, primary_key=True)

    def __init__(self, user_tg_id, file_id, file_caption, file_type, dated):
        self.user_tg_id = user_tg_id
        self.file_id = file_id
        self.file_caption = file_caption
        self.file_type = file_type
        self.dated = dated

    def __repr__(self):
        return f"{self.user_tg_id} {self.file_id} {self.file_caption} {self.file_type}{self.dated}"


class LocationMetro(Base):
    __tablename__ = 'metro_location'
    user_tg_id = Column(String)
    metro_name = Column(String, unique=True)
    country = Column(String)
    city = Column(String)
    heading = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    horizontal_accuracy = Column(String)
    live_period = Column(String)
    date = Column(String, primary_key=True)

    def __init__(self, user_tg_id, metro_name, country, city, heading, latitude, longitude, horizontal_accuracy,
                 live_period, dated):
        self.user_tg_id = user_tg_id
        self.metro_name = metro_name
        self.country = country
        self.city = city
        self.heading = heading
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.date = dated

    def __repr__(self):
        return (f'{self.user_tg_id} {self.metro_name} {self.heading} {self.latitude} {self.longitude} '
                f'{self.horizontal_accuracy} {self.live_period} {self.date}')


class Movies(Base):
    __tablename__ = 'movies_table'
    user_tg_id = Column(String)
    movie_code = Column(String, unique=True)
    file_id = Column(String, unique=True)
    file_caption = Column(String)
    file_type = Column(String)
    dated = Column(String, primary_key=True)

    def __init__(self, user_tg_id, movie_code, file_id, file_caption, file_type, dated):
        self.user_tg_id = user_tg_id
        self.movie_code = movie_code
        self.file_id = file_id
        self.file_caption = file_caption
        self.file_type = file_type
        self.dated = dated

    def __repr__(self):
        return f"{self.user_tg_id} {self.movie_code} {self.file_id} {self.file_caption} {self.file_type}{self.dated}"


Base.metadata.create_all(engine)
