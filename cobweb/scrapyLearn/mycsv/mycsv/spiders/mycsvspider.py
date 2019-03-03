# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from mycsv.items import MycsvItem


class MycsvspiderSpider(CSVFeedSpider):
    name = 'mycsvspider'
    allowed_domains = ['iqianyue.com']

    # 定义要处理的 csv 文件所在地址
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/mydata.csv']
    # 定义 header
    headers = ['name', 'sex', 'addr', 'email']
    # 定义 分隔符
    delimiter = ','

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = MycsvItem()
        
        i['name'] = row['name'].encode()
        i['sex'] = row['sex'].encode()

        print('name: ', i['name'], ' sex: ', i['sex'])
        print('---------------------------------------')
        return i
