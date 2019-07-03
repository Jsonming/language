# -*- coding: utf-8 -*-
import scrapy
from ..items import NewsLink


class VietnamNewsDangLinkSpider(scrapy.Spider):
    name = 'vietnam_news_dang_link'
    allowed_domains = ['www.dangcongsan.vn']
    start_urls = [
        #'http://www.dangcongsan.vn/thoi-su.html?page=1099',
        #"http://www.dangcongsan.vn/lanh-dao-dang-nha-nuoc.html",
        #"http://www.dangcongsan.vn/xay-dung-dang.html",
        #"http://www.dangcongsan.vn/tu-tuong-van-hoa.html",
        #"http://www.dangcongsan.vn/kinh-te.html",
        #"http://www.dangcongsan.vn/xa-hoi.html",
        #"http://www.dangcongsan.vn/khoa-giao.html",
        # "http://www.dangcongsan.vn/xa-hoi.html",
        # "http://www.dangcongsan.vn/khoa-giao.html",
        # "http://www.dangcongsan.vn/phap-luat.html",
        # "http://www.dangcongsan.vn/ban-doc.html",
        # "http://www.dangcongsan.vn/the-thao.html",
        # "http://www.dangcongsan.vn/bien-dao-viet-nam.html",
        # "http://www.dangcongsan.vn/doi-ngoai.html",
        
        # "http://www.dangcongsan.vn/the-gioi.html",
        # "http://www.dangcongsan.vn/the-gioi/tin-tuc.html",
        # "http://www.dangcongsan.vn/the-gioi/the-gioi-noi-ve-viet-nam.html",
        # "http://www.dangcongsan.vn/nguoi-viet-nam-o-nuoc-ngoai.html",
        # "http://www.dangcongsan.vn/the-gioi/nhung-van-de-toan-cau.html",
        
        # "http://www.dangcongsan.vn/ban-doc.html",
        # "http://www.dangcongsan.vn/ban-doc/dieu-tra-theo-don-thu.html",
        # "http://www.dangcongsan.vn/ban-doc/hoi-dap.html",
        # "http://www.dangcongsan.vn/ban-doc/hop-thu-ban-doc.html",
        
         "http://www.dangcongsan.vn/hoc-va-lam-theo-bac.html",
         "http://www.dangcongsan.vn/hoc-va-lam-theo-bac/van-kien-tu-lieu.html",
         "http://www.dangcongsan.vn/hoc-va-lam-theo-bac/tin-hoat-dong.html",
         "http://www.dangcongsan.vn/hoc-va-lam-theo-bac/thong-tin-ve-cuoc-thi.html",
         "http://www.dangcongsan.vn/hoc-va-lam-theo-bac/45-nam-thuc-hien-di-chuc-cua-chu-tich-ho-chi-minh.html",
        
        # "http://www.dangcongsan.vn/doi-ngoai.html",
        # "http://www.dangcongsan.vn/dau-tranh-chong-quan-diem-sai-trai.html",
        # "http://www.dangcongsan.vn/chong-quan-lieu-tham-nhung-lang-phi.html",
        # "http://www.dangcongsan.vn/cung-ban-luan.html",
        #
        # "http://www.dangcongsan.vn/anh.html",
        # "http://www.dangcongsan.vn/dai-hoi-thi-dua-yeu-nuoc.html",
        # "http://www.dangcongsan.vn/hai-phong-thanh-pho-cang-xanh-van-minh-hien-dai.html",
        # "http://www.dangcongsan.vn/bien-dao-viet-nam.html",
        #
        # "http://www.dangcongsan.vn/day-manh-cai-cach-tu-phap-va-hoat-dong-tu-phap.html",
        # "http://www.dangcongsan.vn/day-manh-cai-cach-tu-phap-va-hoat-dong-tu-phap/tin-tuc.html",
        # "http://www.dangcongsan.vn/day-manh-cai-cach-tu-phap-va-hoat-dong-tu-phap/duong-loi-chinh-sach.html",
        # "http://www.dangcongsan.vn/day-manh-cai-cach-tu-phap-va-hoat-dong-tu-phap/hoi-dap.html",
        # "http://www.dangcongsan.vn/huong-ve-bien-dao-que-huong.html",
        #
        # "http://www.dangcongsan.vn/an-toan-giao-thong.html",
        # "http://www.dangcongsan.vn/an-toan-giao-thong/vi-hanh-phuc-cua-moi-nguoi.html",
        # "http://www.dangcongsan.vn/an-toan-giao-thong/giao-thong-24-gio.html",
        # "http://www.dangcongsan.vn/an-toan-giao-thong/van-ban-moi.html",
        # "http://www.dangcongsan.vn/an-toan-giao-thong/nhin-ra-the-gioi.html",
        #
        # "http://www.dangcongsan.vn/doi-moi-can-ban-va-toan-dien-giao-duc-dao-tao.html",
        # "http://www.dangcongsan.vn/doi-moi-can-ban-va-toan-dien-giao-duc-dao-tao/tin-tuc.html",
        # "http://www.dangcongsan.vn/doi-moi-can-ban-va-toan-dien-giao-duc-dao-tao/duong-loi-chinh-sach.html",
        # "http://www.dangcongsan.vn/doi-moi-can-ban-va-toan-dien-giao-duc-dao-tao/dien-dan.html",
        # "http://www.dangcongsan.vn/doi-moi-can-ban-va-toan-dien-giao-duc-dao-tao/chu-nghia-mac-lenin-tu-tuong-ho-chi-minh-ve-giao-duc-dao-tao.html",
        #
        # "http://www.dangcongsan.vn/giao-luu-truc-tuyen.html",
        # "http://www.dangcongsan.vn/tai-chinh-va-chung-khoan.html",
        # "http://www.dangcongsan.vn/tai-chinh-va-chung-khoan/nhung-van-de-tai-chinh-chung-khoan.html",
        # "http://www.dangcongsan.vn/tai-chinh-va-chung-khoan/gia-chung-khoan.html"
        # "http://www.dangcongsan.vn/luat-bien-viet-nam.html",
        # "http://www.dangcongsan.vn/kinh-te-va-hoi-nhap.html",
        # "http://www.dangcongsan.vn/thong-tin-kinh-te.html",
        # "http://www.dangcongsan.vn/phap-luat.html"
    ]

    def parse(self, response):
        links = response.xpath('//div[@class="w-list"]//a[@class="item-title"]/@href').extract()
        links_first = response.xpath('//div[@class="w-list"]//a[@class="item-title"]/@href').extract()
        urls = []
        urls.extend(links)
        urls.extend(links_first)
        urls = list(set(urls))
        for url in urls:
            item = NewsLink()
            item['url'] = url
            item['ori_url'] = response.url
            yield item

        if urls:
            current_page = response.url.split("=")[-1]
            if current_page.isdecimal():
                page = response.url.split("?")[-1]
                nest_url = response.url.replace(page, '') + "page={}".format(int(current_page) + 1)
            else:
                nest_url = response.url + "?page=2"
            yield scrapy.Request(url=nest_url, callback=self.parse, dont_filter=True)
