#!/usr/bin/env python3
# coding=utf-8

from datetime import date

from peewee import *

MYSQL_HOST = '127.0.0.1'
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = ''
MYSQL_PORT = 3306
MYSQL_DB = 'people'

MYSQL_DB = MySQLDatabase(MYSQL_DB, host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USERNAME, passwd=MYSQL_PASSWORD)


class BaseModel(Model):
    class Meta:
        database = MYSQL_DB


class Person(BaseModel):
    id = PrimaryKeyField()
    username = CharField()
    address = CharField()
    birthday = DateField()
    age = IntegerField()
    is_vip = BooleanField()
    gender = CharField()


# MYSQL_DB.create_tables([Person])

ljm_db = Person.select().where(Person.username == 'ljm', Person.gender == 'male', Person.birthday == date(1993, 8, 25))
if len(ljm_db) <= 0:
    ljm = Person(username='ljm', address='北京朝阳', birthday=date(1993, 8, 25), age=23, is_vip=True, gender='male')
else:
    print(ljm_db[0].address)

