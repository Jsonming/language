# -*- coding: utf-8 -*-
import scrapy
from language.items import NewsContentItem
from scrapy_redis.spiders import RedisSpider


class VietnamNewsNetContentSpider(RedisSpider):
    name = 'vietnam_news_net_content'
    allowed_domains = ['vietnamnet.vn']
    # start_urls = [
    #     'https://vietnamnet.vn/vn/giai-tri/the-gioi-sao/duc-tien-trao-hon-145-trieu-giup-nghe-si-xuan-hieu-chua-ung-thu-542468.html'
    # ]

    redis_key = 'vietnam_news_net_link'
    custom_settings = {
        'REDIS_HOST': '47.105.132.57',
        'REDIS_PORT': 6379,
        'REDIS_PARAMS': {
            'password': '',
            'db': 0
        }
    }

    def parse(self, response):
        content = []
        content.extend(response.xpath('//div[@class="ArticleContent"]/p//text()').extract())
        content.extend(response.xpath('//div[@id="Magazine-Acticle"]/p//text()').extract())
        content = ' '.join(content).replace('\r', '').replace('\t', '').replace('\n', '').replace('\xa0', '')
        item = NewsContentItem()
        item['url'] = response.url
        item['content'] = content
        yield item