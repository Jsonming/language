# -*- coding: utf-8 -*-
import scrapy
from ..items import NewsContentItem
from scrapy_redis.spiders import RedisSpider


class BernamaContentSpider(RedisSpider):
    name = 'bernama_content'
    # allowed_domains = ['http://www.bernama.com']
    # start_urls = ['http://www.bernama.com/bm/dunia/news.php?id=1714675/']
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
        content = response.xpath('//div[@class="w3-x-padding"]//text()').extract()
        result = ''.join(content)
        it['content'] = result
        it['url'] = response.url
        yield it
