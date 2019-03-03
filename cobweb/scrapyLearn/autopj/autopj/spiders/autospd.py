# -*- coding: utf-8 -*-
import scrapy
from autopj.items import AutopjItem
from scrapy.http import Request


class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4002203.html']

    def parse(self, response):
        item = AutopjItem()

        item['name'] = response.xpath('//a[@class="pic"]/@title').extract()
        item['price'] = response.xpath('//span[@class="price_n"]/text()').extract()
        item['link'] = response.xpath('//a[@class="pic"]/@href').extract()
        item['comnum'] = response.xpath('//a[@name="P_pl"]/text()').extract()

        yield item

        for i in range(10):
            url = 'http://category.dangdang.com/pg' + str(i) + '-cid4002203.html'

            yield Request(url, callback=self.parse)
