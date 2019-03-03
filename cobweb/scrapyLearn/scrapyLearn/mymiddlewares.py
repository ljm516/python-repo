# 下载中间件

import random
from scrapyLearn.settings import IPPOOL
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware

class IPPOOLS(HttpProxyMiddleware):
	def __init__(self, ip=''):
		self.ip = ip

	def process_request(self, request, spider):
		thisip = random.choice(IPPOOL)

		print('current ip: ', thisip['ipaddr'])
		request.meta['proxy'] = 'http://' + thisip['ipaddr']
