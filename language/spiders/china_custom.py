# -*- coding: utf-8 -*-
import scrapy


class ChinaCustomSpider(scrapy.Spider):
    name = 'china_custom'
    allowed_domains = ['www.chinaunicombidding.cn']
    start_urls = ['http://www.chinaunicombidding.cn/jsp/cnceb/web/info1/infoList.jsp?page=3']

    def parse(self, response):
        print(response.text)



