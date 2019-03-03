# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mycrawlspider.items import MycrawlspiderItem


class LjmingSpider(CrawlSpider):
    name = 'ljming'
    allowed_domains = ['sohu.com']
    start_urls = ['http://sohu.com/']

    #  设置自动爬行的规则： LinkExtractor: 链接提取器，一般用来提取页面中满足条件的链接。

    '''
        allow: 提取符合对应正则表达式的链接
        deny: 不提取符合对应正则表达式的链接
        restrict_xpaths: 使用 xpath 表达式与 allow 共同作用提取出同事符合对应 xpath 表达式和对应正则表达式的链接
        allow_domains: 允许提取的域名，比如我们只想提取某个域名下的链接是会使用
        deny_domains: 禁止提取的域名，比如我们需要限制一定不提取某个域名下的链接时会使用    
    '''

    rules = (
        Rule(LinkExtractor(allow=('.*?/n.*?shtml'), allow_domains=('sohu.com')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = MycrawlspiderItem()
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        i['name'] = response.xpath('/html/head/title/text()').extract()
        i['link'] = response.xpath('//link[@rel="canonical"]/@herf').extract()
        return i
