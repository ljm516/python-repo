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


# method 1
grandma_1 = Person.select().where(Person.name == 'Grandma').get()
print(grandma_1.name)

# method 2
grandma_2 = Person.get(Person.name == 'Grandma')
print(grandma_2.name)

for person in Person.select():
    print(person.name, person.birthday, person.is_relative)

for pet in Pet.select().where(Pet.animal_type == 'cat'):
    print(pet.name, pet.owner.name)
print('==============================')
for pet in Pet.select(Pet, Person).join(Person).where(Pet.animal_type == 'cat').order_by(Pet.name):
    print(pet.name, pet.owner.name)

print('==============================')

for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
    print(pet.name)

for person in Person.select().order_by(Person.birthday.desc()):
    print(person.name, person.birthday)
