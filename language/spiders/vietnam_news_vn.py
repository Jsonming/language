# -*- coding: utf-8 -*-
import scrapy
from ..items import NewsContentItem


class VietnamNewsVnSpider(scrapy.Spider):
    name = 'vietnam_news_vn'
    allowed_domains = ['vnexpress.net/thoi-su']
    start_urls = ['https://vnexpress.net/thoi-su-p2']

    def parse(self, response):
        links = response.xpath('/html/body/section[2]/section[1]/article/h4/a[1]/@href').extract()

        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_item, dont_filter=True)

        current_page = response.url.split('-')[-1].replace('p', '')
        if int(current_page) < 51:
            next_page_url = 'https://vnexpress.net/thoi-su-p{}'.format(int(current_page) + 1)
            yield scrapy.Request(url=next_page_url, callback=self.parse, dont_filter=True)

    def parse_item(self, response):
        description = response.xpath('//section/p/text()').extract()
        paragraph_new = response.xpath('//article//p/text()').extract()
        content = ' '.join(description + paragraph_new).replace('\n', '')
        item = NewsContentItem()
        item['url'] = response.url
        item['content'] = content
        file = r"C:\Users\Administrator\Desktop\vietnam_news_content_new.txt"
        if content:
            with open(file, 'a', encoding='utf8') as f:
                f.write(content + "\n")
