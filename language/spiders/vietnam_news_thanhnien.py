# -*- coding: utf-8 -*-
import re
import scrapy
from ..items import NewsLink


class VietnamNewsThanhnienSpider(scrapy.Spider):
    name = 'vietnam_news_thanhnien'
    allowed_domains = ['thanhnien.vn']
    start_urls = [
        # 'https://thanhnien.vn/thoi-su/trang-1.html',
        # 'https://thanhnien.vn/the-gioi/trang-1.html',
        # 'https://thanhnien.vn/tai-chinh-kinh-doanh/trang-1.html',
        # 'https://thanhnien.vn/doi-song/trang-1.html',
        # 'https://thanhnien.vn/van-hoa/trang-1.html',
        # 'https://thanhnien.vn/gioi-tre/trang-1.html',
        # 'https://thanhnien.vn/giao-duc/trang-1.html',
        # 'https://thanhnien.vn/suc-khoe/trang-1.html',
        # 'https://thanhnien.vn/du-lich/trang-1.html',
        # 'https://thanhnien.vn/cong-nghe/trang-1.html',
        # 'https://thethao.thanhnien.vn/trang-1.html',
        # 'https://xe.thanhnien.vn/trang-1.html',

        'https://thanhnien.vn/thoi-su/trang-1.html',
        'https://thanhnien.vn/the-gioi/trang-1.html',
        'https://thanhnien.vn/tai-chinh-kinh-doanh/trang-1.html',
        'https://thanhnien.vn/doi-song/trang-1.html',
        'https://thanhnien.vn/van-hoa/trang-1.html',
        'https://thanhnien.vn/gioi-tre/trang-1.html',
        'https://thanhnien.vn/giao-duc/trang-1.html',
        'https://thanhnien.vn/suc-khoe/trang-1.html',
        'https://thanhnien.vn/du-lich/trang-1.html',
        'https://thanhnien.vn/cong-nghe/trang-1.html',
        'https://thethao.thanhnien.vn/trang-1.html',
        'https://xe.thanhnien.vn/https://thanhnien.vn/thoi-su/chinh-tri/trang-1.html',
        'https://thanhnien.vn/thoi-su/phap-luat/trang-1.html',
        'https://thanhnien.vn/thoi-su/dan-sinh/trang-1.html',
        'https://thanhnien.vn/thoi-su/viec-lam/trang-1.html',
        'https://thanhnien.vn/thoi-su/quyen-duoc-biet/trang-1.html',
        'https://thanhnien.vn/thoi-su/phong-su-dieu-tra/trang-1.html',
        'https://thanhnien.vn/thoi-su/quoc-phong/trang-1.html',
        'https://thanhnien.vn/the-gioi/kinh-te-the-gioi/trang-1.html',
        'https://thanhnien.vn/the-gioi/quan-su/trang-1.html',
        'https://thanhnien.vn/the-gioi/goc-nhin/trang-1.html',
        'https://thanhnien.vn/the-gioi/ho-so/trang-1.html',
        'https://thanhnien.vn/the-gioi/hau-truong/trang-1.html',
        'https://thanhnien.vn/the-gioi/nguoi-viet-nam-chau/trang-1.html',
        'https://thanhnien.vn/kinh-doanh/chinh-sach-phat-trien/trang-1.html',
        'https://thanhnien.vn/tai-chinh-kinh-doanh/ngan-hang/trang-1.html',
        'https://thanhnien.vn/tai-chinh-kinh-doanh/chung-khoan/trang-1.html',
        'https://thanhnien.vn/tai-chinh-kinh-doanh/doanh-nghiep/trang-1.html',
        'https://thanhnien.vn/tai-chinh-kinh-doanh/doanh-nhan/trang-1.html',
        'https://thanhnien.vn/tai-chinh-kinh-doanh/tieu-dung/trang-1.html',
        'https://thanhnien.vn/tai-chinh-kinh-doanh/lam-giau/trang-1.html',
        'https://thanhnien.vn/tai-chinh-kinh-doanh/dia-oc/trang-1.html',
        'https://thanhnien.vn/doi-song/nguoi-song-quanh-ta/trang-1.html',
        'https://thanhnien.vn/doi-song/gia-dinh/trang-1.html',
        'https://thanhnien.vn/doi-song/am-thuc/trang-1.html',
        'https://thanhnien.vn/doi-song/cong-dong/trang-1.html',
        'https://thanhnien.vn/doi-song/spa-tham-my/trang-1.html',
        'https://thanhnien.vn/van-hoa/dien-anh/trang-1.html',
        'https://thanhnien.vn/van-hoa/truyen-hinh/trang-1.html',
        'https://thanhnien.vn/van-hoa/cau-chuyen/trang-1.html',
        'https://thanhnien.vn/gioi-tre/song-yeu-an-choi/trang-1.html',
        'https://thanhnien.vn/gioi-tre/the-gioi-mang/trang-1.html',
        'https://thanhnien.vn/gioi-tre/ket-noi/trang-1.html',
        'https://thanhnien.vn/giao-duc/tuyen-sinh/2019/trang-1.html',
        'https://thanhnien.vn/giao-duc/hop-thu-tu-van-24-7/trang-1.html',
        'https://thanhnien.vn/giao-duc/du-hoc/trang-1.html',
        'https://thanhnien.vn/giao-duc/chon-nghe/trang-1.html',
        'https://thanhnien.vn/giao-duc/chon-truong/trang-1.html',
        'https://thanhnien.vn/giao-duc/nguoi-thay/trang-1.html',
        'https://thanhnien.vn/suc-khoe/lam-dep/trang-1.html',
        'https://thanhnien.vn/suc-khoe/khoe-dep-moi-ngay/trang-1.html',
        'https://thanhnien.vn/suc-khoe/gioi-tinh/trang-1.html',
        'https://thanhnien.vn/suc-khoe/yeu-da-day/trang-1.html',
        'https://thanhnien.vn/du-lich/kham-pha/trang-1.html',
        'https://thanhnien.vn/du-lich/a-z/trang-1.html',
        'https://thanhnien.vn/du-lich/san-tour/trang-1.html',
        'https://thanhnien.vn/cong-nghe/xu-huong/trang-1.html',
        'https://thanhnien.vn/cong-nghe/san-pham-moi/trang-1.html',
        'https://thanhnien.vn/cong-nghe/kinh-nghiem/trang-1.html',
        'https://thanhnien.vn/cong-nghe/y-tuong/trang-1.html',
        'https://thanhnien.vn/bong-da-viet-nam/trang-1.html',
        'https://thanhnien.vn/bong-da-quoc-te/trang-1.html',
        'https://thanhnien.vn/binh-luan/trang-1.html',
        'https://thanhnien.vn/quan-vot/trang-1.html',
        'https://thanhnien.vn/hau-truong/trang-1.html',
        'https://thanhnien.vn/toan-canh-the-thao/trang-1.html',
        'https://xe.thanhnien.vn/tin-tuc/trang-1.html',
        'https://xe.thanhnien.vn/tu-van/trang-1.html',
        'https://xe.thanhnien.vn/dien-dan/trang-1.html',
        'https://xe.thanhnien.vn/danh-gia-xe/trang-1.html',
        'https://xe.thanhnien.vn/kham-pha/trang-1.html',
        'https://xe.thanhnien.vn/clip/',

    ]

    def parse(self, response):
        links = response.xpath('//article[@class="story"]/a/@href').extract()
        urls = ["https://thanhnien.vn" + item for item in links]
        for url in urls:
            item = NewsLink()
            item['url'] = url
            item['ori_url'] = response.url
            yield item
            # print(item)

        if links:
            current_page = re.findall(r'trang-(.*?)\.html', response.url)
            if current_page:
                current_page = current_page[0]
            else:
                current_page = 1
            current_para = response.url.split('/')[-1]
            next_url = response.url.replace(current_para, '') + "trang-{}.html".format(int(current_page) + 1)
            yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)