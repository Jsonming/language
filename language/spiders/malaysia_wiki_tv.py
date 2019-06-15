# -*- coding: utf-8 -*-
import scrapy
import re

class MalaysiaWikiTvSpider(scrapy.Spider):
    name = 'malaysia_wiki_tv'
    allowed_domains = ['zh.wikipedia.org/wiki/Ntv7#马来语']
    start_urls = ['http://zh.wikipedia.org/wiki/Ntv7#马来语/']

    def parse(self, response):
        content = response.xpath('//*[@id="mw-content-text"]/div/ul[3]//li/text()').extract()
        fil = re.compile(u'[^a-zA-Z.-]+', re.UNICODE)

        with open('C:\\Users\\Administrator\\Desktop\\word2.txt', 'a', encoding='utf8')as f:
            for word in content:
                f.write(word + ',')