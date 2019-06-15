# -*- coding: utf-8 -*-
import scrapy


class MalaysiaMovieSpider(scrapy.Spider):
    name = 'malaysia_movie'
    allowed_domains = ['https://www.gsc.com.my/']
    start_urls = ['https://www.gsc.com.my/']

    def parse(self, response):
        content = response.xpath('//span[@class="MovieTitle truncate"]/text()').extract()
        with open('C:\\Users\\Administrator\\Desktop\\movie.txt', 'a', encoding='utf8')as f:
            f.write(','.join(content))
