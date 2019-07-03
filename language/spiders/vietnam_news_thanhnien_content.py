# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from language.items import NewsContentItem
from language.items import NewsLink


class VietnamNewsThanhnienContentSpider(RedisSpider):
    name = 'vietnam_news_thanhnien_content'
    allowed_domains = ['thanhnien.vn']
    start_urls = [
        # 'https://thanhnien.vn/thoi-su/an-mang-dau-long-chong-giet-vo-truoc-mat-con-gai-vua-rut-don-ly-di-1098127.html',
        "https://thanhnien.vn/thoi-su/moi-mon-40-nam-oan-khuat-noi-dau-con-mai-1024801.html"
    ]

    redis_key = 'vietnam_news_thanhnien_content'
    custom_settings = {
        'REDIS_HOST': '47.105.132.57',
        'REDIS_PORT': 6379,
        'REDIS_PARAMS': {
            'password': '',
            'db': 0
        },
    }

    def parse(self, response):
        title = response.xpath("//h1/text()").extract()
        model = response.xpath('//div[class="sapo"]//text()').extract()

        paragrah = response.xpath('//div[@class="cms-body detail"]/div/text()').extract()
        paragrah_one = response.xpath('//p[@class="paragraph"]/text()').extract()
        paragrah_two = response.xpath('//div[@class="article-body cms-body AdAsia"]//text()').extract()
        paragrah_three = response.xpath('//div[@class="article-section__sub-content"]//p/text()').extract()

        paragrah_list = []
        paragrah_list.extend(title)
        paragrah_list.extend(model)
        paragrah_list.extend(paragrah)
        paragrah_list.extend(paragrah_one)
        paragrah_list.extend(paragrah_two)
        paragrah_list.extend(paragrah_three)

        content = ''.join(paragrah_list).replace('\n', '').replace('\r', '').replace('\t', '')
        if not any([it in response.url for it in ['vtv', 'video', "embed2"]]):
            item = NewsContentItem()
            item['url'] = response.url
            item['content'] = content
            yield item

            # 提取正文中的链接
            # content_links = response.xpath('//a/@href').extract()
            # content_links = list(set(content_links))
            # for link in content_links:
            #     para = link.split('-')[-1]
            #     number = para.split('.')[0]
            #     if number.isdigit():
            #         if 'http' not in link:
            #             content_link = "https://vtv.vn" + link
            #         else:
            #             content_link = link
            #
            #         item = NewsLink()
            #         item['url'] = content_link
            #         item['ori_url'] = response.url
            #         if not any([item in content_link for item in ['jpg', 'png', 'jpeg']]):
            #             yield item
