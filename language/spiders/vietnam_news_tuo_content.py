# -*- coding: utf-8 -*-
import scrapy
import pprint
from language.items import NewsContentItem
from scrapy_redis.spiders import RedisSpider
from language.items import NewsLink


class VietnamNewsTuoContentSpider(RedisSpider):
    name = 'vietnam_news_tuo_content'
    allowed_domains = ['tuoitre.vn']
    start_urls = [
        'https://tuoitre.vn/dia-don-mv-phim-ngan-cho-ngay-tinh-yeu-valentine-20190213160930321.htm'
    ]

    redis_key = 'vietnam_news_tuo_link'
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
        content.extend(response.xpath('//div[@class="content fck"]/p//text()').extract())

        content = ' '.join(content).replace('\r', '').replace('\t', '').replace('\n', '').replace('\xa0', '')
        item = NewsContentItem()
        item['url'] = response.url
        item['content'] = content
        yield item
