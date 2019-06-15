# -*- coding: utf-8 -*-
import scrapy


class MalaysiaSongSpider(scrapy.Spider):
    name = 'malaysia_song'
    allowed_domains = ['www.youtube.com/playlist?list=PLgNjz5kKawRiPXT7l3XT60v3iWogBvGP0']
    start_urls = ['http://www.youtube.com/playlist?list=PLgNjz5kKawRiPXT7l3XT60v3iWogBvGP0/']

    def parse(self, response):
        content = response.xpath('//s/text()').extract()
        with open('C:\\Users\\Administrator\\Desktop\\youtu.html', 'w', encoding='utf8')as f:
            f.write(response.body)
