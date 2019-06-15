# -*- coding: utf-8 -*-
import scrapy
from ..items import MovieName

class VietnamMovieNameSpider(scrapy.Spider):
    name = 'vietnam_movie_name'
    allowed_domains = ['http://movies.hdviet.com']
    urls = ['http://movies.hdviet.com/phim-hdviet-de-cu/trang-{}.html'.format(i) for i in range(1, 3)]
    urls.extend(['http://movies.hdviet.com/phim-hot-trong-thang/trang-{}.html'.format(i) for i in range(1, 35)])
    urls.extend(['http://movies.hdviet.com/phim-bo/trang-{}.html'.format(i) for i in range(1, 41)])
    urls.extend(['http://movies.hdviet.com/phim-le/trang-{}.html'.format(i) for i in range(1, 233)])
    start_urls = urls

    def parse(self, response):
        movie_list = response.xpath('//*[@id="Container-wrap"]/div[5]/div[2]/div[1]/ul[1]/li')
        for movie in movie_list:
            movie_name = movie.xpath('./a/text()').extract()
            if movie_name:
                item = MovieName()
                item['first_name'] = movie_name[0]
                try:
                    item['second_name'] = movie_name[1]
                except:
                    item['second_name'] = ''
                yield item
