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

def get_family_members():
    for person in Person.select():
        print("Name: {} / Birthday: {}".format(person.name,person.bday))

def get_family_member(identificador):
    grandma_ana = Person.select().where(Person.id == identificador).get()
    print("{}'s birthday is {}".format(grandma_ana.name,grandma_ana.bday))

def get_any_member(identificador):
    family_member = Person.get(Person.id == identificador)
    print("{}'s birthday is {}".format(family_member.name,family_member.bday))

def get_pets():
    for pet in Pet.select():
        print("Name: {} / Animal type: {}".format(pet.name,pet.animal_type))

def delete_pets(name):
    query = Pet.delete().where(Pet.name == name)
    deleted_entries = query.execute()
    print("{} deleted record(s)".format(deleted_entries))

def delete_pet(name):
    the_pet = Pet.get(Pet.name == name)
    deleted_entry = the_pet.delete_instance()
    print("{} deleted record(s)".format(deleted_entry))

create_and_connect()
## create_family_members()
## get_family_members()
## get_family_member(9)
## get_any_member(8)

delete_pet("Puffy")
get_pets()