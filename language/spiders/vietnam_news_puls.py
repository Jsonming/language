# -*- coding: utf-8 -*-
import scrapy


class VietnamNewsPulsSpider(scrapy.Spider):
    name = 'vietnam_news_puls'
    allowed_domains = ['www.vietnamplus.vn']
    start_urls = ['http://www.vietnamplus.vn/']

    def parse(self, response):
        pass
