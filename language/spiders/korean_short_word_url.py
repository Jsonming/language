# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import ShortWordLink


class KoreanShortWordUrlSpider(scrapy.Spider):
    name = 'korean_short_word_url'
    allowed_domains = ['http://kr.tingroom.com']
    start_urls = [
        "http://kr.tingroom.com/hych/hywlch/",
        "http://kr.tingroom.com/hych/hyshch/",
        "http://kr.tingroom.com/hych/hyjsjch/",
        "http://kr.tingroom.com/hych/swhych/",
        "http://kr.tingroom.com/hych/syhych/",
        "http://kr.tingroom.com/hych/TOPIKch/",
        "http://kr.tingroom.com/hych/fkhych/",
        "http://kr.tingroom.com/hych/hycjch/",
        "http://kr.tingroom.com/hych/zhuanyech/",
        "http://kr.tingroom.com/hych/huoyonghanyuxuehanyu/",
        "http://kr.tingroom.com/hych/hanyuguanyongyu/",
        "http://kr.tingroom.com/hych/yonghanzixuehanyu/",
        "http://kr.tingroom.com/hych/hanyutaicidapei/",
        "http://kr.tingroom.com/hych/hanguogequjiexi/",
        "http://kr.tingroom.com/hych/hanguoyugudingdapei/",
        "http://kr.tingroom.com/hych/hanyusuyu/",
        "http://kr.tingroom.com/hych/ytybhydc/",
    ]

    def parse(self, response):
        page_cont = response.xpath("//cite/text()").extract()[0]
        page_count = re.findall("[0-9]+", page_cont)[1]
        print(page_count)
        for i in range(1, int(page_count)+1):
            url = response.url + "list_{}.html".format(i)
            yield scrapy.Request(url=url, callback=self.parse_item, dont_filter=True)

    def parse_item(self, response):
        short_word_url = response.xpath('//ul[@class="e2"]//a/@href').extract()
        for url in short_word_url:
            item = ShortWordLink()
            item["url"] = url
            yield item
