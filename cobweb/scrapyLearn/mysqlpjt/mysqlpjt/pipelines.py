# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class MysqlpjtPipeline(object):

    def __init__(self):
        # 与数据库建立连接
        self.conn = pymysql.connect(host='localhost', user='root', passwd='root', db='cobweb')

    def process_item(self, item, spider):
        name = item['name'][0]
        key = item['keywd'][0]
        self.conn.autocommit(True)

        sql = "insert into mytb (title, keywd) VALUES ('" + name + "', '" + key + "')"
        print('sql: {sql}'.format(sql=sql))
        self.conn.query(sql)

        return item

    def close_spider(self, spider):
        self.conn.connect()
