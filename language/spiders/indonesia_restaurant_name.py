# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy_redis.spiders import RedisSpider


class IndonesiaRestaurantNameSpider(RedisSpider):
    name = 'indonesia_restaurant_name'
    allowed_domains = ['www.tripadvisor.co.id/Restaurants-g317101-Pontianak_West_Kalimantan_Kalimantan.html']
    start_urls = [
        'http://www.tripadvisor.co.id/Restaurants-g317101-Pontianak_West_Kalimantan_Kalimantan.html/'
    ]
    redis_key = 'indonesia_restaurant_name'
    custom_settings = {
        # 指定redis数据库的连接参数
        'REDIS_HOST': '123.56.11.156',
        'REDIS_PORT': 6379,
        # 指定 redis链接密码，和使用哪一个数据库
        'REDIS_PARAMS': {
            'password': '',
            'db': 0
        },
    }

    def parse(self, response):
        recommend_restaurant = response.xpath('//a[@class="poiTitle"]/text()').extract()
        list_restaurant = response.xpath('//div[@class="title"]/a/text()').extract()
        page = response.xpath('//*[@id="EATERY_LIST_CONTENTS"]/div[2]/div/div/a[last()]/text()').extract()[0]
        recommend_restaurant = [item.strip() for item in recommend_restaurant]
        list_restaurant = [item.strip() for item in list_restaurant]
        self.save(recommend_restaurant)
        self.save(list_restaurant)

        page = page.strip()
        address_id = re.findall("[0-9]+", response.url)[0]
        for i in range(1, int(page) + 1):
            url = "https://www.tripadvisor.co.id/RestaurantSearch?Action=PAGE&geo={}&ajax=1&sortOrder=relevance&o=a{}&availSearchEnabled=false".format(
                address_id, i * 30)
            yield scrapy.Request(url, callback=self.parse_item, dont_filter=True)

    def parse_item(self, response):
        list_restaurant = response.xpath('//div[@class="title"]/a/text()').extract()
        list_restaurant = [item.strip() for item in list_restaurant]
        self.save(list_restaurant)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\indonesia_temp\indonesia_restaurant.txt', 'a',
                  encoding='utf-8')as f:
            f.write('\n'.join(result))
