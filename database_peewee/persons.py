from peewee import *
from datetime import date

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    bday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

class Pet(Model):
    owner = ForeignKeyField(Person,related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db

def create_and_connect():
    db.connect()
    db.create_tables([Person,Pet],safe=True)

def create_family_members():
    uncle_tommy = Person(name="Tommy",bday=date(2000,11,11),is_relative=True)
    uncle_tommy.save()

    grandma_ana = Person.create(name="Ana",bday=date(1960,10,10),is_relative=True)
    friend_jose = Person.create(name="Jose",bday=date(1986,10,10),is_relative=False)

    tommys_dog = Pet.create(owner=uncle_tommy,name="Pepe",animal_type="dog")
    annas_cat = Pet.create(owner=grandma_ana,name="Puffy",animal_type="cat")

    tommys_dog.name = "Bryan"
    tommys_dog.save()

create_and_connect()
create_family_members()