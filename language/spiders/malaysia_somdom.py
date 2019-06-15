# -*- coding: utf-8 -*-
import scrapy
import re

class MalaysiaSomdomSpider(scrapy.Spider):
    name = 'malaysia_somdom'
    allowed_domains = ['www.somdom.com/malay/t6411']
    start_urls = ['http://www.somdom.com/malay/t6411/',
                  'http://www.somdom.com/malay/t6411-2',
                  'http://www.somdom.com/malay/t6411-3',
                  'http://www.somdom.com/malay/t6411-4',
                  ]

    def parse(self, response):
        content = response.xpath('//*[@id="J_read_main"]//div/text()').extract()
        fil = re.compile(u'[^a-zA-Z.-]+', re.UNICODE)

        with open('C:\\Users\\Administrator\\Desktop\\word2.txt', 'a', encoding='utf8')as f:
            for word in content:
                word = word.strip()
                if word:
                    malaysia_word = fil.sub(' ', word)
                    print(malaysia_word)
                    f.write(malaysia_word + ',')