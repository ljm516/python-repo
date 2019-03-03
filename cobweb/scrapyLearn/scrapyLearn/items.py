# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapylearnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MySpiderItem(scrapy.Item):
    url_name = scrapy.Field()
    url_key = scrapy.Field()
    url_cr = scrapy.Field()
    url_addr = scrapy.Field()
