
from peewee import *
import datetime
from flask_login import UserMixin

DATABASE = SqliteDatabase('pets.sqlite')

class User(UserMixin, Model):
    username=CharField(unique=True)
    email=CharField(unique=True)
    password=CharField()
    phone=CharField()

    class Meta:
        database = DATABASE



class Pet(Model):
    petName = CharField()
    aboutPet=CharField()
    dateLost=DateTimeField(default=datetime.datetime.now)
    found=CharField()
    owner=ForeignKeyField(User, backref='pets')
    photo=CharField()



    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Pet], safe=True)
    print("TABLES Created")
    DATABASE.close()
