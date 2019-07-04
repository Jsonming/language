# -*- coding: utf-8 -*-
import scrapy
from language.items import NewsContentItem
from scrapy_redis.spiders import RedisSpider


class VietnamNewsDangContentSpider(RedisSpider):
    name = 'vietnam_news_dang_content'
    allowed_domains = ['www.dangcongsan.vn']
    start_urls = [
        'http://www.dangcongsan.vn/quoc-phong-an-ninh/danh-gia-dung-thuc-chat-trinh-do-chuyen-mon-ky-thuat-mat-ma-527461.html',
    ]

    redis_key = 'vietnam_news_dang_link'
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
        content.extend(response.xpath('//div[@class="post-content"]//p//text()').extract())
        content.extend(response.xpath('//div[@class="post-content"]//span//text()').extract())

        content = ''.join(content).replace('\n', '').replace('\r', '').replace('\t', '')
        item = NewsContentItem()
        item['url'] = response.url
        item['content'] = content
        yield item
