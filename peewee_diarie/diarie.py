from re import search
from time import strftime
from typing import OrderedDict
from datetime import *

import sys

from peewee import *


db = SqliteDatabase('journal.db')


class Entry(Model):
    # content
    # timestamp
    content = TextField()
    timestamp = DateTimeField(default=datetime.now())

    class Meta:
        database = db


def create_and_connect():
    """ Connects to the database and creates the tables """
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """ Show Menu """  # Docstrings comentarios accesibles desde los help docs.
    choice = None
    while choice != 'q':
        print("\nPress 'q' to quit.")
        for key, value in menu.items():
            print("{}) {}".format(key, value.__doc__))
        choice = input("Action: ").lower().strip()

        if choice in menu:
            menu[choice]()


def add_entry():
    """ Add Entry """
    print("Enter your thoughts.")
    print("\n Press ctrl+D (new line and ctrl+Z on Windows) to finish.\n")
    data = sys.stdin.read().strip()

    if data:
        ans = input("Do you want to save your entry?[y/n]")
        if ans.lower().strip() != 'n':
            Entry.create(content=data)
            print("You entry was saved successfully!")


def view_entries(search_query=None):
    """ View all entries """
    entries = Entry.select().order_by(Entry.timestamp.desc())

    if search_query:
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        print("\n")
        print(timestamp)
        print('+'*len(timestamp))
        print(entry.content)
        print('+'*len(timestamp))
        print("\n")
        print("n) next entry")
        print("d) delete entry")
        print("r) return to menu")

        next_action = input("Action [n/d/r]: ").lower().strip()

        if next_action == 'r':
            break
        elif next_action == 'd':
            delete_entry(entry)


def search_entries():
    """ Search entries """
    search_query = input("Search query: ").strip()
    view_entries(search_query)


def delete_entry(entry):
    """ Delete an entry """
    action = input("Are you sure? [y/n] ")

    if action == 'y':
        entry.delete_instance()
        print("Entry was succesfully deleted!")

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries)
])

if __name__ == '__main__':
    # Permite no ejecutar nada sin invocarlo previamente ...
    # en el codigo al momento de importar.
    create_and_connect()
    menu_loop()
