# -*- coding: utf-8 -*-
import scrapy


class VietnamDiplomaticLinkSpider(scrapy.Spider):
    name = 'vietnam_diplomatic_link'
    allowed_domains = ['www.mofa.gov.vn/vi']
    start_urls = [
        # 'http://www.mofa.gov.vn/vi/nr040807104143/nr111027144142/folder_listing?b_start:int={}'.format(i) for i in
        # range(0, 5 * 275, 5)
        # 'http://www.mofa.gov.vn/vi/nr040807104143/nr111027144142/folder_listing?b_start:int=0'
        "http://www.mofa.gov.vn/vi/nr040807104143/nr111027144142/ns190623215024"

    ]

    # def start_requests(self):
    #     header = {
    #         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    #         "Cookie": "_ga=GA1.3.873859241.1562077386; D0N=d06dcf91481f81c9e08d5a26af5bf255; _gid=GA1.3.1662728525.1562507021"
    #     }
    #     url = 'http://www.mofa.gov.vn/vi/nr040807104143/nr111027144142/folder_listing?b_start:int=0'
    #     yield scrapy.Request(url=url, headers=header, callback=self.parse, dont_filter=True)

    def parse(self, response):
        # links = response.xpath('//td/a/@href').extract()
        print(response.text)
