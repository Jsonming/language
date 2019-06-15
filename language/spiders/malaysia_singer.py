# -*- coding: utf-8 -*-
import scrapy


class MalaysiaSingerSpider(scrapy.Spider):
    name = 'malaysia_singer'
    allowed_domains = ['http://ms.wikipedia.org/wiki/Senarai_penyanyi_Malaysia']
    start_urls = ['http://ms.wikipedia.org/wiki/Senarai_penyanyi_Malaysia/']

    def parse(self, response):
        content = response.xpath('//*[@id="mw-content-text"]/div//div/ul//li/text()').extract()
        with open('C:\\Users\\Administrator\\Desktop\\word2.txt', 'a', encoding='utf8')as f:
            print(content)
