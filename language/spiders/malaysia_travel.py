# -*- coding: utf-8 -*-
import scrapy


class MalaysiaTravelSpider(scrapy.Spider):
    name = 'malaysia_travel'
    allowed_domains = ['http://www.malaysia.travel']
    start_urls = ['http://www.malaysia.travel/zh-cn/cn/about-malaysia/practical-info/say-it-in-malay']

    def parse(self, response):
        with open('C:\\Users\\Administrator\\Desktop\\word.txt', 'a', encoding='utf8')as f:
            trs = response.xpath('//div[@class="first"]//tbody/tr')
            for tr in trs:
                word = tr.xpath('./td/text()')[1].extract()
                print(word)
                # word = word.strip()
                f.write(word + ',')
