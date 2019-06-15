# -*- coding: utf-8 -*-
import scrapy


class FoodpandaSpider(scrapy.Spider):
    name = 'foodpanda'
    allowed_domains = ['www.foodpanda.my/ms/city/kuala-lumpur']
    start_urls = ['http://www.foodpanda.my/ms/city/bayan-baru/',
                  'http://www.foodpanda.my/ms/city/petaling-jaya/',
                  'http://www.foodpanda.my/ms/city/puchong/',
                  'http://www.foodpanda.my/ms/city/shah-alam/',
                  'http://www.foodpanda.my/ms/city/cyberjaya/',
                  'http://www.foodpanda.my/ms/city/johor-bahru?r=1',
                  ]

    def parse(self, response):
        names = response.xpath('//span[@class="name fn"]/text()').extract()
        print(names)
        print(response.url)
        with open('C:\\Users\\Administrator\\Desktop\\foodpanda_stores_name.txt', 'a', encoding='utf8')as f:
            for name in names:
                f.write(name + ',')
