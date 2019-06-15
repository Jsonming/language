# -*- coding: utf-8 -*-
import json
import scrapy
import re
from lxml.html import etree
from ..items import IndonesiaNewsContentItem


class IndonesiaKompasNewsSpider(scrapy.Spider):
    name = 'indonesia_kompas_news'
    allowed_domains = ['https://news.kompas.com']

    # 第一类新闻
    urls = ['https://news.kompas.com/search/all/{}'.format(i) for i in range(589)]
    # urls = ['https://bola.kompas.com/search/all/{}'.format(i) for i in range(667)]
    # urls = ['https://tekno.kompas.com/search/all/{}'.format(i) for i in range(667)]
    # urls = ['https://sains.kompas.com/search/all/{}'.format(i) for i in range(667)]
    # urls = ['https://entertainment.kompas.com/search/all/{}'.format(i) for i in range(667)]
    # urls = ['https://otomotif.kompas.com/search/all/{}'.format(i) for i in range(667)]
    # urls = ['https://lifestyle.kompas.com/search/all/{}'.format(i) for i in range(667)]
    # urls = ['https://properti.kompas.com/search/all/{}'.format(i) for i in range(667)]
    # urls = ['https://travel.kompas.com/search/all/{}'.format(i) for i in range(667)]
    # urls = ['https://edukasi.kompas.com/indeks/{}'.format(i) for i in range(11)]
    # urls = ['https://foto.kompas.com/photo/{}'.format(i) for i in range(6)]
    # urls = ['https://jeo.kompas.com/search?page={}'.format(i) for i in range(12)]

    start_urls = ['https://bola.kompas.com/search/all/1']

    # 第二类新闻
    # def start_requests(self):
    #     for i in range(3):
    #         url = 'https://money.kompas.com/home/more/{}'.format(i)
    #         url = 'https://kolom.kompas.com/home/more/{}'.format(i)
    #         headers = {
    #             "referer": "https://money.kompas.com/",
    #             "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    #             "x-requested-with": "XMLHttpRequest"
    #         }
    #         yield scrapy.FormRequest(url=url, headers=headers, formdata={}, callback=self.parse)

    def parse(self, response):
        url = response.url
        category = url.split('/')[2].split('.')[0]
        class_one = {'news', 'bola', 'tekno', 'sains', 'entertainment', 'otomotif', 'lifestyle', 'properti', 'travel',
                     'foto', 'edukasi', 'jeo'}
        print(category)
        if category in class_one:
            links = response.xpath('//a[@class="article__link"]/@href').extract()
            for link in links:
                url = link + '?page=all'
                yield scrapy.Request(url=url, callback=self.parse_item, dont_filter=True)
        else:
            data = json.loads(response.body.decode('utf8'))
            result = data.get("result")
            html = etree.HTML(result)
            links = html.xpath('//a/@href')
            for link in links:
                yield scrapy.Request(url=link, callback=self.parse_item, dont_filter=True)

    def parse_item(self, response):
        content = response.xpath('//div[@class="read__content"]//text()').extract()
        item = IndonesiaNewsContentItem()
        item['url'] = response.url
        item['content'] = ''.join(content)
        yield item
