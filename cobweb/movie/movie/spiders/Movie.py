# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector, Request

from movie.movie.items import MovieItem


class MovieSpider(scrapy.Spider):
    name = 'Movie'
    url = 'https://movie.douban.com/top250'
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        item = MovieItem()
        selector = Selector(response=response)
        movies = selector.xpath('//div[@class="info"]')

        for movie in movies:
            title = movie.xpath('div[@class="hd"]/a/span/text()').extract()
            full_title = ''

            for each in title:
                full_title += each

            movie_info = movie.xpath('div[@class="bd"]/p/text()').extract()[0]
            star = movie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            quote = movie.xpath('div[@class="bd"]/p/span/text()').extract()

            if quote:
                quote = quote[0]

            else:
                quote = ''

            item['title'] = full_title
            item['movie_info'] = movie_info
            item['quote'] = quote
            item['star'] = star

            yield item

        next_page = selector.xpath('//span[@class="next"]/link/@href').extract()

        if next_page:
            next_page = next_page[0]
            print(self.url + str(next_page))
            yield Request(self.url + str(next_page), callback=self.parse)
