# -*- coding: utf-8 -*-
import scrapy
from ..items import NewsLink
from scrapy_redis.spiders import RedisSpider


class VietnamNewsNhandanSpider(scrapy.Spider):
    name = 'vietnam_news_nhandan'
    allowed_domains = ['www.nhandan.org.vn']
    start_urls = [
        'http://www.nhandan.org.vn/chinhtri'
        # 'http://www.nhandan.org.vn/kinhte',
        # "http://www.nhandan.org.vn/vanhoa",
        # "http://www.nhandan.org.vn/xahoi",
        # "http://www.nhandan.org.vn/phapluat",
        # "http://www.nhandan.org.vn/du-lich",
        # "https://www.nhandan.org.vn/thegioi",
        # "https://www.nhandan.org.vn/thethao"
        # "http://www.nhandan.org.vn/giaoduc",
        # "http://www.nhandan.org.vn/y-te",
        # "http://www.nhandan.org.vn/khoahoc-congnghe",
        # "http://www.nhandan.org.vn/bandoc",
        # "http://www.nhandan.org.vn/hanoi",    #  这是一个特殊的列表
        # "http://www.nhandan.org.vn/tphcm",    # 跟上一个一样是一个特殊的列表
    ]

    # redis_key = 'vietnam_news_link_new'
    # custom_settings = {
    #     'REDIS_HOST': '123.56.11.156',
    #     'REDIS_PORT': 6379,
    #     'REDIS_PARAMS': {
    #         'password': '',
    #         'db': 0
    #     },
    # }

    def parse(self, response):
        next_page_link = []
        next_page_zero = response.xpath(
            '//*[@id="wrapper"]/div[1]/div[3]/div[3]/div[1]/div[2]/div/div/ul/li[last()]/a/@href').extract()
        next_page_one = response.xpath(
            '//*[@id="wrapper"]/div[1]/div[3]/div[2]/div[1]/div[2]/div/div/ul/li[last()]/a/@href').extract()
        next_page_two = response.xpath('/html/body/div[4]/div[2]/div[7]/div[2]/ul/li[last()]/a/@href').extract()
        next_page_link.extend(next_page_zero)
        next_page_link.extend(next_page_one)
        next_page_link.extend(next_page_two)
        if next_page_link:
            print(next_page_link)
            next_url = next_page_link[0]
            yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)

        links = []
        links_zero = response.xpath(
            '//*[@id="wrapper"]/div[1]/div[3]/div[2]/div[1]/div/div/div[1]/div/div/h5/a/@href').extract()
        links_one = response.xpath(
            '//*[@id="wrapper"]/div[1]/div[3]/div[1]/div[1]/div/div/div/div/div/h5/a/@href').extract()
        links_two = response.xpath('//*[@id="wrapper"]/div[1]/div[3]/div[3]/div[1]/div[1]/div/h5/a/@href').extract()
        links_three = response.xpath('//*[@id="wrapper"]/div[1]/div[3]/div[2]/div[1]/div[1]/div/h5/a/@href').extract()
        links_four = response.xpath('/html/body/div[4]/div[2]/div[6]/div[1]/div[4]/div/div/div/h3/a/@href').extract()
        links.extend(links_zero)
        links.extend(links_one)
        links.extend(links_two)
        links.extend(links_three)
        links.extend(links_four)
        links = ["http://www.nhandan.org.vn" + item for item in links]
        print(links)

        if not links:
            item = NewsLink()
            item['ori_url'] = response.url
            yield item
        else:
            for url in links:
                item = NewsLink()
                item['url'] = url
                yield item

