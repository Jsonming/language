# -*- coding: utf-8 -*-
import scrapy
from ..items import NewsContentItem
from scrapy_redis.spiders import RedisSpider


class VietnamNewsPlusContentSpider(RedisSpider):
    name = 'vietnam_news_plus_content'
    allowed_domains = ['www.vietnamplus.vn']
    # start_urls = [
    #     'https://www.vietnamplus.vn/nhieu-nhan-vien-huawei-tung-lam-viec-voi-quan-doi-trung-quoc/579032.vnp',
    # ]

    redis_key = 'vietnam_news_puls'
    custom_settings = {
        'REDIS_HOST': '47.105.132.57',
        'REDIS_PORT': 6379,
        'REDIS_PARAMS': {
            'password': '',
            'db': 0
        },
    }

    def parse(self, response):
        title = response.xpath('//h1/text()').extract()
        summery = response.xpath('//div[@class="details__summary cms-desc"]//text()').extract()
        paragraph = response.xpath('//div[@class="content article-body cms-body "]//text()').extract()
        paragraph_one = response.xpath('//div[@class="content article-body cms-body AdAsia"]//text()').extract()

        text = []
        text.extend(title)
        text.extend(summery)
        text.extend(paragraph)
        text.extend(paragraph_one)
        content = ''.join(text).replace('\r\n', ' ').replace('\n', ' ')
        item = NewsContentItem()
        item['url'] = response.url
        item['content'] = content
        return item
