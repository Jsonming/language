# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import NewsLink
from ..items import NewsContentItem


class VietnamNewsVtvContentSpider(RedisSpider):
    name = 'vietnam_news_vtv_content'
    allowed_domains = ['vtv.vn']
    start_urls = [
        # 'https://vtv.vn/trong-nuoc/sach-gia-sach-lau-gay-hau-qua-khon-luong-20190620155150671.htm'
        # 'https://vtv.vn/vtv8/lien-tiep-xay-ra-chay-rung-tai-phu-yen-20190628113739609.htm',
        # 'https://vtv.vn/vtv9/lu-lut-o-trung-quoc-khien-17-nguoi-thiet-mang-20190613182044515.htm'
        # 'https://vtv.vn/chuyen-dong-24h/thu-tuong-nhat-xin-loi-vi-bao-cao-quy-luong-huu-co-the-bi-qua-tai-khi-nguoi-gia-song-tho-20190613160839671.htm'
        # "https://vtv.vn/magazine/ban-hang-da-kenh-la-mot-xu-the-rat-tu-nhien-khong-the-ngan-lai-duoc-20180516112626842.htm"
        # "https://vtv.vn/news-20190326151103975.htm"
        "https://vtv.vn/trong-nuoc/no-luc-thu-gom-rac-giam-ap-luc-o-nhiem-tren-vinh-nha-trang-20190516071056576.htm"
    ]

    redis_key = 'vietnam_news_vtv'
    custom_settings = {
        'REDIS_HOST': '47.105.132.57',
        'REDIS_PORT': 6379,
        'REDIS_PARAMS': {
            'password': '',
            'db': 0
        },
    }

    def parse(self, response):
        title = response.xpath('//h1/text()').extract()
        title_one = response.xpath('//h2/text()').extract()

        paragrah_list = []
        paragrah = response.xpath('//div[@class="content_detail ta-justify"]//p/text()').extract()
        paragrah_one = response.xpath('//div[@data-field="body"]//p//text()').extract()
        paragrah_two = response.xpath('//div[@class="sp-detail-content"]//p//text()').extract()

        paragrah_list.extend(title)
        paragrah_list.extend(title_one)
        paragrah_list.extend(paragrah)
        paragrah_list.extend(paragrah_one)
        paragrah_list.extend(paragrah_two)

        content = ''.join(paragrah_list).replace('\n', '').replace('\r', '').replace('\t', '')

        item = NewsContentItem()
        item['url'] = response.url
        item['content'] = content
        yield item

        # 提取正文中的链接
        content_links = response.xpath('//a/@href').extract()
        content_links = list(set(content_links))
        for link in content_links:
            para = link.split('-')[-1]
            number = para.split('.')[0]
            if number.isdigit():
                if 'http' not in link:
                    content_link = "https://vtv.vn" + link
                else:
                    content_link = link

                item = NewsLink()
                item['url'] = content_link
                item['ori_url'] = response.url
                if not any([item in content_link for item in ['jpg', 'png', 'jpeg']]):
                    yield item
#