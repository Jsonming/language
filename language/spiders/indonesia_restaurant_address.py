# -*- coding: utf-8 -*-
import scrapy
from ..items import ShortWordLink


class IndonesiaRestaurantAddressSpider(scrapy.Spider):
    name = 'indonesia_restaurant_address'
    allowed_domains = ['www.tripadvisor.co.id/Restaurants-g294225-Indonesia.html#LOCATION_LIST']
    start_urls = [
        'http://www.tripadvisor.co.id/Restaurants-g294225-Indonesia.html#LOCATION_LIST/',
        # 'https://www.tripadvisor.co.id/Restaurants-g294225-oa{}-Indonesia.html#LOCATION_LIST'.format(i) for i in
        # range(20, 20 * 29, 20)
    ]

    def parse(self, response):
        # address_links = response.xpath('//*[@id="BROAD_GRID"]/div/div/div/div/div[1]/div[2]/a/@href').extract()
        address_links = response.xpath('//*[@id="LOCATION_LIST"]/ul/li/a/@href').extract()
        # address_links = ['https://www.tripadvisor.co.id' + item for item in address_links]
        # for link in address_links:
        #     item = ShortWordLink()
        #     item['url'] = link
        #     yield item

        # address = response.xpath('//*[@id="LOCATION_LIST"]/ul/li/a/text()').extract()
        # address = [item.split('di')[-1].strip() for item in address]
        # self.save(address)

        address = response.xpath('//*[@id="BROAD_GRID"]/div/div/div/div/div[1]/div[2]/a/text()').extract()
        address = [item.split('di')[-1].strip() for item in address]
        self.save(address)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\indonesia_temp\indonesia_city.txt', 'a',
                  encoding='utf-8')as f:
            f.write('\n'.join(result))
