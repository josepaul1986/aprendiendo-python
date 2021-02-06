from peewee import *

db = SqliteDatabase('journal.db')

class Entry(Model):
    #content
    #timestamp

    class Meta:
        database = db

def menu_loop():
    """ Show Menu """

def add_entry():
    """ Add Entry """

def view_entries():
    """ View all entries """

def delete_entry(entry):
    """ Delete entry """