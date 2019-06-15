# -*- coding: utf-8 -*-
import json
import scrapy
import re
from urllib.parse import unquote
from ..items import TradeName


class VietnamShoopeeNameSpider(scrapy.Spider):
    name = 'vietnam_shoopee_name'
    allowed_domains = ['https://shopee.vn']
    urls = []
    # urls.extend(['https://shopee.vn/api/v2/search_items/?by=relevancy&keyword=ch%C3%A2n%20v%C3%A1y%20d%C3%A0i&limit=50&newest={}&order=desc&page_type=search'.format(
    #         i) for i in range(0, 100 * 50 + 1, 50)])
    # urls.extend(['https://shopee.vn/api/v2/search_items/?by=relevancy&keyword=%C4%91%E1%BB%93%20b%C6%A1i%20b%C3%A9%20g%C3%A1i&limit=50&newest={}&order=desc&page_type=search'.format(
    #         i) for i in range(0, 100 * 50 + 1, 50)])
    # urls.extend(['https://shopee.vn/api/v2/search_items/?by=relevancy&keyword=t%E1%BB%A7%20nh%E1%BB%B1a%20%C4%91%C3%A0i%20loan&limit=50&newest={}&order=desc&page_type=search'.format(
    #         i) for i in range(0, 53 * 50 + 1, 50)])
    # urls.extend(['https://shopee.vn/api/v2/search_items/?by=relevancy&keyword=m%E1%BA%B7t%20n%E1%BA%A1%20ng%E1%BB%A7&limit=50&newest={}&order=desc&page_type=search'.format(
    #         i) for i in range(0, 100 * 50 + 1, 50)])
    # urls.extend(['https://shopee.vn/api/v2/search_items/?by=relevancy&keyword=son%20kem%20l%C3%AC&limit=50&newest={}&order=desc&page_type=search'.format(
    #         i) for i in range(0, 100 * 50 + 1, 50)])
    urls.extend(['https://shopee.vn/api/v2/search_items/?by=relevancy&keyword=%E1%BB%91p%20l%C6%B0ng%20a3s&limit=50&newest={}&order=desc&page_type=search'.format(
            i) for i in range(0, 1 * 50 + 1, 50)])
    # urls.extend(['https://shopee.vn/api/v2/search_items/?by=relevancy&keyword=d%C3%A9p%20nam&limit=50&newest={}&order=desc&page_type=search'.format(
    #         i) for i in range(0, 100 * 50 + 1, 50)])
    # urls.extend(['https://shopee.vn/api/v2/search_items/?by=relevancy&keyword=%C4%91i%E1%BB%87n%20tho%E1%BA%A1i%20gi%C3%A1%20r%E1%BA%BB&limit=50&newest={}&order=desc&page_type=search'.format(
    #         i) for i in range(0, 100 * 50 + 1, 50)])
    start_urls = urls

    def parse(self, response):
        req_url = response.url
        category = re.findall('keyword=(.*?)&', req_url)[0]
        data = json.loads(response.body)
        items = data.get("items")
        if items:
            for item in items:
                name = item.get("name")
                if name:
                    trade_name = TradeName()
                    trade_name['category'] = unquote(category).encode('utf8')
                    trade_name['content'] = name.encode('utf8')
                    print(name)


                    # yield trade_name

