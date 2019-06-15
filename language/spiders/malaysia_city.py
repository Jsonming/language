# -*- coding: utf-8 -*-
import scrapy


class MalaysiaCitySpider(scrapy.Spider):
    name = 'malaysia_city'
    allowed_domains = ['https://ms.wikipedia.org']
    start_urls = ['https://ms.wikipedia.org/wiki/Negeri_dan_Wilayah_Persekutuan_di_Malaysia']

    def parse(self, response):
        with open('C:\\Users\\Administrator\\Desktop\\单词\\word.txt', 'a', encoding='utf8')as f:
            trs = response.xpath('//div/[@class="first"]//tbody/tr').extract()
            for tr in trs:
                word = tr.xpath('./td/text()')[1].extract()
                word = word.strip()
                f.write(word)

