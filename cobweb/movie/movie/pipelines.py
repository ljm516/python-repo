# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class MoviePipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='cobweb')

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "INSERT INTO movie (name, movieInfo, star, quote) VALUES ('" + item['title'] \
              + "', '" + str(item['movie_info']) + "', '" + item['star'] + "', '" + item['quote'] + "')"
        print('{sql}'.format(sql=sql))

        self.cursor.execute(sql)
        self.conn.autocommit(True)

        return item
