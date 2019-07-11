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
        # 'https://tuoitre.vn/vng-tu-nhung-buoc-di-esports-so-khoi-den-bom-tan-mobile-legends-bang-bang-20190612135605021.htm'
        # 'https://tuoitre.vn/xe-csgt-binh-duong-gay-tai-nan-1-nguoi-tu-vong-20190609212738957.htm'
        'https://tuoitre.vn/de-nghi-bac-tat-ca-khang-cao-vu-that-thoat-3-608-ti-o-ngan-hang-dong-a-20190529092940243.htm'
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
        content.extend(response.xpath('//div[@class="content fck"]/div//text()').extract())
        content.extend(response.xpath('//div[@class="sp-detail-content"]/p//text()').extract())

        content = ' '.join(content).replace('\r', '').replace('\t', '').replace('\n', '').replace('\xa0', '')
        item = NewsContentItem()
        item['url'] = response.url
        item['content'] = content
        yield item
