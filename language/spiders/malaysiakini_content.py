# -*- coding: utf-8 -*-
import scrapy
from ..items import NewsContentItem
from scrapy_redis.spiders import RedisSpider


class MalaysiakiniContentSpider(RedisSpider):
    name = 'malaysiakini_content'
    # allowed_domains = ['www.malaysiakini.com/hiburan/329131']
    # start_urls = ['http://www.malaysiakini.com/hiburan/329131/']
    redis_key = 'news_link'
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
        it = NewsContentItem()
        content = response.xpath('//div[@class="mk-content-text"]//text()').extract()
        it['content'] = ''.join(content)
        it['url'] = response.url
        yield it
