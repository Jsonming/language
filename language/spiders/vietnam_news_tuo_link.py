# -*- coding: utf-8 -*-
import scrapy
import pprint
import re
from language.items import NewsLink


class VietnamNewsTuoLinkSpider(scrapy.Spider):
    name = 'vietnam_news_tuo_link'
    allowed_domains = ['tuoitre.vn']
    start_urls = [
        # 'https://tuoitre.vn/tin-moi-nhat.htm'
        # 'https://tuoitre.vn/thoi-su.htm',
        # 'https://tuoitre.vn/the-gioi.htm',
        # 'https://tuoitre.vn/phap-luat.htm',
        # 'https://tuoitre.vn/kinh-doanh.htm',
        # 'https://tuoitre.vn/xe.htm',
        # 'https://tuoitre.vn/nhip-song-tre.htm',
        # 'https://tuoitre.vn/van-hoa.htm',
        # 'https://tuoitre.vn/giai-tri.htm',
        # 'https://tuoitre.vn/giao-duc.htm',
        # 'https://tuoitre.vn/khoa-hoc.htm',
        # 'https://tuoitre.vn/suc-khoe.htm',
        # 'https://tuoitre.vn/gia-that.htm',
        # 'https://tuoitre.vn/ban-doc-lam-bao.htm',
        # 'https://tuoitre.vn/media.htm',
        # 'https://tuoitre.vn/thoi-su.htm',
        # 'https://tuoitre.vn/the-gioi.htm',
        # 'https://tuoitre.vn/phap-luat.htm',
        # 'https://tuoitre.vn/kinh-doanh.htm',
        # 'https://tuoitre.vn/xe.htm',
        # 'https://tuoitre.vn/nhip-song-tre.htm',
        # 'https://tuoitre.vn/van-hoa.htm',
        # 'https://tuoitre.vn/giai-tri.htm',
        # 'https://tuoitre.vn/giao-duc.htm',
        # 'https://tuoitre.vn/khoa-hoc.htm',
        # 'https://tuoitre.vn/suc-khoe.htm',
        # 'https://tuoitre.vn/gia-that.htm',
        # 'https://tuoitre.vn/ban-doc-lam-bao.htm',

        # 'https://congnghe.tuoitre.vn',
        # 'https://congnghe.tuoitre.vn/timeline/200029/trang-1.htm',
        # 'https://thethao.tuoitre.vn',
        # 'https://thethao.tuoitre.vn/timeline/1209/trang-1.htm'
        # 'https://thethao.tuoitre.vn/timeline/1209/trang-287.htm'
        # 'https://dulich.tuoitre.vn',
        'https://dulich.tuoitre.vn/timeline/home-page-1.htm'
        # 'https://congnghe.tuoitre.vn',
        # 'https://congnghe.tuoitre.vn/timeline/200029/trang-1.htm'
        # 'https://thethao.tuoitre.vn',
        # 'https://thethao.tuoitre.vn/timeline/1209/trang-2.htm'
        # 'https://dulich.tuoitre.vn',
        # 'https://dulich.tuoitre.vn/timeline/home-page-2.htm'

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
