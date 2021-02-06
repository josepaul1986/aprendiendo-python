from typing import OrderedDict
from peewee import *
from datetime import *

db = SqliteDatabase('journal.db')

menu_items = OrderedDict([
    ('a','add entry'),
    ('v','view entry'),
    ('d','delete entry')
])

class Entry(Model):
    #content
    #timestamp
    content = TextField()
    timestamp = DateTimeField(default=datetime.now())

    class Meta:
        database = db

def create_and_connect():
    """ Connects to the database and creates the tables """
    db.connect()
    db.create_tables([Entry],safe=True)

def menu_loop():
    """ Show Menu """ ##Docstrings comentarios que seran accesibles desde los help docs desde python help.

def add_entry():
    """ Add Entry """

def view_entries():
    """ View all entries """

def delete_entry(entry):
    """ Delete entry """

if __name__ == '__main__': ## Permite no ejecutar nada sin invocarlo previamente en el codigo al momento de importar.
    create_and_connect()
    menu_loop()
