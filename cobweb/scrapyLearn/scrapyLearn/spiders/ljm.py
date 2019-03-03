# -*- coding: utf-8 -*-

import scrapy

from scrapyLearn.items import MySpiderItem


class LjmSpider(scrapy.Spider):
    name = 'ljm'
    allowed_domains = ['baidu.com']
    start_urls = [
        'https://www.baidu.com/s?wd=java'
    ]

    # 实现参数传递
    # def __init__(self, myurl=None, *args, **kwargs):
    #     super(LjmSpider, self).__init__(*args, **kwargs)
    #     print('要爬取的网页地址: ', myurl)

    #     # 重新定义 start_urls 属性，属性值为传进来的参数值
    #     self.start_urls = [myurl]

    def parse(self, response):
        item = MySpiderItem()
        body = response.body
        print('响应内容: {data}'.format(data=body))
        item['url_name'] = response.xpath("/html/head/title/text()")
        print('url_name:', item['url_name'])
