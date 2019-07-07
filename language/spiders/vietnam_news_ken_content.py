# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from language.items import NewsContentItem


class VietnamNewsKenContentSpider(RedisSpider):
    name = 'vietnam_news_ken_content'
    allowed_domains = ['kenh14.vn']
    # start_urls = [
        # 'http://kenh14.vn/xuc-dong-nguoi-cha-o-sai-gon-om-con-khoc-trong-hanh-phuc-sau-hon-4-thang-tim-kiem-moi-mon-20190703172628968.chn'
        # "http://kenh14.vn/dan-sao-viet-cung-te-tuu-khoe-sac-tren-tham-do-su-kien-20170309230551411.chn"
        # "http://kenh14.vn/cuoc-dua-ky-thu-cac-hoa-hau-tai-mat-vi-leo-60m-thang-day-st-binh-an-ve-dich-dau-tien-20190706223821038.chn"
        # "http://kenh14.vn/10-dieu-nen-biet-ve-black-panther-2-ai-cung-hao-huc-mong-doi-so-4-vi-da-duoc-nha-hang-trong-endgame-2019070222305589.chn"
        # "http://kenh14.vn/running-man-on-troi-lien-binh-phat-da-biet-choi-do-ma-con-tut-duoc-quan-tran-thanh-20190707000419163.chn"
        # "http://kenh14.vn/ngoai-me-vu-so-khanh-ve-nha-di-con-van-con-2-cuc-pham-lay-lai-niem-tin-lay-chong-cho-chi-em-20190705163051741.chn"
    # ]

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
