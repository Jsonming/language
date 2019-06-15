# -*- coding: utf-8 -*-
import scrapy
from ..items import NewsLinkItem


class MalaysiakiniLinkSpider(scrapy.Spider):
    name = 'malaysiakini_link'
    allowed_domains = ['www.malaysiakini.com/my/latest/news']
    urls = ["http://www.malaysiakini.com/my/latest/news?page={}".format(i) for i in range(1, 5000)]
    urls.extend(["https://www.malaysiakini.com/my/tag/parlimen?page={}".format(i) for i in range(1, 1000)])
    urls.extend(["https://www.malaysiakini.com/my/tag/pilihaneditor?page={}".format(i) for i in range(1, 1000)])
    urls.extend(["https://www.malaysiakini.com/my/tag/global?page={}".format(i) for i in range(1, 1000)])
    urls.extend(["https://www.malaysiakini.com/my/latest/columns?page={}".format(i) for i in range(1, 1000)])
    urls.extend(["https://www.malaysiakini.com/my/latest/letters?page={}".format(i) for i in range(1, 1000)])
    urls.extend(["https://www.malaysiakini.com/my/tag/laporankhas?page={}".format(i) for i in range(1, 1000)])
    urls.extend(["https://www.malaysiakini.com/my/tag/ulasan?page={}".format(i) for i in range(1, 1000)])
    urls.extend(["https://www.malaysiakini.com/my/tag/wawancara?page={}".format(i) for i in range(1, 1000)])
    urls.extend(["https://www.malaysiakini.com/my/latest/photos?page={}".format(i) for i in range(1, 50)])
    urls.extend(["https://www.malaysiakini.com/my/latest/sukan?page={}".format(i) for i in range(1, 1000)])
    urls.extend(["https://www.malaysiakini.com/my/latest/hiburan?page={}".format(i) for i in range(1, 1000)])

    start_urls = urls

    def parse(self, response):
        req_url = response.url
        category_url = req_url.split('?')[0]
        category = category_url.split('/')[-1]
        teasers = response.xpath('//a[@class="uk-position-cover"]')
        for teaser in teasers:
            short_url = teaser.xpath('./@href').extract()[0]
            url = 'https://www.malaysiakini.com' + short_url
            item = NewsLinkItem()
            item['category'] = category
            item['url'] = url
            yield item
