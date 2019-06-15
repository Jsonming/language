# -*- coding: utf-8 -*-
import scrapy
from ..items import ShortWordLink
import json


class MalaysiaGoodsNameSpider(scrapy.Spider):
    name = 'malaysia_goods_name'
    allowed_domains = ['www.11street.my']
    start_urls = ['http://www.11street.my/']

    def parse(self, response):
        type_links = response.xpath('//li[@class="main-categories collapsible"]//a/@href').extract()
        for url in type_links:
            if "https" not in url:
                clas_id = url.split('/')[-1]
                if clas_id.isdigit():
                    for i in range(1, 10):
                        page_url = "https://www.11street.my/totalsearch/TotalSearchAction/new/getProductSearchAjax.do?&mCtgrNo={}&sCtgrNo=0&isCategoryNavigation=Y&kwd={}&pageNum={}".format(
                            clas_id, clas_id, i)
                        print(page_url)
                        yield scrapy.Request(url=page_url, callback=self.parse_item, dont_filter=True)

    def parse_item(self, response):
        names = []
        data = json.loads(response.body)
        productList = data.get("productList")
        for product in productList:
            name = product.get("prdNm")
            names.append(name)
        with open(r'C:\Users\Administrator\Desktop\malaya_temp\goods_name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(names))
