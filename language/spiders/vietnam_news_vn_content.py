# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import NewsContentItem


class VietnamNewsVnContentSpider(RedisSpider):
    name = 'vietnam_news_vn_content'
    allowed_domains = ['vnexpress.net']
    # start_urls = [
    #     'https://vnexpress.net/phap-luat/an-ninh-trat-tu-1953975.html',
    #
    # ]

    redis_key = 'vietnam_news_vn'
    custom_settings = {
        'REDIS_HOST': '47.105.132.57',
        'REDIS_PORT': 6379,
        'REDIS_PARAMS': {
            'password': '',
            'db': 0
        },
    }

    def parse(self, response):
        description = response.xpath('/html/body/section[2]/section[1]/section[1]/p/text()').extract()
        paragraph = response.xpath('//article//text()').extract()

        content = ' '.join(description + paragraph).replace('\n', '')
        item = NewsContentItem()
        item['url'] = response.url
        item['content'] = content
        return item
