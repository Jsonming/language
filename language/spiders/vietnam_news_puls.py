# -*- coding: utf-8 -*-
import re
import scrapy
from ..items import NewsLink
from scrapy_redis.spiders import RedisSpider


class VietnamNewsPulsSpider(RedisSpider):
    name = 'vietnam_news_puls'
    allowed_domains = ['www.vietnamplus.vn']
    start_urls = [
        # 'https://www.vietnamplus.vn/chude/bien-dong/205.vnp',
        # 'https://www.vietnamplus.vn/chude/xay-dung-dang/820.vnp',
        # 'https://www.vietnamplus.vn/chude/hop-quoc-hoi/186.vnp',
        # 'https://www.vietnamplus.vn/chude/gia-dien/1030.vnp',
        # 'https://www.vietnamplus.vn/chude/duong-day-danh-bac-hang-nghin-ty/1035.vnp',
        # 'https://www.vietnamplus.vn/chude/dich-ta-lon-chau-phi/1012.vnp',
        # 'https://www.vietnamplus.vn/chude/brexit/770.vnp',
        # 'https://www.vietnamplus.vn/chude/tinh-hinh-venezuela/768.vnp',

        # 'https://www.vietnamplus.vn/chinhtri.vnp',
        # 'https://www.vietnamplus.vn/kinhte.vnp',
        # 'https://www.vietnamplus.vn/xahoi.vnp',
        # 'https://www.vietnamplus.vn/doisong.vnp',
        # 'https://www.vietnamplus.vn/vanhoa.vnp',
        # 'https://www.vietnamplus.vn/thethao.vnp',

        # 'https://www.vietnamplus.vn/khoahoc.vnp',
        # 'https://www.vietnamplus.vn/congnghe.vnp',
        # 'https://www.vietnamplus.vn/otoxemay.vnp',
        # 'https://www.vietnamplus.vn/moitruong.vnp',
        # 'https://www.vietnamplus.vn/dulich.vnp',
        # 'https://www.vietnamplus.vn/tinthitruong.vnp',
        # 'https://www.vietnamplus.vn/chuyenla.vnp',
        # 'https://www.vietnamplus.vn/rapnewsplus.vnp',
        # 'https://www.vietnamplus.vn/newsgame.vnp',
        # 'https://www.vietnamplus.vn/infographics.vnp',
        # 'https://www.vietnamplus.vn/timeline.vnp',
        # 'https://www.vietnamplus.vn/topicnews.vnp',
        # 'https://www.vietnamplus.vn/photo360.vnp',
        # 'https://www.vietnamplus.vn/megastory.vnp',
        # 'https://www.vietnamplus.vn/chude/bao-so-12-gay-nhieu-thiet-hai/885.vnp',
        "https://www.vietnamplus.vn/chude/nissanrenaultmitsubishi-va-be-boi-cua-ong-ghosn/987.vnp"

    ]

    redis_key = 'vietnam_news_plus_content'
    custom_settings = {
        'REDIS_HOST': '47.105.132.57',
        'REDIS_PORT': 6379,
        'REDIS_PARAMS': {
            'password': '',
            'db': 0
        },
    }

    def parse(self, response):
        links = response.xpath('//article/h2/a/@href').extract()
        urls = ["https://www.vietnamplus.vn" + link for link in links]
        for url in urls:
            item = NewsLink()
            item['url'] = url
            yield item

        current_page = re.findall(r"trang(.*?)\.vnp", response.url)
        if current_page:
            current_page = int(current_page[0])
        else:
            current_page = 1

        last_page = response.xpath('//*[@id="mainContent_ContentList1_pager"]/ul/li[last()]/a/text()').extract()
        if current_page < int(last_page[0]):
            if "trang" in response.url:
                nest_para = response.url.split('/')[-1]
                nest_page = response.url.replace(nest_para, '') + "trang{}.vnp".format(current_page + 1)
            else:
                nest_para = response.url.split('.')[-1]
                nest_page = response.url.replace("."+nest_para, '/') + "trang{}.vnp".format(current_page + 1)

            yield scrapy.Request(url=nest_page, callback=self.parse, dont_filter=True)
