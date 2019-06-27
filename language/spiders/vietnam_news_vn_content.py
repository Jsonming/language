# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import NewsContentItem


class VietnamNewsVnContentSpider(RedisSpider):
    name = 'vietnam_news_vn_content'
    allowed_domains = ['vnexpress.net']
    # start_urls = [
    #     'https://vnexpress.net/the-gioi/dac-nhiem-dot-kich-giai-cuu-con-tin-sydney-ba-nguoi-chet-3121010-tong-thuat.html',
    #
    # ]

    redis_key = 'vietnam_news_vn_content'
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
        paragraph_one = response.xpath('//div[@class="text_live"]//text()').extract()
        paragraph_two = response.xpath('///*[@id="warpper"]/div/div/p/text()').extract()
        paragraph_three = response.xpath('//p[@class="Normal"]//text()').extract()
        paragraph_four = response.xpath('//*[@id="article_content"]/div/div/p/text()').extract()
        paragraph_five = response.xpath('//html/body//div/p/text()').extract()
        content = []
        content.extend(description)
        content.extend(paragraph)
        content.extend(paragraph_one)
        content.extend(paragraph_two)
        content.extend(paragraph_three)
        content.extend(paragraph_four)
        content.extend(paragraph_five)

        content = ' '.join(content).replace('\n', '')
        if 'video' not in response.url:
            item = NewsContentItem()
            item['url'] = response.url
            item['content'] = content
            return item
