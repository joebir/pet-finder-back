from peewee import *
import datetime
from flask_login import UserMixin

DATABASE = SqliteDatabase('dogs.sqlite')

class User(UserMixin, Model):
    username=CharField(unique=True)
    email=CharField(unique=True)
    password=CharField()
    phone=numbersd

    class Meta:
        database = DATABASE



class Pet(Model):
    #coumns
    name = CharField()
    owner = ForeignKeyField(User, backref='dogs')
    type = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    date_lost = DateTimeField(default=datetime.datetime.now)
    pet_detail:CharField()

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Pet], safe=True)
    print("TABLES Created")
    DATABASE.close()
