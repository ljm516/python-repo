# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem

class MyxmlspiderSpider(XMLFeedSpider):
    name = 'myxmlspider'
    allowed_domains = ['sina.com.cn']
    # xml 源地址
    start_urls = ['http://blog.sina.com.cn/rss/1615888477.xml']
    
    iterator = 'iternodes' # you can change this; see the docs
    
    # 开始迭代的节点
    itertag = 'rss' # change it accordingly

    def parse_node(self, response, selector):
        i = MyxmlItem()

        # 使用 Xpath 表达式将对应信息提取处理，并存储到对应的 item 中
        i['title'] = selector.select('/rss/channel/item/title/text()').extract()
        i['link'] = selector.select('/rss/channel/item/link/text()').extract()
        i['author'] = selector.select('/rss/channel/item/author/text()').extract()

        # 通过 for 循环以此遍历提取出来存在 item 中的信息并输出
        for j in range(len(i['title'])):
            print('第' + str(j+1) + '篇文章')
            print('标题:', i['title'][j])
            print('对应的链接: ', i['link'][j])
            print('对应的作者: ', i['author'][j])

            print('---------------------------------------')
        return i
