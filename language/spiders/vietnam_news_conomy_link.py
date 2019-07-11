# -*- coding: utf-8 -*-
import re
import scrapy
from language.items import NewsLink


class VietnamNewsConomyLinkSpider(scrapy.Spider):
    name = 'vietnam_news_conomy_link'
    allowed_domains = ['vneconomy.vn']
    start_urls = [
        # 'http://vneconomy.vn/thoi-su.htm',
        # 'http://vneconomy.vn/tai-chinh.htm',
        # 'http://vneconomy.vn/chung-khoan.htm',
        # 'http://vneconomy.vn/doanh-nhan.htm',
        # 'http://vneconomy.vn/dia-oc.htm',
        # 'http://vneconomy.vn/thi-truong.htm',
        # 'http://vneconomy.vn/the-gioi.htm',
        # 'http://vneconomy.vn/cuoc-song-so.htm',
        'http://vneconomy.vn/xe-360.htm',

        'http://vneconomy.vn/timeline/9920/trang-1.htm',

    ]

    def parse(self, response):
        links = response.xpath('//div[@class="infonews"]/a/@href').extract()
        if links:
            for link in links:
                if "http" not in link:
                    url = "http://vneconomy.vn" + link
                else:
                    url = link

                item = NewsLink()
                item['url'] = url
                item['ori_url'] = response.url
                yield item

            current_page = re.findall('trang-(.*?)\.htm', response.url)
            if current_page:
                next_page = int(current_page[0]) + 1
                next_url = '/'.join(response.url.split('/')[:-1]) + "/trang-{}.htm".format(next_page)
            else:
                next_page = 2
                next_url = '.'.join(response.url.split('.')[:-1]) + "/trang-{}.htm".format(next_page)
            yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
