# -*- coding: utf-8 -*-
import scrapy
from ..items import ImgLink


class IndonesiaGoodsLinkSpider(scrapy.Spider):
    name = 'indonesia_goods_link'
    allowed_domains = ['www.tokopedia.com/p']
    start_urls = ['http://www.tokopedia.com/p/']

    def parse(self, response):
        links = response.xpath('//div[@class="_2GHyylTH"]/div/div[2]//a/@href').extract()
        links = ["https://www.tokopedia.com"+ item for item in links]
        for link in links:
            item = ImgLink()
            item["url"] = link
            yield item