# -*- coding: utf-8 -*-
import scrapy
from ..items import NewsContentItem
from ..items import NewsLink
import json
import re


class VietnamNewsVnSpider(scrapy.Spider):
    name = 'vietnam_news_vn'
    allowed_domains = ['vnexpress.net']
    start_urls = [
        # 'https://vnexpress.net/thoi-su',
        'https://vnexpress.net/the-gioi',
        'https://vnexpress.net/kinh-doanh',
        'https://vnexpress.net/giai-tri',
        # 'https://vnexpress.net/the-thao',
        # 'https://vnexpress.net/phap-luat',
        # 'https://vnexpress.net/giao-duc',
        # 'https://vnexpress.net/suc-khoe',
        # 'https://vnexpress.net/doi-song',
        # 'https://vnexpress.net/du-lich',
        # 'https://vnexpress.net/khoa-hoc',
        # 'https://vnexpress.net/so-hoa',
        # 'https://vnexpress.net/oto-xe-may',
        # 'https://vnexpress.net/y-kien',
        # 'https://vnexpress.net/tam-su',
        # 'https://vnexpress.net/cuoi',


        # 'https://vnexpress.net/ajax/goc-nhin?category_id=1003450&page=1&exclude=3&rule=2'
    ]

    def parse(self, response):
        # data = json.loads(response.text)
        # message = data.get("message")
        # links = []
        # for it in message:
        #     links.append(it.get("share_url"))
        # for url in links:
        #     item = NewsLink()
        #     item['url'] = url
        #     item["ori_url"] = response.url
        #     yield item
        # current_page = re.findall(r"&page=(.*?)&", response.url)[0]
        # if message:
        #     nest_url = 'https://vnexpress.net/ajax/goc-nhin?category_id=1003450&page={}&exclude=3&rule=2'.format(int(current_page)+1)
        #     yield scrapy.Request(url=nest_url, callback=self.parse, dont_filter=True)

        links = response.xpath('/html/body/section/section[1]/article/h4/a[1]/@href').extract()

        for url in links:
            item = NewsLink()
            item['url'] = url
            item["ori_url"] = response.url
            yield item

        nest_link = []
        nest_link_zero = response.xpath('//*[@id="pagination"]/a[@class="next"]/@href').extract()
        nest_link_one = response.xpath('/html/body/section[3]/section[1]/div[2]/a[last()]/@href').extract()
        nest_link_two = response.xpath('/html/body/section[2]/section[1]/div[2]/a[last()]/@href').extract()
        nest_link.extend(nest_link_zero)
        nest_link.extend(nest_link_one)
        nest_link.extend(nest_link_two)

        if nest_link:
            if "https" not in nest_link[0]:
                next_page_url = 'https://vnexpress.net' + nest_link[0]
            else:
                next_page_url = nest_link[0]
            yield scrapy.Request(url=next_page_url, callback=self.parse, dont_filter=True)
            print(nest_link)
            print(next_page_url)

    # def parse_item(self, response):
    #     description = response.xpath('//section/p/text()').extract()
    #     paragraph_new = response.xpath('//article//p/text()').extract()
    #     content = ' '.join(description + paragraph_new).replace('\n', '')
    #     item = NewsContentItem()
    #     item['url'] = response.url
    #     item['content'] = content
    #     file = r"C:\Users\Administrator\Desktop\vietnam_news_content_new.txt"
    #     if content:
    #         with open(file, 'a', encoding='utf8') as f:
    #             f.write(content + "\n")
