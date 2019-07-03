# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from language.items import NewsContentItem


class VietnamNewsKenContentSpider(scrapy.Spider):
    name = 'vietnam_news_ken_content'
    allowed_domains = ['kenh14.vn']
    start_urls = [
        'http://kenh14.vn/xuc-dong-nguoi-cha-o-sai-gon-om-con-khoc-trong-hanh-phuc-sau-hon-4-thang-tim-kiem-moi-mon-20190703172628968.chn'
    ]

    redis_key = 'vietnam_news_ken_link'
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
        title = response.xpath('//h1/text()').extract()
        sub_title = response.xpath('//h2/text()').extract()
        content.extend(title)
        content.extend(sub_title)

        content.extend(response.xpath('//div[@class="klw-new-content"]//text()').extract())
        content = ''.join(content).replace('\n', '').replace('\r', '').replace('\t', '')
        item = NewsContentItem()
        item['url'] = response.url
        item['content'] = content
        yield item
