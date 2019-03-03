from peewee import *

db = SqliteDatabase('people.db')


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db


class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db


db.connect()

uncle_bob = Person.select().where(Person.name == 'Bob').get()
herb = Person.select().where(Person.name == 'Herb').get()

print (uncle_bob.name)
print (herb.name)

bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
print('create bob_kitty success')
herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
print('create herb_fido success')
herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
print('create herb_mittens success')
herb_mittens_jr = Pet.create(owner=herb, name='Mittents Jr', animal_type='cat')
print('create herb_mittens_jr success')
