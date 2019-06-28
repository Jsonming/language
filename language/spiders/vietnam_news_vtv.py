# -*- coding: utf-8 -*-
import scrapy


class VietnamNewsVtvSpider(scrapy.Spider):
    name = 'vietnam_news_vtv'
    allowed_domains = ['vtv.vn']
    start_urls = ['http://vtv.vn/']

    def parse(self, response):
        pass
