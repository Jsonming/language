# -*- coding: utf-8 -*-
import scrapy
from ..items import NewsContentItem
from scrapy_redis.spiders import RedisSpider
from scrapy import spiders


class VietnamNewsNhandanContentSpider(RedisSpider):
    name = 'vietnam_news_nhandan_content'
    redis_key = 'vietnam_news_nhandan_content'
    custom_settings = {
        'REDIS_HOST': '47.105.132.57',
        'REDIS_PORT': 6379,
        'REDIS_PARAMS': {
            'password': '',
            'db': 0
        },
    }

    def parse(self, response):
        con = response.xpath('//div[@class="ndcontent"]/text()').extract()
        cont = response.xpath('//*[@id="wrapper"]/div[1]/div[3]/div/div/div[1]/div/div/text()').extract()
        content = response.xpath('//div/p//text()').extract()
        content = ''.join(content + cont + con)
        item = NewsContentItem()
        item['url'] = response.url
        item['content'] = content
        yield item
