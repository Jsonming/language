# -*- coding: utf-8 -*-
import scrapy
import json

class DoorhasSpider(scrapy.Spider):
    name = 'doorhas'
    allowed_domains = ['www.baidu.com']
    # with open('C:\\Users\\Administrator\\Desktop\\city.txt', 'r', encoding='gbk')as f:
    #     data = f.read()
    # citys = data.split(',')
    #
    # start_urls = [
    #     'https://api.doordash.com/v1/seo_stores/?delivery_city_slug={}&store_only=true&limit=50&offset={}'.format(
    #         city, offset) for city in citys for offset in range(0, 601, 50)]
    start_urls = ['https://api.doordash.com/v1/seo_stores/?delivery_city_slug=barton-hills-tx-restaurants&store_only=true&limit=50&offset=400']

    def parse(self, response):
        names = []
        stores = json.loads(response.body).get("stores")
        for store in stores:
            store_name = store.get("business").get("name")
            names.append(store_name)
        with open('C:\\Users\\Administrator\\Desktop\\name.txt', 'a', encoding='utf-8')as f:
            f.write(','.join(names))

