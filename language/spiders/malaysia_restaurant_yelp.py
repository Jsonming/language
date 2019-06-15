# -*- coding: utf-8 -*-
import scrapy
import os


class MalaysiaRestaurantYelpSpider(scrapy.Spider):
    name = 'malaysia_restaurant_yelp'
    allowed_domains = ['www.yelp.com']
    start_urls = ['https://www.yelp.com/search?cflt=restaurants&find_loc=No.%2011%2C%20Jalan%20Kuchai%20Lama%2C%2058200%20Kuala%20Lumpur%2C%20Malaysia&start=0']

    def parse(self, response):
        restaurants = response.xpath('//*[@id="wrap"]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/ul/li/div/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/h3/a/text()').extract()
        names = [item.strip() for item in restaurants]

        folder = r"D:\datatang\language\language\files"
        if not os.path.exists(folder):
            os.mkdir(folder)

        with open(r'{}\{}.txt'.format(folder, 'restaurant_name'), 'a', encoding='utf8')as f:
            f.write('\n'.join(names))

        next_button = response.xpath('//*[@id="wrap"]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/div/div[2]/div/div[last()]/a/@href').extract()
        if next_button:
            next_url = 'https://www.yelp.com' + next_button[0]
            yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
