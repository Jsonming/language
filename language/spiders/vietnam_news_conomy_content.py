# -*- coding: utf-8 -*-
import scrapy
import pprint
from language.items import NewsContentItem
from scrapy_redis.spiders import RedisSpider


class VietnamNewsConomyContentSpider(RedisSpider):
    name = 'vietnam_news_conomy_content'
    allowed_domains = ['vneconomy.vn']
    start_urls = [
        'http://vneconomy.vn/co-hoi-de-lam-bao-mot-cach-tu-te-20190620235804509.htm'
    ]

    redis_key = 'vietnam_news_conomy_link'
    custom_settings = {
        'REDIS_HOST': '47.105.132.57',
        'REDIS_PORT': 6379,
        'REDIS_PARAMS': {
            'password': '',
            'db': 0
        },
    }

    def parse(self, response):
        content = []
        content.extend(response.xpath('//div[@class="contentdetail"]/p//text()').extract())

        content = ' '.join(content).replace('\r', '').replace('\t', '').replace('\n', '').replace('\xa0', '')
        item = NewsContentItem()
        item['url'] = response.url
        item['content'] = content
        yield item
