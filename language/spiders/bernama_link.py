# -*- coding: utf-8 -*-
import scrapy
from ..items import NewsLinkItem


class BernamaLinkSpider(scrapy.Spider):
    name = 'bernama_link'
    allowed_domains = ['www.bernama/bm/dunia/list.php']
    urls = ["http://www.bernama.com/bm/am/list.php?page={}".format(i) for i in range(1, 182)]
    urls.extend(["http://www.bernama.com/bm/ekonomi/list.php?page={}".format(i) for i in range(1, 39)])
    urls.extend(["http://www.bernama.com/bm/ekonomi/pasaran/list.php?page={}".format(i) for i in range(1, 20)])
    urls.extend(["http://www.bernama.com/bm/politik/list.php?page={}".format(i) for i in range(1, 14)])
    urls.extend(["http://www.bernama.com/bm/sukan/list.php?page={}".format(i) for i in range(1, 27)])
    urls.extend(["http://www.bernama.com/bm/rencana/list.php?page={}".format(i) for i in range(1, 3)])
    urls.extend(["http://www.bernama.com/bm/dunia/list.php?page={}".format(i) for i in range(1, 13)])
    start_urls = urls

    def parse(self, response):
        req_url = response.url
        category = req_url.split('/')[-2]
        category_url = req_url.split('?')[0]
        category_url = category_url.replace('list.php', '')
        teasers = response.xpath('//div[@class="w3-justify"]')
        for teaser in teasers:
            short_url = teaser.xpath('.//a/@href').extract()[0]
            url = category_url + short_url
            item = NewsLinkItem()
            item['category'] = category
            item['url'] = url
            yield item
