# -*- coding: utf-8 -*-
import scrapy
import json
from lxml import etree
from ..items import NewsLink
import datetime


class VietnamNewsKenLinkSpider(scrapy.Spider):
    name = 'vietnam_news_ken_link'
    allowed_domains = ['kenh14.vn']
    start_urls = [
        "http://kenh14.vn/star/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/tv-show/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/cine/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/musik/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/beauty-fashion/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/doi-song/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/an-ca-the-gioi/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/xa-hoi/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/the-gioi/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/sport/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/hoc-duong/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/doi-song/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/doi-song/nhan-vat/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/xem-an-choi/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/doi-song/tram-yeu/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/beauty-fashion/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/beauty-fashion/skincare/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/beauty-fashion/makeup-hair/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/beauty-fashion/review-by-kenh14/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/beauty-fashion/fashion/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/sport/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/sport/bong-da/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/sport/hau-truong/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/sport/the-thao-khac/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/video/the-thao/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/sport/ngoai-hang-anh/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/musik/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/musik/au-my/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/musik/chau-a/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/musik/viet-nam/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/musik/edm/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/cine/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/cine/mot-phim/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/cine/phim-viet-nam/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/cine/phim-au-my/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/cine/phim-chau-a/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/2-tek/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/2-tek/mobile/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/2-tek/concept/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/2-tek/ung-dung-thu-thuat/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/2-tek/cong-nghe-vui/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/star/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/star/sao-viet/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/star/paparazzi/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/xa-hoi/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/xa-hoi/phap-luat/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/xa-hoi/nong-tren-mang/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/xa-hoi/song-xanh/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/hoc-duong/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/hoc-duong/nguoi-viet-tre/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/hoc-duong/du-hoc/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/hoc-duong/ban-tin-46/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/the-gioi/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/the-gioi/chum-anh/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/the-gioi/kham-pha/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/the-gioi/la-cool/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/esports/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/esports/cao-thu/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/esports/dau-truong/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/tv-show/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/suc-khoe-gioi-tinh/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/nhom-chu-de/lgbt/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/nhom-chu-de/nha-la-noi-de-ve/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/nhom-chu-de/magazine/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/nhom-chu-de/doc-cham/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/nhom-chu-de/photo-story/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/nhom-chu-de/hanh-trinh-wechoice-2018/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/nhom-chu-de/live-green/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "http://kenh14.vn/adv/{}.chn".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)

        # "http://kenh14.vn/timeline/laytinmoitronglist-2217-2-1-1-1-1-1-0-3-1.chn"
        # "http://kenh14.vn/timeline/laytinmoitronglist-1-2-1-1-1-1-{}-0-1-1.chn".format(i) for i in range(1, 200)
        # "http://kenh14.vn/timeline/laytinmoitronglist-1-2-1-1-1-1-{}-0-2-1.chn".format(i) for i in range(1, 200)
        # "http://kenh14.vn/timeline/laytinmoitronglist-1-2-1-1-1-1-{}-0-3-1.chn".format(i) for i in range(1, 200)
        # "http://kenh14.vn/timeline/laytinmoitronglist-1-2-1-1-1-1-{}-0-4-1.chn".format(i) for i in range(1, 200)
    ]

    def parse(self, response):
        # resp = json.loads(response.text)
        # data = resp.get("data")
        # if data:
        #     html = etree.HTML(data)
        #     links = html.xpath("//a/@href")
        #     links = list(set(links))
        #     urls = ["http://kenh14.vn" + item for item in links if "http" not in item]
        #     for url in urls:
        #         item = NewsLink()
        #         item['url'] = url
        #         item['ori_url'] = response.url
        #         yield item
        #
        #     nest_base_url = response.url.split("-")[0]
        #     param = response.url.split("-")[2:]
        #     next_page = int(response.url.split("-")[1]) + 1
        #     next_url = nest_base_url + "-" + "-".join([str(next_page)] + param)
        #     yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)

        links = response.xpath('//h3[@class="knswli-title"]/a/@href').extract()
        urls = ["http://kenh14.vn" + item for item in links if "http" not in item]
        for url in urls:
            item = NewsLink()
            item['url'] = url
            item['ori_url'] = response.url
            yield item

        next_page = response.xpath('//li[@class="next-page"]/a/@href').extract()
        if next_page:
            if "http" not in next_page:
                page_url = "http://kenh14.vn" + next_page[0]
            else:
                page_url = next_page[0]
            yield scrapy.Request(url=page_url, callback=self.parse, dont_filter=True)
