from main import db
from flask import Blueprint
from main import bcrypt
from models.labels import Label
from models.musicians import Musician
from models.songs import Song
from models.credits import Credit
from datetime import time, date


db_commands = Blueprint("db", __name__)


@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")


@db_commands.cli.command("seed")
def seed_db():
    # Create the labels first
    label1 = Label(
        name="Warner Records",
        type="Major",
    )
    db.session.add(label1)

    label2 = Label(
        name="Sony Records",
        type="Major",
    )
    db.session.add(label2)

    label3 = Label(
        name="Universal Records",
        type="Major",
    )
    db.session.add(label3)

    label4 = Label(
        name="Blonded Records",
        type="Independent",
    )
    db.session.add(label4)

    label5 = Label(
        name="Golf Records",
        type="Independent",
    )
    db.session.add(label5)
    db.session.commit()

    # Create Admin Musician
    admin_musician = Musician(
        first_name="Admin",
        last_name="Admin",
        profession="Admin",
        phone_number="404",
        email="admin@admin.com",
        password=bcrypt.generate_password_hash("password123").decode("utf-8"),
        admin=True
    )
    db.session.add(admin_musician)

    # Create Musicians
    musician1 = Musician(
        first_name="Frank",
        last_name="Ocean",
        profession="Singer",
        phone_number="404",
        email="frank@email.com",
        password=bcrypt.generate_password_hash("123456").decode("utf-8"),
        label_id=label4.id
    )
    db.session.add(musician1)

    musician2 = Musician(
        first_name="Mike",
        last_name="Dean",
        profession="Producer",
        phone_number="404",
        email="mike@email.com",
        password=bcrypt.generate_password_hash("123456").decode("utf-8"),
        label_id=label1.id
    )
    db.session.add(musician2)

    musician3 = Musician(
        first_name="Jack",
        last_name="Antonoff",
        profession="Songwriter",
        phone_number="404",
        email="jack@email.com",
        password=bcrypt.generate_password_hash("123456").decode("utf-8"),
        label_id=label3.id
    )
    db.session.add(musician3)

    musician4 = Musician(
        first_name="Steve",
        last_name="Lacey",
        profession="Guitarist",
        phone_number="404",
        email="steve@email.com",
        password=bcrypt.generate_password_hash("123456").decode("utf-8"),
        label_id=label2.id
    )
    db.session.add(musician4)

    musician5 = Musician(
        first_name="Tyler",
        last_name="Okonma",
        profession="Rapper",
        phone_number="404",
        email="tyler@email.com",
        password=bcrypt.generate_password_hash("123456").decode("utf-8"),
        label_id=label5.id
    )
    db.session.add(musician5)

    musician6 = Musician(
        first_name="Kenny",
        last_name="Beats",
        profession="Pianist",
        phone_number="404",
        email="kenny@email.com",
        password=bcrypt.generate_password_hash("123456").decode("utf-8"),
        label_id=label2.id
    )
    db.session.add(musician6)

    musician7 = Musician(
        first_name="Thunder",
        last_name="Cat",
        profession="Bassist",
        phone_number="404",
        email="thunder@email.com",
        password=bcrypt.generate_password_hash("123456").decode("utf-8"),
        label_id=label3.id
    )
    db.session.add(musician7)

    musician8 = Musician(
        first_name="Anderson",
        last_name="Paak",
        profession="Drummer",
        phone_number="404",
        email="anderson@email.com",
        password=bcrypt.generate_password_hash("123456").decode("utf-8"),
        label_id=label3.id
    )
    db.session.add(musician8)

    musician9 = Musician(
        first_name="Jeff",
        last_name="Ellis",
        profession="Mixing Engineer",
        phone_number="404",
        email="jeff@email.com",
        password=bcrypt.generate_password_hash("123456").decode("utf-8"),
    )
    db.session.add(musician9)

    musician10 = Musician(
        first_name="Dave",
        last_name="Pensado",
        profession="Mastering Engineer",
        phone_number="404",
        email="dave@email.com",
        password=bcrypt.generate_password_hash("123456").decode("utf-8"),
    )
    db.session.add(musician10)
    db.session.commit()

    # Create Songs
    song1 = Song(
        title="Ivy",
        genre="Alternative",
        duration=time(hour=0, minute=4, second=9),
        date_finished=date(2016, 8, 1)
    )
    db.session.add(song1)

    song2 = Song(
        title="Bad Habit",
        genre="Pop",
        duration=time(hour=0, minute=3, second=52),
        date_finished=date(2022, 1, 30)
    )
    db.session.add(song2)

    song3 = Song(
        title="Suede",
        genre="RNB",
        duration=time(hour=0, minute=2, second=54),
        date_finished=date(2016, 6, 6)
    )
    db.session.add(song3)

    song4 = Song(
        title="911",
        genre="Rap",
        duration=time(hour=0, minute=4, second=15),
        date_finished=date(2017, 8, 8)
    )
    db.session.add(song4)

    song5 = Song(
        title="Biking",
        genre="RNB",
        duration=time(hour=0, minute=4, second=37),
        date_finished=date(2017, 9, 9)
    )
    db.session.add(song5)

    song6 = Song(
        title="Thinkin Bout You",
        genre="Pop",
        duration=time(hour=0, minute=3, second=20),
        date_finished=date(2012, 6, 11)
    )
    db.session.add(song6)
    db.session.commit()

    # Create Credits
    credit1 = Credit(
        description="Vocals, lyrics",
        contribution_date=date(2011, 1, 1),
        song_id=song1.id,
        musician_id=musician2.id
    )
    db.session.add(credit1)

    credit2 = Credit(
        description="Vocals, lyrics",
        contribution_date=date(2014, 3, 3),
        song_id=song4.id,
        musician_id=musician2.id
    )
    db.session.add(credit2)

    credit3 = Credit(
        description="Vocals, lyrics",
        contribution_date=date(2015, 1, 1),
        song_id=song5.id,
        musician_id=musician2.id
    )
    db.session.add(credit3)

    credit4 = Credit(
        description="Vocals, lyrics",
        contribution_date=date(2014, 12, 11),
        song_id=song6.id,
        musician_id=musician2.id
    )
    db.session.add(credit4)

    credit5 = Credit(
        description="Production",
        contribution_date=date(2011, 1, 1),
        song_id=song3.id,
        musician_id=musician3.id
    )
    db.session.add(credit5)

    credit6 = Credit(
        description="Songwriting",
        contribution_date=date(2014, 12, 11),
        song_id=song6.id,
        musician_id=musician4.id
    )
    db.session.add(credit6)

    credit7 = Credit(
        description="Vocals, lyrics, production",
        contribution_date=date(2020, 1, 11),
        song_id=song2.id,
        musician_id=musician5.id
    )
    db.session.add(credit7)

    credit8 = Credit(
        description="Guitar",
        contribution_date=date(2017, 12, 11),
        song_id=song4.id,
        musician_id=musician5.id
    )
    db.session.add(credit8)

    credit9 = Credit(
        description="Lyrics",
        contribution_date=date(2015, 2, 2),
        song_id=song4.id,
        musician_id=musician7.id
    )
    db.session.add(credit9)

    credit10 = Credit(
        description="Rap feature",
        contribution_date=date(2015, 2, 2),
        song_id=song5.id,
        musician_id=musician6.id
    )
    db.session.add(credit10)

    credit11 = Credit(
        description="Production",
        contribution_date=date(2015, 12, 11),
        song_id=song6.id,
        musician_id=musician7.id
    )
    db.session.add(credit11)

    credit12 = Credit(
        description="Bass guitar",
        contribution_date=date(2019, 10, 5),
        song_id=song3.id,
        musician_id=musician8.id
    )
    db.session.add(credit12)

    credit13 = Credit(
        description="Drums, vocals",
        contribution_date=date(2013, 5, 5),
        song_id=song3.id,
        musician_id=musician9.id
    )
    db.session.add(credit13)

    credit14 = Credit(
        description="Mixing",
        contribution_date=date(2012, 9, 5),
        song_id=song6.id,
        musician_id=musician10.id
    )
    db.session.add(credit14)

    credit15 = Credit(
        description="Mixing",
        contribution_date=date(2011, 1, 1),
        song_id=song1.id,
        musician_id=musician10.id
    )
    db.session.add(credit15)

    credit16 = Credit(
        description="Mastering",
        contribution_date=date(2023, 1, 1),
        song_id=song1.id,
        musician_id=musician1.id
    )
    db.session.add(credit16)
    db.session.commit()

    print("Tables seeded")


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")
