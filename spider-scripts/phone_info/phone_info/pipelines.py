# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from peewee import MySQLDatabase, Model, PrimaryKeyField, CharField

MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'ljm'
MYSQL_PASSWD = ''
MYSQL_DB = 'spider'

db = MySQLDatabase(MYSQL_DB, host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWD)


class BaseModel(Model):
    class Meta:
        database = db


class Phone_Info(BaseModel):
    id = PrimaryKeyField()
    number = CharField()
    head = CharField()
    province = CharField()
    city = CharField()
    operator = CharField()


class PhoneInfoPipeline(object):

    def process_item(self, item, spider):
        phone_info = Phone_Info(number=item['phone'], operator=item['operator'],
                                head=item['head'], province=item['province'], city=item['city'])
        phone_info.save()
        return item
