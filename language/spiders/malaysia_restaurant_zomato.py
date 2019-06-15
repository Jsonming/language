# -*- coding: utf-8 -*-
import scrapy
import os

class MalaysiaRestaurantZomatoSpider(scrapy.Spider):
    name = 'malaysia_restaurant_zomato'
    allowed_domains = ['www.zomato.com']
    start_urls = ['https://www.zomato.com/kuala-lumpur/best-dinner-in-kuchai-entrepreneurs-park']

    def parse(self, response):
        restaurants = response.xpath(
            '//*[@id="orig-search-list"]/div/div[1]/div/article/div[1]/div/div[2]/div[1]/div[1]/a[1]/text()').extract()
        names = [item.strip() for item in restaurants]
        folder = r"D:\datatang\language\language\files"
        if not os.path.exists(folder):
            os.mkdir(folder)

        with open(r'{}\{}.txt'.format(folder, 'restaurant_name'), 'a', encoding='utf8')as f:
            f.write('\n'.join(names))

        next_button = response.xpath(
            '//*[@id="search-results-container"]/div[2]/div[1]/div[2]/div/div/a[last()]/@href').extract()
        if next_button:
            next_url = 'https://www.zomato.com' + next_button[0]
            yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
