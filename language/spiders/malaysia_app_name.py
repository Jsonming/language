# -*- coding: utf-8 -*-
import scrapy
import os


class MalaysiaAppNameSpider(scrapy.Spider):
    name = 'malaysia_app_name'
    allowed_domains = ['www.zomato.com/kuala-lumpur/dinner']
    start_urls = ['https://www.zomato.com/kuala-lumpur/dinner?page=301']

    def parse(self, response):
        names = response.xpath(
            '//*[@id="orig-search-list"]/div/div[1]/div/article/div[1]/div/div[2]/div[1]/div[1]/a[1]/text()').extract()
        names = [item.strip() for item in names]
        self.save(names)
        next_url = response.xpath('//*[@id="search-results-container"]/div[2]/div[1]/div[2]/div/div/a[@title="Next Page"]/@href').extract()
        next_url = "https://www.zomato.com" + next_url[0]
        return scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)

    def save(self, result):
        folder = r"C:\Users\Administrator\Desktop\malaya_temp"
        if not os.path.exists(folder):
            os.mkdir(folder)
        with open(r'{}\restaurant_name.txt'.format(folder), 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))
