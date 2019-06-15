# -*- coding: utf-8 -*-
import scrapy
from ..items import NewsContentItem
from scrapy_redis.spiders import RedisSpider


class VietnamNewsNhandanContentSpider(RedisSpider):
    name = 'vietnam_news_nhandan_content'
    redis_key = 'vietnam_news_link'
    custom_settings = {
        # 指定redis数据库的连接参数
        'REDIS_HOST': '123.56.11.156',
        'REDIS_PORT': 6379,
        # 指定 redis链接密码，和使用哪一个数据库
        'REDIS_PARAMS': {
            'password': '',
            'db': 0
        },
    }

    def parse(self, response):
        content = response.xpath('//div/p/text()').extract()
        content = ''.join(content)
        item = NewsContentItem()
        item['url'] = response.url
        item['content'] = content
        yield item
