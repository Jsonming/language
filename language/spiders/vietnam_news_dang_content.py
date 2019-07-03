# -*- coding: utf-8 -*-
import scrapy
from language.items import NewsContentItem
from scrapy_redis.spiders import RedisSpider


class VietnamNewsDangContentSpider(RedisSpider):
    name = 'vietnam_news_dang_content'
    allowed_domains = ['www.dangcongsan.vn']
    start_urls = [
        'http://dangcongsan.vn/thoi-su/thu-tuong-ket-thuc-chuyen-tham-du-hoi-nghi-thuong-dinh-g20-va-tham-chinh-thuc-nhat-ban-527205.html',
        "http://dangcongsan.vn/khoa-giao/bao-so-2-gay-mua-lon-huong-vao-quang-ninh-hai-phong-527352.html"
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
        title = response.xpath('//h1/text()').extract()
        content.extend(title)
        content.extend(response.xpath('//div[@class="post-content"]//p/text()').extract())

        content = ''.join(content).replace('\n', '').replace('\r', '').replace('\t', '')
        item = NewsContentItem()
        item['url'] = response.url
        item['content'] = content
        yield item
