# -*- coding: utf-8 -*-
import json

import scrapy
from phone_info.items import PhoneInfoItem


class PhoneSpiderSpider(scrapy.Spider):
    name = 'phone_spider'
    allowed_domains = ['mobsec-dianhua.baidu.com']
    base_url = "http://mobsec-dianhua.baidu.com/dianhua_api/open/location?tel={}"
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(PhoneSpiderSpider, self).__init__(*args, **kwargs)
        phone_head = [1480000, 1650000, 1670000, 1910000, 1620000, 1700000, 1710000]

        for head in phone_head:
            stop_flag = head + 9999
            while head <= stop_flag:
                self.start_urls.append(self.base_url.format(head))
                head += 1

        print("start_urls size={}".format(len(self.start_urls)))

    def parse(self, response):
        rsp_content = response.text
        json_obj = json.loads(rsp_content)

        data_json = json_obj['response']
        rsp_header = json_obj['responseHeader']
        if rsp_header['status'] != 200:
            print("response not success")

        request_phone = response.url.split('=')[1]
        print('request_phone={}'.format(request_phone))

        item = PhoneInfoItem()
        item['phone'] = request_phone
        item['head'] = request_phone[:3]
        if data_json[str(request_phone)] is not None and data_json[request_phone]['detail'] is not None:
            item['operator'] = data_json[request_phone]['detail']['operator']
            item['province'] = data_json[request_phone]['detail']['province']
            item['city'] = data_json[request_phone]['detail']['area'][0]['city']

            print("item={}".format(item))
        else:
            item['operator'] = ''
            item['province'] = ''
            item['city'] = ''

        yield item
