# -*- coding: utf-8 -*-
import scrapy
import pprint
import datetime
import re
from language.items import NewsLink


class VietnamNewsTuoLinkSpider(scrapy.Spider):
    name = 'vietnam_news_tuo_link'
    allowed_domains = ['tuoitre.vn']
    start_urls = [
        # 'https://tuoitre.vn/xem-theo-ngay/{}.htm'.format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(10*365)
        # 'https://tuoitre.vn/thoi-su/xem-theo-ngay/{}.htm'.format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(10*365)
        # 'https://tuoitre.vn/the-gioi/xem-theo-ngay/{}.htm'.format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(10*365)
        # 'https://tuoitre.vn/phap-luat/xem-theo-ngay/{}.htm'.format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(10*365)
        # 'https://tuoitre.vn/kinh-doanh/xem-theo-ngay/{}.htm'.format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(10*365)
        # 'https://tu:oitre.vn/xe/xem-theo-ngay/{}.htm'.format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(10*365)
        # 'https://tuoitre.vn/nhip-song-tre/xem-theo-ngay/{}.htm'.format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(10*365)
        # 'https://tuoitre.vn/van-hoa/xem-theo-ngay/{}.htm'.format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(10*365)
        # 'https://tuoitre.vn/giai-tri/xem-theo-ngay/{}.htm'.format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(10*365)
        # 'https://tuoitre.vn/giao-duc/xem-theo-ngay/{}.htm'.format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(10*365)
        # 'https://tuoitre.vn/khoa-hoc/xem-theo-ngay/{}.htm'.format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(10*365)
        # 'https://tuoitre.vn/suc-khoe/xem-theo-ngay/{}.htm'.format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(10*365)
        # 'https://tuoitre.vn/gia-that/xem-theo-ngay/{}.htm'.format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(10*365)
        # 'https://tuoitre.vn/ban-doc-lam-bao/xem-theo-ngay/{}.htm'.format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(10*365)


        # 'https://congnghe.tuoitre/{}.htm'.format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(10*365)
        # 'https://dulich.tuoitre/{}.htm'.format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(10*365)
        # 'https://congnghe.tuoitre/{}.htm'.format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(10*365)
        # 'https://thethao.tuoitre/{}.htm'.format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(10*365)
        # 'https://dulich.tuoitre/{}.htm'.format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(10*365)

    ]

    def parse(self, response):
        links = []
        links.extend(response.xpath('//li[@class="news-item"]/a/@href').extract())
        links.extend(response.xpath('//ul[@class="lstnews ajaxloaded"]//a/@href').extract())
        links = list(set(links))
        if links:
            for link in links:
                if "http" not in link:
                    url = "https://tuoitre.vn" + link
                else:
                    url = link
                item = NewsLink()
                item['url'] = url
                item['ori_url'] = response.url
                yield item
            if "trang" in response.url:
                current_page = re.findall('trang-(.*?)\.htm', response.url)
                if current_page:
                    next_page = int(current_page[0]) + 1
                    next_url = '/'.join(response.url.split('/')[:-1]) + "/trang-{}.htm".format(next_page)
                else:
                    next_page = 2
                    next_url = '.'.join(response.url.split('.')[:-1]) + "/trang-{}.htm".format(next_page)
                yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
            elif "page" in response.url:
                current_page = re.findall('home-page-(.*?).htm', response.url)
                if current_page:
                    next_page = int(current_page[0]) + 1
                    next_url = '/'.join(response.url.split('/')[:-1]) + "/home-page-{}.htm".format(next_page)
                else:
                    next_page = 2
                    next_url = '.'.join(response.url.split('.')[:-1]) + "/home-page-{}.htm".format(next_page)
                yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
