# -*- coding: utf-8 -*-
import scrapy


class VietnamTikiSpider(scrapy.Spider):
    name = 'vietnam_tiki'
    allowed_domains = ['https://tiki.vn/']
    start_urls = ['https://tiki.vn/dien-thoai-may-tinh-bang/c1789?src=mega-menu']

    def parse(self, response):
        category_list = response.xpath('//*[@id="header"]/div[3]/div/nav/ul//a')
        for category in category_list:
            link = category.xpath('./@href').extract()
            cate = category.xpath('./text()').extract()
            url = link[0]
            cla = cate[0].strip()

            print(url)
            # print(cla)


        # url = 'https://tiki.vn/chuong-trinh/dien-gia-dung-gia-soc?ref=main-category-banner&_lc=Vk4wMzkwMTkwMTc%3D&src=home3_menu_diengiadung'
        # req = scrapy.Request(url=url, callback=self.parse_item, dont_filter=True)
        # req.meta['category'] = 'Nạp Dung Lượng 3G/4G'
        # yield req

    def parse_item(self, response):
        name = response.xpath('//div[@class="lp-product-item sc-fjdhpX igOxad"]//a/@href').extract()
        print(name)
        print(response.meta['category'])