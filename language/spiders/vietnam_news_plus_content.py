# -*- coding: utf-8 -*-
import scrapy
from ..items import NewsContentItem


class VietnamNewsPlusContentSpider(scrapy.Spider):
    name = 'vietnam_news_plus_content'
    allowed_domains = ['www.vietnamplus.vn']
    start_urls = ['https://www.vietnamplus.vn/tong-thong-cong-hoa-chile-bat-dau-tham-cap-nha-nuoc-toi-viet-nam/474380.vnp']

    def parse(self, response):
        title = response.xpath('//h1/text()').extract()
        summery = response.xpath('//div[@class="details__summary cms-desc"]//text()').extract()
        paragraph = response.xpath('//div[@class="content article-body cms-body "]//text()').extract()
        text = []
        text.extend(title)
        text.extend(summery)
        text.extend(paragraph)
        content = ''.join(text).replace('\r\n', ' ').replace('\n', ' ')
        item = NewsContentItem()
        item['url'] = response.url
        item['content'] = content
        return item




