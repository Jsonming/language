# -*- coding: utf-8 -*-
import scrapy


class MalaysiaGoodsNewSpider(scrapy.Spider):
    name = 'malaysia_goods_new'
    allowed_domains = ['www.11street.my/category/travel-ticket/malaysia/5492']
    # start_urls = ['http://www.11street.my/category/travel-ticket/malaysia/5492/']
    # start_urls = [' https://www.11street.my/totalsearch/TotalSearchAction/new/getProductSearchAjax.do?lCtgrNo=5490&mCtgrNo=5492&sCtgrNo=0&totalCount=80&isCategoryNavigation=Y&kwd=5492']
    # start_urls = ['https://www.11street.my/totalsearch/TotalSearchAction/new/getSearchAdditionalDataAjax.do?lCtgrNo=5490&mCtgrNo=5492&sCtgrNo=0&isCategoryNavigation=Y&kwd=5492&hasAdvert=true']
    start_urls = ['https://www.11street.my/totalsearch/TotalSearchAction/new/getProductSearchAjax.do?lCtgrNo=5490&mCtgrNo=5492&sCtgrNo=0&totalCount=80&isCategoryNavigation=Y&kwd=5492&pageNum=2']


    def parse(self, response):
        names = response.xpath('//*[@id="productlist"]/li[2]/dlv/div[2]/h3/a/text()').extract()
        print(names)
