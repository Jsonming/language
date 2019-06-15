# -*- coding: utf-8 -*-
import scrapy


class YeduArticleSpider(scrapy.Spider):
    name = 'yedu_article'
    allowed_domains = ['www.ryedu.net/Article/201703/54950.html']
    start_urls = ['http://www.ryedu.net/Article/201703/54950.html']

    def parse(self, response):
        with open('C:\\Users\\Administrator\\Desktop\\word2.txt', 'a', encoding='utf8')as f:
            trs = response.xpath('//div[@class="c_content_overflow"]//text()').extract()
            for tr in trs:
                if '\xa0' in tr:
                    word = tr.split('\xa0')[1]
                    print(word)
                    f.write(word + ',')