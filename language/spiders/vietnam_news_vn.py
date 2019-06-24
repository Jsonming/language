# -*- coding: utf-8 -*-
import scrapy
from ..items import NewsContentItem
from ..items import NewsLink


class VietnamNewsVnSpider(scrapy.Spider):
    name = 'vietnam_news_vn'
    allowed_domains = ['vnexpress.net/thoi-su']
    start_urls = ['https://vnexpress.net/thoi-su']

    def parse(self, response):
        links = response.xpath('/html/body/section/section[1]/article/h4/a[1]/@href').extract()

        for url in links:
            item = NewsLink()
            item['url'] = url
            item["ori_url"] = response.url
            yield item

        nest_link = response.xpath('//*[@id="pagination"]/a[@class="next"]/@href').extract()
        if nest_link:
            next_page_url = 'https://vnexpress.net' + nest_link[0]
            yield scrapy.Request(url=next_page_url, callback=self.parse, dont_filter=True)

    # def parse_item(self, response):
    #     description = response.xpath('//section/p/text()').extract()
    #     paragraph_new = response.xpath('//article//p/text()').extract()
    #     content = ' '.join(description + paragraph_new).replace('\n', '')
    #     item = NewsContentItem()
    #     item['url'] = response.url
    #     item['content'] = content
    #     file = r"C:\Users\Administrator\Desktop\vietnam_news_content_new.txt"
    #     if content:
    #         with open(file, 'a', encoding='utf8') as f:
    #             f.write(content + "\n")
