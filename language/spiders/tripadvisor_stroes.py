# -*- coding: utf-8 -*-
import scrapy


class TripadvisorStroesSpider(scrapy.Spider):
    name = 'tripadvisor_stroes'
    allowed_domains = ['www.tripadvisor.co.id']
    # start_urls = ['https://www.tripadvisor.co.id/RestaurantSearch?Action=PAGE&geo=306997&ajax=1&itags=10591&sortOrder=relevance&o=a{}&availSearchEnabled=false'.format(i) for i in range(0, 751, 30)]
    start_urls = ['https://www.tripadvisor.cn/RestaurantSearch?Action=PAGE&geo=298570&ajax=1&itags=10591&sortOrder=relevance&o=a{}&availSearchEnabled=false'.format(i) for i in range(1300, 2300, 30)]

    def parse(self, response):
        names = response.xpath('//a[@class="property_title"]/text()').extract()
        print(names)
        print(response.url)
        with open('C:\\Users\\Administrator\\Desktop\\tripadvisor_stores_name.txt', 'a', encoding='utf8')as f:
            for name in names:
                f.write(name + ',')
