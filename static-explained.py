# when to use class method and static method
import os
import csv

class Person:
    def __init__(self):
        pass
    @staticmethod
    def is_age_valid(age):
        return 0 < age < 150


print(Person.is_age_valid(35)) # this is a static method

class Database:

    @classmethod
    def connect(cls, uri):
        print("Connecting to database {}".format(uri))
        pass

    @classmethod
    def read_csv(cls, uri):
        with open(uri, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            items = list(reader)
        return items

Database.connect('db://localhost:5432')
print(Database.read_csv('items.csv'))