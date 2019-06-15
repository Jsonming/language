# -*- coding: utf-8 -*-
import scrapy
import json

class IndonesiaNewsCnnLinkSpider(scrapy.Spider):
    name = 'indonesia_news_cnn_link'
    allowed_domains = ['www.cnnindonesia.com/nasional/indeks/3']
    start_urls = ['http://www.cnnindonesia.com/nasional/indeks/3/']

    def parse(self, response):
        news_link = response.xpath('//*[@id="content"]/div/div[4]/div/div[1]/article/a/@href').extract()
        # print(news_link)
        url = "https://www.cnnindonesia.com/nasional/indeks/3/2?date=Semua%20Tgl&kanal=3"
        yield scrapy.Request(url, callback=self.parse_item, dont_filter=True)

    def parse_item(self, response):
        data = response.xpath('//article/a/@href').extract()
        print(data)
        print(response.body)