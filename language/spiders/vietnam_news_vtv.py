# -*- coding: utf-8 -*-
import re
import scrapy
from ..items import NewsLink
import datetime


class VietnamNewsVtvSpider(scrapy.Spider):
    name = 'vietnam_news_vtv'
    allowed_domains = ['vtv.vn']
    start_urls = [
        # 'https://vtv.vn/trong-nuoc.htm',
        # 'https://vtv.vn/timeline/121/trang-1.htm',
        # 'https://vtv.vn/the-gioi.htm',
        # "https://vtv.vn/timeline/122/trang-1.htm",
        # 'https://vtv.vn/the-thao.htm',
        # 'https://vtv.vn/the-thao/special/trang-1.htm'
        # 'https://vtv.vn/the-thao/bong-da-trong-nuoc/trang-1.htm'
        # 'https://vtv.vn/the-thao/bong-da-quoc-te/trang-1.htm'
        # 'https://vtv.vn/the-thao/tennis/trang-1.htm',
        # 'https://vtv.vn/the-thao/cac-mon-khac/trang-1.htm',
        # 'https://vtv.vn/the-thao/ben-le/trang-1.htm',
        # 'https://vtv.vn/truyen-hinh.htm',
        # 'https://vtv.vn/timeline/88/trang-1.htm',
        # 'https://vtv.vn/van-hoa-giai-tri.htm',
        # "https://vtv.vn/timeline/87/trang-1.htm",
        # 'https://vtv.vn/kinh-te.htm',
        # "https://vtv.vn/timeline/90/trang-1.htm",
        # 'https://vtv.vn/tieu-dung.htm',
        # "https://vtv.vn/timeline/220/trang-1.htm",
        # 'https://vtv.vn/doi-song.htm',
        # "https://vtv.vn/timeline/132/trang-1.htm",
        # 'https://vtv.vn/suc-khoe.htm',
        # "https://vtv.vn/suc-khoe/nong/trang-1.htm",
        # "https://vtv.vn/suc-khoe/benh-hiem-ngheo/trang-1.htm",
        # "https://vtv.vn/suc-khoe/y-hoc-the-gioi/trang-1.htm",
        # "https://vtv.vn/suc-khoe/tieu-diem/trang-1.htm",
        # "https://vtv.vn/suc-khoe/song-khoe/trang-1.htm",
        # "https://vtv.vn/suc-khoe/benh-vien-online/trang-1.htm",
        # "https://vtv.vn/suc-khoe/tiep-suc-nguoi-benh/trang-1.htm",
        # 'https://vtv.vn/giao-duc.htm',
        # "https://vtv.vn/timeline/192/trang-1.htm"
        # 'https://vtv.vn/cong-nghe.htm',
        # "https://vtv.vn/timeline/109/trang-1.htm",
        # "https://vtv.vn/timeline/80/trang-1.htm",
        # 'https://vtv.vn/goc-khan-gia.htm',
        # "https://vtv.vn/timeline/120/trang-1.htm"
        # "https://vtv.vn/timeline/{}/trang-1.htm".format(i) for i in range(0, 100)
        # 'https://vtv.vn/magazine.htm',
        # "https://vtv.vn/ajax/loadmagazine-page3.htm"
        # "https://vtv.vn/timeline/120/trang-61.htm",
        # "https://vtv.vn/timeline/191/trang-35.htm",
        # "https://vtv.vn/timeline/189/trang-46.htm",
        # "https://vtv.vn/timeline/179/trang-49.htm",
        # "https://vtv.vn/timeline/184/trang-52.htm",
        # "https://vtv.vn/timeline/103/trang-63.htm",
        # "https://vtv.vn/timeline/180/trang-51.htm",
        # "https://vtv.vn/timeline/133/trang-53.htm",
        # "https://vtv.vn/timeline/104/trang-59.htm",
        # "https://vtv.vn/timeline/122/trang-59.htm",
        # "https://vtv.vn/timeline/197/trang-10.htm",
        # "https://vtv.vn/timeline/185/trang-50.htm",
        # "https://vtv.vn/timeline/192/trang-22.htm",
        # "https://vtv.vn/timeline/196/trang-11.htm",
        # "https://vtv.vn/timeline/198/trang-1.htm",
        # "https://vtv.vn/timeline/134/trang-56.htm",
        # "https://vtv.vn/timeline/188/trang-45.htm",
        # "https://vtv.vn/timeline/101/trang-61.htm",
        # "https://vtv.vn/timeline/132/trang-61.htm",
        # 'https://vtv.vn/timeline/166/trang-54.htm',
        # 'https://vtv.vn/timeline/182/trang-49.htm',
        # 'https://vtv.vn/timeline/131/trang-65.htm',
        # 'https://vtv.vn/timeline/178/trang-52.htm',
        # 'https://vtv.vn/timeline/130/trang-58.htm',
        # 'https://vtv.vn/timeline/102/trang-61.htm',
        # 'https://vtv.vn/timeline/109/trang-57.htm',

        # "https://vtv.vn/trong-nuoc/xem-theo-ngay/{}.htm".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(365, 10*365)
        # "https://vtv.vn/kinh-te/xem-theo-ngay/{}.htm".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        "https://vtv.vn/viet-nam-va-the-gioi/xem-theo-ngay/{}.htm".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "https://vtv.vn/viet-nam-hom-nay/xem-theo-ngay/{}.htm".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "https://vtv.vn/chuyen-dong-24h/xem-theo-ngay/{}.htm".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "https://vtv.vn/the-gioi/xem-theo-ngay/{}.htm".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "https://vtv.vn/doi-song/xem-theo-ngay/{}.htm".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "https://vtv.vn/goc-khan-gia/xem-theo-ngay/{}.htm".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "https://vtv.vn/truyen-hinh/xem-theo-ngay/{}.htm".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "https://vtv.vn/van-hoa-giai-tri/xem-theo-ngay/{}.htm".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "https://vtv.vn/viet-nam-hom-nay/xem-theo-ngay/{}.htm".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "https://vtv.vn/doi-song/xem-theo-ngay/{}.htm".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "https://vtv.vn/giao-duc/xem-theo-ngay/{}.htm".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "https://vtv.vn/cong-nghe/xem-theo-ngay/{}.htm".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
        # "https://vtv.vn/goc-khan-gia/xem-theo-ngay/{}.htm".format((datetime.datetime.today() + datetime.timedelta(days=-i)).strftime("%d-%m-%Y")) for i in range(0, 6 * 365)
    ]

    def parse(self, response):
        title = response.xpath('//h4/a/@href').extract()
        icon = response.xpath('//li/p[last()]/a/@href').extract()
        paragrah = response.xpath('//div[@class="item itemsmall"]/h3/a/@href').extract()
        links = []
        links.extend(title)
        links.extend(icon)
        links.extend(paragrah)

        urls = ['https://vtv.vn' + item for item in links]
        for url in urls:
            item = NewsLink()
            item['url'] = url
            item['ori_url'] = response.url
            yield item

        # if links:
        #     current_page = re.findall(r'trang-(.*?)\.htm', response.url)[0]
        #     current_para = response.url.split('/')[-1]
        #     next_url = response.url.replace(current_para, '') + "trang-{}.htm".format(int(current_page) + 1)
        #     yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)

        next_page = response.xpath(
            '//*[@id="admWrapsite"]/div[3]/div[5]/div[2]/div[1]/div[3]/a[last()]/@href').extract_first()
        next_url = 'https://vtv.vn' + next_page
        yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
