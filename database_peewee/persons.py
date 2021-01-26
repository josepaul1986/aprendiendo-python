from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    bday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db
