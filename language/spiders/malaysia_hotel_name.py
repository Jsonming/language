# -*- coding: utf-8 -*-
import scrapy


class MalaysiaHotelNameSpider(scrapy.Spider):
    name = 'malaysia_hotel_name'
    allowed_domains = ['www.booking.com/searchresults.id.html']
    start_urls = [
        'https://www.booking.com/searchresults.id.html?aid=356980&label=gog235jc-1FCAsooQFCHXBlbWFuZGFuZ2FuLWluZGFoLWd1ZXN0LWhvdXNlSDNYA2iJAogBAZgBErgBGMgBDNgBAegBAfgBDIgCAagCBLgC3fXc5QXAAgE&lang=id&sid=f36e8318f5aa14566fca0a3248f8bf12&sb=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.id.html%3Faid%3D356980%3Blabel%3Dgog235jc-1FCAsooQFCHXBlbWFuZGFuZ2FuLWluZGFoLWd1ZXN0LWhvdXNlSDNYA2iJAogBAZgBErgBGMgBDNgBAegBAfgBDIgCAagCBLgC3fXc5QXAAgE%3Bsid%3Df36e8318f5aa14566fca0a3248f8bf12%3Bsb_price_type%3Dtotal%26%3B&ss=kuala+lumpur&is_ski_area=0&checkin_year=&checkin_month=&checkout_year=&checkout_month=&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1']

    def parse(self, response):
        content = response.xpath('//span[@class="sr-hotel__name\n"]//text()').extract()
        names = [name.strip() for name in content]
        print(names)
        print(len(names))
        with open(r'C:\Users\Administrator\Desktop\malaya_temp\hotel_name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(names))

        next_url = response.xpath('//*[@id="search_results_table"]/div[4]/nav/ul/li[3]/a/@href').extract()
        next_url = "https://www.booking.com" + next_url[0]
        return scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
